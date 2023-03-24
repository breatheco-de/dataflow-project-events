import numpy as np 
import pandas as pd 


##### Values for inputs #####

### cohort_users ###
idx = [1, 2, 3, 4, 5, 6]
role = ['student', 'STUDENT', 'teacher', 'student', 'STUDENT', 'student']
finantial_status = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
educational_status = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
created_at = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
updated_at = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
cohort_id = [11, 12, 11, 12, 13, 14]
user_id = [111, 222, 333, 111, 444, 555]
watching = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

dict_cohort_users = {'id':idx, 'role':role, 'finantial_status':finantial_status,
                        'educational_status':educational_status, 'created_at':created_at,
                        'updated_at':updated_at, 'cohort_id':cohort_id, 'user_id':user_id,
                        'watching':watching}

### cohorts ###
id_ = [11, 12, 13, 14]
slug = ['cohort-1', 'cohort-2', 'cohort-3', 'cohort-4']
name = ['Cohort-1', 'Cohort-2', 'Cohort-3', 'Cohort-4']
kickoff_date = [np.nan, np.nan, np.nan, np.nan]
ending_date = [np.nan, np.nan, np.nan, np.nan]
current_day = [np.nan, np.nan, np.nan, np.nan]
stage = ['ACTIVE', 'STARTED', 'INACTIVE', 'ACTIVE']
language = ['en', 'es', 'es', 'en']
created_at = [np.nan, np.nan, np.nan, np.nan]
updated_at = [np.nan, np.nan, np.nan, np.nan]
academy_id = [np.nan, np.nan, np.nan, np.nan]
timezone = [np.nan, np.nan, np.nan, np.nan]
private = [np.nan, np.nan, np.nan, np.nan]
never_ends = [False, False, False, True]
schedule_id = [np.nan, np.nan, np.nan, np.nan]
syllabus_version_id = [np.nan, np.nan, np.nan, np.nan]
online_meeting_url = [np.nan, np.nan, np.nan, np.nan]
remote_available = [np.nan, np.nan, np.nan, np.nan]
current_module = [np.nan, np.nan, np.nan, np.nan]
history_log = [np.nan, np.nan, np.nan, np.nan]
is_hidden_on_prework = [np.nan, np.nan, np.nan, np.nan]

dict_cohorts = {'id':id_, 'slug':slug, 'name':name, 'kickoff_date':kickoff_date, 
        'ending_date':ending_date, 'current_day':current_day, 'stage':stage, 
        'language':language, 'created_at':created_at, 'updated_at':updated_at, 
        'academy_id':academy_id, 'timezone':timezone, 'private':private, 
        'never_ends':never_ends, 'schedule_id':schedule_id,
        'syllabus_version_id':syllabus_version_id, 'online_meeting_url':online_meeting_url,
        'remote_available':remote_available, 'current_module':current_module,
        'history_log':history_log, 'is_hidden_on_prework':is_hidden_on_prework}

##### Expected inputs #####
expected_inputs = [pd.DataFrame(dict_cohort_users), pd.DataFrame(dict_cohorts)]


##### Values for output #####
user_id = [111, 222, 444, 555]
slug = ['cohort-1, cohort-2', 'cohort-2', 'not actively studying', 'not actively studying']

dict_output = {'user_id':user_id, 'slug':slug}

### Expected output ###
expected_output = pd.DataFrame(dict_output)



def run(cohort_users, cohorts):

    # Consider only rows with student as role
    cohort_users = cohort_users[cohort_users['role'].str.lower()=='student']

    # Remove unnecessary columns
    cohort_users = cohort_users.drop(columns=['id', 'role', 'finantial_status', 'educational_status', 'created_at', 'updated_at', 'watching'])

    # Remove unnecessary columns
    cohorts = cohorts.drop(columns=['name', 'kickoff_date', 'ending_date', 'current_day', 'language', 
            'created_at', 'updated_at', 'academy_id', 'timezone', 'private', 'schedule_id',
            'syllabus_version_id', 'online_meeting_url', 'remote_available', 'current_module', 
            'history_log', 'is_hidden_on_prework'])

    # Consider only cohorts with stage ACTIVE or STARTED
    cohorts = cohorts[cohorts['stage'].isin(['ACTIVE', 'STARTED'])]

    # Consider only cohorts that end
    cohorts = cohorts[cohorts['never_ends']==False]

    # Merge both dataframes
    cohort_users_with_slug = cohort_users.merge(cohorts, left_on='cohort_id', right_on='id', how='left')

    # Concatenate all slugs associated with the same user_id
    cohort_users_with_slug['slug'] = cohort_users_with_slug['slug'].replace({np.nan: None})
    grouped_df = cohort_users_with_slug.groupby('user_id').agg({'slug': lambda x: ', '.join([str(i) for i in x if i is not None])}).reset_index()
    grouped_df['slug'] = grouped_df['slug'].replace({'':np.nan})

    # Add suffixes when merging for easy identification
    cohort_users_with_slug = cohort_users_with_slug.merge(grouped_df, on='user_id', suffixes=('_simple', '_concatenated'))

    # Remove unnecessary columns
    cohort_users_with_slug = cohort_users_with_slug.drop(columns=['cohort_id', 'id', 'stage', 'never_ends', 'slug_simple'])

    # Rename column
    cohort_users_with_slug = cohort_users_with_slug.rename(columns={'slug_concatenated':'slug'})

    # Remove duplicates, so there is a single row per user_id, containing all slugs associated with each user_id
    cohort_users_with_slug = cohort_users_with_slug.drop_duplicates()
    
    # Replace value for those without slug
    cohort_users_with_slug['slug'] = cohort_users_with_slug['slug'].fillna('not actively studying')

    return cohort_users_with_slug