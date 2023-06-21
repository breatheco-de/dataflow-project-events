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


def run(df, df2, df3):
    """
    This function takes care of merging both datasets, events and attendees.
    """
    print('Shape of df before merge', df.shape)
    print('Shape of df2 before merge', df2.shape)

    # Merge dataframes
    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id', 'excerpt',
                                                                          'eventbrite_sync_description', 'eventbrite_url',
                                                                          'eventbrite_id', 'banner'], axis=1)
    print('Shape of merged_df', merged_df.shape)

    # Convert to datetime once
    merged_df['starting_at'] = pd.to_datetime(merged_df['starting_at']).dt.tz_localize(None)
    merged_df['attended_at'] = pd.to_datetime(merged_df['attended_at']).dt.tz_localize(None)

    # Sort values
    merged_df = merged_df.sort_values(['email', 'starting_at'])

    # Identify new registrations
    first_events = merged_df.groupby('email').first().reset_index()
    first_events['is_new_register'] = True
    merged_df = merged_df.merge(first_events[['email', 'is_new_register']], on='email', how='left')
    merged_df['is_new_register'] = merged_df['is_new_register'].fillna(False)

    # Prepare df3
    df3 = df3.dropna(subset=['ac_deal_id'])
    df3['created_at'] = pd.to_datetime(df3['created_at']).dt.tz_localize(None)

    # Create dictionary for faster access
    first_created_dates_dict = df3.groupby('email')['created_at'].min().to_dict()

    # Calculate 'won_after_even' using vectorized operations
    attended_emails = merged_df['email']
    attended_at_dates = merged_df['attended_at']
    form_entry_dates = attended_emails.map(first_created_dates_dict)

    # Ensure that NaT values are handled correctly
    valid_dates_mask = attended_at_dates.notna() & form_entry_dates.notna()
    time_difference = (form_entry_dates - attended_at_dates).dt.days

    # Create 'won_after_even' column
    merged_df['won_after_even'] = (valid_dates_mask & (time_difference <= 15)).astype(int)

    return merged_df