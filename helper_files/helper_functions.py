import requests
from helper_files.consts import DISNEY_API_URL, DISNEY_API_HEADERS, DISNEY_PARK_FACILITIES


def process_facilities_dict(entry):
    new_date_dict = {}

    for facility_info in entry['facilities']:
        facilityName = facility_info.pop('facilityName')
        new_date_dict[facilityName] = facility_info

    entry['facilities'] = new_date_dict
    return entry


def process_single_date_dict(entry):
    return process_facilities_dict(entry=entry)

    

def process_all_calendar_availabilities(data):
    processed_data = {}
    for entry in data['calendar-availabilities']:
        date_key = entry.pop('date')  # Remove the date and use it as the key
        processed_data[date_key] = process_single_date_dict(entry=entry)  # Assign the rest of the dictionary to the date key
    return processed_data


def fetch_all_calendar_dates(destination_id, product_types, num_months):
    """
    Fetches blockout dates from the Disney API.

    Args:
    product_types (list of str): List of product types.
    destination_id (str): The destination ID (e.g., 'WDW' for Walt Disney World).
    num_months (int): Number of months to fetch data for.

    Returns:
    dict: The JSON response from the API.
    """
    # Prepare the query parameters
    params = {
        'product-types': ','.join(product_types),
        'destinationId': destination_id,
        'numMonths': num_months
    }
    # Send the GET request
    response = requests.get(url = DISNEY_API_URL, params=params, headers=DISNEY_API_HEADERS)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        response.raise_for_status()  # Raise an HTTPError if the request was not successful