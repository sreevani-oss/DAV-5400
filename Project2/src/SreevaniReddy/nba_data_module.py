
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class NBADataHandler:
    '''
    A class to handle the extraction, processing, and visualization of NBA data.

    Methods:
        fetch_data(years): Fetches NBA data for the specified years.
        process_data(data): Processes the raw NBA data into a structured format.
        visualize_data(data): Creates visualizations for the processed NBA data.
    '''

    def __init__(self):
        '''
        Initializes the NBADataHandler class.
        '''
        self.base_url = 'https://www.basketball-reference.com/awards/awards_{year}.html#mvp'

    def fetch_data(self, years):
        '''
        Fetches NBA data for the specified years.

        Args:
            years (range): A range of years for which to fetch the data.

        Returns:
            DataFrame: A pandas DataFrame containing the fetched NBA data.
        '''
        data = []
        for year in years:
            url = self.base_url.format(year=year)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'id': 'mvp'})
            rows = table.find_all('tr')

            data_year = []
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                if len(cols) > 0:
                    data_year.append({
                        'Year': year,
                        'Player': cols[0],
                        'Age': cols[1],
                        'Tm': cols[2],
                        'First': cols[3],
                        'Pts Won': cols[4],
                        'Pts Max': cols[5],
                        'Share': cols[6],
                        'G': cols[7],
                        'MP': cols[8],
                        'PTS': cols[9],
                        'TRB': cols[10],
                        'AST': cols[11],
                        'STL': cols[12],
                        'BLK': cols[13],
                        'FG%': cols[14],
                        '3P%': cols[15],
                        'FT%': cols[16],
                        'WS': cols[17],
                        'WS/48': cols[18]
                    })

            df_year = pd.DataFrame(data_year)
            data.append(df_year)

        return pd.concat(data)

    def process_data(self, data):
        '''
        Processes the raw NBA data into a structured format.

        Args:
            data (DataFrame): The raw NBA data as a pandas DataFrame.

        Returns:
            DataFrame: The processed NBA data as a pandas DataFrame.
        '''
        data['PTS'] = pd.to_numeric(data['PTS'], errors='coerce')
        return data

    def visualize_data(self, data):
        '''
        Creates visualizations for the processed NBA data.

        Args:
            data (DataFrame): The processed NBA data as a pandas DataFrame.
        '''
        sns.set(style="whitegrid")
        plt.figure(figsize=(18, 10))

        # Distribution of MVP awards by age
        age_distribution = data['Age'].value_counts().sort_index()
        plt.subplot(2, 2, 1)
        age_distribution.plot(kind='bar', color='skyblue')
        plt.title('Distribution of MVP Awards by Age')
        plt.xlabel('Age')
        plt.ylabel('Number of Awards')

        # Trends in the number of points scored by MVPs over the years
        average_points_per_year = data.groupby('Year')['PTS'].mean()
        plt.subplot(2, 2, 2)
        average_points_per_year.plot(kind='line', marker='o', color='green')
        plt.title('Average Points Scored by MVPs Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Average Points')

        # Team-wise distribution of MVP awards
        team_distribution = data['Tm'].value_counts()
        plt.subplot(2, 2, 4)
        team_distribution.plot(kind='bar', color='purple')
        plt.title('Team-wise Distribution of MVP Awards')
        plt.xlabel('Team')
        plt.ylabel('Number of Awards')

        plt.tight_layout()
        plt.show()
