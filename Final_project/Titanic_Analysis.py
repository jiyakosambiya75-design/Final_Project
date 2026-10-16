
# Titanic Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter


# 1. Load and clean the dataset
def load_and_clean_data(file_path="Titanic-Dataset.csv"):
    try:
        data = pd.read_csv(file_path)

        required_columns = [
            "Survived", "Sex", "Pclass", "Age", "Embarked"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in data.columns
        ]

        if missing_columns:
            print("Error: Missing required columns:", missing_columns)
            return None

        # Fill missing Age values with the median
        data["Age"] = data["Age"].fillna(data["Age"].median())

        # Fill missing Embarked values with the mode
        embarked_mode = data["Embarked"].mode()

        if not embarked_mode.empty:
            data["Embarked"] = data["Embarked"].fillna(
                embarked_mode[0]
            )

        print("Dataset loaded and cleaned successfully!")
        return data

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    except pd.errors.EmptyDataError:
        print("Error: The dataset file is empty.")
        return None

    except pd.errors.ParserError:
        print("Error: Could not read the CSV file correctly.")
        return None


# 2. Display dataset overview
def show_data_overview(data):
    print("\n" + "=" * 40)
    print("           DATA OVERVIEW")
    print("=" * 40)

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nDataset Information:")
    data.info()

    print("\nMissing Values Count:")
    print(data.isnull().sum())

    print("\nDataset Shape:", data.shape)


# 3. Display survival statistics
def show_summary_stats(data):
    print("\n" + "=" * 40)
    print("         SURVIVAL STATISTICS")
    print("=" * 40)

    print("\nTotal Passengers:", len(data))

    survival_rate = data["Survived"].mean() * 100
    print(f"Overall Survival Rate: {survival_rate:.2f}%")

    print("\nSurvival Rate by Gender:")
    gender_rate = data.groupby("Sex")["Survived"].mean() * 100
    print(gender_rate.round(2).astype(str) + "%")

    print("\nSurvival Rate by Passenger Class:")
    class_rate = data.groupby("Pclass")["Survived"].mean() * 100
    print(class_rate.round(2).astype(str) + "%")

    print("\nSurvival Rate by Class and Gender:")
    class_gender_rate = (
        data.groupby(["Pclass", "Sex"])["Survived"].mean() * 100
    )
    print(class_gender_rate.round(2).astype(str) + "%")

    print("=" * 40)


# 4. Display survival rate by age group
def show_survival_by_age_group(data):
    age_data = data.copy()

    age_data["Age Group"] = pd.cut(
        age_data["Age"],
        bins=[0, 12, 18, 60, float("inf")],
        labels=["Child", "Teenager", "Adult", "Senior"],
        include_lowest=True
    )

    survival_rate = (
        age_data.groupby("Age Group", observed=False)["Survived"].mean()
        * 100
    )

    print("\n" + "=" * 40)
    print("       SURVIVAL RATE BY AGE GROUP")
    print("=" * 40)

    print(survival_rate.round(2).astype(str) + "%")


# 5. Plot survival rate by gender
def plot_survival_by_gender(data):
    plt.figure(figsize=(6, 4))

    ax = sns.barplot(
        data=data,
        x="Sex",
        y="Survived",
        color="steelblue"
    )

    ax.yaxis.set_major_formatter(PercentFormatter(1))
    plt.title("Survival Rate by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Rate")
    plt.tight_layout()
    plt.show()


# 6. Plot survival rate by passenger class and gender
def plot_survival_by_class(data):
    plt.figure(figsize=(7, 5))

    ax = sns.barplot(
        data=data,
        x="Pclass",
        y="Survived",
        hue="Sex",
        palette="Set1"
    )

    ax.yaxis.set_major_formatter(PercentFormatter(1))
    plt.title("Survival Rate by Passenger Class and Gender")
    plt.xlabel("Passenger Class (1 = First, 2 = Second, 3 = Third)")
    plt.ylabel("Survival Rate")
    plt.tight_layout()
    plt.show()


# 7. Plot age distribution
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


# 8. Display full dashboard
def plot_full_dashboard(data):
    sns.set_theme(style="whitegrid")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Overall survival count
    sns.countplot(
        data=data,
        x="Survived",
        ax=axes[0, 0],
        color="steelblue"
    )

    axes[0, 0].set_title("Overall Survival Count")
    axes[0, 0].set_xticks([0, 1])
    axes[0, 0].set_xticklabels(["Died", "Survived"])
    axes[0, 0].set_xlabel("Survival Status")
    axes[0, 0].set_ylabel("Passenger Count")

    # Survival by gender
    sns.barplot(
        data=data,
        x="Sex",
        y="Survived",
        ax=axes[0, 1],
        color="steelblue"
    )

    axes[0, 1].yaxis.set_major_formatter(PercentFormatter(1))
    axes[0, 1].set_title("Survival Rate by Gender")
    axes[0, 1].set_ylabel("Survival Rate")

    # Survival by class and gender
    sns.barplot(
        data=data,
        x="Pclass",
        y="Survived",
        hue="Sex",
        ax=axes[1, 0],
        palette="Set1"
    )

    axes[1, 0].yaxis.set_major_formatter(PercentFormatter(1))
    axes[1, 0].set_title("Survival by Class and Gender")
    axes[1, 0].set_ylabel("Survival Rate")

    # Age distribution
    sns.histplot(
        data=data,
        x="Age",
        hue="Survived",
        kde=True,
        element="step",
        palette="Set2",
        ax=axes[1, 1]
    )

    axes[1, 1].set_title("Age Distribution by Survival Status")
    axes[1, 1].set_ylabel("Passenger Count")

    plt.tight_layout()
    plt.show()


# 9. Main menu
def main():
    data = load_and_clean_data()

    if data is None:
        print("Project stopped. Please check your dataset file.")
        return

    while True:
        print("\n" + "=" * 40)
        print("    TITANIC SURVIVAL ANALYSIS MENU")
        print("=" * 40)
        print("1. View Dataset Overview")
        print("2. View Survival Statistics")
        print("3. Plot Survival Rate by Gender")
        print("4. Plot Survival by Class and Gender")
        print("5. Plot Age Distribution")
        print("6. Display Full Dashboard")
        print("7. Survival Rate by Age Group")
        print("8. Exit")
        print("=" * 40)

        option = input("Enter your option (1-8): ").strip()

        if option == "1":
            show_data_overview(data)

        elif option == "2":
            show_summary_stats(data)

        elif option == "3":
            plot_survival_by_gender(data)

        elif option == "4":
            plot_survival_by_class(data)

        elif option == "5":
            plot_age_distribution(data)

        elif option == "6":
            plot_full_dashboard(data)

        elif option == "7":
            show_survival_by_age_group(data)

        elif option == "8":
            print("Thank you for using Titanic Analysis!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


# Run the program
if __name__ == "__main__":
    main()
    
