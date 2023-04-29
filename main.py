from scripts.data_exploration import DataExploration
from scripts.data_processor import DataProcessor

# Create a DataProcessor instance
data_processor = DataProcessor('data/games-release.csv')

# Load the data
data_processor.load_data()

# Convert data types
data_processor.convert_data_types()

# Remove commas
data_processor.remove_commas()

# Convert Rating
data_processor.convert_rating()

# Convert release date
data_processor.convert_release_date()

# Access processed data
processed_data = data_processor.data

# Create a DataExploration instance
data_exploration = DataExploration(processed_data)

# Calculate Mean Values
mean_values = data_exploration.calculate_mean()
mean_values = mean_values.round(decimals=2)
print(mean_values, "\n")

# Calculate Median Values
median_values = data_exploration.calculate_median()
median_values = median_values.round(decimals=2)
print(median_values, "\n")

# Calculate standard deviation
std_dev = data_exploration.calculate_standard_deviation()
std_dev = std_dev.round(decimals=2)
print(std_dev)

# Plot Histogram
data_exploration.plot_histogram('peak_players')

# Plot box plot
data_exploration.plot_boxplot('rating')

# Plot density plot
data_exploration.plot_density('total_reviews')




