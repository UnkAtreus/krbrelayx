#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="krbrelayx",
    version="1.0.0",
    author="Dirk-jan Mollema",
    author_email="dirkjan@fox-it.com",
    description="Kerberos relaying and unconstrained delegation abuse toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dirkjanm/krbrelayx",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    scripts=[
        "addspn.py",
        "dnstool.py",
        "krbrelayx.py",
        "printerbug.py",
    ],
    entry_points={
        "console_scripts": [
            "addspn=addspn:main",
            "dnstool=dnstool:main",
            "krbrelayx=krbrelayx:main",
            "printerbug=printerbug:main",
        ],
    },
)