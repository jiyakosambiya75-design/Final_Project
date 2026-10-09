# Titanic Data Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data(file_path='Titanic-Dataset.csv'):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"\nError: Could not find '{file_path}'. Ensure the file is in the current directory.")
        return None

    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

    return data


def show_summary_stats(data):
    print("\n", "=!" * 20)
    print("         Dataset Summary ")
    print("=!" * 20)
    print(f"Total Passengers Analyzed : {len(data)}")
    print(f"Overall Survival Rate     : {data['Survived'].mean() * 100:.2f}%\n")

    print(" Survival Rate by Sex ")
    print((data.groupby('Sex')['Survived'].mean() * 100).map('{:.2f}%'.format))

    print("\n Survival Rate (%) By Class ")
    print((data.groupby('Pclass')['Survived'].mean() * 100).map('{:.2f}%'.format))

    print("\n Survival Rate by Class & Sex ")
    print((data.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100).map('{:.2f}%'.format))
    print("=" * 40)


def show_data_overview(data):
    print("\n", "*" * 40)
    print("            DATA OVERVIEW")
    print("=" * 40)

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nDataset Information:")
    data.info()

    print("\nMissing Values Count:")
    print(data.isnull().sum())
    print("=" * 40)


def plot_survival_by_gender(data):
    # Show survival rates for male and female passengers
    plt.figure(figsize=(6, 4))
    sns.barplot(data=data, x='Sex', y='Survived', palette='Set1')
    plt.title('Survival Rate by Gender')
    plt.ylabel('Survival Rate')
    plt.show()


def plot_survival_by_class(data):
    # Compare survival rates across passenger classes and genders
    plt.figure(figsize=(7, 5))
    sns.barplot(data=data, x='Pclass', y='Survived', hue='Sex', palette='Set1')
    plt.title('Survival Rate by Passenger Class & Gender')
    plt.ylabel('Survival Rate')
    plt.xlabel('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)')
    plt.show()


def plot_age_distribution(data):
    # Display passenger ages according to survival status
    plt.figure(figsize=(8, 5))
    sns.histplot(data=data, x='Age', hue='Survived', kde=True,
                 element='step', palette='Set2')
    plt.title('Age Distribution by Survival Status')
    plt.xlabel('Age')
    plt.ylabel('Passenger Count')
    plt.show()


def plot_full_dashboard(data):
    # Create a dashboard with four different visualizations
    sns.set_theme(style="whitegrid")
    figure, axes = plt.subplots(2, 2, figsize=(12, 8))

    sns.countplot(ax=axes[0, 0], data=data, x='Survived', palette='Set2')
    axes[0, 0].set_title('Overall Survival Count')
    axes[0, 0].set_xticks([0, 1])
    axes[0, 0].set_xticklabels(['Died', 'Survived'])

    sns.barplot(ax=axes[0, 1], data=data, x='Sex', y='Survived', palette='Set1')
    axes[0, 1].set_title('Survival Rate by Gender')

    sns.barplot(ax=axes[1, 0], data=data, x='Pclass', y='Survived',
                hue='Sex', palette='Set1')
    axes[1, 0].set_title('Survival Rate by Class & Gender')

    sns.histplot(ax=axes[1, 1], data=data, x='Age', hue='Survived',
                 kde=True, element='step', palette='Set2')
    axes[1, 1].set_title('Age Distribution by Survival Status')

    plt.tight_layout()
    plt.show()


while True:
    dataset = load_and_clean_data()

    if dataset is None:
        print("Exiting application due to missing dataset file.")
        break

    print("\n", "=!" * 20)
    print("    TITANIC SURVIVAL ANALYSIS MENU")
    print("=!" * 20)
    print("1. View Dataset Overview & Data Info")
    print("2. View Statistical Survival Rates")
    print("3. Plot Survival Rate by Gender")
    print("4. Plot Survival Rate by Passenger Class & Gender")
    print("5. Plot Age Distribution by Survival Status")
    print("6. Display Full Visualization Dashboard")
    print("7. Exit")
    print("=" * 40)

    option = input("Enter your option (1-7): ").strip()

    if option == '1':
        show_data_overview(dataset)
    elif option == '2':
        show_summary_stats(dataset)
    elif option == '3':
        plot_survival_by_gender(dataset)
    elif option == '4':
        plot_survival_by_class(dataset)
    elif option == '5':
        plot_age_distribution(dataset)
    elif option == '6':
        plot_full_dashboard(dataset)
    elif option == '7':
        print("\nExiting Titanic Analysis Tool. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please select a number between 1 and 7.")
