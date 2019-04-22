from setuptools import setup

setup(
    name='anothertt',
    python_requires='>3.6',
    version='0.0.5',
    description='None',
    url='http://github.com/maruschin',
    author='Evgenii Marushchenko',
    author_email='maruschin@gmail.com',
    license='Unlicense',
    packages=['anothertt'],
    install_requires=[
        'pillow',
    ],
    zip_safe=False,
)

