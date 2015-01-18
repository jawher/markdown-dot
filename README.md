What is it
==========

A Python Markdown extension that replaces inline dot graph defintions with an image tag pointing to the generated graph image.

Please note that I developed this specifically for my Perlican based blog and hence output directories and other stuff is hard coded.

# Installation

Checkout and *easy_install* or *pip install* it:

    $ git clone git://github.com/jawher/markdown-dot.git
    $ cd markdown-dot
    $ easy_install .

# Usage

Activate the `dot` extension and place the graph defintions in your markup like so:

```
{% dot output.png
	digraph G {
		rankdir=LR
		S0 -> A [label="-"]
		A -> B [label="-"]
		A -> C [label=">"]

		A [peripheries=2]
		B [peripheries=2]
		C [peripheries=2]
	}
%}
```

The block above will then be replaced with an `img` tag pointing to the generated png file.

If the file name starts with a `!`, the image will still be generated but no `img` tag will be included in the result.

# Troubleshooting

Please consider using [Github issues tracker](http://github.com/jawher/markdown-dot/issues) to submit bug reports or feature requests.


# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
