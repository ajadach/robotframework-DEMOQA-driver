from setuptools import setup, find_packages

setup(
    name='robotframework-DEMOQA-driver',
    version='0.1.3',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires = [
        'robotframework',
        'robotframework-seleniumlibrary',
        'chromedriver_autoinstaller',
        'lxml'
    ],
    author='Artur Ziółkowksi',
    author_email='artur.k.ziolkowski@gmail.com',
    description="UI driver to support demoqa.com",
    python_requires=">=3.6",
    include_package_data=True
)

