from setuptools import setup, find_packages

setup(
    name="agency-os",
    version="0.1.0",
    author="Hussain Alkhatib",
    author_email="h2311065@gmail.com",
    description="Professional AI Agent Orchestration CLI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HussainAlkatib/agency-os",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "agency=agency_cli.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.7',
)
