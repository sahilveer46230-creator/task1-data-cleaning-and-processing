
import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\netflix_titles.csv")

# 1. Basic Info
print("Initial Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# 2. Handle Missing Values
# Drop rows where title is missing
df.dropna(subset=["title"], inplace=True)

# Fill missing 'country' with 'Unknown'
df["country"].fillna("Unknown", inplace=True)

# Fill missing 'rating' with 'Not Rated'
df["rating"].fillna("Not Rated", inplace=True)

# Fill missing 'date_added' with mode value
df["date_added"].fillna(df["date_added"].mode()[0], inplace=True)

# 3. Remove Duplicates
df.drop_duplicates(inplace=True)

# 4. Standardize Text Columns
df["type"] = df["type"].str.strip().str.title()   # Movie, Tv Show
df["country"] = df["country"].str.strip()

# 5. Convert Dates
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# 6. Rename Columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 7. Fix Data Types
# Convert release_year to int
df["release_year"] = df["release_year"].astype(int)

# 8. Save Cleaned Dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("Final Shape:", df.shape)
print("Cleaning Completed! Cleaned file saved as netflix_cleaned.csv")
