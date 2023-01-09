import pandas as pd
import numpy as np


def run(Q_df, df_questions):
    # Merge the dataframe to its previous columns and delete auxiliary columns
    df_questions = df_questions.merge(Q_df, how = 'left', left_on = ['User_ID', 'Datetime', 'Text'],
                    right_on = ['User_ID', 'Datetime', 'Text']).drop(['Diff_in_seconds','Diff_abs','Not_previous_author','Text_raw'], axis=1)

    # Merge text in rows that have the same Q_message_ID
    df_questions['Text'] = df_questions.groupby(['Q_message_ID'])['Text'].transform(lambda x : ' '.join(x))

    # Delete empty columns
    df_questions.dropna(axis=1, how='all', inplace=True)

    # Merge timestamp in rows that have the same Q_message_ID
    df_questions['Timestamp'] = df_questions.groupby(['Q_message_ID'])['Timestamp'].transform(lambda x : ','.join(map(str, x)))

    # Rename columns to make it explicit that they correspond to questions
    df_questions.rename(columns={'User_ID':'Q_User_ID', 'Datetime':'Q_Datetime', 'Text':'Q_Text', 
                            'Timestamp':'Q_Timestamp', 'Full_Name':'Q_Full_Name', 'Email':'Q_Email',
                            'Permalink':'Q_Permalink', 'Slack_username':'Q_Slack_username', 
                            'Is_agent':'Q_from_Agent'},inplace=True)

    # Drop duplicates
    df_questions.drop_duplicates(subset=["Q_Timestamp", "Q_Text"], keep='first', inplace=True)

    return df_questions