# we will use this to install src as a local package
from setuptools import setup, find_packages

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Sachin S',
    author_email='Your Email',
    license='MIT',
    packages=find_packages(),
    # this find packages will look for constructor file __init_ _ and wherever it finds it, the same folder will be considered as a package
    install_requires=[]
)