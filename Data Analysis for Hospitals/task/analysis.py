import pandas as pd
import matplotlib.pyplot as plt

# Set the number of columns to display in the terminal
pd.set_option('display.max_columns', 8)

# Read 3 CSV files containing the datasets
general = pd.read_csv("files/test/general.csv")
prenatal = pd.read_csv("files/test/prenatal.csv")
sports = pd.read_csv("files/test/sports.csv")

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
df.dropna(axis=0, thresh=1, inplace=True)

df['gender'] = df['gender'].replace(['male', 'man', 'female', 'woman'], ['m', 'm', 'f', 'f'])
df.loc[(df['hospital'] == 'prenatal') & (df['gender'].isna()), 'gender'] = 'f'

cols_to_fill = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[cols_to_fill] = df[cols_to_fill].fillna(0)

# Count the occurrences of each name
# hospital_counts = df['hospital'].value_counts()

# Calculate the hospital with the most clients
# top_hospital = hospital_counts.idxmax()

# Calculate the proportion of 'stomach' diagnosis in 'general' hospital patients
# stomach_clients_general = df[(df['hospital'] == 'general') & (df['diagnosis'] == 'stomach')].shape[0] /
# df[df['hospital'] == 'general'].shape[0]
# stomach_clients_general = round(stomach_clients_general, 3)

# Calculate the proportion of 'dislocation' diagnosis in 'sports' hospital patients
# dislocation_clients_sports = df[(df['hospital'] == 'sports') & (df['diagnosis'] == 'dislocation')].shape[0] /
# df[df['hospital'] == 'sports'].shape[0]
# dislocation_clients_sports = round(dislocation_clients_sports, 3)

# Calculate the absolute difference in median ages between 'general' and 'sports' hospitals
# median_age_general = df[df['hospital'] == 'general']['age'].mean()
# median_age_sports = df[df['hospital'] == 'sports']['age'].mean()
# age_difference = abs(median_age_general - median_age_sports)

# Calculate the number of blood tests in each hospital and find the one with the most tests
# blood_general = df[(df['hospital'] == 'general') & (df['blood_test'] == 't')].shape[0]
# blood_sports = df[(df['hospital'] == 'sports') & (df['blood_test'] == 't')].shape[0]
# blood_prenatal = df[(df['hospital'] == 'prenatal') & (df['blood_test'] == 't')].shape[0]

# most_blood_hospital = ''
# most_blood_clients = 0
#
# if blood_general > blood_sports and blood_general > blood_prenatal:
#     most_blood_hospital = 'general'
#     most_blood_clients = blood_general
# elif blood_sports > blood_general and blood_sports > blood_prenatal:
#     most_blood_hospital = 'sports'
#     most_blood_clients = blood_sports
# elif blood_prenatal > blood_general and blood_prenatal > blood_sports:
#     most_blood_hospital = 'prenatal'
#     most_blood_clients = blood_prenatal

# print(f"Answer 2: {top_hospital}")
# print(f"Answer 2: {stomach_clients_general}")
# print(f"Answer 3: {dislocation_clients_sports}")
# print(f"Answer 4: {age_difference}")
# print(f"Answer 5: {most_blood_hospital}, {most_blood_clients} blood tests")

# # print(f"Data shape: {df.shape}")
# print(df.sample(n=20, random_state=30))

# The most common age of a patient ------------------------------------
ages = {}
age_ranges = ['0-15', '15-35', '35-55', '55-75', '70-80']

for age_range in age_ranges:
    age_start, age_end = map(int, age_range.split('-'))
    age_counts = df[(df['age'] >= age_start) & (df['age'] <= age_end)]['age'].count()
    ages[age_range] = age_counts

most_common_age_range = max(ages, key=ages.get)
print(f"The answer to the 1st question: {most_common_age_range}")

plt.bar(ages.keys(), ages.values())
plt.xlabel('Age Range')
plt.ylabel('Number of Patients')
plt.title('Number of Patients in Each Age Range')
plt.show()

# The most common diagnosis among patients ------------------------------
all_diagnosis = {}

for diagnosis in df['diagnosis']:
    if diagnosis in all_diagnosis:
        all_diagnosis[diagnosis] += 1
    else:
        all_diagnosis[diagnosis] = 1

most_common_diagnosis = max(all_diagnosis, key=all_diagnosis.get)

print(f"The answer to the 2st question: {most_common_diagnosis}")

diagnosis_labels = all_diagnosis.keys()
diagnosis_counts = all_diagnosis.values()

plt.pie(diagnosis_counts, labels=diagnosis_labels, autopct='1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Distribution of Patient Diagnoses")
plt.show()

# Height distribution by hospitals -----------------------------------
height_data_by_hospital = {}

for hospital, group in df.groupby('hospital'):
    height_data_by_hospital[hospital] = group['height']

print(f"The answer to the 3rd question: It's because in sports people must be higher.")

height_data_list = list(height_data_by_hospital.values())

plt.violinplot(height_data_list, showmedians=True, showmeans=True)

plt.title("Height Distribution by Hospitals")
plt.xticks(range(1, len(height_data_by_hospital) + 1), height_data_by_hospital.keys(), rotation=45)
plt.xlabel('Hospital')
plt.ylabel('Height')
plt.grid()

plt.show()
