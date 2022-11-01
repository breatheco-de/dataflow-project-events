import pandas as pd
import numpy as np
from datetime import datetime

#inputs as lists
ids = [44, 30]
created_dates = ['ab','bc']
updated_dates = ['ab','bc']
organization_ids = ['ab','ab']
author_ids = ['NaN','NaN']
eventbrite_organizer_ids = ['NaN','NaN']
venue_ids = ['NaN','NaN']

#expected input as dataframe
expected_inputs = [{'id':ids, 'created_at':created_dates,'updated_at':updated_dates,'organization_id':organization_ids, 
                'author_id':author_ids,'eventbrite_organizer_id':eventbrite_organizer_ids,'venue_id':venue_ids}]

#values for Output
output_ids= [44, 30]

#expected output
expected_output = [{'id':output_ids}]



def run(df2):
    """
    This function takes care of dropping useless and null columns in events dataset.
    """
  
    print('Shape before dropping useless and null columns', df2.shape)

    #Useless columns
    TO_DROP_EVENTS = ['created_at','updated_at','organization_id']

    #Drop useless columns in events
    df2.drop(TO_DROP_EVENTS, axis=1, inplace=True)

    #Drop null columns in events
    df2 = df2.dropna(axis=1, how='all')

    print('Shape after dropping useless and null columns', df2.shape)

    return df2

