import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Load the data from the CSV file into a DataFrame
df = pd.read_csv("Maryland_Report.csv")

# Convert 'Number of Records' column to numeric by removing commas
df['Number of Records'] = df['Number of Records'].replace(',', '', regex=True).astype(int)

# Sort the DataFrame by 'Number of Records' in descending order
df_sorted = df.sort_values(by='Number of Records', ascending=False)

# Select the top 20 rows
top_20 = df_sorted.head(20)

# Plotting the bar chart
plt.figure(figsize=(12, 8))
plt.bar(top_20['Common Name'], top_20['Number of Records'], color='skyblue')
plt.xlabel('Common Name')
plt.ylabel('Number of Records')
plt.title('Top 20 Invasive Plant Species in Maryland')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


html_str = mpld3.fig_to_html(fig)
Html_file= open("graphs.html","w")
Html_file.write(html_str)
Html_file.close()

