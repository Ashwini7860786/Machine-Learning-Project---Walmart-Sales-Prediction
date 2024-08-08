from setuptools import find_package,setup



setup(
    name='Machine Learning Project - Walmart Sales Prediction',
    version='0.0.1',
    author='Ashwini Kumar',
    author_email='ashwini7860786@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0',
        'seaborn>=0.10.0',
        'scikit-learn>=0.22.0',
        'statsmodels>=0.11.0',
        'ipython>=7.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)