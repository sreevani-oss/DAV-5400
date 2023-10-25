#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def summary_statistics(self) -> pd.DataFrame:
        """Returns summary statistics for numeric attributes."""
        return self.data.describe()

    def histogram(self, year: str):
        """Plots histogram for grant amounts of a given year."""
        plt.figure(figsize=(12, 6))
        plt.hist(self.data[year].dropna(), bins=30, edgecolor='black', alpha=0.7)
        plt.title(f'Distribution of Grant Amounts ({year})')
        plt.xlabel('Grant Amounts')
        plt.ylabel('Number of Countries')
        plt.grid(axis='y')
        plt.show()

    def boxplot(self, year: str):
        """Plots boxplot for grant amounts of a given year."""
        plt.figure(figsize=(12, 6))
        plt.boxplot(self.data[year].dropna(), vert=False)
        plt.title(f'Boxplot of Grant Amounts ({year})')
        plt.xlabel('Grant Amounts')
        plt.grid(axis='x')
        plt.show()


# In[ ]:




