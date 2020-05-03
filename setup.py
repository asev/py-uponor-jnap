from distutils.core import setup

setup(
    name='UponorJnap',
    packages=['UponorJnap'],
    version='0.1',
    license='MIT',
    description='Library for communication with Uponor X-265',
    author='asev',
    author_email='pypi@sev.lt',
    url='https://github.com/asev',
    download_url='https://github.com/asev/py-uponor-jnap/archive/0.1.tar.gz',
    keywords=['uponor', 'heating', 'control'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
