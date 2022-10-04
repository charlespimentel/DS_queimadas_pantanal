import streamlit as st

st.set_page_config(
    page_title="Dashboard - Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos no Brasil",
    page_icon=":fire:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('Dashboard - Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos no Brasil')  
st.write('''
    A fim de facilitar a visualização dos resultados para um público não técnico da área de Ciências Geoespaciais, foi desenvolvido um dashboard dinâmico utilizando a biblioteca Streamlit, que é uma biblioteca de código aberto para a criação de aplicativos web para a linguagem de programação Python. O dashboard foi desenvolvido utilizando o dataset de focos de queimadas do Pantanal de 2012 à 2021, que foi previamente tratado e analisado. O dashboard possui 3 páginas, sendo elas: a página inicial, que apresenta um mapa com a localização dos focos de queimadas no Pantanal, a página de análise exploratória dos dados, que apresenta gráficos com informações sobre os dados de queimadas no Pantanal, e a página de previsão de focos de queimadas, que apresenta um gráfico com a previsão de focos de queimadas no Pantanal para o ano de 2022. O arquivo de código do dashboard está disponível no repositório do projeto no GitHub.
''')
st.sidebar.success('Selecione uma página acima')