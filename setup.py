# setup.py

from setuptools import setup, find_packages
import os

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Extract the version number from a version file or define it here
version = "1.0.0"

setup(
    name="print_project",  # Package name (must be unique if uploading to PyPI)
    version=version,
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to concatenate Python project files into a single text file with .gitignore-like exclusions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/concatenate_project",  # Replace with your repository URL
    package_dir={"": "src"},  # Tells setuptools that packages are under src/
    packages=find_packages(where="src"),  # Automatically find packages in src/
    install_requires=[
        "pathspec==0.10.1",  # Specify exact versions for reproducibility
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Ensure this matches your LICENSE file
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify your Python version requirements
    entry_points={
        'console_scripts': [
            'concatenate_project=concatenate_project.main:main',  # Creates a CLI command
        ],
    },
    include_package_data=True,  # Includes files specified in MANIFEST.in
    zip_safe=False,  # Whether the package can be safely installed and run from a zip file
)
