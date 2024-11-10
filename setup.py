from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Updated variables
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "Charles Bartels Squire"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="squire-bartels",
    description="A small local package for ML-based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/squire-bartels/ML-Based-Book-Recommender-System",  
    author_email="charlesbartelssquire@gmail.com",
    packages=find_packages(),
    python_requires=" 3.13.0",
    install_requires=LIST_OF_REQUIREMENTS
)



