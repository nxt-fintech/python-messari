from setuptools import setup

requires = ["requests"]

setup(
    name="pymessari",
    version="0.2.0",
    url="https://github.com/nxt-fintech/pymessari",
    description="client library for messari api",
    author="Next Finance Tech",
    license="APACHE LICENSE, VERSION 2.0",
    packages=["pymessari"],
    install_requires=requires,
    classifiers=["Programming Language :: Python"],
    keywords=["messari"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
