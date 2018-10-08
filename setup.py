from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    author='Marco Rossi',
    author_email='developer@marco-rossi.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Use Microsoft PowerPoint within Python with the help of COM',
    extras_require={'test': ['pytest', 'python-pptx']},
    install_requires=['comtypes'],
    keywords=['com', 'powerpoint'],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='pptcom',
    packages=['pptcom'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0', 'setuptools_scm'],
    url='https://github.com/m-rossi/pptcom',
    use_scm_version=True,
)
