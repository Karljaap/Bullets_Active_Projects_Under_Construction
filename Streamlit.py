import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

"""
# Data Description
This dataset provides information about school projects currently under construction in New York City, including new schools (Capacity) and Capital Improvement Projects (CIP).
The data is collected and maintained by the School Construction Authority (SCA) and is updated quarterly. It has been publicly available since October 9, 2011.

# Dictionary Column
| **Column Name**       | **Description**                                              | **API Field Name**      | **Data Type**      |
|----------------------|----------------------------------------------------------|----------------------|-------------------|
| **School Name**           | Name of the school                                      | `name`                 | Text             |
| **BoroughCode**           | Borough code where the school is located              | `boro`                 | Text             |
| **Geographical District** | District where the school is located                  | `geo_dist`             | Number           |
| **Project Description**   | Description of the construction work                  | `projdesc`             | Text             |
| **Construction Award**    | Value of the prime construction contract              | `award`                | Number           |
| **Project Type**         | Identifies whether the project is **CIP** or **Capacity** | `constype`             | Text             |
| **Building ID**           | Unique identifier of the building                     | `buildingid`           | Text             |
| **Building Address**      | Address of the building under construction            | `building_address`     | Text             |
| **City**                 | City where the project is located                      | `city`                 | Text             |
| **Borough**              | Name of the borough where the school is located       | `borough`              | Text             |
| **Latitude**             | Latitude of the site location                         | `latitude`             | Number           |
| **Longitude**            | Longitude of the site location                        | `longitude`            | Number           |
| **Community Board**      | NYC community district associated with the site      | `community_board`      | Number           |
| **Council District**     | NYC City Council district where the site is located  | `community_council`    | Number           |
| **BIN**                 | Building Identification Number (BIN)                  | `bin`                  | Number           |
| **BBL**                 | Borough, Block, and Lot number (BBL)                  | `bbl`                  | Number           |
| **Census Tract (2020)**  | Census tract where the site is located (Census 2020) | `census_tract`         | Number           |
| **Neighborhood Tabulation Area (NTA) (2020)** | NYC Neighborhood Tabulation Area (Census 2020) | `nta`                  | Text             |
| **Location 1**           | System-generated column for mapping representation   | `location_1`           | Location         |
"""


# Load the CSV data file
def load_data(path):
    return pd.read_csv(path)


DATA_PATH = "all_data.csv"
df = load_data(DATA_PATH)


# Create a map focused on New York City with a school-related icon
def create_map(data):
    nyc_coordinates = [40.7128, -74.0060]  # Center of New York City
    mapa = folium.Map(location=nyc_coordinates, zoom_start=12, tiles="OpenStreetMap")

    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<b>{row['name']}</b><br>{row['projdesc']}<br>Lat: {row['latitude']}, Lon: {row['longitude']}",
            tooltip=f"{row['name']} ({row['latitude']}, {row['longitude']})",
            icon=folium.Icon(icon="graduation-cap", prefix="fa", color="blue")
        ).add_to(mapa)

    return mapa


# Display the map in Streamlit
st.title("Interactive Map of NYC School Construction Projects")
st_folium(create_map(df), width=700, height=500)
