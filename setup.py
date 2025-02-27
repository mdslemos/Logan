from setuptools import setup, find_packages

setup(
    name="logan",
    version="1.0.0",
    description="Logan: The Log Analyzer",
    author="Miguel Lemos Santos",
    author_email="mdslemos@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "loguru",
        # Add any other dependencies here, e.g., "requests", "pandas"
    ],
    entry_points={
        "console_scripts": [
            "logan=main:main",  # Ensure this points to the correct function in main.py
        ],
    },
)