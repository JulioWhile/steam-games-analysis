import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DataExploration:

    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews']
        mean_values = self.data[numeric_columns].mean()

        return mean_values

    def calculate_median(self):
        numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews']
        median_values = self.data[numeric_columns].median()

        return median_values

    def calculate_standard_deviation(self):
        numeric_columns = ['peak_players', 'positive_reviews', 'negative_reviews', 'total_reviews']
        standard_deviation = np.std(self.data[numeric_columns])

        return standard_deviation

    def plot_histogram(self, column):
        # Plot histogram of a specific column
        plt.hist(self.data[column], bins=10)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')

        plt.show()

    def plot_boxplot(self, column):
        # Plot box plot of a specific column
        plt.boxplot(self.data[column])
        plt.xlabel(column)
        plt.ylabel('Value')
        plt.title(f'Box Plot of {column}')

        plt.show()

    def plot_density(self, column):
        # Plot density plot of a specific column
        sns.kdeplot(self.data[column])
        plt.xlabel(column)
        plt.ylabel('Density')
        plt.title(f'Density Plot of {column}')

        plt.show()