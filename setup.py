# setup.py

from setuptools import setup

setup(
    name='ic',
    version='0.1',
    py_modules=['cli'],
    entry_points={
        'console_scripts': [
            'ic = cli:main',
        ],
    },
)
