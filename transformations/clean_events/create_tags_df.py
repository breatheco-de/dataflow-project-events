import pandas as pd
import numpy as np
from datetime import datetime

def run(merged_df):
    
    #create a event tags dataframe to explode tags

    tags_df = merged_df.groupby(['event_id','title','tags'])['tags'].agg(['count']).reset_index()

    tags_df.rename(columns = {'count':'event_registrants'}, inplace = True)

    #converting tags column in lowercase and then in a list instead of string

    tags_df['tags'] = tags_df['tags'].str.lower()

    tags_df['tags'] = tags_df.tags.apply(lambda x: x.split('|'))

    #Exploding the list to rows

    tags_df = tags_df.explode('tags').drop_duplicates()

