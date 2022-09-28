import pandas as pd
import numpy as np
from datetime import datetime

def run(df):
    """
    This function takes care of dropping useless and null columns in registered dataset, and also dropping testing rows.
    """

    #Useless columns
    TO_DROP_REGISTERED = ['id', 'created_at','updated_at','status']

    #Drop useless columns in registered_in_events
    df.drop(TO_DROP_REGISTERED, axis=1, inplace=True)

    #Drop null columns in registered
    df.dropna(axis=1, how='all', inplace=True)

    #Drop rows with test emails used for registration
    df = df2[df2["email"].str.contains("@4geeks") == False]