import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = pd.DataFrame({
    'starting_at': ['2020-10-14 16:30:00+00:00', '2020-10-14 16:30:00+00:00'],
    'ending_at': ['2020-10-14 16:30:00+00:00', '2020-10-14 16:30:00+00:00'],
    'published_at': ['2020-10-14 16:30:00+00:00', '2020-10-14 16:30:00+00:00'],
    'attended_at': [np.nan, np.nan],
    'tags': ['career-support,event-attendee', 'aa'],
    'description': ['crea tu primera web con html,y css', 'aa'],
    'title': ['Html,y css', 'aa'],
    'event_id': [38, 39],
    'lang': [np.nan, np.nan]
})

expected_output = pd.DataFrame({
    'starting_at': [pd.to_datetime('2020-10-14 16:30:00'), pd.to_datetime('2020-10-14 16:30:00')],
    'ending_at': [pd.to_datetime('2020-10-14 16:30:00'), pd.to_datetime('2020-10-14 16:30:00')],
    'published_at': [pd.to_datetime('2020-10-14 16:30:00'), pd.to_datetime('2020-10-14 16:30:00')],
    'attended_at': ['Undefined', 'Undefined'],
    'tags': ['career-support|event-attendee', 'aa'],
    'description': ['crea tu primera web con html y css', 'aa'],
    'title': ['Html y css', 'aa'],
    'event_id': [38, 39],
    'lang': ['es', 'en']
})

def run(df):
    print("Changing columns datatype...")

    # Print the initial state of the DataFrame
    print("Initial DataFrame:")
    print(df.head())

    # Change type for datetime columns only if not already datetime
    datetime_columns = ['starting_at', 'ending_at', 'published_at', 'attended_at', 'form_created_at', 'won_at']
    for column in datetime_columns:
        if column in df.columns:
            if not pd.api.types.is_datetime64_any_dtype(df[column]):
                print(f"Converting column '{column}' to datetime...")
                df[column] = pd.to_datetime(df[column], errors='coerce')
                print(f"Conversion complete. Null values in '{column}': {df[column].isnull().sum()}")
            else:
                print(f"Column '{column}' is already in datetime format. No conversion needed.")

    print("Columns converted successfully.")

    # Change datetime formats
    print("Changing datetime formats...")
    for column in datetime_columns:
        if column in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[column]):
                df[column] = df[column].dt.strftime('%Y-%m-%d %H:%M')
                print(f"Column '{column}' formatted. Sample data: {df[column].head()}")
            else:
                print(f"Column '{column}' is not in datetime format. Skipping formatting.")

    # Change format back to datetime if needed
    print("Changing format back to datetime...")
    for column in datetime_columns:
        if column in df.columns:
            if pd.api.types.is_string_dtype(df[column]):
                df[column] = pd.to_datetime(df[column], errors='coerce')
                print(f"Column '{column}' converted back to datetime. Null values now: {df[column].isnull().sum()}")

    # Replacements
    print("Replacing commas in certain columns...")
    df['tags'] = df['tags'].str.replace(',', '|')
    df['description'] = df['description'].str.replace(',', ' ')
    df['title'] = df['title'].str.replace(',', ' ')

    print("Replacements complete. Sample tags: ", df['tags'].head())

    # Handle nulls
    print("Replacing nulls with 'Undefined' in attended_at...")
    df['attended_at'].fillna('Undefined', inplace=True)

    print("Nulls replaced. Sample attended_at: ", df['attended_at'].head())

    # Assignations
    print("Assigning languages based on event_id...")
    df['lang'] = np.where((df['event_id'].isin([35, 36, 38, 40, 414, 37, 130, 123, 41, 122, 141, 42, 146, 125, 145, 46, 48, 47, 49, 131,
                                                  127, 85, 86, 84, 121, 128, 119, 181, 189, 184, 135, 134, 136, 182, 192, 193, 137, 138,
                                                  139, 186, 195, 198, 217, 196, 213, 203, 212, 205, 204, 209, 211, 218, 262, 339, 268,
                                                  260, 263, 142, 183, 140, 432, 261, 363, 264, 344, 340, 308, 316])),'es',
                                                  df['lang'])

    df['lang'] = np.where((df['event_id'].isin([39, 43, 187, 45, 44, 190, 144, 50, 51, 126, 180, 191, 132, 129, 120, 185, 188, 197, 200,
                                                  194, 199, 201, 202, 206, 216, 208, 252, 214, 251, 254, 368, 357, 124, 207, 210, 215])),'en',
                                                  df['lang'])

    print("Language assignment complete. Sample languages: ", df['lang'].head())

    return df