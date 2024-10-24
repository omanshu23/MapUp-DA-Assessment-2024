# -*- coding: utf-8 -*-
"""Ques5.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HHIVTGi2kI--UaDNHp0Euq3vq4AufyZO

#Question 6: Decode Polyline, Convert to DataFrame with Distances
"""

import polyline

# Coordinates for Balaghat, MP, India
coordinates = [(21.8156, 80.1885)]  # Latitude and Longitude of Balaghat

# Encode the coordinates into a polyline string
encoded_polyline = polyline.encode(coordinates)
print(encoded_polyline)

import pandas as pd
import polyline
from geopy.distance import geodesic

def decode_polyline(polyline_str):
    # Decode the polyline string into a list of (latitude, longitude) tuples
    coordinates = polyline.decode(polyline_str)

    # Create a DataFrame with latitude and longitude
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])

    # Calculate distances using the Haversine formula
    df['distance'] = [0] + [geodesic(df.iloc[i], df.iloc[i - 1]).meters for i in range(1, len(df))]

    return df

# Example usage
polyline_str = "ozcdCcylhN"
df = decode_polyline(polyline_str)
print(df)

