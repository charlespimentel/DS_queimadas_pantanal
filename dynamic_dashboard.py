import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import contextily as ctx
import plotly.express as px
import plotly.graph_objects as go
import folium


@st.cache(persist=True)
def fetch_data(url):
    data = gpd.read_file(url)
    return data

df = gpd.read_file('Data_Result/queimadas_pantanal_2012_2021.geojson')

st.title('Dashboard - Queimadas no Pantanal: uma análise exploratória dos últimos 10 anos no Brasil')

ano = st.selectbox(
    'Selecione o ano para visualizar os dados',
    (2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012))

# Número de queimadas no ano selecionado
st.subheader('Número de queimadas no ano selecionado')
st.write(df[df['Ano'] == ano].shape[0])

# Número de queimadas por mês no ano selecionado
st.subheader('Número de queimadas por mês no ano selecionado')
st.write(df[df['Ano'] == ano].groupby('Mes').size())

# Mapa ploty com as queimadas no ano selecionado usando o plotly express no campo 'geometry'
st.subheader('Mapa com as queimadas no ano selecionado')
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









