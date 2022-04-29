from setuptools import setup, find_packages
import codecs
import os

# here = os.path.abspath(os.path.dirname(__file__))
#
# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Python SDK for frontend components usage'
LONG_DESCRIPTION = 'A package that allows to use front-end components to simplify ' \
                   'building of web pages for ekp plugins'

# Setting up
setup(
    name="python-ekp-sdk",
    version=VERSION,
    author="Earn Keeper (Gavin Shaw)",
    author_email="gavin@earnkeeper.io",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['eventlet==0.33.0', 'pycoingecko==2.2.0', 'python-socketio==5.6.0'],
    keywords=['python', 'earnkeeper', 'sdk', 'components'],
    license = 'GNU',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)