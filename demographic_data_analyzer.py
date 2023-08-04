# Data Analysis with Python Projects - Freecodecamp Course

#############################
# Demographic Data Analyzer #
#############################

"""
In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted
from the 1994 Census database. You must use Pandas to answer the following questions:
- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

"""

# Libraries
import pandas as pd

# Solution
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df.loc[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors)/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education.loc[higher_education['salary'] == '>50K'])/len(higher_education))*100, 1)
    lower_education_rich = round((len(lower_education.loc[lower_education['salary'] == '>50K'])/len(lower_education))*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = round(len(df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])/len(df.loc[df['hours-per-week'] == 1])*100)

    # What country has the highest percentage of people that earn >50K?
    countries_rich_amount = {}
    for country in df['native-country'].unique():
        countries_rich_amount[country] = len(df.loc[(df['native-country'] == country) & (df['salary'] == '>50K')])
    countries_rich_percentage = {}
    for country, rich_people in countries_rich_amount.items():
        countries_rich_percentage[country] = round((countries_rich_amount[country]/len(df.loc[df['native-country'] == country])) * 100, 1)
    highest_earning_country = max(zip(countries_rich_percentage.values(), countries_rich_percentage.keys()))[1]
    highest_earning_country_percentage = countries_rich_percentage[highest_earning_country]

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indians = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = rich_indians.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }