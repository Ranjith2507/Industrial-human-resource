# -*- coding: utf-8 -*-
"""hum_res.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hlQUKJ334YSjkNRfm_wBZV152J6moCVw
"""

!pip install streamlit pandas folium

import streamlit as st
import pandas as pd
import folium

# Load the industrial human resources data
data_files = pd.read_csv('/content/drive/MyDrive/data/*.csv')

#df = pd.concat(pd.read_csv(datafile, encoding=('ISO-8859-1'),low_memory =False).assign(sourcefilename = datafile) for datafile in data_files)

Latitude=['Main Workers-Total-Persons,Marginal Workers-Total-Persons,Marginal Workers-Rural-Persons,Marginal Workers-Urban-Persons,Main Workers-Total-Males,Main Workers-Total-Females']
Longitude=['Marginal Workers-Total-Males,Marginal Workers-Total-Females,Marginal Workers-Rural-Males,Marginal Workers-Rural-Females,Marginal Workers-Urban-Males,Marginal Workers-Urban-Females']


# Create a Streamlit app
st.title('Industrial Human Resources Geo-Visualization')

# Filter options
department_options = sorted(data_files['Department'].unique())
selected_department = st.sidebar.selectbox('Select Department', department_options)

# Filter the data based on selected department
filtered_data = data_files[data_files['Department'] == selected_department]

# Display the filtered data
st.subheader('Department: {}'.format(selected_department))
st.dataframe(filtered_data)

# Create a map centered on the filtered data
center_lat = filtered_data['Latitude'].mean()
center_lon = filtered_data['Longitude'].mean()
map_data = filtered_data[['Latitude', 'Longitude']]
marker_cluster = folium.plugins.MarkerCluster().add_to(folium.Map(location=[center_lat, center_lon], zoom_start=12))

# Add markers to the map
for index, row in map_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(marker_cluster)

# Render the map in Streamlit
st.subheader('Geospatial Distribution')
folium_static_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
folium_static_map.add_child(marker_cluster)
st.markdown(folium_static_map._repr_html_(), unsafe_allow_html=True)