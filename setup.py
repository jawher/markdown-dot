from setuptools import setup, find_packages

setup(
    name = "Markdown dot extension",
    version = "0.1.3",
    py_modules = ["mdx_dot"],
    install_requires = ['Markdown>=2.5.0'],
    author = "Jawher",
    author_email = "me@example.com",
    description = "Markdown dot extension",
    license = "MIT",
    keywords = "markdown dot graphviz",
    url = "https://github.com/jawher/markdown-dot",
)
