import numpy as np 
import pandas as pd 


##### Values for inputs #####

### slack ###
Channel_ID = ['Channel', 'Channel', 'Channel', 'Channel', 'Channel']
Channel_Slug = ['channel-slug', 'channel-slug', 'channel-slug', 'channel-slug', 'channel-slug']
Timestamp = [np.nan, np.nan, np.nan, np.nan, np.nan]
Timestamp_Thread = [np.nan, np.nan, np.nan, np.nan, np.nan]
User_ID = [np.nan, np.nan, np.nan, np.nan, np.nan]
Full_Name = ['User_1', 'User_2', 'User_3', 'User_4', 'User_1']
Email = ['user_1@mail.com', 'user_2@mail.com', 'user_3@mail.com', 'user_4@mail.com', 'user_1@mail.com']
Permalink = [np.nan, np.nan, np.nan, np.nan, np.nan]
Text = [np.nan, np.nan, np.nan, np.nan, np.nan]
Text_raw = [np.nan, np.nan, np.nan, np.nan, np.nan]
Slack_username = [np.nan, np.nan, np.nan, np.nan, np.nan]
Team_ID = [np.nan, np.nan, np.nan, np.nan, np.nan]
Team_Name = [np.nan, np.nan, np.nan, np.nan, np.nan]
Is_Bot = [False, False, False, False, False]

dict_slack = {'Channel_ID':Channel_ID, 'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp,
            'Timestamp_Thread':Timestamp_Thread, 'User_ID':User_ID, 'Full_Name':Full_Name,
            'Email':Email, 'Permalink':Permalink, 'Text':Text, 'Text_raw':Text_raw,
            'Slack_username':Slack_username, 'Team_ID':Team_ID, 'Team_Name':Team_Name, 
            'Is_Bot':Is_Bot}

### auth_user ###
id_ = [111, 222, 555, 444]
first_name = [np.nan, np.nan, np.nan, np.nan]
last_name = [np.nan, np.nan, np.nan, np.nan]
email = ['user_1@mail.com', 'user_3@mail.com', 'user_5@mail.com', 'user_4@mail.com']
date_joined = [np.nan, np.nan, np.nan, np.nan]

dict_auth_user = {'id':id_, 'first_name':first_name, 'last_name':last_name,
                'email':email, 'date_joined':date_joined}

### cohort_users_with_slug ###
user_id = [111, 222, 444, 555]
slug = ['cohort-1, cohort-2', 'cohort-2', np.nan, np.nan]

dict_cohort_users_with_slug = {'user_id':user_id, 'slug':slug}

##### Expected inputs #####
expected_inputs = [pd.DataFrame(dict_slack), pd.DataFrame(dict_auth_user), pd.DataFrame(dict_cohort_users_with_slug)]


##### Values for output #####
Channel_ID = ['Channel', 'Channel', 'Channel', 'Channel', 'Channel']
Channel_Slug = ['channel-slug', 'channel-slug', 'channel-slug', 'channel-slug', 'channel-slug']
Timestamp = [np.nan, np.nan, np.nan, np.nan, np.nan]
Timestamp_Thread = [np.nan, np.nan, np.nan, np.nan, np.nan]
User_ID = [np.nan, np.nan, np.nan, np.nan, np.nan]
Full_Name = ['User_1', 'User_2', 'User_3', 'User_4', 'User_1']
Email = ['user_1@mail.com', 'user_2@mail.com', 'user_3@mail.com', 'user_4@mail.com', 'user_1@mail.com']
Permalink = [np.nan, np.nan, np.nan, np.nan, np.nan]
Text = [np.nan, np.nan, np.nan, np.nan, np.nan]
Text_raw = [np.nan, np.nan, np.nan, np.nan, np.nan]
Slack_username = [np.nan, np.nan, np.nan, np.nan, np.nan]
Team_ID = [np.nan, np.nan, np.nan, np.nan, np.nan]
Team_Name = [np.nan, np.nan, np.nan, np.nan, np.nan]
Is_Bot = [False, False, False, False, False]
slug = ['cohort-1, cohort-2', np.nan, 'cohort-2', np.nan, 'cohort-1, cohort-2']

dict_output = {'Channel_ID':Channel_ID, 'Channel_Slug':Channel_Slug, 'Timestamp':Timestamp,
            'Timestamp_Thread':Timestamp_Thread, 'User_ID':User_ID, 'Full_Name':Full_Name,
            'Email':Email, 'Permalink':Permalink, 'Text':Text, 'Text_raw':Text_raw,
            'Slack_username':Slack_username, 'Team_ID':Team_ID, 'Team_Name':Team_Name, 
            'Is_Bot':Is_Bot, 'slug':slug}

##### Expected output #####
expected_output = pd.DataFrame(dict_output)



def run(df_slack, auth_user, cohort_users_with_slug):

    # Remove unnecessary columns
    auth_user = auth_user.drop(columns=['first_name', 'last_name', 'date_joined'])

    # Merge df_slack and auth_user so each message has the user_id
    slack_with_user_id = df_slack.merge(auth_user, left_on='Email', right_on='email', how='left')

    # Merge with cohort_users_with_slug so each message has the slug
    slack_with_slug = slack_with_user_id.merge(cohort_users_with_slug, left_on='id', right_on='user_id', how='left')

    # Remove unnecessary columns
    slack_with_slug = slack_with_slug.drop(columns=['id', 'email', 'user_id'])

    return slack_with_slug