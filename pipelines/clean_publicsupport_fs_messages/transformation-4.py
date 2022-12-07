import pandas as pd
import numpy as np
from datetime import datetime


def run(df1,df2):
    """
    This function combines both dataframes.
    """

    print('Shape of df1 before combining', df1.shape)
    print('Shape of df2 before combining', df2.shape)

    #create a list from df1 question_id column
    question_ids_list = df1['Question_ID'].tolist()

    def id_autocompletion(search):
        for id in question_ids_list:
            if search in id:
                return id
    
        return None

    df2['Key_to_Question_ID'] =  df2['Key_to_Question_ID'].apply(id_autocompletion)
    df2['Key_to_Question_ID'] =  np.where(df2['Key_to_Question_ID'].isnull(), str(df2['Answer_Dt_Thread']), df2['Key_to_Question_ID'])
    
    final_df = pd.merge(df1, df2[['Answer_User_ID','Answer_Full_Name','Answer_email','Answer_from_Agent','Answer_Text','Answer_ID','Key_to_Question_ID',
                'Answer_Datetime','Answer_Dt_Thread','Response_time']], how = 'left', left_on = ['Question_ID'], right_on = ['Key_to_Question_ID'])


    print('Shape of final_df', final_df.shape)
    
    return final_df