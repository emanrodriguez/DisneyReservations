"""
Included all the data processing from the API requests and responses from Disney's API
"""

from typing import List, Dict, Optional, Any
import requests
from common.consts import DISNEY_PARKS_API_URLS, DISNEY_API_HEADERS, Parks
from server.src.utils import utils
from pprint import pprint
class ProcessParkCalendar:
    """
    Used to Process data from Disney API Response
    """

    def __init__(self, data: Optional[Dict] = None) -> None:
        self.data = data

    def process_single_date_dict(self, single_entry: Optional[Dict] = None):
        """
        Processes and reformats a single date entry.
        """
        facilities_list = single_entry['facilities']
        return utils.transform_dict_list(facilities_list,'facilityName')

    def process_calendar_data(self, raw_cal_data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Processes the calendar data from a json response from Disney's API
        """
        if raw_cal_data is None:
            raw_cal_data = self.data
        processed_data = {}
        for single_entry in raw_cal_data['calendar-availabilities']:
            # Remove the date and use it as the key
            date_key = single_entry.pop('date')
            processed_data[date_key] = self.process_single_date_dict(
                single_entry=single_entry)  # Assign the rest of the dictionary to the date key
        return processed_data
    

    def process_api_response(self, raw_json_response: Optional[List] = None):
        """
        Processes and reformats the pass type and calendar data.
        """
        if raw_json_response is None:
            raw_json_response = self.data
        reformatted_data = utils.transform_dict_list(raw_json_response,'passType')
        for passType, calendarJson in reformatted_data.items():
            reformatted_data[passType] = self.process_calendar_data(raw_cal_data=calendarJson)
        
        pprint(reformatted_data)

    

def fetch_all_calendar_dates(dest_enum, product_types: List[str], num_months: int = 3) -> Dict:
    """
    Fetches calendar dates information from specific annual pass(es) using the Disney API.

    Args:
    product_types (list of str): List of product types.
    dest_id (str): The destination ID (e.g., 'WDW' for Walt Disney World).
    num_months (int): Number of months to fetch data for.

    Returns:
    dict: The JSON response from the API.
    """
    # Prepare the query parameters
    params = {
        'product-types': ','.join(product_types),
        'destinationId': utils.get_enum_value(dest_enum),
        'numMonths': num_months
    }
    # Send the GET request
    response = requests.get(url=DISNEY_PARKS_API_URLS[dest_enum], params=params, headers=DISNEY_API_HEADERS)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        response.raise_for_status()  # Raise an HTTPError if the request was not successful
        return {}
