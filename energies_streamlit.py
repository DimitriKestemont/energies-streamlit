import streamlit as st

st.title("Représentations de la production d'énergie solaire et éolienne")
st.subheader("Données de 2012 à 2023")

import pandas as pd

df_data_nationales = pd.read_pickle('df_data_nationales.pkl')

import plotly

print(f"Plotly version check: {plotly.__version__}")

df_complementaire = df_data_nationales[['Eolien', 'Solaire']]

df_complementaire_month = df_complementaire.resample('ME').sum()
df_complementaire_year = df_complementaire.resample('YE').sum()

st.badge("Les données par mois")
st.write(df_complementaire_month)

import plotly.graph_objects as go

period = df_complementaire_month.index
eolien = df_complementaire_month['Eolien']
solaire = df_complementaire_month['Solaire']

fig = go.Figure(data=[
    go.Bar(name='Eolien', x=period, y=eolien),
    go.Bar(name='Solaire', x=period, y=solaire)
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.update_layout(legend_title_text = "Production type")
fig.update_layout(title_text="Production d'energie éolien et solaire par mois")
fig.update_xaxes(title_text="Mois")
fig.update_yaxes(title_text="Production")
fig.update_layout(hovermode="x")
#fig.update_layout(hovermode="x unified")
fig.update_layout(title_font_lineposition="under")
fig.update_layout(title_font_color="gray")
fig.update_layout(title_font_family="monospace")
st.subheader("La complémentarité par mois")
st.write(fig)

st.subheader("Les données par ans")
st.write(df_complementaire_year)

period = df_complementaire_year.index
eolien = df_complementaire_year['Eolien']
solaire = df_complementaire_year['Solaire']

fig = go.Figure(data=[
    go.Bar(name='Eolien', x=period, y=eolien),
    go.Bar(name='Solaire', x=period, y=solaire)
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.update_layout(legend_title_text = "Production type")
fig.update_layout(title_text="Production d'energie éolien et solaire par ans")
fig.update_xaxes(title_text="Années")
fig.update_yaxes(title_text="Production")
#fig.update_layout(hovermode="x")
fig.update_layout(hovermode="x unified")
fig.update_layout(title_font_lineposition="under")
fig.update_layout(title_font_color="gray")
fig.update_layout(title_font_family="monospace")
st.badge("La complémentarité par ans")
st.write(fig)

st.write("Did you like this dashboard?")
st.feedback("faces")
st.feedback("stars")
st.feedback("thumbs")