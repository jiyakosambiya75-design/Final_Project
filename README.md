# 🚢 TITANIC SURVIVAL DATA ANALYSIS SYSTEM
> **An Interactive Terminal-Based Data Exploratory Suite for the RMS Titanic Disaster**

---

## 🗺️ THE VISUAL PROJECT MAP
```text
 🚢 [Root Repository]
  │
  ├── 📊 Titanic-Dataset.csv       # Raw Historical Data Source
  ├── 🐍 titanic_analysis.py       # Core Interactive Execution Application
  └── 📝 README.md                 # Interactive Presentation Manual
```

---

## 🚀 QUICK START & REPRODUCTION SPEEDRUN

### 🛠️ 1. Environment Preparation
Ensure your Python workspace is fully configured with the required plotting and analytics dependencies. Execute the following installation string in your shell environment:

```bash
pip install numpy pandas matplotlib seaborn
```

### 🏃 2. Launching the Analytical Workspace
To fire up the interactive terminal engine, verify that `Titanic-Dataset.csv` sits squarely in the exact same execution directory as your script, then trigger:

```bash
python titanic_analysis.py
```

---

## ⚙️ ENGINE FUNCTIONALITY BREAKDOWN

Your python architecture operates on a cyclical, failure-resistant processing sequence:

```text
[Launch Application] ──> [load_and_clean_data()] ──> Check for 'Titanic-Dataset.csv'
                                                                 │
          ┌──────────────────────────────────────────────────────┴───┐
          ▼ (If Missing)                                             ▼ (If Found)
[Print FileNotFoundError Exception]                        [Impute Age & Embarked Missing Data]
          │                                                          │
[Exit Application Engine] <───────────────────────────────── [Engage interactive Loop Menu]
```

---

## 🧭 INTERACTIVE MENU CORE MATRIX

When the suite is initialised, the console exposes a 7-stage evaluation pipeline. Here is exactly what happens under the hood for each explicit user interaction sequence:

### 📥 Option 1: View Dataset Overview & Data Info
* **Program Action:** Executes `show_data_overview(dataset)`.
* **Console Response:** Invokes `.head()` to expose structural orientation, triggers `.info()` to reveal deep data architecture types, and logs `.isnull().sum()` to trace data voids.

### 📈 Option 2: View Statistical Survival Rates
* **Program Action:** Executes `show_summary_stats(dataset)`.
* **Console Response:** Prints aggregated survival percentages explicitly broken down across cross-sections of Passenger Class (`Pclass`), Gender (`Sex`), and a matrix combining both attributes simultaneously.

### 📊 Option 3: Plot Survival Rate by Gender
* **Program Action:** Executes `plot_survival_by_gender(dataset)`.
* **Console Response:** Halts execution to dynamically render a high-contrast Seaborn barplot isolating gender survival vectors using the `Set1` design theme.

### 🗂️ Option 4: Plot Survival Rate by Passenger Class & Gender
* **Program Action:** Executes `plot_survival_by_class(dataset)`.
* **Console Response:** Spawns a multi-dimensional categorical chart utilizing the `hue` extraction mechanism to map out class vulnerabilities alongside gender realities.

### ⏳ Option 5: Plot Age Distribution by Survival Status
* **Program Action:** Executes `plot_age_distribution(dataset)`.
* **Console Response:** Builds an interactive Kernel Density Estimate (`kde=True`) layered directly on a step-histogram using the `Set2` canvas theme.

### 🖼️ Option 6: Display Full Visualization Dashboard
* **Program Action:** Executes `plot_full_dashboard(dataset)`.
* **Console Response:** Instantiates a clean 2x2 coordinate sub-plotting window via Matplotlib (`plt.subplots(2, 2)`), binding structural counts, categorical survival patterns, and age distributions into a singular matrix.

### 🛑 Option 7: Exit Application
* **Program Action:** Breaks the execution runtime loop cleanly.
* **Console Response:** Terminates application logic and prints a formal farewell sequence safely.

---

## 🔍 DEEP HISTORICAL ANALYTICS MATRIX

Based directly on the categorical aggregation pipelines calculated in your `show_summary_stats` engine routines, the historical facts pattern resolves down to these essential points:

| Analytical Category | High-Probability Cohort | Vulnerable Cohort | Primary Behavioral Vector |
| :--- | :--- | :--- | :--- |
| **👩‍💼 Biological Gender** | Female Passengers | Male Passengers | Driven by historical emergency maritime rescue protocols ("Women & Children First"). |
| **🎟️ Socio-Economic Status** | First Class (`Pclass 1`) | Third Class (`Pclass 3`) | Driven by physical structural cabin proximity to top-deck lifeboat launch stations. |
| **👶 Generational Age** | Toddlers & Children | Young Adults (18-35) | Evident through standard normal distribution steps visible on your histogram interface. |

---

## 🛠️ CRITICAL CODE ENGINEERING ANALYSIS

Your application utilizes highly specialized routines designed to stabilize and transform standard structured inputs:

### 🧹 Fault-Tolerant Data Imputation Protocol
```python
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
```
* **Strategic Logic:** `Age` fields are structurally stabilized using a robust **Median** calculation, safeguarding data balances from extreme outlier values. Unassigned `Embarked` parameters are reconciled via the historical mathematical **Mode**, instantly aligning missing points with the most statistically probable seaport origin.

### 🎛️ Dynamic Sub-Plot Coordination
```python
figure, axes = plt.subplots(2, 2, figsize=(12, 8))
```
* **Strategic Logic:** Instead of generating competing standalone plotting screens, this script establishes an efficient coordinate space map (`axes[0,0]` through `axes[1,1]`), bundling structural features into a singular dashboard matrix.

---

## 📜 OPEN ACCESSIBILITY LICENSE
Distributed explicitly under the **MIT License**. Build, branch, or scale this terminal tool freely across your data engineering studies!
