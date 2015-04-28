try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.1.201502'

setup(
    name='hockeyappwrapper',
    version=__version__,
    packages=[
        'hockeyapp',
    ],
    url='https://github.com/samdfonseca/hockeyappwrapper',
    install_requires=[
        'requests>=2.5.1',
        'simplejson>=3.6.5',
        'boltons>=0.6.3',
    ],
    description='Python binding to the HockeyApp API'
)

