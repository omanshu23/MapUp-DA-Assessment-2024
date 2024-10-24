# -*- coding: utf-8 -*-
"""Ques5.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HHIVTGi2kI--UaDNHp0Euq3vq4AufyZO

#Question 5: Find All Dates in a Text
"""

import re

def find_all_dates(text):
    date_patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',
        r'\b\d{2}/\d{2}/\d{4}\b',
        r'\b\d{4}\.\d{2}\.\d{2}\b'
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    return dates

# Test case
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))

