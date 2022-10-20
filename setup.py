from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_de_imagens",
    version="0.0.1",
    author="Alan_Torres",
    author_email="ats_hq@yahoo.com.br",
    description="Pacote para processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alan-Torres-S/Projeto-DIO---Criacao-de-pacotes-em-Python-.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)