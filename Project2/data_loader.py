
import pandas as pd
import requests

class DataLoader:
    """
    DataLoader is responsible for loading and preprocessing agricultural data.
    It can load data from a CSV file or fetch it directly from the USDA API.

    Attributes:
        file_path (str, optional): Path to the CSV file containing the data.
    """

    def __init__(self, file_path=None):
        """
        Initializes DataLoader with an optional path to the data file.

        Parameters:
            file_path (str, optional): Path to the CSV file.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Loads the data from the CSV file.

        Returns:
            DataFrame: A pandas DataFrame containing the loaded data.
        """
        if self.file_path:
            data = pd.read_csv(self.file_path)
            return data
        else:
            print("File path not provided.")
            return None

    def load_data_from_api(self, api_key, commodity, state, year):
        """
        Fetches data from the USDA API based on the specified parameters.

        Parameters:
            api_key (str): API key for accessing the USDA API.
            commodity (str): Commodity description.
            state (str): State code.
            year (str): Year of the data.

        Returns:
            DataFrame: A pandas DataFrame containing the data fetched from the API.
        """
        base_url = "https://quickstats.nass.usda.gov/api/api_GET/"
        params = {
            "key": api_key,
            "commodity_desc": commodity,
            "state_alpha": state,
            "year": year,
            "format": "JSON"
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json().get('data', [])
                return pd.DataFrame(data)
            else:
                print(f"Error: {response.status_code} - {response.json()}")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def preprocess_data(self, data):
        """
        Performs basic preprocessing on the dataset such as handling missing values.

        Parameters:
            data (DataFrame): The pandas DataFrame to preprocess.

        Returns:
            DataFrame: The preprocessed pandas DataFrame.
        """
        # Example preprocessing step: Drop rows with missing values
        data_cleaned = data.dropna()
        return data_cleaned
