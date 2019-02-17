import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DS_Alg",
    version="0.0.1",
    author="Sridhar Adhikarla",
    author_email="adhikarla2sridhar@yahoo.com",
    description="A package with collection of Data Structures and Algorithms!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sridhar1029/DS_Alg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)