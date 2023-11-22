import requests
import xml.etree.ElementTree as ET
import pandas as pd

class XMLDataHandler:
    """
    Handles the fetching, parsing, and conversion of XML data to a pandas DataFrame.

    Methods:
    fetch_and_parse_xml: Fetch and parse XML data from a given URL.
    xml_to_dataframe: Convert parsed XML data to a pandas DataFrame.
    """

    def fetch_and_parse_xml(self, url):
        """
        Fetch XML data from a given URL and parse it.

        Args:
            url (str): The URL to fetch XML data from.

        Returns:
            ElementTree: Parsed XML data.
        """
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        return root

    def xml_to_dataframe(self, root):
        """
        Convert parsed XML data to a pandas DataFrame.

        Args:
            root (ElementTree): The root of the parsed XML data.

        Returns:
            DataFrame: A pandas DataFrame containing data from the XML.
        """
        data = []
        for sitemap in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'):
            loc = sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            lastmod = sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod').text if sitemap.find('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod') is not None else None
            data.append({'loc': loc, 'lastmod': lastmod})

        return pd.DataFrame(data)
