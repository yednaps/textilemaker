from setuptools import setup, find_packages

setup(
    name='Textilemaker',
    version='0.1',
    py_modules=['tilemaker'],
    install_requires=[
        'Click',
        'Pillow',
        'sys',
        'random',
        'cPickle',
    ],
    entry_points='''
        [console_scripts]
        tilemaker=tilemaker:maketile
    ''',
)
