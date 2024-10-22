from setuptools import setup, find_packages

setup(
    name='Git Sync Tool',
    version='0.1.0',
    description='Easily sync repos across devices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Miguel Flores-Acton',
    author_email='mfacton1@gmail.com',
    url='https://github.com/mfacton/git-sync-tool',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'prettytable',
        'tqdm',
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'gsync=gsync:main',
        ],
    },
)