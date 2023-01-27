import pandas as pd
import numpy as np


# Values for inputs

# Questions
Q_User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_3']
Q_Datetime = [pd.to_datetime('11/11/2022 17:10:10'), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('12/3/2022 2:45:06')]
Q_Text = ['Question from User 1', 'Question from User 2', 'Question from User 3']
Q_message_ID = [1, 2, 3]
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Q_Timestamp = ['11/11/2022 17:10:10', '11/12/2022 19:30:23,11/12/2022 19:32:47,11/12/2022 19:35:59', '12/3/2022 2:45:06']
Q_Full_Name = ['Name_1', 'Name_2', 'Name_3']
Q_Email = ['Email_1@gmail.com', 'Email_2@gmail.com', 'Email_3@gmail.com']
Q_Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_3']
Q_Slack_username = ['User_1', 'User_2', 'User_3']
Q_from_Bot = [0, 0, 0]
Q_from_Agent = [0, 0, 0]

dict_questions = {'Q_User_ID':Q_User_ID, 'Q_Datetime':Q_Datetime, 'Q_Text':Q_Text, 'Q_message_ID':Q_message_ID, 'Channel_Slug':Channel_Slug,
                'Q_Timestamp':Q_Timestamp, 'Q_Full_Name':Q_Full_Name, 'Q_Email':Q_Email, 'Q_Permalink':Q_Permalink,
                'Q_Slack_username':Q_Slack_username, 'Q_from_Bot':Q_from_Bot, 'Q_from_Agent':Q_from_Agent}

# Answers
A_User_ID = ['U_ID_4', 'U_ID_4', 'U_ID_1']
A_Datetime = [pd.to_datetime('12/3/2022 4:10:34'), pd.to_datetime('11/13/2022 4:30:45'), pd.to_datetime('11/13/2022 2:10:15')]
A_Text = ['Answer from user 4 to question from user 3', 'Answer from user 4 to question from user 2', 'Answer from user 1 to question from user 2']
A_message_ID = [1, 2, 3]
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
A_Timestamp = ['12/3/2022 4:10:34', '11/13/2022 4:30:45', '11/13/2022 2:10:15']
Key_to_Q_Timestamp = ['12/3/2022 2:45:06', '11/12/2022 19:30:23', '11/12/2022 19:30:23']
A_Full_Name = ['Name_4', 'Name_4', 'Name_1']
A_Email = ['Email_4@gmail.com', 'Email_4@gmail.com', 'Email_1@gmail.com']
A_Permalink = ['Permalink_A_1', 'Permalink_A_2', 'Permalink_A_3']
A_Slack_username = ['User_4', 'User_4', 'User_1']
A_from_Bot = [0, 0, 0]
A_from_Agent = [0, 0, 0]
A_Datetime_Thread = [pd.to_datetime('12/3/2022 2:45:06'), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('11/12/2022 19:30:23')]
Response_time = [pd.to_datetime('12/3/2022 4:10:34') - pd.to_datetime('12/3/2022 2:45:06'),
                pd.to_datetime('11/13/2022 4:30:45') - pd.to_datetime('11/12/2022 19:30:23'),
                pd.to_datetime('11/13/2022 2:10:15') - pd.to_datetime('11/12/2022 19:30:23')]

dict_answers = {'Unnamed: 0_x':[1, 2, 3], 'Unnamed: 0_y':[1, 2, 3], 'A_User_ID':A_User_ID, 'A_Datetime':A_Datetime, 'A_Text':A_Text, 'A_message_ID':A_message_ID,
                'Channel_Slug':Channel_Slug, 'A_Timestamp':A_Timestamp, 'Key_to_Q_Timestamp':Key_to_Q_Timestamp,
                'A_Full_Name':A_Full_Name, 'A_Email':A_Email, 'A_Permalink':A_Permalink, 'A_Slack_username':A_Slack_username,
                'A_from_Bot':A_from_Bot, 'A_from_Agent':A_from_Agent, 'A_Datetime_Thread':A_Datetime_Thread,
                'Response_time':Response_time}

# Expected inputs
expected_inputs = [pd.DataFrame(dict_questions), pd.DataFrame(dict_answers)]


# Values for output

Q_User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_2', 'U_ID_3']
Q_Datetime = [pd.to_datetime('11/11/2022 17:10:10'), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('12/3/2022 2:45:06')]
Q_Text = ['Question from User 1', 'Question from User 2', 'Question from User 2', 'Question from User 3']
Q_message_ID = [1, 2, 2, 3]
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Q_Timestamp = ['11/11/2022 17:10:10', '11/12/2022 19:30:23,11/12/2022 19:32:47,11/12/2022 19:35:59', '11/12/2022 19:30:23,11/12/2022 19:32:47,11/12/2022 19:35:59', '12/3/2022 2:45:06']
Q_Full_Name = ['Name_1', 'Name_2', 'Name_2', 'Name_3']
Q_Email = ['Email_1@gmail.com', 'Email_2@gmail.com', 'Email_2@gmail.com', 'Email_3@gmail.com']
Q_Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_2', 'Permalink_3']
Q_Slack_username = ['User_1', 'User_2', 'User_2', 'User_3']
Q_from_Bot = [0, 0, 0, 0]
Q_from_Agent = [0, 0, 0, 0]
A_User_ID = [np.nan, 'U_ID_4', 'U_ID_1', 'U_ID_4']
A_Datetime = [pd.to_datetime(np.nan), pd.to_datetime('11/13/2022 4:30:45'), pd.to_datetime('11/13/2022 2:10:15'), pd.to_datetime('12/3/2022 4:10:34')]
A_Text = [np.nan, 'Answer from user 4 to question from user 2', 'Answer from user 1 to question from user 2', 'Answer from user 4 to question from user 3']
A_message_ID = [np.nan, 2, 3, 1]
A_Timestamp = [np.nan, '11/13/2022 4:30:45', '11/13/2022 2:10:15', '12/3/2022 4:10:34']
Key_to_Q_Timestamp = [np.nan, '11/12/2022 19:30:23,11/12/2022 19:32:47,11/12/2022 19:35:59', '11/12/2022 19:30:23,11/12/2022 19:32:47,11/12/2022 19:35:59', '12/3/2022 2:45:06']
A_Full_Name = [np.nan, 'Name_4', 'Name_1', 'Name_4']
A_Email = [np.nan, 'Email_4@gmail.com', 'Email_1@gmail.com', 'Email_4@gmail.com']
A_Permalink = [np.nan, 'Permalink_A_2', 'Permalink_A_3', 'Permalink_A_1']
A_Slack_username = [np.nan, 'User_4', 'User_1', 'User_4']
A_from_Bot = [np.nan, 0, 0, 0]
A_from_Agent = [np.nan, 0, 0, 0]
A_Datetime_Thread = [pd.to_datetime(np.nan), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('11/12/2022 19:30:23'), pd.to_datetime('12/3/2022 2:45:06')]
Response_time = [pd.to_datetime(np.nan),
                pd.to_datetime('11/13/2022 4:30:45') - pd.to_datetime('11/12/2022 19:30:23'),
                pd.to_datetime('11/13/2022 2:10:15') - pd.to_datetime('11/12/2022 19:30:23'),
                pd.to_datetime('12/3/2022 4:10:34') - pd.to_datetime('12/3/2022 2:45:06')]

dict_output = {'Q_User_ID':Q_User_ID, 'Q_Datetime':Q_Datetime, 'Q_Text':Q_Text, 'Q_message_ID':Q_message_ID, 'Channel_Slug':Channel_Slug,
                'Q_Timestamp':Q_Timestamp, 'Q_Full_Name':Q_Full_Name, 'Q_Email':Q_Email, 'Q_Permalink':Q_Permalink,
                'Q_Slack_username':Q_Slack_username, 'Q_from_Bot':Q_from_Bot, 'Q_from_Agent':Q_from_Agent, 
                'A_User_ID':A_User_ID, 'A_Datetime':A_Datetime, 'A_Text':A_Text, 'A_message_ID':A_message_ID,
                'A_Timestamp':A_Timestamp, 'Key_to_Q_Timestamp':Key_to_Q_Timestamp, 'A_Full_Name':A_Full_Name, 'A_Email':A_Email, 
                'A_Permalink':A_Permalink, 'A_Slack_username':A_Slack_username, 'A_from_Bot':A_from_Bot, 'A_from_Agent':A_from_Agent, 
                'A_Datetime_Thread':A_Datetime_Thread, 'Response_time':Response_time}

# Expected output
expected_output = pd.DataFrame(dict_output)


def run(df_questions, df_answers):

    """
    This function combines both dataframes.
    """

    questions_timestamps = df_questions['Q_Timestamp'].tolist()

    def autocompletion_merged_timestamps(Key_to_Q):
        for timestamp in questions_timestamps:
            if Key_to_Q in str(timestamp):
                return timestamp
    
        return None

    df_answers['Key_to_Q_Timestamp'] =  df_answers['Key_to_Q_Timestamp'].apply(autocompletion_merged_timestamps)
    df_answers['Key_to_Q_Timestamp'] =  np.where(df_answers['Key_to_Q_Timestamp'].isnull(), str(df_answers['A_Datetime_Thread']), df_answers['Key_to_Q_Timestamp'])

    final_df = pd.merge(df_questions, df_answers, left_on = ['Q_Timestamp', 'Channel_Slug'], right_on = ['Key_to_Q_Timestamp', 'Channel_Slug'], how = 'left')
    final_df = final_df.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)
    
    return final_df