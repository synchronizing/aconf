import setuptools

from aconf import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="aconf",
    version=__version__,
    author="Felipe Faria",
    description="Global memory-based configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/synchronizing/aconf",
    install_requires=required,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
