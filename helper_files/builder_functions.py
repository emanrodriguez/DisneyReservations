import requests
from helper_files.consts import DISNEY_API_URL, DISNEY_API_HEADERS

def fetch_blockout_dates(destination_id, product_types, num_months):
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