#!/usr/bin/env python3
"""
Setup script for Pkr_Notes project
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
    return long_description

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="pkr-notes",
    version="1.0.0",
    author="Pkr_Notes Team",
    author_email="your.email@example.com",
    description="A YOLOv8-based object detection system for Pakistani Rupee banknotes",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Pkr_Notes",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.910",
        ],
        "gpu": [
            "torch>=2.0.0+cu118",
            "torchvision>=0.15.0+cu118",
        ],
    },
    entry_points={
        "console_scripts": [
            "pkr-detect=detect_pkr:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="computer-vision, object-detection, yolo, yolo8, banknote-detection, pakistani-rupee, pkr",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/Pkr_Notes/issues",
        "Source": "https://github.com/yourusername/Pkr_Notes",
        "Documentation": "https://github.com/yourusername/Pkr_Notes#readme",
    },
)
