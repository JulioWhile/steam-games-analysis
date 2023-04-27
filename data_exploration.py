import pandas as pd
from datetime import datetime

# Read the CSV file
steam_data = pd.read_csv('datasets/games-release-ALL.csv')

# Specify the data types for each column
dtypes = {
    'game': str,
    'link': str,
    'release': str,
    'peak_players': str,
    'positive_reviews': str,
    'negative_reviews': str,
    'total_reviews': str,
    'rating': str
}

# Convert the columns to their respective data types
steam_data = steam_data.astype(dtypes)

# Remove commas from numeric columns
numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews']
steam_data[numeric_columns] = steam_data[numeric_columns].replace(',', '', regex=True)

# Convert 'rating' column to float
steam_data[numeric_columns] = steam_data[numeric_columns].apply(pd.to_numeric, errors='coerce', downcast='integer')
steam_data['rating'] = steam_data['rating'].str.rstrip('%').astype(float)

# Convert 'release' into a date
steam_data["release"] = pd.to_datetime(steam_data["release"], format="%b %d %Y")

# Print the resulting DataFrame
print(steam_data.dtypes)
print("\n")

# Calculate the 'AVG' for the rating of all games
# WHERE release year > 2005
# AND positive_reviews > 100
mean_rating = steam_data.loc[
    (pd.to_datetime(steam_data["release"]).dt.year > 2005) &
    (steam_data["positive_reviews"] > 100),
    "rating"
].mean()

print("Mean rating: {:.2f}".format(mean_rating))

median_rating = steam_data.loc[
    (pd.to_datetime(steam_data["release"]).dt.year > 2005) &
    (steam_data["positive_reviews"] > 100),
    "rating"
].median()
print("Median rating: {:.2f}".format(median_rating))

