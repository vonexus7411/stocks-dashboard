from setuptools import setup, find_packages

setup(
    name="stocks-app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "matplotlib>=3.7.1",
        "numpy>=1.24.3",
        "tk",
        "polygon-api-client",
        "python-dotenv>=1.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "pylint>=2.17.0",
            "pyinstaller>=5.13.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "stocks=main:main",
        ],
    },
    author="Anthony Fugit",
    author_email="anthony.fugit@outlook.com",
    description="A desktop application for stock market analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="stocks, finance, analysis, trading",
    url="https://github.com/vonexus/stocks",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.10",
        "Operating System :: MacOS :: MacOS X",
    ],
)