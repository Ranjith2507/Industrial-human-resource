import streamlit as st
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load the dataset

data_files = sorted(glob('/content/drive/MyDrive/data/*.csv'))

df = pd.concat(pd.read_csv(datafile, encoding=('ISO-8859-1'),low_memory =False).assign(sourcefilename = datafile) for datafile in data_files)
department=['Main Workers-Total-Persons,Marginal Workers-Total-Persons,Marginal Workers-Rural-Persons,Marginal Workers-Urban-Persons']
job_title=['Main Workers-Total-Males,Main Workers-Total-Females,Marginal Workers-Total-Males,Marginal Workers-Total-Females,Marginal Workers-Rural-Males,Marginal Workers-Rural-Females,Marginal Workers-Urban-Males,Marginal Workers-Urban-Females']


# Sidebar filters
st.sidebar.header("Filters")
department = st.sidebar.selectbox("Department", data["Department"].unique())
job_title = st.sidebar.selectbox("Job Title", data["Job Title"].unique())

# Apply filters
filtered_data = data[(data["Department"] == department) & (data["Job Title"] == job_title)]

# Show filtered data
st.write(filtered_data)

# Map visualization
st.header("Geo-Visualization")
location_data = filtered_data[["Latitude", "Longitude"]].dropna()

# Create a folium map centered at the mean location
center_latitude = location_data["Latitude"].mean()
center_longitude = location_data["Longitude"].mean()
map = folium.Map(location=[center_latitude, center_longitude], zoom_start=10)

# Add markers for each employee
for index, row in location_data.iterrows():
    folium.Marker([row["Latitude"], row["Longitude"]]).add_to(map)

# Render the map
st.markdown(map._repr_html_(), unsafe_allow_html=True)