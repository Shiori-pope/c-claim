# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="c-claim",
    version="1.0.0",
    description="标准刑法案由数据集",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zhijie Liu, Zixuan Feng, Ran Qiu, Jiarong Ge",
    license="CC BY-SA 4.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "c_claim": ["data/*.csv", "data/*.jsonl", "data/*.txt"],
    },
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: Creative Commons Attribution Share Alike 4.0 International (CC BY-SA 4.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
    ],
    keywords="法律 刑法 案由 司法解释",
)
