"""setup.py file."""
import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = 'YACT Team'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name="yact",
    version='0.0.1',
    packages=find_packages(),
    author="YACT Team",
    author_email="",
    description="Yet Another CLI Tool",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/GGabriele/yact",
    include_package_data=True,
    install_requires=reqs,
)