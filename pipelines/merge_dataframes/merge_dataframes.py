import pandas as pd
import numpy as np
from datetime import datetime

expected_inputs = [
    pd.DataFrame({"email": ["aa", "bb", "cc"], "event_id": ["1", "2", "2"]}),
    pd.DataFrame(
        {
            "id": ["1", "2"],
            "title": ["aa", "bb"],
            "excerpt": ["aa", "bb"],
            "eventbrite_sync_description": ["aa", "bb"],
            "eventbrite_url": ["aa", "bb"],
            "eventbrite_id": ["aa", "bb"],
            "banner": ["aa", "bb"],
        }
    ),
]

expected_output = pd.DataFrame(
    {
        "email": ["aa", "bb", "cc"],
        "event_id": ["1", "2", "2"],
        "title": ["aa", "bb", "bb"],
    }
)


def run(df, df2):
    """
    This function takes care of merging both datasets, events and attendees.
    """
    print("Shape of df before merge", df.shape)
    print("Shape of df2 before merge", df2.shape)

    merged_df = pd.merge(df, df2, left_on="event_id", right_on="id", how="left").drop(
        [
            "id",
            "excerpt",
            "eventbrite_sync_description",
            "eventbrite_url",
            "eventbrite_id",
            "banner",
        ],
        axis=1,
    )

    # Define the fields to transform
    datetime_fields = ["starting_at", "attended_at", "form_created_at", "won_at"]

    for field in datetime_fields:
        merged_df[field] = pd.to_datetime(merged_df[field])
        merged_df[field] = (
            merged_df[field].dt.tz_localize("UTC", ambiguous="infer")
            if merged_df[field].dt.tz is None
            else merged_df[field].dt.tz_convert("UTC")
        )

    merged_df["is_new_registree"] = merged_df.groupby("email")["created_at"].transform(
        lambda x: x == x.min()
    )

    # Print only the transformed datetime columns
    print("------------------------")
    print("Transformed datetime columns in merged_df:")
    print("------------------------")
    
    # Printing the transformed datetime columns
    print(merged_df[datetime_fields])

    return merged_df
