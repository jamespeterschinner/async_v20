import os

from setuptools import setup, find_packages
from async_v20 import __version__


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='async_v20',
      version=__version__,
      description="Asynchronous wrapper for OANDA's v20 REST API",
      long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
      author='James Peter Schinner',
      author_email='james.peter.schinner@gmail.com',
      url='https://github.com/jamespeterschinner/async_v20',
      license='MIT',
      packages=find_packages(),
      install_requires=['aiohttp>=3.0.0',
                        'ujson>=1.35',
                        'yarl>=0.12.0',
                        'pandas'],
      classifiers=['Programming Language :: Python :: 3.6', 'Development Status :: 4 - Beta',
                   'Framework :: AsyncIO',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP :: Session'],
      keywords='algorithmic trading oanda v20 REST asyncio ',
      )
