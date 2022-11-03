import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = pd.DataFrame({
    'email': ['daniela@gmail.com'],
    'event_id': [38],
    'title': ['Html y css'],
    'tags': ['Career-support|Event-attendee']
})

expected_output = pd.DataFrame({
    'event_id': [38,38],
    'title': ['Html y css','Html y css'],
    'tags': ['career-support','event-attendee'],
    'event_registrants': [1,1]
})


def run(df):
    
    #create a event tags dataframe to explode tags

    tags_df = df.groupby(['event_id','title','tags'])['tags'].agg(['count']).reset_index()

    tags_df.rename(columns = {'count':'event_registrants'}, inplace = True)

    #converting tags column in lowercase and then in a list instead of string

    tags_df['tags'] = tags_df['tags'].str.lower()

    tags_df['tags'] = tags_df.tags.apply(lambda x: x.split('|'))

    #Exploding the list to rows

    tags_df = tags_df.explode('tags').drop_duplicates()

    return tags_df

