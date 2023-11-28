#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Inference:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def top_n_countries(self, year: str, n: int) -> pd.DataFrame:
        """Identifies top N countries/entities based on grant amounts for a given year."""
        return self.data[['Country Name', year]].nlargest(n, year)

    def plot_grant_trends(self, countries: list):
        """Plots grant trends for given countries/entities over the years."""
        trend_data = self.data[self.data['Country Name'].isin(countries)].set_index('Country Name').iloc[:, 3:-1].transpose()
        plt.figure(figsize=(16, 8))
        for country in trend_data.columns:
            plt.plot(trend_data.index, trend_data[country], label=country, marker='o')
        plt.title('Grant Trends for Selected Entities')
        plt.xlabel('Year')
        plt.ylabel('Grant Amounts')
        plt.legend()
        plt.grid(axis='y')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def global_grant_trend(self):
        """Analyzes and plots the global trend of grant allocations over the years."""
        # Summing grant amounts for each year
        yearly_totals = self.data.iloc[:, 3:].sum()
    
        # Converting the index to a list of years (as strings)
        years = list(yearly_totals.index.astype(str))
        total_grants = yearly_totals.values
    
        # Plotting
        plt.figure(figsize=(16, 8))
        plt.plot(years, total_grants, marker='o')
        plt.title('Global Trend of Grant Allocations Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Total Grant Amount')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()





# In[ ]:




