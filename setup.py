#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='carbonnow',
    version='0.2',
    description='carbon.now.sh API Wrapper powered by Carbonara',
    long_description='long_description',
    long_description_content_type='text/markdown',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    author='Pokurt',
    author_email='poki@pokurt.me',
    url='https://github.com/OpenRestfulAPI/carbon-now-sh-API-Wrapper',
    packages=setuptools.find_packages(exclude='example.py'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['aiohttp','asyncio'],
    python_requires='>=3.6',
)
