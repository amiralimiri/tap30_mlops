from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="tap30-ride-demand-mlops",
    version="0.1.0",
    author="Amirali Miri",
    packages=find_packages(),
    install_requires=requirements,
)
