# -*- coding: utf-8 -*-
"""Ques7.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HHIVTGi2kI--UaDNHp0Euq3vq4AufyZO

#Question 12: Calculate Toll Rate
"""

def calculate_toll_rate(df):
    vehicle_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    for vehicle, coeff in vehicle_coefficients.items():
        df[vehicle] = df['distance'] * coeff

    return df

# Example usage
toll_rates_df = calculate_toll_rate(unrolled_df)
print(toll_rates_df)

