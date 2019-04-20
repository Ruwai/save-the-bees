import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(

    name="save-the-bees",
    version="0.0.1",
    author="Ruwai",
    description="Command Line App dedicated towards saving the bees!",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Ruwai/save-the-bees",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[

        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha"
    ],
    entry_points='''
        [console_scripts]
        save-the-bees=save-the-bees.main:cli
    ''',

    )