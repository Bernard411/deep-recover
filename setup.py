from setuptools import setup, find_packages

setup(
    name="deep-recover",
    version="1.0.0",
    description="Recover deleted files via filesystem metadata parsing and raw signature carving.",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "deep-recover=deep_recover.cli:main",
        ],
    },
)
