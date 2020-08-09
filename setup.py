from setuptools import setup, find_packages

setup(
    name='DevopsX5Test',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pylint',
        'pytest',
        'pytest-ordering',
        'python-dateutil'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)