#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Get the directory of this script
here = os.path.abspath(os.path.dirname(__file__))

# Read README
readme_path = os.path.join(here, "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Kerberos relaying and unconstrained delegation abuse toolkit"

# Read requirements
requirements_path = os.path.join(here, "requirements.txt")
if os.path.exists(requirements_path):
    with open(requirements_path, "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
else:
    requirements = ["impacket", "ldap3", "dnspython", "pycryptodome"]

setup(
    name="krbrelayx",
    version="1.0.0",
    author="Dirk-jan Mollema",
    description="Kerberos relaying and unconstrained delegation abuse toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dirkjanm/krbrelayx",
    packages=find_packages(),
    py_modules=["addspn", "dnstool", "krbrelayx", "printerbug"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "addspn=addspn:main",
            "dnstool=dnstool:main", 
            "krbrelayx=krbrelayx:main",
            "printerbug=printerbug:main",
        ],
    },
)