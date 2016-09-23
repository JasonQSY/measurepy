from setuptools import setup

setup(
    name = 'measurepy',
    version = '0.1',
    description = 'A python module to boost first-step data analysis after measurements.',
    url = 'http://github.com/JasonQSY/measurepy',
    author = 'JasonQSY',
    author_email = 'jasonsyqian@gmail.com',
    license = 'MIT',
    packages = ['measurepy'],
    install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
    ],
    zip_safe = False
)
