import streamlit as st
import folium
from streamlit_folium import st_folium

# Título de la aplicación
st.title('Mapa Interactivo con Folium y Streamlit')

# Descripción de la aplicación
st.markdown("""
Esta aplicación permite seleccionar una ciudad para visualizar en el mapa interactivo. 
Puedes ver marcadores en diferentes ubicaciones y un círculo en la ciudad seleccionada.
""")

# Lista de ciudades con coordenadas
cities = {
    "Nueva York": [40.7128, -74.0060],
    "San Francisco": [37.7749, -122.4194],
    "Los Angeles": [34.0522, -118.2437],
    "Chicago": [41.8781, -87.6298],
    "Miami": [25.7617, -80.1918]
}

# Selección de ciudad
selected_city = st.selectbox("Selecciona una ciudad", list(cities.keys()))

# Crear un mapa de Folium centrado en la ciudad seleccionada
mapa = folium.Map(location=cities[selected_city], zoom_start=10)

# Agregar marcador en la ciudad seleccionada
folium.Marker(cities[selected_city], popup=selected_city).add_to(mapa)

# Agregar un círculo en la ciudad seleccionada
folium.Circle(
    location=cities[selected_city],
    radius=1000,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(mapa)

# Mostrar el mapa en la aplicación Streamlit
st_folium(mapa, width=700, height=500)

# Agregar marcadores en otras ciudades
for city, coords in cities.items():
    if city != selected_city:
        folium.Marker(coords, popup=city).add_to(mapa)

# Mostrar el mapa actualizado en la aplicación Streamlit
st_folium(mapa, width=700, height=500)
