import pandas as pd
import numpy as np


# Values for inputs
Channel_ID = ['CAZ9W99U4', 'CAZ9W99U4', 'CAZ9W99U4', 'CAZ9W99U4']
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Timestamp = ['11/27/2022 2:53:19', '11/11/2022 17:14:26', '11/19/2022 19:35:47', '12/3/2022 2:40:06']
Timestamp_Thread = ['11/26/2022 2:42:32', np.nan, np.nan, '12/2/2022 21:13:07']
User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_3', 'U_ID_4']
Full_Name = ['Name_1', 'Bot', 'Name_3', 'Tomas Gonzalez']
Email = ['Email_1@gmail.com', 'Bot@gmail.com', 'Email_3@gmail.com', 'tgonzalez@4geeksacademy.com']
Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_3', 'Permalink_4']
Text = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Answer from tgonzalez']
Text_raw = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Answer from tgonzalez']
Slack_username = ['User_1', 'Bot', 'User_3', 'tgonzalez']
Team_ID = ['T0BFXMWMV', 'T0BFXMWMV', 'T0BFXMWMV', 'T0BFXMWMV']
Team_Name = ['4Geeks Academy', '4Geeks Academy', '4Geeks Academy', '4Geeks Academy']
Is_Bot = [False, True, False, False]

dict_inputs = {'Channel_ID': Channel_ID, 'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp, 
                'Timestamp_Thread':Timestamp_Thread, 'User_ID':User_ID, 'Full_Name':Full_Name,
                'Email':Email, 'Permalink':Permalink, 'Text':Text, 'Text_raw':Text_raw,
                'Slack_username':Slack_username, 'Team_ID':Team_ID, 'Team_Name':Team_Name, 'Is_Bot':Is_Bot}


# Expected inputs
expected_inputs = pd.DataFrame.from_dict(dict_inputs)


# Values for output
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Timestamp = ['11/27/2022 2:53:19', '11/11/2022 17:14:26', '11/19/2022 19:35:47', '12/3/2022 2:40:06']
Timestamp_Thread = ['11/26/2022 2:42:32', np.nan, np.nan, '12/2/2022 21:13:07']
User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_3', 'U_ID_4']
Full_Name = ['Name_1', 'Bot', 'Name_3', 'Tomas Gonzalez']
Email = ['Email_1@gmail.com', 'Bot@gmail.com', 'Email_3@gmail.com', 'tgonzalez@4geeksacademy.com']
Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_3', 'Permalink_4']
Text = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Answer from tgonzalez']
Text_raw = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Answer from tgonzalez']
Slack_username = ['User_1', 'Bot', 'User_3', 'tgonzalez']
Is_Bot = [0, 1, 0, 0]
Is_a_question = [0, 1, 1, 0]
Is_agent = [0, 0, 0, 1]
Datetime = [pd.to_datetime('11/27/2022 2:53:19'), pd.to_datetime('11/11/2022 17:14:26'), pd.to_datetime('11/19/2022 19:35:47'), pd.to_datetime('12/3/2022 2:40:06')]
Datetime_Thread = [pd.to_datetime('11/26/2022 2:42:32'), pd.to_datetime(np.nan), pd.to_datetime(np.nan), pd.to_datetime('12/2/2022 21:13:07')]

dict_output = {'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp, 'Timestamp_Thread':Timestamp_Thread, 
                'User_ID':User_ID, 'Full_Name':Full_Name, 'Email':Email, 'Permalink':Permalink, 'Text':Text, 
                'Text_raw':Text_raw, 'Slack_username':Slack_username, 'Is_Bot':Is_Bot, 'Is_a_question':Is_a_question,
                'Is_agent':Is_agent, 'Datetime':Datetime, 'Datetime_Thread':Datetime_Thread}


# Expected outputs
expected_output = pd.DataFrame.from_dict(dict_output)



def run(df):

    """ This function creates and modifies some columns"""

    # Delete columns that have the same value in all rows
    df.drop(columns=['Channel_ID', 'Team_ID', 'Team_Name'], inplace=True)

    # Create a column to know if it is a question 
    # (it is considered a question if it is not an answer in a thread)
    df['Is_a_question'] = np.where(df['Timestamp_Thread'].isnull(), 1, 0)

    # Create column to identify if it is an agent or not
    support_agent_emails = ['aalejo@gmail.com', 'tgonzalez@4geeksacademy.com']
    df['Is_agent'] = np.where(df['Email'].isin(support_agent_emails), 1, 0)

    # Encode the column to know if it is a message from a Bot
    df['Is_Bot'] = np.where(df['Is_Bot'] == True, 1, 0)

    # Change type to datetime
    df['Datetime'] = pd.to_datetime(df['Timestamp'])
    df['Datetime_Thread'] = pd.to_datetime(df['Timestamp_Thread'])

    return df