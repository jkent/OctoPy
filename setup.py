from setuptools import setup, find_packages
import octopy

#with open("README.md", 'r') as f:
#    readme = f.read()

setup(
    name='main',
    version=octopy.version,
    packages=find_packages(exclude=['tests']),
    author='Jeff Kent',
    author_email='jeff@jkent.net',
    description='A "bridge first" multi-platform bot.',
    zip_safe=False,
    license='BSD',
    keywords='irc discord slack plugin bridge bot',
    url='https://github.com/jkent/main',
#    long_description=readme,
    install_requires=[
        'aioprocessing'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
