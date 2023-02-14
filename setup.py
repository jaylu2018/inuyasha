# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('inuyasha/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='inuyasha',
    version=version,
    url='https://github.com/jaylu2018/miku/tree/main',
    license='Apache License 2.0',
    author='luyh',
    author_email='2806767301@qq.com',
    description='automation testing framework based on Pytest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={
        'inuyasha': ['/*.inuyasha'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'playwright~=1.30.0',
        'pytest-playwright~=0.3.0',
        'requests~=2.28.2',
        'pytest_cases~=3.6.13',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'inuyasha = inuyasha.cli:main',
        ]
    },
    extras_require={
    },
)
