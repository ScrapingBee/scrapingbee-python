from setuptools import setup

setup(
    name='scrapingbee',
    version='1.1.0',
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
