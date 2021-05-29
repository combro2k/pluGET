import setuptools

from distutils.core import setup

setup(
    name='pluGET',
    version='0.1dev',
    packages=[
        'pluGET',
        'pluGET.handlers',
        'pluGET.plugin',
        'pluGET.serverjar',
        'pluGET.utils',
    ],
    package_dir={'pluGET': 'src'},
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    entry_points = {
        'console_scripts': [
            'pluGET=pluGET:mainFunction'
        ],
    },
    install_requires=[
        'urllib3>=1.21.1',
        'requests>=2.25.1',
        'paramiko>=2.7.2',
        'bcrypt>=3.2.0',
        'cryptography>=3.4.6',
        'pynacl>=1.4.0',
        'cffi>=1.14.5',
        'six>=1.15.0',
        'pycparser>=2.20',
        'pysftp>=0.2.9',
        'rich>=9.13.0',
        'commonmark>=0.9.1',
        'Pygments>=2.8.1',
        'typing_extensions>=3.7.4.3',
    ],
)
