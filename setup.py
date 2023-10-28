from setuptools import setup, find_packages

setup(
    name='robotframework-DEMOQA-driver',
    version='0.1.1',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires = [
        'robotframework',
        'robotframework-seleniumlibrary',
        'chromedriver_autoinstaller'
    ],
    author='Artur Ziółkowksi',
    author_email='artur.k.ziolkowski@gmail.com',

)
