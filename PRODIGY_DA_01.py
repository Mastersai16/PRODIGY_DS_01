# # Task-01
#Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, 
#such as the distribution of ages or genders in a population.

# Using Python libraries to visualize the distribution of a continuous variable

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'India.csv')

df.head(1)

sns.histplot(df['Age-standardised mean systolic blood pressure (mmHg)'], bins = 7)


'''he ASBP in this population is generally higher than the recommended levels.
The World Health Organization (WHO) recommends that the ASBP be less than 120 mmHg for adults aged 18-64 years and 
less than 130 mmHg for adults aged 65 years and older.'''


'''the higher ASBP in the oldest age group is likely due to a number of factors,
including age-related changes in the heart and blood vessels.'''

'''The higher ASBP in men than in women is likely due to a number of factors, 
including hormonal differences and lifestyle differences.'''

'''The graph highlights the importance of blood pressure control in all adults. 
High blood pressure is a major risk factor for heart disease, stroke, and other chronic diseases.
Also important to check your health regularly'''

'''Here are some tips for controlling blood pressure:

Eat a healthy diet, including plenty of fruits, vegetables, and whole grains.
Limit your salt intake.
Exercise regularly.
Maintain a healthy weight.
Avoid smoking and excessive alcohol consumption.'''
