import pandas as pd

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
    '''
    This transformation pretends to add two new columns to the first dataframe.

    A new column called: is_new_register: boolean that indicates if its the first event
    attended by an user (email)

    A second column called won_after_event: boolean that indicates if the user has an ac_deal_id
    up to 15 days from the first event attended, this can be checked using the created_at of the df2,
    also needs to check that the email doesn't already had a form entry before the event
    
    '''
    print(df.columns, "first dataframe, merged")
    # df main columns: email, event_id, starting_at
    print(df2.columns, "second dataframe, form entries")
    # df2 main columns: email, created_at, ac_deal_id

    # Replace "Undefined" with NaN in attended_at column
    df.loc[df['attended_at'] == 'Undefined', 'attended_at'] = pd.NaT
    
    df['starting_at'] = pd.to_datetime(df['starting_at']).dt.tz_localize(None)
    df['attended_at'] = pd.to_datetime(df['attended_at']).dt.tz_localize(None)
    
    # Sort values in merged dataframe with respective of email and starting at of event
    df = df.sort_values(['email', 'starting_at'])

    # Identify new registrations
    first_events = df.groupby('email')['starting_at'].idxmin()  # Get index of first event for each user

    # Create 'is_new_register' column
    df['is_new_register'] = df.index.isin(first_events)  # isin() checks if df.index is in first_events

    # Prepare df2
    df2 = df2.dropna(subset=['ac_deal_id'])
    df2['created_at'] = pd.to_datetime(df2['created_at']).dt.tz_localize(None)

    # Create dictionary for faster access, this is the creation of the form entry
    first_created_dates_dict = df2.groupby('email')['created_at'].min().to_dict()

    # Calculate 'won_after_even' using vectorized operations
    attended_emails = df['email']
    attended_at_dates = df['attended_at']
    form_entry_dates = attended_emails.map(first_created_dates_dict)

    # Ensure that NaT values are handled correctly
    valid_dates_mask = attended_at_dates.notna() & form_entry_dates.notna()
    time_difference = (form_entry_dates - attended_at_dates).dt.days


    # This column means that the form entry for that email was created up to 15 days 
    # after the attendance of the event
    df['won_after_even'] = (valid_dates_mask & (time_difference <= 15)).astype(int)

    return df
