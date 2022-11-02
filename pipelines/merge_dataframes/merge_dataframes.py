import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = [[{
    'email': ['aa','bb'],
    'event_id': ['aa','bb'],
    'attended_at': ['NaN','NaN']
}],

[{
    'id': ['aa', 'bb'],
    'title': ['aa','bb'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
}]]

expected_output = [{
    'email': ['aa','bb'],
    'event_id': ['aa','bb'],
    'attended_at': ['NaN','NaN'],
    'title': ['aa','bb']
}]


def run(df,df2):
    """
    This function takes care of merging both datasets, events and attendies.
    """


    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                        'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)

    return merged_df