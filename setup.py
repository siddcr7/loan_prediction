# setup.py
from setuptools import setup, find_packages

setup(
    name="loan_prediction",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "fastapi",
        "uvicorn",
        "streamlit",
        "pydantic",
        "joblib",
        "pytest",
        "python-multipart",
    ],
    author="Siddharth",
    author_email="siddharthshirwadkar@gmail.com",
    description="ML project for loan prediction",
    keywords="machine learning, loan prediction, fastapi, streamlit",
    url="https://github.com/yourusername/loan-prediction",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)