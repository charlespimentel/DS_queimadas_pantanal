import streamlit as st
import geopandas as gpd
import plotly.express as px

st.title('Mapa de Queimadas no Pantanal dos últimos 10 anos')
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

# Mapa ploty com as queimadas no ano selecionado usando o plotly express no campo 'geometry'
st.subheader('Mapa com as queimadas no ano selecionado')
with st.spinner('Carregando mapa...'):
    fig = px.choropleth_mapbox(df[df['Ano'] == ano], geojson=df[df['Ano'] == ano].geometry, locations=df[df['Ano'] == ano].index,
                                color='Ano',
                                color_continuous_scale="Viridis",
                                range_color=(12, 21),
                                mapbox_style="carto-positron",
                                zoom=3, center={"lat": -15.7801, "lon": -47.9292},
                                opacity=0.5,
                                labels={'Ano': 'Ano'}
                                )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig)