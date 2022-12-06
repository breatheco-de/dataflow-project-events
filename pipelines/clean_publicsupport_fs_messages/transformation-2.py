import pandas as pd
import numpy as np
from datetime import datetime


#list of values in columns
ids = [44, 30]
created_dates = ['ab','bc']
updated_dates = ['ab','bc']
event_ids = [121,38]
status = ['ab','bc']
attended_dates = ['NaN','NaN']

#expected input
expected_inputs = [{'id': ids,'created_at':created_dates,'updated_at':updated_dates,'event_id':event_ids, 
                'status':status,'attended_at': attended_dates}]

#values for Output
output_event_ids = [121,38]
output_attended_dates = ['NaN','NaN']

#expected output
expected_output = [{'event_id':output_event_ids, 'attended_at':output_attended_dates}]


def run(df):
    """
    This function creates a dataframe only for answers.
    """

    print('Shape before creating new answers_df', df.shape)

    A_df = df[df['Is_a_question'] == 0]

    answers = A_df.groupby(['User_ID','Datetime'])[['Text']]
    df_answers = pd.DataFrame(answers.sum().reset_index())

    df_answers['Diff_in_Seconds'] = (df_answers.sort_values('Datetime').groupby('User_ID').Datetime.diff())
    df_answers['Diff_in_Seconds'] = df_answers['Diff_in_Seconds'].fillna(pd.Timedelta(seconds=0))
    df_answers['Diff_in_Seconds'] = df_answers['Diff_in_Seconds']/np.timedelta64(1,'s')
    df_answers['diff_abs'] = df_answers.Diff_in_Seconds.abs()
    df_answers['same_author'] = df_answers['User_ID'].ne(df_answers['User_ID'].shift().bfill()).astype(int)

    def create_AnswerId(dfx):
        for group in dfx.groupby(['User_ID']):
            dfx['messageId'] = dfx.diff_abs.gt(300).cumsum() + 1 + dfx.same_author.cumsum()
        return dfx
    create_AnswerId(df_answers)


    #Merge dataframe to its previous columns
    df_answers = df_answers.merge(A_df, how = 'left', left_on = ['User_ID', 'Datetime', 'Text'],
    right_on = ['User_ID', 'Datetime', 'Text']).drop(['Diff_in_Seconds','diff_abs','same_author','Text_raw'], axis=1)


    #Create new response time column 
    df_answers['Response_time'] = df_answers['Datetime'] - df_answers['Datetime_Thread']


    #Merge text and timestamps in rows that have the same messageId
    df_answers['Text'] = df_answers.groupby(['messageId'])['Text'].transform(lambda x : ' '.join(x))


    #rename to ids in both dataframes
    df_answers.rename(columns={"Timestamp": "Answer_ID", "Timestamp_Thread": "Key_to_Question_ID",
                        "User_ID":"Answer_User_ID","Full_Name":"Answer_Full_Name","Email":"Answer_email","Text":"Answer_Text","Is_agent":"Answer_from_Agent",
                        "Datetime":"Answer_Datetime", "Datetime_Thread":"Answer_Dt_Thread"},inplace=True)

    df_answers = df_answers.drop_duplicates(subset=["Answer_Text"],keep='first')


    print('Shape of new answers_df', df_answers.shape)
    
    return df_answers