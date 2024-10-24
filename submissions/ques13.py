# -*- coding: utf-8 -*-
"""Ques13.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HHIVTGi2kI--UaDNHp0Euq3vq4AufyZO

#Question 13: Calculate Time-Based Toll Rates
"""

import pandas as pd

def calculate_time_based_toll_rates(toll_rates_df, distance_df):
    print("Unique startDay values:", toll_rates_df['startDay'].unique())
    print("Unique startTime values:", toll_rates_df['startTime'].unique())

    toll_rates_df['startDay'] = toll_rates_df['startDay'].str.strip()
    toll_rates_df['startTime'] = toll_rates_df['startTime'].str.strip()

    toll_rates_df['start_datetime'] = pd.to_datetime(
        toll_rates_df['startDay'] + ' ' + toll_rates_df['startTime'],
        format='%A %H:%M:%S',
        errors='coerce'
    )

    if toll_rates_df['start_datetime'].isnull().any():
        print(toll_rates_df[toll_rates_df['start_datetime'].isnull()])
        raise ValueError("There are invalid dates in the dataset. Please check startDay and startTime formats.")

    toll_rates_df['start_day'] = toll_rates_df['start_datetime'].dt.day_name()
    toll_rates_df['start_time'] = toll_rates_df['start_datetime'].dt.time

    weekday_intervals = [
        (pd.Timestamp('00:00:00').time(), pd.Timestamp('10:00:00').time(), 0.8),
        (pd.Timestamp('10:00:00').time(), pd.Timestamp('18:00:00').time(), 1.2),
        (pd.Timestamp('18:00:00').time(), pd.Timestamp('23:59:59').time(), 0.8)
    ]

    weekend_discount = 0.7

    vehicle_types = ['moto', 'car', 'rv', 'bus', 'truck']
    for vehicle in vehicle_types:
        toll_rates_df[vehicle] = 1.0

    for i, row in toll_rates_df.iterrows():
        if row['start_day'] in ['Saturday', 'Sunday']:
            toll_rates_df.loc[i, vehicle_types] *= weekend_discount
        else:
            for interval in weekday_intervals:
                if interval[0] <= row['start_time'] <= interval[1]:
                    toll_rates_df.loc[i, vehicle_types] *= interval[2]
                    break

    toll_rates_df.drop(columns=['start_datetime', 'start_day', 'start_time'], inplace=True)

    return toll_rates_df

toll_rates_df = pd.read_csv('/content/dataset-1.csv')
distance_df = pd.read_csv('/content/dataset-2.csv')

time_based_toll_rates_df = calculate_time_based_toll_rates(toll_rates_df, distance_df)
print(time_based_toll_rates_df)

