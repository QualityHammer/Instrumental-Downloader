from setuptools import setup


with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="instrumental_dl",
    version=0.1,
    packages=[
        'instrumental_dl', 'instrumental_dl.common',
        'instrumental_dl.logger', 'instrumental_dl.config'
    ],
    package_data={
        'config': ['keywords.txt']
    },

    install_requires=['youtube_dl>=2019.9.28'],
    python_requires='>=3.6',

    author="QualityHammer",
    author_email="agingllama@gmail.com",
    description="Download the instrumental for almost any song",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='instrumental downloader',
    url='https://github.com/QualityHammer/instrumental-downloader',

    entry_points={
        'console_scripts': ['instrumental_dl=bin.instrumental_dl:main']
    }
)
