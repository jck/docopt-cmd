from setuptools import setup

setup(
    name='docopt-cmd',
    version='0.0.1',
    author='Keerthan Jaic',
    author_email='jckeerthan@gmail.com',
    description='Pythonic commands and subcommands for docopt',
    license='MIT',
    keywords='option arguments parsing optparse argparse getopt, command, subcommand',
    url='http://docopt.org',
    py_modules=['docopt'],
    long_description=open('README.rst').read(),
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Topic :: Utilities',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'License :: OSI Approved :: MIT License',
        ],
    install_requires=['docopt']
)
