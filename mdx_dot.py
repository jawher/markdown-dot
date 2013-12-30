#!/usr/bin/env python

import re
import markdown
import os
import subprocess
import tempfile
import md5

# Global vars
FENCED_BLOCK_RE = re.compile( \
    r'^\{% dot\s+(?P<out>[^\s]+)\s*\n(?P<code>.*?)%}\s*$',
    re.MULTILINE | re.DOTALL
    )


class DotBlockExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add DotBlockPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.add('dot_block',
                                 DotBlockPreprocessor(md),
                                 "_begin")


class DotBlockPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        markdown.preprocessors.Preprocessor.__init__(self, md)

    def run(self, lines):
        """ Match and store Fenced Code Blocks in the HtmlStash. """

        text = "\n".join(lines)
        while 1:
            m = FENCED_BLOCK_RE.search(text)
            if m:
                out = m.group('out')
                out_file = "content/images/graphviz/" + out
                img_href = "images/graphviz/" + out
                format = os.path.splitext(out)[1][1:].strip()
                code = m.group('code')
                cache_marker = "cache/" + out + "-" + md5.new(code).hexdigest()

                ensure_dir_exists(out_file)
                ensure_dir_exists(cache_marker)

                if (not os.path.exists(out_file)) or (not os.path.exists(cache_marker)):
                    print("generate " + out)
                    inp = tempfile.NamedTemporaryFile(delete=False)
                    inp.write(code)
                    inp.flush()
                    print(subprocess.check_output(['dot -T' + format + ' -o ' + out_file + ' ' + inp.name], shell=True))
                    inp.close()
                    fcache = open(cache_marker, "w")
                    fcache.close()
                else:
                    print("pass " + out)

                img = "![" + out + "](/" + img_href + ")"
                text = '%s\n%s\n%s' % (text[:m.start()], img, text[m.end():])
            else:
                break
        return text.split("\n")


def ensure_dir_exists(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def makeExtension(configs=None):
    return DotBlockExtension(configs=configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
