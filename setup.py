from setuptools import find_packages, setup

setup(
    name="price-parser",
    version="0.4.0",
    description="Extract price and currency from a raw string",
    long_description=open("README.rst", encoding="utf8").read()
    + "\n\n"
    + open("CHANGES.rst").read(),
    author="Mikhail Korobov",
    author_email="kmike84@gmail.com",
    url="https://github.com/scrapinghub/price-parser",
    packages=find_packages(exclude=["tests"]),
    package_data={"price_parser": ["py.typed"]},
    install_requires=[
        "attrs >= 17.3.0",
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
