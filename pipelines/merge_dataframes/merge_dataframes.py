import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = [pd.DataFrame({
    'email': ['aa','bb','cc'],
    'event_id': ['1','2','2']
}),

pd.DataFrame({
    'id': ['1', '2'],
    'title': ['aa','bb'],
    'excerpt':['aa','bb'],
    'eventbrite_sync_description':['aa','bb'],
    'eventbrite_url':['aa','bb'],
    'eventbrite_id':['aa','bb'],
    'banner':['aa','bb']
})]

expected_output = pd.DataFrame({
    'email': ['aa','bb','cc'],
    'event_id': ['1','2','2'],
    'title': ['aa','bb','bb']
})

def run(df, df2):
    """
    This function takes care of merging both datasets, events and attendees.
    """
    print('Shape of df before merge', df.shape)
    print('Shape of df2 before merge', df2.shape)
    print("Merging dataframes")

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id", how='left').drop(['id', 'excerpt',
                        'eventbrite_sync_description', 'eventbrite_url', 'eventbrite_id', 'banner'], axis=1)

    print("------------------------")
    print("Data types of merged_df:")
    print("------------------------")
    
    # Convert datetime fields
    datetime_columns = ['starting_at', 'attended_at', 'form_created_at', 'won_at']
    for field in datetime_columns:
        if field in merged_df.columns:  # Check if the field exists in merged_df
            merged_df[field] = pd.to_datetime(merged_df[field], errors="coerce")
            if merged_df[field].dt.tz is None:
                merged_df[field] = merged_df[field].dt.tz_localize('UTC', ambiguous='infer')
            else:
                merged_df[field] = merged_df[field].dt.tz_convert('UTC')

    print("Adding a new column")
    merged_df['is_new_registree'] = merged_df.groupby('email')['created_at'].transform(lambda x: x == x.min())

    # Print only the datetime columns
    print("------------------------")
    print("Datetime columns in merged_df:")
    print("------------------------")
    print(merged_df[datetime_columns].head())  # Display the first few rows of the datetime columns
    
    return merged_df
