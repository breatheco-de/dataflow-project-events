import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def to_dt(value):
    return datetime.strptime(value, '%m/%d/%Y %H:%M:%S')


# list of values in columns
expected_inputs = pd.DataFrame({
    "User_ID": ['U0426RW6CR5', 'U0426RW6CR5', 'U0426RW6CR5', 'ASDSDFSDF'],
    "Timestamp": [to_dt('11/11/2022 15:23:37'), to_dt('11/11/2022 15:25:37'), to_dt('11/11/2022 17:23:37'), to_dt('11/11/2022 17:24:37')],
    # "Timestamp_Thread": [to_dt('11/11/2022 15:23:37'), to_dt('11/11/2022 15:25:37'), to_dt('11/11/2022 17:23:37')],
    "Text": ["hola", 'papi', 'otro', 'lejos'],
})

# expected output
expected_output = pd.DataFrame({
    "User_ID": ['U0426RW6CR5', 'U0426RW6CR5'],
    "Timestamp": ['11/11/2022 15:23:37', '11/11/2022 17:23:37'],
    # "Timestamp_Thread": ['11/11/2022 15:23:37', '11/11/2022 17:23:37'],
    "Text": ['hola papi', 'otro'],
})


def run(df, stream=None):
    """
    This function takes care of dropping useless and null columns in registered dataset, and also dropping testing rows.
    """

    print('Shape before dropping columns', df.shape)

    # df['Time_diff'] = df['Timestamp'].diff(1)

    print('Shape after dropping columns', df.shape)

    return df
