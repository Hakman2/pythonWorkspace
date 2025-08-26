import pandas as pd

df = pd.read_csv(r"C:\Users\BI-TECH\Downloads\pythonWorkspace\shapes\student_scores.csv")
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
 
df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 80 else
              "B" if x >= 70 else
              "C" if x >= 50 else
              "F"
)

print(df.head())
print(df.columns)

