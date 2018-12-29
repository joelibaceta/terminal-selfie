import sys
from setuptools import setup, find_packages

setup(
    name="terminal_selfie",
    version="1.0.0",
    author="Joel Ibaceta",
    author_email="mail@joelibaceta.com",
    license='MIT',
    description="It is a simple tool to take a selfie using terminal",
    long_description="It is a simple tool to take a selfie using terminal",
    url="https://github.com/joelibaceta/terminal_selfie",
    project_urls={
        'Source': 'https://github.com/joelibaceta/terminal_selfie',
        'Tracker': 'https://github.com/joelibaceta/terminal_selfie/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['opencv-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='selfie terminal opencv',
    entry_points={
        "console_scripts": [
            'take-selfie=terminal_selfie.cli:main'
        ]
    }
)