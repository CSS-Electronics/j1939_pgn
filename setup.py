from setuptools import setup

setup(
    name='J1939',
    version='0.0.1',
    author='Christian Steiniche',
    author_email='css@csselectronics.com',
    packages=['J1939'],
    scripts=[],
    url="https://github.com/CSS-Electronics/j1939/",
    license='LICENSE',
    description='Python module for working with SAE J1939 CAN-bus messages',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
)