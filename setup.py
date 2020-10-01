from setuptools import setup
setup(
    name = 'accuweather_cli',
    version = '0.1.0',
    packages = ['accuweather_cli'],
    entry_points = {
        'console_scripts': [
            'accuweather = accuweather_cli.__main__:main'
        ]
    })