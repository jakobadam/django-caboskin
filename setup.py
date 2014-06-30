from setuptools import setup, find_packages

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='caboskin',
    version='0.1',
    description='common django cabo skin.',
    long_description=readme,
    author='Jakob A. Dam',
    author_email='jakob.a.dam@gmail.com',
    packages=find_packages(),
    license='BSD',
    zip_safe=False,
)
