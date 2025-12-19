# 🐾 Pandas Dojo — Full Training Levels

Welcome to the Pandas Dojo.  
No timelines.  
Just **levels → drills → questions → problems** to forge mastery.

---

# 🐾 LEVEL 0 — Boot Sequence (Awareness)

**Goal:** Know your tools & environment.

## Drills
- Create a folder for your datasets.  
- Load a CSV from disk.  
- Load a CSV from an online link.  
- Print: `shape`, `columns`, `dtypes`, `head`, `tail`.

## Questions
- Difference between `shape` and `info`?  
- Why does dtype matter?  
- What breaks when numbers are stored as strings?

## Problems
- CSV loads numbers as object → identify cause.  
- File has 50 columns, you need 10 → how to verify?  
- Weird encoding on load → what do you check?

---

# 🐾 LEVEL 1 — DF Fundamentals (Motor Control)

**Goal:** Navigate a DataFrame fast.

## Drills
- Select: one column, many columns, row slice, row by index.  
- Filter: single condition, two conditions, OR, NOT.  
- Create & reuse boolean masks.  
- Drop columns and rows.

## Questions
- Mental diff between selecting columns vs filtering rows?  
- When can chained filters misbehave?  
- Why boolean masks > plain filtering?

## Problems
- Extract rows where age is 20–35.  
- Remove bottom 20 rows.  
- Keep only name, age, city & verify stability.

---

# 🐾 LEVEL 2 — Data Cleaning (Deep Surgery)

**Goal:** Fix messy, inconsistent data.

## Drills
- Convert dtype to int, float, category, datetime.  
- Detect missing values.  
- Drop missing rows.  
- Fill missing using mean, 0, "Unknown".  
- Replace garbage strings.  
- Extract username from email, year from date, first name from full name.

## Questions
- Why dtype conversion early?  
- Strategic diff: `dropna` vs `fillna`?  
- When is replace > fill?  
- Why dates-as-string is dangerous?

## Problems
- Clean salary column with: `"5000"`, `"5,000"`, `"$5000"`, `NaN`.  
- Fix mixed-format date column.  
- Clean mixed-type age column.

---

# 🐾 LEVEL 3 — Grouping, Summaries & Combining (Strategic Thinking)

**Goal:** Compress data & find patterns.

## Drills
- Group by columns: count/mean/sum/min/max.  
- Group by two columns.  
- Create pivot tables.  
- Use value_counts across multiple columns.  
- Merge: inner, left, right, outer.  
- Concat rows and columns.

## Questions
- Why is groupby more powerful than filtering?  
- Conceptual difference: merge vs concat?  
- Why pivot tables matter?

## Problems
- Students dataset → avg marks per subject, top scorer per subject.  
- Employees dataset → count per department, highest salary per dept.  
- Merge datasets with mismatches → detect mismatched keys.

---

# 🐾 LEVEL 4 — Transformations (Shape-Shifting Mode)

**Goal:** Bend data into new forms.

## Drills
- Apply a function to a column.  
- Map using a dictionary.  
- Applymap to entire DF.  
- Remove duplicates.  
- Rank values.  
- Normalize 0–1.  
- Bin numbers: fixed bins & quantile bins.

## Questions
- When is apply > map?  
- Why quantile bins > fixed bins for skewed data?  
- Risks of apply (performance)?

## Problems
- Tag transaction amounts small/medium/large.  
- Normalize them.  
- Remove duplicate SKUs & detect inconsistent duplicates.  
- Rank top 10% salaries.

---

# 🐾 LEVEL 5 — Time Series (Temporal Awareness)

**Goal:** Understand data across time.

## Drills
- Convert column to datetime.  
- Sort by date.  
- Extract year/month/day.  
- Resample daily→weekly, weekly→monthly.  
- Compute rolling averages.  
- Detect spikes with diff + shift.

## Questions
- Why datetime dtype exists?  
- What insights appear only after resampling?  
- How does rolling window smooth noise?

## Problems
- Detect weeks with >40% sales jump.  
- Compute 7-day moving visitor average.  
- Detect month-wise seasonal pattern.

---

# 🐾 LEVEL 6 — Full Project (Real-World Combat)

**Goal:** Apply everything end-to-end.

## Tasks
- Pick a messy dataset.  
- Clean types, missing, strings, dates.  
- Summaries + groupings.  
- Transform into new columns.  
- Write plain-English insights.  
- Export cleaned + analyzed files.

## Questions
- Which insights are meaningful vs noise?  
- Which transformations helped most?  
- Which mistakes wasted time?

## Problems
- Re-do project with totally different dataset.  
- Merge 2–3 datasets.  
- Create 10 original questions & answer with pandas.

---

# 🐾 LEVEL X — Self-Dataset (Master Forging)

**Goal:** Build your own dataset.

## Drills
Track something for 3–7 days:  
- mood, expenses, food, workouts, screen time, ML training logs.  
- Build dataset → clean → analyze → extract patterns.

## Questions
- Hardest column to clean?  
- Most surprising trend?  
- What would change with more data?

---

# Start

Say **“meow start level 0”** to begin the guided step-by-step dojo.
