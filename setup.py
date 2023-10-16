from setuptools import setup, find_packages


setup(
    name="safari",
    packages=find_packages(exclude=[]),
    version="0.0.1",
    license="MIT",
    description="",
    install_requires=[
        "opt_einsum",
    ],
)
