from setuptools import setup


__version__ = '0.0.1'

with open('README.md') as f:
    __readme__ = f.read()

setup(
    name='pyazo',
    version=__version__,
    description = 'Gyazo API client',
    long_description=__readme__,
    author='mtwtkman',
    url='https://github.com/mtwtkman/pyazo',
    install_requires=['requests']
)
