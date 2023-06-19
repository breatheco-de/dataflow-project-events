import pandas as pd
import random
from datetime import datetime, timedelta


def run(df,df2, df3):
    """
    This function takes care of merging both datasets, events and attendies.
    """
    # print('Shape of df before merge', df.shape)
    # print('Shape of df2 before merge', df2.shape)

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id'], axis=1)


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
    print(won_after_event_counts)

    return merged_df
        
# Create mock data for df
df_data = {
    'event_id': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
    'email': ['john@example.com', 'mary@example.com', 'john@example.com', 'adam@example.com', 'mary@example.com',
              'adam@example.com', 'john@example.com', 'adam@example.com', 'mary@example.com', 'adam@example.com'],
    'starting_at': [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3), datetime(2023, 1, 4),
                     datetime(2023, 1, 5), datetime(2023, 1, 6), datetime(2023, 1, 7), datetime(2023, 1, 8),
                     datetime(2023, 1, 9), datetime(2023, 1, 10)],
    'attended_at': [datetime(2023, 1, 3), datetime(2023, 1, 4), datetime(2023, 1, 4), datetime(2023, 1, 6),
                    datetime(2023, 1, 6), datetime(2023, 1, 6), datetime(2023, 1, 9), datetime(2023, 1, 9),
                    datetime(2023, 1, 9), datetime(2023, 1, 9)]
}

df = pd.DataFrame(df_data)

# Create mock data for df2
df2_data = {
    'id': [1, 2, 3, 4],
    'location': ['New York', 'San Francisco', 'Chicago', 'Los Angeles']
}

df2 = pd.DataFrame(df2_data)

# Create mock data for df3
df3_data = {
    'email': ['john@example.com', 'mary@example.com', 'adam@example.com'],
    'ac_deal_id': [None, 2, 3],
    'created_at': [datetime(2023, 1, 2), datetime(2023, 1, 3), datetime(2023, 1, 5)]
}

df3 = pd.DataFrame(df3_data)

# Call the run function with the mock data
result = run(df, df2, df3)