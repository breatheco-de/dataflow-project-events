import pandas as pd
import numpy as np

def run(df_questions, df_answers):

    """
    This function combines both dataframes.
    """

    question_ids_list = df_questions['Q_Timestamp'].tolist()

    def id_autocompletion(search):
        for id in question_ids_list:
            if search in id:
                return id
    
    return None

    df_answers['Key_to_Q_Timestamp'] =  df_answers['Key_to_Q_Timestamp'].apply(id_autocompletion)
    df_answers['Key_to_Q_Timestamp'] =  np.where(df_answers['Key_to_Q_Timestamp'].isnull(), str(df_answers['A_Datetime_Thread']), df_answers['Key_to_Q_Timestamp'])

    final_df = pd.merge(df_questions, df_answers, left_on = ['Q_Timestamp', 'Channel_Slug'], right_on = ['Key_to_Q_Timestamp', 'Channel_Slug'], how = 'left')
    
    return final_df