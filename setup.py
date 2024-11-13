from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Updated variables
REPO_NAME = "Global Book Recommendation System"
AUTHOR_USER_NAME = "Charles Bartels Squire"
SRC_REPO = "global_book_recommender"
LIST_OF_REQUIREMENTS = [
    "streamlit",       # Streamlit for web app
    "numpy",           # NumPy for numerical operations
    "pandas",          # Pandas for data manipulation
    "scikit-learn"  # Scikit-learn for machine learning algorithms
]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="squire-bartels",
    description="A small local package for ML-based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/squire-bartels/global_book_recommendation_system",
    author_email="charlesbartelssquire@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7, <3.12",  # Python version range
    install_requires=LIST_OF_REQUIREMENTS
)
