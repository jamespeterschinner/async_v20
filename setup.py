from setuptools import setup, find_packages

setup(name='async_v20',
      version='0.1',
      description="Asynchronous wrapper for OANDA's v20 REST API",
      url='N/A',
      author='James Peter Schinner',
      author_email='james.peter.schinner@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['aiohttp>=2.2.5',
                        'pytest>=3.2.2',
                        'ujson==1.35',
                        'yarl==0.12.0']
)