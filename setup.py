from setuptools import setup, find_packages

setup(
    name='deobshell',
    version='1.0.0',
    packages=find_packages(),
    description='A tool for deobfuscating PowerShell code as part of malware analysis.',
    entry_points={
        'console_scripts': [
            'deobshell=deobshell.main:main',
        ],
    },
    include_package_data=True,
)