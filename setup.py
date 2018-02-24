from setuptools import setup, find_packages
setup(
    name="NetPBM",
    version="0.1.2",
    packages=['netpbm'],
    # scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Mark Schwartz",
    author_email="mrbloozman@gmail.com",
    description="Provides NetPBM class to load .pbm, .pgm, or .ppm files",
    license="MIT",
    # keywords="hello world example examples",
    # url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://www.github.com/mrbloozman/Python_NetPBM",
    }

    # could also include long_description, download_url, classifiers, etc.
)