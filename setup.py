import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-contracts",
    version="0.1.1",
    author="Gino Jacob",
    author_email="gvjacob@outlook.com",
    description="Function contracts for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gvjacob/contracts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)