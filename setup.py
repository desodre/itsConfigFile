from setuptools import setup

setup(
    name='its_config_file',
    version='1.0.0',
    py_modules=['main'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'its_config_file=main:main'
        ]
    },
)