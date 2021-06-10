import os

from setuptools import setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'scrapingbee', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name='scrapingbee',
    version=about['__version__'],
    url='https://github.com/scrapingbee/scrapingbee-python',
    description='ScrapingBee Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ari Bajo Rouvinen',
    author_email='arimbr@gmail.com',
    maintainer='Pierre de Wulf',
    maintainer_email='hello@scrapingbee.com',
    license='MIT',
    packages=['scrapingbee'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)
