import pandas as pd
import numpy as np
from datetime import datetime

#inputs as lists
ids = [44, 30]
created_dates = ['ab','bc']
updated_dates = ['ab','bc']
organization_ids = ['ab','ab']
author_ids = np.full(2,np.nan)
eventbrite_organizer_ids = np.full(2,np.nan)
venue_ids = np.full(2,np.nan)

#expected input as dataframe
expected_inputs = pd.DataFrame({'id':ids, 'created_at':created_dates,'updated_at':updated_dates,'organization_id':organization_ids, 
                'author_id':author_ids,'eventbrite_organizer_id':eventbrite_organizer_ids,'venue_id':venue_ids})

#values for Output
output_ids= [44, 30]

#expected output
expected_output = pd.DataFrame({'id':output_ids})



def run(df):
    """
    This function takes care of dropping useless and null columns in events dataset.
    """
    print('data antes de transformacion',df)
    print('tipo antes de transformacion',type(df))
    print('Shape before dropping useless and null columns', df.shape)

    #Useless columns
    TO_DROP_EVENTS = ['created_at','updated_at','organization_id']

    #Drop useless columns in events
    df.drop(TO_DROP_EVENTS, axis=1, inplace=True)

    #Drop null columns in events
    df.dropna(axis=1, how='all', inplace=True)

    print('Shape after dropping useless and null columns', df.shape)

    return df

