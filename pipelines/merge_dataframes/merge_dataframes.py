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


def run(df,df2, df3):
    """
    This function takes care of merging both datasets, events and attendies.
    """
    # print('Shape of df before merge', df.shape)
    # print('Shape of df2 before merge', df2.shape)

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                        'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)


    merged_df['starting_at'] = pd.to_datetime(merged_df['starting_at'])
    merged_df = merged_df.sort_values(['email', 'starting_at'])

    # Get first events for each email
    first_events = merged_df.groupby('email').first().reset_index()


    # Count new persons registered per event
    new_persons = first_events['event_id'].value_counts().reset_index()
    new_persons.columns = ['event_id', 'New persons registered']

    # Merge new_persons column into original dataframe
    merged_df = merged_df.merge(new_persons, on='event_id', how='left')

    # I want to obtain the first form entry for each email
    df3 = df3.dropna(subset=['ac_deal_id'])
    df3['created_at'] = pd.to_datetime(df3['created_at'])

    first_created_dates = df3.groupby('email')['created_at'].min()


    merged_df['won_after_even'] = False  # Initialize 'won_after_even' column with False values

    df3['created_at'] = pd.to_datetime(df3['created_at']).dt.tz_localize(None)

    merged_df['starting_at'] = pd.to_datetime(merged_df['starting_at']).dt.tz_localize(None)
    merged_df['attended_at'] = pd.to_datetime(merged_df['attended_at']).dt.tz_localize(None)  # Added timezone localization 
    

    for index, row in merged_df.iterrows():
        email = row['email']
        event_start = row['attended_at'] 
        form_entry_created = first_created_dates.get(email)

        # Check if 'attended_at' is not NaT
        if pd.notnull(event_start) and form_entry_created is not None:
            time_difference = form_entry_created - event_start
            if time_difference.days <= 15:
                merged_df.at[index, 'won_after_even'] = True

    won_after_event_counts = merged_df[merged_df['won_after_even']].groupby('event_id').size()
    # Convert 'won_after_event' to int for proper summation
    merged_df['won_after_even'] = merged_df['won_after_even'].astype(int)

    summary_df = merged_df.groupby('event_id').agg({'won_after_even': 'sum'}).reset_index()
    
    summary_df = merged_df.groupby('event_id').agg({
    'won_after_even': 'sum',
    'New persons registered': 'first'  # assuming 'New persons registered' is same for all rows of an 'event_id'
    }).reset_index()

    print(summary_df['event_id'].duplicated().any())
    return merged_df
        