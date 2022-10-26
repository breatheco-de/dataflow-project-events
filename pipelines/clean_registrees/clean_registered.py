import pandas as pd
import numpy as np
from datetime import datetime


TO_DROP_REGISTERED = ['id', 'created_at','updated_at','status']

#list of values in columns

ids = [35, 44, 30]
emails = ['marketing@4geeksacademy.com','daniela@gmail.com','dani@outlook.com']
created_dates = ['2021-01-22 04:13:22.481858+00:00', '2021-01-22 04:13:22.481858+00:00','2021-01-22 04:13:22.481858+00:00']
updated_dates = ['2021-01-22 04:13:22.481892+00:00','2021-01-22 04:13:22.481892+00:00','2021-01-22 04:13:22.481892+00:00']
event_ids = [86,121,38]
status = ['PENDING','PENDING','PENDING']
attended_dates = ['NaN', 'NaN','NaN']


#expected input as dataframe
expected_inputs = [{'id': ids,'email':emails,'created_at':created_dates,'updated_at':updated_dates,'event_id':event_ids, 'status':status,
        'attended_at': attended_dates}]

#values for Output

output_emails = ['daniela@gmail.com','dani@outlook.com']
output_event_ids = [121,38]
output_attended_dates = ['NaN','NaN']

#expected output
expected_output = [{'email':output_emails, 'event_id':output_event_ids, 'attended_at':output_attended_dates}]



def run(df):
    """
    This function takes care of dropping useless and null columns in registered dataset, and also dropping testing rows.
    """

    TO_DROP_REGISTERED = ['id', 'created_at','updated_at','status']

    #Drop useless columns in registered_in_events
    df.drop(TO_DROP_REGISTERED, axis=1, inplace=True)

    #Drop rows with test emails used for registration

    df.drop(df[df['email'].str.contains('@4geeks')].index)
    
    return df