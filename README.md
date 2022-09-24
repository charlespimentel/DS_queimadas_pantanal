![](imgs/Queimadas%20no%20Pantanal%20uma%20an%C3%A1lise%20explorat%C3%B3ria%20dos%20%C3%BAltimos%2010%20anos.png)

# Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos
Este repositório tem como objetivo armazenar e organizar os códigos utilizados para a geração dos relatórios, visualizações e proveniências utilizados no artigo Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos produzido na disciplina de Fundamentos de Ciência de Dados do PPGI-UFRJ. O artigo pode ser acessado [aqui](artigo_queimadas_pantanal.doc) e o arquivo da apresentação [aqui](apresentação.pdf).

## Estrutura do repositório
O repositório está organizado da seguinte forma:
- [`Data_Lasa_12_20`](Data_Lasa_12_21/): contém os dados utilizados para a análise.
- [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb): contém os códigos utilizados para a análise exploratória dos dados de queimadas do LASA no Pantanal.
- [`README.md`](README.md): contém a descrição do repositório.
- [`requirements.txt`](requirements.txt): contém as dependências utilizadas no projeto exportadas para arquivo txt.
- [`environment.yml`](environment.yml): contém as dependências utilizadas no projeto exportadas para arquivo yml.
- [`prov_generator.ipynb`](prov_generator.ipynb): contém o script utilizado para a geração das proveniências dos dados.

## Dependências
Para executar os códigos do projeto, é necessário instalar as dependências contidas no arquivo `requirements.txt` ou `environment.yml`. Foi utilizado o [Anaconda](https://www.anaconda.com/products/distribution) para a criação do ambiente de desenvolvimento do projeto. Para instalar as dependências, basta executar o seguinte comando no terminal:
```bash
conda env create -f environment.yml
```
## Execução
Para executar os códigos do projeto, utilize um jupyter notebook ou o google colab. 
Jupyter notebook:
```bash
jupyter notebook
```
Para executar os códigos no google colab, basta clicar no botão abaixo:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/charlespimentel/DS_queimadas_pantanal/blob/main/exploratory_data_analysis.ipynb)

Para executar o dashboard, basta executar o arquivo `dynamic-dashboard.py` no terminal:
```bash
streamlit dynamic_dashboard.py
```

## Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Autores
- **Charles Pimentel** - [charlespimentel](https://github.com/charlespimentel)
- **Isaac D'Césares** - [idcesares](https://github.com/idcesares)

## Citação
Se você utilizar este repositório em seu trabalho, por favor, cite o artigo:
```bibtex
@article{pimentel&dcesares2022queimadas,
  title={Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos},
  author={Pimentel, Charles and D'Césares, Isaac},
  year={2022}
}
```