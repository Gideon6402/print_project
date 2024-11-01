# setup.py

from setuptools import setup, find_packages
import os

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Extract the version number from a version file or define it here
version = "1.0.0"

setup(
    name="print_project",
    version=version,
    author="Gideon",
    url="https://github.com/gideon6402/print_project",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pathspec==0.10.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'print_project=main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)


# Old name: concatenate_project