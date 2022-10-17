import pandas as pd
import numpy as np
from datetime import datetime

expected_input = [{
    'id': [35, 44, 30],
    'email': ['marketing@4geeksacademy.com','daniela@gmail.com','dani@outlook.com'],
    'created_at': ['2021-01-22 04:13:22.481858+00:00', '2021-01-22 04:13:22.481858+00:00','2021-01-22 04:13:22.481858+00:00'],
    'updated_at': ['2021-01-22 04:13:22.481892+00:00','2021-01-22 04:13:22.481892+00:00','2021-01-22 04:13:22.481892+00:00'],
    'event_id': [86,121,38],
    'status': ['PENDING','PENDING','PENDING'],
    'attended_at': ['NaN', 'NaN','NaN']
}]

expected_output = [{
    'email': ['daniela@gmail.com','dani@outlook.com'],
    'event_id': [121,38],
    'attended_at': ['NaN','NaN']
}]

def run(df):
    """
    This function takes care of dropping useless and null columns in registered dataset, and also dropping testing rows.
    """

    #Useless columns
    TO_DROP_REGISTERED = ['id', 'created_at','updated_at','status']

    #Drop useless columns in registered_in_events
    df.drop(TO_DROP_REGISTERED, axis=1, inplace=True)

    #Drop rows with test emails used for registration
    df = df[df["email"].str.contains("@4geeks") == False]