import os
from setuptools import setup

setup(
    name="my_pypi_package",
    packages=['my_pypi_package'],
    version="0.1",
    author="Bharat Saini",
    author_email="itsbharatsaini@gmail.com",
    description="An easy example of a Python package",
    long_description="My_own_Python_package contains a funny game for calculating the result of arithmetic operations applied to an unknow number given by the player",
    long_description_content_type="text/markdown",
    url="",
    keywords=['pip', 'pypi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
