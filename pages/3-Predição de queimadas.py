import streamlit as st
import geopandas as gpd
import pandas as pd
from prophet import Prophet

pd.options.plotting.backend = "plotly"

st.title('Análise preditiva de Queimadas no Pantanal para 2022')

@st.cache(persist=True)
def fetch_data(url):
    data = gpd.read_file(url)
    return data

with st.spinner('Carregando base de dados...'):
    df = fetch_data('Data_Result/queimadas_pantanal_2012_2021.geojson')

def dataset_adjustment(df):
    df_prophet = df.groupby('Data').sum()['Area'].reset_index(name='Area')
    df_prophet.columns = ['ds', 'y']
    df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])
    return df_prophet

def dataset_normalization(df_prophet):
    threshhold_prophet = df_prophet['y'].mean() + 3*df_prophet['y'].std()
    df_prophet = df_prophet[df_prophet['y'] < threshhold_prophet]
    return df_prophet

df_prophet = dataset_adjustment(df)
df_prophet = dataset_normalization(df_prophet)

m = Prophet()
m.fit(df_prophet)

future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)

st.write('Gráfico da previsão do modelo')
st.write(m.plot(forecast))
st.write(m.plot_components(forecast))

st.write('Selecionar o ano 2022 do dataset de previsão')
print(f"Área de queimada prevista para o ano de 2022: {forecast[forecast['ds'].dt.year == 2022].yhat.sum().round(2)} milhão de ha")

st.write('Tabela com os dados de previsão para o ano de 2022')
st.write(forecast[forecast['ds'].dt.year == 2022][['ds', 'yhat', 'yhat_lower', 'yhat_upper']])