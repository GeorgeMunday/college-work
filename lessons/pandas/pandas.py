import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and drop rows where all elements are NaN
df = pd.read_csv("data.csv").dropna(how="all")
print(df.head(999))

# Set the index if the column "Unnamed: 0" exists
if "Unnamed: 0" in df.columns:
    df.set_index("Unnamed: 0", inplace=True)

# Plot the scatter plot
df.plot(kind="scatter", x="calories", y="abv")

# Add title and labels
plt.title("Beer")
plt.xlabel("Calories")
plt.ylabel("ABV")

# Adjust layout and show the plot
plt.tight_layout()
plt.show()