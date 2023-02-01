import pandas as pd
import numpy as np


# Values for inputs
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Timestamp = ['11/26/2022 2:50:20', '11/13/2022 17:14:20', '11/26/2022 2:53:40', '11/13/2022 17:27:30', '11/13/2022 17:30:20', '11/19/2022 19:35:59', '11/19/2022 19:37:20', '12/3/2022 2:55:06']
Timestamp_Thread = ['11/26/2022 2:42:32', '11/13/2022 16:42:32', '11/26/2022 2:52:20', '11/13/2022 16:42:32', '11/13/2022 16:42:32', '11/19/2022 19:20:00', '11/19/2022 19:20:00', np.nan]
User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_1', 'U_ID_2', 'U_ID_2', 'U_ID_3', 'U_ID_4', 'U_ID_5']
Full_Name = ['Name_1', 'Name_2', 'Name_1', 'Name_2', 'Name_2', 'Name_3', 'Name_4', 'Name_5']
Email = ['Email_1@gmail.com', 'Email_2@gmail.com', 'Email_1@gmail.com', 'Email_2@gmail.com', 'Email_2@gmail.com', 'Email_3@gmail.com', 'Email_4@gmail.com', 'Email_5@gmail.com']
Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_3', 'Permalink_4', 'Permalink_5', 'Permalink_6', 'Permalink_7', 'Permalink_8']
Text = ['Answer from User 1', 'Answer from user 2 indep', 'Answer from User 1 to other thread', 'Answer from User 2 part 1', 'Answer from User 2 part 2', 'Answer from User 3', 'Answer from User 4 to same thread that User 3', 'Question from User 5']
Text_raw = ['Answer from User 1', 'Answer from user 2 indep', 'Answer from User 1 to other thread', 'Answer from User 2 part 1', 'Answer from User 2 part 2', 'Answer from User 3', 'Answer from User 4 to same thread that User 3', 'Question from User 5']
Slack_username = ['User_1', 'User_2', 'User_1', 'User_2', 'User_2', 'User_3', 'User_4', 'User_5']
Is_Bot = [0, 0, 0, 0, 0, 0, 0, 0]
Is_a_question = [0, 0, 0, 0, 0, 0, 0, 1]
Is_agent = [0, 0, 0, 0, 0, 0, 0, 0]
Datetime = [pd.to_datetime('11/26/2022 2:50:20'), pd.to_datetime('11/13/2022 17:14:20'), pd.to_datetime('11/26/2022 2:53:40'), pd.to_datetime('11/13/2022 17:27:30'), pd.to_datetime('11/13/2022 17:30:20'), pd.to_datetime('11/19/2022 19:35:59'), pd.to_datetime('11/19/2022 19:37:20'), pd.to_datetime('12/3/2022 2:55:06')]
Datetime_Thread = [pd.to_datetime('11/26/2022 2:42:32'), pd.to_datetime('11/13/2022 16:42:32'), pd.to_datetime('11/26/2022 2:52:20'), pd.to_datetime('11/13/2022 16:42:32'), pd.to_datetime('11/13/2022 16:42:32'), pd.to_datetime('11/19/2022 19:20:00'), pd.to_datetime('11/19/2022 19:20:00'), pd.to_datetime(np.nan)]

dict_inputs = {'Unnamed: 0':[1, 2, 3, 4, 5, 6, 7, 8], 'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp, 'Timestamp_Thread':Timestamp_Thread,
                'User_ID':User_ID, 'Full_Name':Full_Name, 'Email':Email, 'Permalink':Permalink, 'Text':Text,
                'Text_raw':Text_raw, 'Slack_username':Slack_username, 'Is_Bot':Is_Bot, 'Is_a_question':Is_a_question,
                'Is_agent':Is_agent, 'Datetime':Datetime, 'Datetime_Thread':Datetime_Thread}


# Expected inputs
expected_inputs = pd.DataFrame.from_dict(dict_inputs)


# Values for output

A_User_ID = ['U_ID_1', 'U_ID_1', 'U_ID_2', 'U_ID_2', 'U_ID_3', 'U_ID_4']
A_Datetime = [pd.to_datetime('11/26/2022 2:50:20'), pd.to_datetime('11/26/2022 2:53:40'), pd.to_datetime('11/13/2022 17:14:20'), pd.to_datetime('11/13/2022 17:27:30'), pd.to_datetime('11/19/2022 19:35:59'), pd.to_datetime('11/19/2022 19:37:20')]
A_Datetime_Thread = [pd.to_datetime('11/26/2022 2:42:32'), pd.to_datetime('11/26/2022 2:52:20'), pd.to_datetime('11/13/2022 16:42:32'), pd.to_datetime('11/13/2022 16:42:32'), pd.to_datetime('11/19/2022 19:20:00'), pd.to_datetime('11/19/2022 19:20:00')]
A_Text = ['Answer from User 1', 'Answer from User 1 to other thread', 'Answer from user 2 indep', 'Answer from User 2 part 1 Answer from User 2 part 2', 'Answer from User 3', 'Answer from User 4 to same thread that User 3']
A_message_ID = [1, 1+(pd.to_datetime('11/26/2022 2:52:20')-pd.to_datetime('11/26/2022 2:42:32'))/np.timedelta64(1,'s'), 2, 3, 4, 5]
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
A_Timestamp = ['11/26/2022 2:50:20', '11/26/2022 2:53:40', '11/13/2022 17:14:20', '11/13/2022 17:27:30,11/13/2022 17:30:20', '11/19/2022 19:35:59', '11/19/2022 19:37:20']
Key_to_Q_Timestamp = ['11/26/2022 2:42:32', '11/26/2022 2:52:20', '11/13/2022 16:42:32', '11/13/2022 16:42:32', '11/19/2022 19:20:00', '11/19/2022 19:20:00']
A_Full_Name = ['Name_1', 'Name_1', 'Name_2', 'Name_2', 'Name_3', 'Name_4']
A_Email = ['Email_1@gmail.com', 'Email_1@gmail.com', 'Email_2@gmail.com', 'Email_2@gmail.com', 'Email_3@gmail.com', 'Email_4@gmail.com']
A_Permalink = ['Permalink_1', 'Permalink_3', 'Permalink_2', 'Permalink_4', 'Permalink_6', 'Permalink_7']
A_Slack_username = ['User_1', 'User_1', 'User_2', 'User_2', 'User_3', 'User_4']
A_from_Bot = [0, 0, 0, 0, 0, 0]
A_from_Agent = [0, 0, 0, 0, 0, 0]
Response_time = [pd.to_datetime('11/26/2022 2:50:20') - pd.to_datetime('11/26/2022 2:42:32'),
                pd.to_datetime('11/26/2022 2:53:40') - pd.to_datetime('11/26/2022 2:52:20'),
                pd.to_datetime('11/13/2022 17:14:20') - pd.to_datetime('11/13/2022 16:42:32'),
                pd.to_datetime('11/13/2022 17:27:30') - pd.to_datetime('11/13/2022 16:42:32'),
                pd.to_datetime('11/19/2022 19:35:59') - pd.to_datetime('11/19/2022 19:20:00'),
                pd.to_datetime('11/19/2022 19:37:20') - pd.to_datetime('11/19/2022 19:20:00')]

dict_output = {'A_User_ID':A_User_ID, 'A_Datetime':A_Datetime, 'A_Datetime_Thread':A_Datetime_Thread, 'A_Text':A_Text, 
                'A_message_ID':A_message_ID, 'Channel_Slug':Channel_Slug, 'A_Timestamp':A_Timestamp, 'Key_to_Q_Timestamp':Key_to_Q_Timestamp,
                'A_Full_Name':A_Full_Name, 'A_Email':A_Email, 'A_Permalink':A_Permalink, 'A_Slack_username':A_Slack_username,
                'A_from_Bot':A_from_Bot, 'A_from_Agent':A_from_Agent, 'Response_time':Response_time}


# Expected output
expected_output = pd.DataFrame.from_dict(dict_output)


def run(df):

    """This function creates the dataframe for answers and some new columns"""

    # Create dataframe only for answers
    A_df = df[df['Is_a_question'] == 0]

    answers = A_df.groupby(['User_ID','Datetime', 'Datetime_Thread'])[['Text']]
    df_answers = pd.DataFrame(answers.sum().reset_index())

    df_answers.loc[:, 'Datetime'] = pd.to_datetime(df_answers['Datetime'])
    df_answers.loc[:, 'Datetime_Thread'] = pd.to_datetime(df_answers['Datetime_Thread'])
    A_df.loc[:, 'Datetime'] = pd.to_datetime(A_df['Datetime'])
    A_df.loc[:, 'Datetime_Thread'] = pd.to_datetime(A_df['Datetime_Thread'])

    # Create new column to know the difference in seconds between answers from the same user
    df_answers['Diff_in_seconds'] = (df_answers.sort_values('Datetime').groupby('User_ID').Datetime.diff())
    df_answers['Diff_in_seconds'] = df_answers['Diff_in_seconds'].fillna(pd.Timedelta(seconds=0))
    df_answers['Diff_in_seconds']=df_answers['Diff_in_seconds']/np.timedelta64(1,'s')
    df_answers['Diff_abs'] = df_answers['Diff_in_seconds'].abs()

    # Create new column that indicates if the author of the previous answer is different from the author of the current answer
    df_answers['Not_previous_author'] = df_answers['User_ID'].ne(df_answers['User_ID'].shift().bfill()).astype(int)
      
    # Create new column that indicates the difference in seconds between timestamp_thread from answers from the same user
    df_answers['Diff_Thread'] = (df_answers.sort_values('Datetime_Thread').groupby('User_ID').Datetime_Thread.diff())
    df_answers['Diff_Thread'] = df_answers['Diff_Thread'].fillna(pd.Timedelta(seconds=0))
    df_answers['Diff_Thread'] = df_answers['Diff_Thread']/np.timedelta64(1,'s')

    # Create function to indicate message ID following the criteria:
    # 1. The ID should change if there is more than 300 seconds between one answer and the next
    # 2. The ID should change if the author of the previous answer is different from the author of the current answer
    # 3. The ID should change if there is a difference between timestamp_thread from one answer and the next
    def create_AnswerId(df_x):
        for group in df_x.groupby('User_ID'):
            df_x['A_message_ID'] = df_x['Diff_abs'].gt(300).cumsum() + 1 + df_x['Not_previous_author'].cumsum() + df_x['Diff_Thread']
        return df_x
    
    # Apply function   
    create_AnswerId(df_answers)

    # Merge the dataframe to its previous columns and delete auxiliary columns
    df_answers = df_answers.merge(A_df, how = 'left', left_on = ['User_ID', 'Datetime', 'Datetime_Thread', 'Text'],
                right_on = ['User_ID', 'Datetime', 'Datetime_Thread', 'Text']).drop(['Diff_in_seconds', 
                'Diff_abs', 'Not_previous_author', 'Diff_Thread', 'Text_raw', 'Is_a_question'], axis=1)

    # Calculate the response time
    df_answers['Response_time'] = df_answers['Datetime'] - df_answers['Datetime_Thread']

    # Merge text in rows that have the same A_message_ID
    df_answers['Text'] = df_answers.groupby(['A_message_ID'])['Text'].transform(lambda x : ' '.join(x))

    # Merge timestamp in rows that have the same A_message_ID
    df_answers['Timestamp'] = df_answers.groupby(['A_message_ID'])['Timestamp'].transform(lambda x : ','.join(map(str, x)))

    # Rename columns to make it explicit that they correspond to answers
    df_answers.rename(columns={'User_ID':'A_User_ID', 'Datetime':'A_Datetime', 'Text':'A_Text', 'Timestamp':'A_Timestamp', 
                            'Timestamp_Thread':'Key_to_Q_Timestamp', 'Full_Name':'A_Full_Name', 'Email':'A_Email', 
                            'Permalink':'A_Permalink', 'Slack_username':'A_Slack_username', 'Is_Bot':'A_from_Bot', 
                            'Is_agent':'A_from_Agent', 'Datetime_Thread':'A_Datetime_Thread'},inplace=True)

    # Drop duplicates
    df_answers.drop_duplicates(subset=['A_Timestamp', 'A_Text'], keep='first', inplace=True)

    return df_answers