import pandas as pd
import numpy as np
from datetime import datetime

def run(df):
    """
    This function takes care of dropping useless and null columns in both datasets, and also dropping testing rows.
    """
    #Useless columns
    TO_DROP_EVENTS = ['created_at','updated_at','organization_id']
    
    #Drop useless columns in events
    df.drop(TO_DROP_EVENTS, axis=1, inplace=True)

    #Drop null columns in events
    df.dropna(axis=1, how='all', inplace=True)