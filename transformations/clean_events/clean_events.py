import pandas as pd
import numpy as np
from datetime import datetime

expected_input = [{
    'id': [121, 38],
    'title': ['Crea un producto','Hola']
    'created_at': ['2020-10-14 16:30:00+00:00','2020-10-14 16:30:00+00:00'],
    'updated_at': ['2020-10-14 16:30:00+00:00','2020-10-14 16:30:00+00:00'],
    'organization_id': [35, 34],
    'author_id': ['NaN','NaN'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
}]

expected_output = [{
    'id': [121, 38],
    'title': ['Crea un producto','Hola'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
}]


def run(df2):
    """
    This function takes care of dropping useless and null columns in events dataset.
    """
    #Useless columns
    TO_DROP_EVENTS = ['created_at','updated_at','organization_id']
    
    #Drop useless columns in events
    df2.drop(TO_DROP_EVENTS, axis=1, inplace=True)

    #Drop null columns in events
    df2.dropna(axis=1, how='all', inplace=True)