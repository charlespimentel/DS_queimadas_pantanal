import streamlit as st
import geopandas as gpd
import plotly.express as px

st.title('Análise estatística de Queimadas no Pantanal dos últimos 10 anos')

@st.cache(persist=True)
def fetch_data(url):
    data = gpd.read_file(url)
    return data

with st.spinner('Carregando base de dados...'):
    df = fetch_data('Data_Result/queimadas_pantanal_2012_2021.geojson')
st.success('Base de dados carregada com sucesso!')

ano = st.selectbox(
    'Selecione o ano para visualizar os dados',
    (2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012))

# Número de queimadas no ano selecionado
st.subheader('Número de focos de queimadas no ano selecionado')
st.write(df[df['Ano'] == ano].shape[0], 'focos de queimadas')

# Quantidade de área queimada no ano selecionado
st.subheader('Quantidade de área queimada no ano selecionado')
st.write(df[df['Ano'] == ano].area.sum(), 'milhões de hectares')

# Gráfico de barras com o número de queimadas por mês no ano selecionado
st.subheader('Número de focos queimadas por mês no ano selecionado')
with st.spinner('Carregando gráfico...'):
    fig = px.bar(df[df['Ano'] == ano].groupby('Mes').size().reset_index(name='Count'), x='Mes', y='Count', color='Count', color_continuous_scale="Viridis")
    st.plotly_chart(fig)