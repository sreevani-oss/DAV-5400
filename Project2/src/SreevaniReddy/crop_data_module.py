
import requests
import pandas as pd

class CropDataHandler:
    '''
    A class to handle the interaction with the USDA agricultural data API and process corn crop data.

    Methods:
        fetch_crop_data(api_key, commodity, state, year): Fetches crop data from the USDA API.
        process_data(data): Processes the raw crop data into a structured format.
    '''

    def __init__(self):
        '''
        Initializes the CropDataHandler class.
        '''
        self.base_url = "https://quickstats.nass.usda.gov/api/api_GET/"

    def fetch_crop_data(self, api_key, commodity, state, year):
        '''
        Fetches crop data from the USDA API.

        Args:
            api_key (str): API key for accessing USDA data.
            commodity (str): Type of commodity to fetch (e.g., "Corn").
            state (str): State code (e.g., "CA").
            year (str): Year of the data (e.g., "2020").

        Returns:
            DataFrame: A pandas DataFrame containing the fetched crop data.
        '''
        params = {
            "key": api_key,
            "commodity_desc": commodity,
            "state_alpha": state,
            "year": year,
            "format": "JSON"
        }

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json().get('data', [])
                return pd.DataFrame(data)
            else:
                print(f"Error: {response.status_code} - {response.json()}")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        


