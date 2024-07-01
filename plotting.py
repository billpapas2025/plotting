import streamlit as st
import pydeck as pdk

# Título de la aplicación
st.title('Mapa Interactivo con Pydeck y Streamlit')

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

# Crear el objeto del mapa
selected_coords = cities[selected_city]

# Crear un círculo alrededor de la ciudad seleccionada
circle_layer = pdk.Layer(
    "ScatterplotLayer",
    data=[{"position": selected_coords}],
    get_position="position",
    get_radius=1000,  # Radio en metros
    get_fill_color=[0, 0, 255, 160],  # Color azul
    pickable=True
)

# Crear marcadores para todas las ciudades
markers = pdk.Layer(
    "ScatterplotLayer",
    data=[{"name": city, "position": coords} for city, coords in cities.items()],
    get_position="position",
    get_radius=200,  # Radio en metros
    get_fill_color=[255, 0, 0, 160],  # Color rojo
    pickable=True
)

# Configurar la vista inicial del mapa
view_state = pdk.ViewState(
    latitude=selected_coords[0],
    longitude=selected_coords[1],
    zoom=10,
    pitch=0
)

# Crear el objeto del mapa
mapa = pdk.Deck(
    layers=[circle_layer, markers],
    initial_view_state=view_state,
    tooltip={"text": "{name}"}
)

# Mostrar el mapa en la aplicación Streamlit
st.pydeck_chart(mapa)
