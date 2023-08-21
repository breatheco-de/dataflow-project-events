import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = pd.DataFrame({
    'starting_at': ['2020-10-14 16:30:00+00:00','2020-10-14 16:30:00+00:00'],
    'ending_at': ['2020-10-14 16:30:00+00:00','2020-10-14 16:30:00+00:00'],
    'published_at': ['2020-10-14 16:30:00+00:00','2020-10-14 16:30:00+00:00'],
    'attended_at': [np.nan,np.nan],
    'tags':['career-support,event-attendee','aa'],
    'description':['crea tu primera web con html,y css','aa'],
    'title': ['Html,y css','aa'],
    'event_id': [38,39],  
    'lang': [np.nan,np.nan]
})

expected_output = pd.DataFrame({
    'starting_at': [pd.to_datetime('2020-10-14 16:30:00'),pd.to_datetime('2020-10-14 16:30:00')],
    'ending_at': [pd.to_datetime('2020-10-14 16:30:00'),pd.to_datetime('2020-10-14 16:30:00')],
    'published_at': [pd.to_datetime('2020-10-14 16:30:00'),pd.to_datetime('2020-10-14 16:30:00')],
    'attended_at': ['Undefined','Undefined'],
    'tags':['career-support|event-attendee','aa'],
    'description':['crea tu primera web con html y css','aa'],
    'title':['Html y css','aa'],
    'event_id': [38,39],  
    'lang':['es','en']
})


def run(df):
    
    #Clean dates

    #change type
    df['starting_at'] = df['starting_at'].apply(pd.to_datetime)
    df['created_at'] = df['created_at'].apply(pd.to_datetime)
    df['ending_at'] = df['ending_at'].apply(pd.to_datetime)
    df['form_created_at'] = df['form_created_at'].apply(pd.to_datetime)
    df['published_at'] = df['published_at'].apply(pd.to_datetime)
    df['attended_at'] = df['attended_at'].apply(pd.to_datetime)

    #Changing format
    df['starting_at'] = df['starting_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['created_at'] = df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['ending_at'] = df['ending_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['form_created_at'] = df['form_created_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['attended_at'] = df['attended_at'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['published_at'] = df['published_at'].dt.strftime('%Y-%m-%d %H:%M:%S')

    #Format change also changed the type to object, so we need to convert it to datetime again 
    df['starting_at'] = df['starting_at'].apply(pd.to_datetime)
    df['created_at'] = df['created_at'].apply(pd.to_datetime)
    df['ending_at'] = df['ending_at'].apply(pd.to_datetime)
    df['published_at'] = df['published_at'].apply(pd.to_datetime)
    df['form_created_at'] = df['form_created_at'].apply(pd.to_datetime)
    df['attended_at'] = df['attended_at'].apply(pd.to_datetime)


    #Replacements

    #Replacing commas in certain columns
    df['tags'] = df['tags'].str.replace(',', '|')
    df['description'] = df['description'].str.replace(',', ' ')
    df['title'] = df['title'].str.replace(',', ' ')

    #Replacing nulls with 'undefined'

    df = df.replace(np.nan, 'Undefined', regex=True)


    #Assignations

    #Assign language to events with missing info.
    df['lang'] = np.where((df['event_id'].isin([35,36,38,40,414,37,130,123,41,122,141,42,146,125,145,46,48,47,49,131,
                                                        127,85,86,84,121,128,119,181,189,184,135,134,136,182,192,193,137,138,
                                                        139,186,195,198,217,196,213,203,212,205,204,209,211,218,262,339,268,
                                                        260,263,142,183,140,432,261,363,264,344,340,308,316])),'es',
                                                        df['lang'])

    df['lang'] = np.where((df['event_id'].isin([39,43,187,45,44,190,144,50,51,126,180,191,132,129,120,185,188,197,200,
                                                        194,199,201,202,206,216,208,252,214,251,254,368,357,124,207,210,215])),'en', 
                                                        df['lang'])


    return df

    
