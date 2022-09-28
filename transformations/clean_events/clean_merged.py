import pandas as pd
import numpy as np
from datetime import datetime

def run(df3):
    
    #Clean dates

    #change type
    df3['starting_at'] = df3['starting_at'].apply(pd.to_datetime)
    df3['ending_at'] = df3['ending_at'].apply(pd.to_datetime)
    df3['published_at'] = df3['published_at'].apply(pd.to_datetime)

    #Changing format
    df3['starting_at'] = df3['starting_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df3['ending_at'] = df3['ending_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df3['published_at'] = df3['published_at'].dt.strftime('%Y-%m-%d %H:%M:%S')

    #Format change also changed the type to object, so we need to convert it to datetime again 
    df3['starting_at'] = df3['starting_at'].apply(pd.to_datetime)
    df3['ending_at'] = df3['ending_at'].apply(pd.to_datetime)
    df3['published_at'] = df3['published_at'].apply(pd.to_datetime)





    #Replacements

    #Replacing commas in certain columns
    df3['tags'] = df3['tags'].str.replace(',', ' ')
    df3['description'] = df3['description'].str.replace(',', ' ')
    df3['title'] = df3['title'].str.replace(',', ' ')

    #Replacing nulls with 'undefined'

    df3 = df3.replace(np.nan, 'Undefined', regex=True)





    #Assignations

    #Assign language to events with missing info.
    df3['lang'] = np.where((df3['event_id'].isin([35,36,38,40,414,37,130,123,41,122,141,42,146,125,145,46,48,47,49,131,
                                                        127,85,86,84,121,128,119,181,189,184,135,134,136,182,192,193,137,138,
                                                        139,186,195,198,217,196,213,203,212,205,204,209,211,218,262,339,268,
                                                        260,263,142,183,140,432,261,363,264,344,340,308,316])),'es', df3['lang'])

    df3['lang'] = np.where((df3['event_id'].isin([39,43,187,45,44,190,144,50,51,126,180,191,132,129,120,185,188,197,200,
                                                        194,199,201,202,206,216,208,252,214,251,254,368,357,124,207,210,215])),'en', df3['lang'])