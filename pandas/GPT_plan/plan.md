[Plan](https://www.geeksforgeeks.org/pandas/pandas-tutorial/)

# 🐾 PANDAS MASTERY ROADMAP (Cat-Dojo Edition)

A level-based, practical training path designed to help you master Pandas by doing, experimenting, and building real mini-projects.

---

## **LEVEL 0 — Preparation (30 minutes)**

### **Goal:** Pure readiness.

**Do:**

* Install pandas
* Create a `pandas_lab` folder
* Open Jupyter/VSCode
* Load 2 test files:

  * `sample.csv` (10 rows)
  * `large.csv` (5000+ rows from Kaggle)

**Checkpoints:**

* ✔️ Can import pandas
* ✔️ Can read a CSV without googling
* ✔️ Can print shape, columns

---

## **LEVEL 1 — DataFrame Core Moves (the fundamentals)**

### **Goal:** Move through DataFrames effortlessly.

### **Learn:**

* `.head()`, `.tail()`, `.info()`, `.describe()`
* Column selection
* Row filtering
* Boolean masking
* Chaining (`df[condition][columns]`)

### **Micro-drills:**

* Load CSV → show first 5 rows
* Select 3 specific columns
* Filter rows where age > 30
* Filter with multiple conditions
* Drop columns/rows

### **Mini Project #1 — Student Marks Cleaner:**

* Clean missing values
* Remove students with <35 marks
* Sort top scorers
* Export to CSV

**Checkpoint:**

* ✔️ You can manipulate columns/rows without thinking.

---

## **LEVEL 2 — Data Types & Cleaning (the real battle)**

### **Goal:** Clean data with precision.

### **Learn:**

* `.astype()` conversions
* `.isna()`, `.dropna()`, `.fillna()`
* `.replace()`
* String ops: `.str.lower()`, `.str.extract()`
* Datetime: `pd.to_datetime()`

### **Micro-drills:**

* Convert salary column to int
* Replace "N/A" and "missing" with NaN
* Extract username from email
* Fix mixed types in columns
* Parse dates & sort

### **Mini Project #2 — Zomato Cleaning Lite:**

Fix a messy CSV with:

* Wrong types
* Garbage strings
* Missing ratings
* Date issues

**Checkpoint:**

* ✔️ You can clean messy real-world data.

---

## **LEVEL 3 — Merging, Grouping, Aggregating**

### **Goal:** Summarize and combine datasets.

### **Learn:**

* `merge()` (inner/left/right)
* `concat()` (rows/columns)
* `groupby()` + `agg()`
* `value_counts()`
* Pivot tables

### **Micro-drills:**

* Merge students with fees
* Group employees by department
* Count category frequencies
* Create pivot table

### **Mini Project #3 — IPL Mini Analysis:**

* Use matches + deliveries datasets
* Find top batsman per season
* Compute purple/orange cap stats
* Export summaries

**Checkpoint:**

* ✔️ You can join and summarize real data.

---

## **LEVEL 4 — Advanced Manipulation**

### **Goal:** Transform data like a pro.

### **Learn:**

* `.apply()` vs `.map()` vs `.applymap()`
* Lambdas in pandas
* `.duplicated()`
* `.nlargest()`
* Normalization & scaling
* Binning: `pd.cut`, `pd.qcut`

### **Micro-drills:**

* Normalize salary column
* Tag age groups
* Remove duplicates
* Apply a custom function
* Find top 10 expenses

### **Mini Project #4 — Expense Analyzer:**

* Load personal expenses CSV
* Categorize
* Summaries
* Wasteful spending detection
* Monthly breakdown

**Checkpoint:**

* ✔️ You can reshape, transform, categorize anything.

---

## **LEVEL 5 — Time Series & Visualization**

### **Goal:** Understand trends over time.

### **Learn:**

* `.resample()`
* `.shift()`
* Rolling windows
* `.plot()` for quick visuals

### **Micro-drills:**

* Convert timestamp → datetime
* Compute weekly/monthly averages
* Moving average of sales
* Spike detection via shift + diff

### **Mini Project #5 — Covid Timeseries Lite:**

* Weekly/monthly charts
* Rolling average
* Peak detection

**Checkpoint:**

* ✔️ You understand temporal patterns.

---

## **LEVEL 6 — Final Boss: Full Project**

Pick one dataset and deeply analyze it:

* Zomato
* IPL
* Airbnb
* Covid
* Car price
* Titanic
* Customer churn

### **Rules:**

* Clean → preprocess → analyze → visualize
* Document everything
* Export final insights

**Checkpoint:**

* ✔️ You can handle a real project confidently.

---

## **LEVEL X — Forge Your Own Dataset**

Track something from your life for 7 days:

* Food
* Mood
* Expenses
* Screen time
* ML training logs

Analyze it using the above skills.
This builds real mastery like nothing else.

---

## **End Goal**

By following this roadmap sincerely, you will be capable of analyzing, cleaning, transforming, and extracting insights from any dataset placed before you.
