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
    This function takes care of dropping testing rows.
    """
    
    print('Shape before dropping test rows', df.shape)

    #Drop rows with test emails used for registration

    # Drop testing rows
    df = df[df["email"].str.contains("@4geeks") == False]
    df = df[df["email"].str.contains("@stcsolutions") == False]
    df = df[df["email"].str.contains("aalejo@gmail") == False]


    print('Shape after dropping test rows', df.shape)
    
    return df
