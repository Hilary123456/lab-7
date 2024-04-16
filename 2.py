import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data2.csv')

# Selecting the specified column (3rd column, index 2 for 0-based index)
column_data = data.iloc[:, 2]  # Adjusting index as necessary

# Calculating standard deviation
std_deviation = column_data.std()
print(f"Стандартное отклонение: {std_deviation}")

# Creating histogram
plt.figure(figsize=(10, 6))
plt.hist(column_data, bins=16, alpha=0.75, color='blue')
plt.title('Гистограмма столбца 3 из data2.csv')
plt.xlabel('Solids')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()