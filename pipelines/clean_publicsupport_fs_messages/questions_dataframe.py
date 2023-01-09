import pandas as pd
import numpy as np

# Values for inputs
Channel_Slug = ['public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack', 'public-support-full-stack']
Timestamp = ['11/27/2022 2:53:19', '11/11/2022 17:14:26', '11/19/2022 19:35:47', '12/3/2022 2:40:06', '11/19/2022 19:33:47', '11/19/2022 19:35:59', '12/3/2022 2:50:06']
Timestamp_Thread = ['11/26/2022 2:42:32', np.nan, np.nan, '12/2/2022 21:13:07', np.nan, np.nan, np.nan]
User_ID = ['U_ID_1', 'U_ID_2', 'U_ID_3', 'U_ID_4', 'U_ID_3', 'U_ID_3', 'U_ID_4']
Full_Name = ['Name_1', 'Bot', 'Name_3', 'Tomas Gonzalez', 'Name_3', 'Name_3', 'Tomas Gonzalez']
Email = ['Email_1@gmail.com', 'Bot@gmail.com', 'Email_3@gmail.com', 'tgonzalez@4geeksacademy.com', 'Email_3@gmail.com', 'Email_3@gmail.com', 'tgonzalez@4geeksacademy.com']
Permalink = ['Permalink_1', 'Permalink_2', 'Permalink_3', 'Permalink_4', 'Permalink_5', 'Permalink_6', 'Permalink_7']
Text = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Question from tgonzalez', 'Question from User 3 part 0', 'Question from User 3 part 2', 'Question from tgonzalez 10 minutes later']
Text_raw = ['Answer from User 1', 'Question from Bot', 'Question from User 3', 'Question from tgonzalez', 'Question from User 3 part 0', 'Question from User 3 part 2', 'Question from tgonzalez 10 minutes later']
Slack_username = ['User_1', 'Bot', 'User_3', 'tgonzalez', 'User_3', 'User_3', 'tgonzalez']
Is_Bot = [0, 1, 0, 0, 0, 0, 0]
Is_a_question = [0, 1, 1, 1, 1, 1, 1]
Is_agent = [0, 0, 0, 1, 0, 0, 1]
Datetime = [pd.to_datetime('11/27/2022 2:53:19'), pd.to_datetime('11/11/2022 17:14:26'), pd.to_datetime('11/19/2022 19:35:47'), pd.to_datetime('12/3/2022 2:40:06'), pd.to_datetime('11/19/2022 19:33:47'), pd.to_datetime('11/19/2022 19:35:59'), pd.to_datetime('12/3/2022 2:50:06')]
Datetime_Thread = [pd.to_datetime('11/26/2022 2:42:32'), pd.to_datetime(np.nan), pd.to_datetime(np.nan), pd.to_datetime('12/2/2022 21:13:07'), pd.to_datetime(np.nan), pd.to_datetime(np.nan), pd.to_datetime(np.nan)]

dict_inputs = {'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp, 'Timestamp_Thread':Timestamp_Thread, 
                'User_ID':User_ID, 'Full_Name':Full_Name, 'Email':Email, 'Permalink':Permalink, 'Text':Text, 
                'Text_raw':Text_raw, 'Slack_username':Slack_username, 'Is_Bot':Is_Bot, 'Is_a_question':Is_a_question,
                'Is_agent':Is_agent, 'Datetime':Datetime, 'Datetime_Thread':Datetime_Thread}


# Expected inputs
expected_inputs = pd.DataFrame.from_dict(dict_inputs)


# Expected output values

User_ID = ['U_ID_2', 'U_ID_3', 'U_ID_3', 'U_ID_3', 'U_ID_4', 'U_ID_4']
Datetime = [pd.to_datetime('11/11/2022 17:14:26'), pd.to_datetime('11/19/2022 19:33:47'), pd.to_datetime('11/19/2022 19:35:47'), pd.to_datetime('11/19/2022 19:35:59'), pd.to_datetime('12/3/2022 2:40:06'), pd.to_datetime('12/3/2022 2:50:06')]
Text = ['Question from Bot', 'Question from User 3 part 0', 'Question from User 3', 'Question from User 3 part 2', 'Question from tgonzalez', 'Question from tgonzalez 10 minutes later']
Diff_in_seconds = [0.0, 0.0, 120.0, 12.0, 0.0, 600.0]
Diff_abs = [0.0, 0.0, 120.0, 12.0, 0.0, 600.0]
Not_previous_author = [0, 1, 0, 0, 1, 0]
Q_message_ID = [1, 2, 2, 2, 3, 4]

dict_output = {'User_ID':User_ID, 'Datetime':Datetime, 'Text':Text, 'Diff_in_seconds':Diff_in_seconds,
                'Diff_abs':Diff_abs, 'Not_previous_author':Not_previous_author, 'Q_message_ID':Q_message_ID}


# Expected output
expected_output = pd.DataFrame.from_dict(dict_output)


def run(df):

    """This function creates the dataframe for questions and some new columns"""

    # Create dataframe only for questions
    Q_df = df[df['Is_a_question'] == 1]

    questions = Q_df.groupby(['User_ID','Datetime'])[['Text']]
    df_questions = pd.DataFrame(questions.sum().reset_index())

    # Create new column to know the difference in seconds between questions from the same user
    df_questions['Diff_in_seconds'] = (df_questions.sort_values('Datetime').groupby('User_ID').Datetime.diff())
    df_questions['Diff_in_seconds'] = df_questions['Diff_in_seconds'].fillna(pd.Timedelta(seconds=0))
    df_questions['Diff_in_seconds']=df_questions['Diff_in_seconds']/np.timedelta64(1,'s')
    df_questions['Diff_abs'] = df_questions['Diff_in_seconds'].abs()

    # Create new column that indicates if the author of the previous question is different from the author of the current question
    df_questions['Not_previous_author'] = df_questions['User_ID'].ne(df_questions['User_ID'].shift().bfill()).astype(int)

    # Create function to indicate message ID following the criteria:
    # 1. The ID should change if there is more than 300 seconds between one question and the next
    # 2. The ID ahould change if the author of the previous question is different from the author of the current question
    def create_QuestionId(df_x):
        for group in df.groupby(['User_ID']):
            df_x['Q_message_ID'] = df_x['Diff_abs'].gt(300).cumsum() + 1 + df_x['Not_previous_author'].cumsum()
        return df_x

    # Apply function    
    create_QuestionId(df_questions)

    return df_questions