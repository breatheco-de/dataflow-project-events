import pandas as pd
import numpy as np
from datetime import datetime


#list of values in columns
ids = [44, 30]
created_dates = ['ab','bc']
updated_dates = ['ab','bc']
event_ids = [121,38]
status = ['ab','bc']
attended_dates = ['NaN','NaN']

#expected input
expected_inputs = [{'id': ids,'created_at':created_dates,'updated_at':updated_dates,'event_id':event_ids, 
                'status':status,'attended_at': attended_dates}]

#values for Output
output_event_ids = [121,38]
output_attended_dates = ['NaN','NaN']

#expected output
expected_output = [{'event_id':output_event_ids, 'attended_at':output_attended_dates}]


def run(df):
    """
    This function takes care of dropping useless and null columns in registered dataset, and also dropping testing rows.
    """

    print('Shape before dropping columns', df.shape)

    TO_DROP_REGISTERED = ['id', 'created_at','updated_at','status']

    #Drop useless columns in registered_in_events
    df.drop(TO_DROP_REGISTERED, axis=1, inplace=True)

    print('Shape after dropping columns', df.shape)
    
    return df