from setuptools import setup

setup(
    name="paskell",
    version="0.1.0",
    py_modules=["paskell"],
    entry_points={
        "console_scripts": [
            "paskell = paskell:main",
        ],
    },
    description="a Python package that communicates between Python and Haskell",
    long_description="Paskell requires your Haskell file has been fully compiled and can run as an executable. For Windows users, their Haskell file must be [file_name].exe, and for Unix users it should be ./[file_name] Paskell will not run your Haskell file if it was not compiled.",
    long_description_content_type="text/markdown",
    author="Ibn Aleem",
    url="https://github.com/ibnaleem/paskell",
    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="haskell, functional programming, paskell",
    project_urls={
        "Source": "https://github.com/ibnaleem/paskell",
        "Tracker": "https://github.com/ibnaleem/paskell/issues",
    },
)