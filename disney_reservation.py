import requests
import json
from helper_files.helper_functions import fetch_all_calendar_dates,process_all_calendar_availabilities
from pprint import pprint


response = fetch_all_calendar_dates(destination_id='DLR',product_types=['believe-key-pass'],num_months=1)
pprint(process_all_calendar_availabilities(response[0]))
