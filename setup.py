import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="binod", 
    version="0.0.1",
    author="binod",
    author_email="binodtharu@binod.com",
    description="Who is binod ?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayushmankumar7/binod",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)