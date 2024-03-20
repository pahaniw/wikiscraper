import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find("table", {'class': 'wikitable'})
data = []
if table is not None:  # Check if the table is found
    for row in table.find_all('tr')[1:]:  # Start from the second row to skip headers
        columns = row.find_all(['th', 'td'])
        if len(columns) >= 3:  # Ensure there are at least 3 columns
            Title = columns[2].text.strip()
            Gross = columns[3].text.strip()
            if Title and Gross:
                data.append([Title, Gross])

    # Define the 'data' list before creating the DataFrame
df = pd.DataFrame(data, columns=['Title', 'Gross'])
# Print or use the DataFrame as needed
print(df)