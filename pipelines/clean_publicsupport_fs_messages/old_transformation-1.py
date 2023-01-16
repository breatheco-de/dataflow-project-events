import pandas as pd
import numpy as np
from datetime import datetime


def run(df):
    """
    This function cleans the initial dataframe.
    """
    
    print('Shape before cleaning initial dataframe', df.shape)

    
    #Creating 2 new columns
    df['Is_a_question'] = np.where(df['Timestamp_Thread'].isnull(), 1, 0)

    support_agent_ids = ['1','5301']
    support_agent_name = ['Alejandro Sanchez','Tomas Gonzalez']

    df['Is_agent'] = np.where(df['User_ID'].isin(support_agent_ids) | df['Full_Name'].isin(support_agent_name), 1, 0)

    #Encoding column
    df['Is_Bot'] = np.where(df['Is_Bot'] == True, 1, 0)

    #Converting timestamp column
    df['Datetime'] = pd.to_datetime(df['Timestamp'])
    df['Datetime_Thread'] = pd.to_datetime(df['Timestamp_Thread'])


    print('Shape after cleaning initial dataframe', df.shape)
    
    return df