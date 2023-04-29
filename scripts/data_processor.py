import pandas as pd


class DataProcessor:
    numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews']

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        # Load CSV into a Pandas DataFrame
        self.data = pd.read_csv(self.file_path)

    def convert_data_types(self):
        # Specify the data types for each column
        dtypes = {
            'game': str,
            'link': str,
            'release': str,
            **{column: str for column in self.numeric_columns},
            'rating': str
        }

        # Convert the columns to their respective data types
        self.data = self.data.astype(dtypes)

    def remove_commas(self):
        # Remove commas from numeric columns
        self.data[self.numeric_columns] = self.data[self.numeric_columns].replace(',', '', regex=True)

    def convert_rating(self):
        # Convert 'rating' column to float
        self.data[self.numeric_columns] = self.data[self.numeric_columns].apply(pd.to_numeric, errors='coerce',
                                                                                downcast='integer')
        self.data['rating'] = self.data['rating'].str.rstrip('%').astype(float)

    def convert_release_date(self):
        # Convert 'release' into a date
        self.data["release"] = pd.to_datetime(self.data["release"], format="%b %d %Y")
