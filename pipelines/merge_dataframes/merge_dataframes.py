import pandas as pd
import numpy as np
from datetime import datetime

expected_input = [[{
    'email': ['daniela@gmail.com','dani@outlook.com'],
    'event_id': [121,38],
    'attended_at': ['NaN','NaN']
}],

[{
    'id': [121, 38],
    'title': ['Crea un producto','Hola'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
}]]

expected_output = [{
    'email': ['daniela@gmail.com','dani@outlook.com'],
    'event_id': [121,38],
    'attended_at': ['NaN','NaN'],
    'title': ['Crea un producto','Hola']
}]


def run(df,df2):
    """
    This function takes care of merging both datasets, events and attendies.
    """


    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                        'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)

    return merged_df