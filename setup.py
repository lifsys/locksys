from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="locksys",
    version="0.2.0",
    author="Lifsys, Inc.",
    author_email="info@lifsys.com",
    description="A Python library for securely retrieving API keys from 1Password vaults",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lifsys/locksys",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "onepasswordconnectsdk",
    ],
)
