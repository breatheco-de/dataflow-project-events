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

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id").drop(['id','excerpt',
                        'eventbrite_sync_description','eventbrite_url','eventbrite_id','banner'], axis=1)

    print('Shape of merged_df', merged_df.shape)
    
    # Making sure that 'starting_at', 'attended_at' and 'form_created_at' are datetime fields
    # Localizing to UTC if the object is timezone naive, otherwise converting to UTC timezone
    for field in ['starting_at', 'attended_at', 'form_created_at']:
        merged_df[field] = pd.to_datetime(merged_df[field])
        merged_df[field] = merged_df[field].dt.tz_localize('UTC', ambiguous='infer') if merged_df[field].dt.tz is None else merged_df[field].dt.tz_convert('UTC')
    
    # Sorting the dataframe by 'starting_at' column
    merged_df = merged_df.sort_values('starting_at')

    # Adding 'is_new_registree' column
    merged_df['is_new_registree'] = ~merged_df.duplicated('email')

    # Adding 'won_after_event' column
    merged_df['lead_after_event'] = (
        (merged_df['form_ac_deal_id'].notna()) &
        ((merged_df['form_created_at'] - merged_df['attended_at']).dt.days <= 15)
    )

    merged_df['won_at'] = merged_df['won_at'].apply(pd.to_datetime)

    return merged_df
