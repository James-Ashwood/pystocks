from setuptools import find_packages, setup

setup(
    name='pysytocks',
    packages=find_packages(include=['pystocks']),
    version='0.1.0',
    description='The python library "pystocks". Used to analyze financial and stock data for data-scientists and financial adivsors with limited programming knowledge.',
    author='James-Ashwood',
    license='MIT',
    install_requires=["yfinance", "numpy", "pandas", "matplotlib"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)