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
    This function creates a dataframe only for questions.
    """

    print('Shape before creating new questions_df', df.shape)

    Q_df = df[df['Is_a_question'] == 1]

    questions = Q_df.groupby(['User_ID','Datetime'])[['Text']]
    df_questions = pd.DataFrame(questions.sum().reset_index())

    df_questions['Diff_in_Seconds'] = (df_questions.sort_values('Datetime').groupby('User_ID').Datetime.diff())

    df_questions['Diff_in_Seconds'] = df_questions['Diff_in_Seconds'].fillna(pd.Timedelta(seconds=0))

    df_questions['Diff_in_Seconds'] = df_questions['Diff_in_Seconds']/np.timedelta64(1,'s')

    df_questions['diff_abs'] = df_questions.Diff_in_Seconds.abs()

    df_questions['same_author'] = df_questions['User_ID'].ne(df_questions['User_ID'].shift().bfill()).astype(int)

    def create_QuestionId(dfx):
        for group in dfx.groupby(['User_ID']):
            dfx['messageId'] = dfx['diff_abs'].gt(300).cumsum() + 1 + dfx.same_author.cumsum()
        return dfx

    create_QuestionId(df_questions)

    df_questions = df_questions.merge(Q_df, how = 'left', left_on = ['User_ID', 'Datetime', 'Text'],
    right_on = ['User_ID', 'Datetime', 'Text']).drop(['Diff_in_Seconds','diff_abs','same_author','Text_raw'], axis=1)

    print('Shape of new questions_df', df_questions.shape)
    
    return df_questions