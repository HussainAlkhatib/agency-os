from setuptools import setup, find_packages

setup(
    name="agency-cli",
    version="0.1.0",
    author="Agency Team",
    author_email="contact@agency-agents.com",
    description="Professional AI Agent Orchestration CLI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/agency-cli",
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
