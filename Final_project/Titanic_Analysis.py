
# Titanic Data Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load and Clean Data
def load_and_clean_data(file_path="Titanic-Dataset.csv"):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"\nError: Could not find '{file_path}'.")
        print("Please upload the Titanic CSV file first.")
        return None

    data["Age"] = data["Age"].fillna(data["Age"].median())
    data["Embarked"] = data["Embarked"].fillna(
        data["Embarked"].mode()[0]
    )

    return data


# 2. Show Summary Statistics
def show_summary_stats(data):
    print("\n", "=!" * 20)
    print("         Dataset Summary")
    print("=!" * 20)

    print(f"Total Passengers Analyzed: {len(data)}")
    print(
        f"Overall Survival Rate: "
        f"{data['Survived'].mean() * 100:.2f}%\n"
    )

    print("Survival Rate by Sex")
    print(
        (data.groupby("Sex")["Survived"].mean() * 100)
        .map("{:.2f}%".format)
    )

    print("\nSurvival Rate by Class")
    print(
        (data.groupby("Pclass")["Survived"].mean() * 100)
        .map("{:.2f}%".format)
    )

    print("\nSurvival Rate by Class and Sex")
    print(
        (data.groupby(["Pclass", "Sex"])["Survived"].mean() * 100)
        .map("{:.2f}%".format)
    )

    print("=" * 40)


# 3. Show Dataset Overview
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


# 4. Plot Survival by Gender
def plot_survival_by_gender(data):
    plt.figure(figsize=(6, 4))

    sns.barplot(
        data=data,
        x="Sex",
        y="Survived",
        hue="Sex",
        palette="Set1",
        legend=False
    )

    plt.title("Survival Rate by Gender")
    plt.ylabel("Survival Rate")
    plt.tight_layout()
    plt.show()


# 5. Plot Survival by Passenger Class
def plot_survival_by_class(data):
    plt.figure(figsize=(7, 5))

    sns.barplot(
        data=data,
        x="Pclass",
        y="Survived",
        hue="Sex",
        palette="Set1"
    )

    plt.title("Survival Rate by Passenger Class and Gender")
    plt.ylabel("Survival Rate")
    plt.xlabel("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)")
    plt.tight_layout()
    plt.show()


# 6. Plot Age Distribution
def plot_age_distribution(data):
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=data,
        x="Age",
        hue="Survived",
        kde=True,
        element="step",
        palette="Set2"
    )

    plt.title("Age Distribution by Survival Status")
    plt.xlabel("Age")
    plt.ylabel("Passenger Count")
    plt.tight_layout()
    plt.show()


# 7. Full Visualization Dashboard
def plot_full_dashboard(data):
    sns.set_theme(style="whitegrid")

    figure, axes = plt.subplots(2, 2, figsize=(12, 8))

    sns.countplot(
        ax=axes[0, 0],
        data=data,
        x="Survived",
        hue="Survived",
        palette="Set2",
        legend=False
    )

    axes[0, 0].set_title("Overall Survival Count")
    axes[0, 0].set_xticks([0, 1])
    axes[0, 0].set_xticklabels(["Died", "Survived"])

    sns.barplot(
        ax=axes[0, 1],
        data=data,
        x="Sex",
        y="Survived",
        hue="Sex",
        palette="Set1",
        legend=False
    )

    axes[0, 1].set_title("Survival Rate by Gender")

    sns.barplot(
        ax=axes[1, 0],
        data=data,
        x="Pclass",
        y="Survived",
        hue="Sex",
        palette="Set1"
    )

    axes[1, 0].set_title("Survival Rate by Class and Gender")

    sns.histplot(
        ax=axes[1, 1],
        data=data,
        x="Age",
        hue="Survived",
        kde=True,
        element="step",
        palette="Set2"
    )

    axes[1, 1].set_title("Age Distribution by Survival Status")

    plt.tight_layout()
    plt.show()


# 8. Main Menu
def main():
    dataset = load_and_clean_data()

    if dataset is None:
        print("Please upload the dataset and run the code again.")
        return

    while True:
        print("\n", "=!" * 20)
        print("    TITANIC SURVIVAL ANALYSIS MENU")
        print("=!" * 20)
        print("1. View Dataset Overview and Data Info")
        print("2. View Statistical Survival Rates")
        print("3. Plot Survival Rate by Gender")
        print("4. Plot Survival Rate by Passenger Class and Gender")
        print("5. Plot Age Distribution by Survival Status")
        print("6. Display Full Visualization Dashboard")
        print("7. Exit")
        print("=" * 40)

        option = input("Enter your option (1-7): ").strip()

        if option == "1":
            show_data_overview(dataset)

        elif option == "2":
            show_summary_stats(dataset)

        elif option == "3":
            plot_survival_by_gender(dataset)

        elif option == "4":
            plot_survival_by_class(dataset)

        elif option == "5":
            plot_age_distribution(dataset)

        elif option == "6":
            plot_full_dashboard(dataset)

        elif option == "7":
            print("\nExiting Titanic Analysis Tool. Goodbye!")
            break

        else:
            print(
                "\nInvalid choice. Please select a number between 1 and 7."
            )


if __name__ == "__main__":
    main()
