import pandas as pd
import numpy as np
from datetime import datetime

emails= ['a@4geeksacademy.com', 'd@gmail.com', 'bc', 'c@gmail.com']


dict = {'email':emails}

#expected input as dataframe
expected_inputs = pd.DataFrame(dict)

#values for Output
output_emails = ['d@gmail.com', 'bc', 'c@gmail.com']

#expected output
expected_output = pd.DataFrame({'email':output_emails})


def run(df):
    """
    This function cleans the initial dataframe.
    """
    
    print('Shape before cleaning initial dataframe', df.shape)

    
    #Creating 2 new columns
    df['Is_a_question'] = np.where(df['Timestamp_Thread'].isnull(), 1, 0)

    support_agents = ['1','5301']
    df['Is_agent'] = np.where(df['User_ID'].isin(support_agents), 1, 0)

    #Encoding column
    df['Is_Bot'] = np.where(df['Is_Bot'] == True, 1, 0)

    #Converting timestamp column
    df['Datetime'] = pd.to_datetime(df['Timestamp'])
    df['Datetime_Thread'] = pd.to_datetime(df['Timestamp_Thread'])


    print('Shape after cleaning initial dataframe', df.shape)
    
    return df


