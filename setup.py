from setuptools import setup, find_packages

# declara o arquivo README.md carrega ele para que 
# seja usado no campo long_description
with open("README.md", "r") as f:
    page_description = f.read()

# carrega o arquivo para especificar os packages dependentes
# quando for criar o arquivo não colocar a versão a menos que seja necessário
# colocar a versão no arquivo requirements, ira forçar o uso daquela versão
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    # nome do package, será o mesmo usado no import
    name="test-img-prc-0001",
    # versão no mesmo formato da PEP
    version="0.0.1",
    author="Repodi",
    #author_email="mail@",
    description="Image processing package",
    # usa o arquivo README pre carregado
    long_description=page_description,
    long_description_content_type="text/markdown",
    #url="my_github_repository_project_link"
    # busca os packages automaticamente
    packages=find_packages(),
    # carrega o contetudo do arquivo pre carregado
    install_requires=requirements,
    # especifica a versão mínima do python
    python_requires='>=3.8',
)