from setuptools import setup

with open('README.rst', "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="types-rdkit",
    version="2021.09.4",
    description="Typing stubs for RDKit",
    long_description=long_description + "\n\n",
    long_description_content_type="text/x-rst",
    author="Bas van Beek",
    url="https://github.com/BvB93/types-rdkit",
    install_requires=[],
    packages=['rdkit-stubs'],
    package_data={'rdkit-stubs': ["py.typed", "**/*.pyi"]},
    license="Apache-2.0 license",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Typing :: Stubs Only",
    ]
)
