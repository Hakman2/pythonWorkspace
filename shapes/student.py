import pandas as pd

df = pd.read_csv("https://insiders.vscode.dev/github/Hakman2/pythonWorkspace/blob/main/shapes/__pycache__/student_scores.csv")
df["Average"] = df["Age"].apply(lambda x: "Adult" if x >= 18 else "Minor")
df.to_csv("https://insiders.vscode.dev/github/Hakman2/pythonWorkspace/blob/main/shapes/__pycache__/student_updatedscores.csv", index=False)
print(df)
