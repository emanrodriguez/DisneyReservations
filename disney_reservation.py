import requests
import json
from helper_files.builder_functions import fetch_blockout_dates
from helper_files.process_availabilites import process_calendar_availabilities
from pprint import pprint
# class DisneyReservation:
#     def __init__(self) -> None:
#         self.reservation_url = "https://disneyland.disney.go.com/passes/blockout-dates/api/get-availability/?product-types=inspire-key-pass,believe-key-pass,enchant-key-pass,imagine-key-pass,dream-key-pass&destinationId=DLR&numMonths=3"



#     def print_dates(self):
# url = "https://disneyland.disney.go.com"
response = fetch_blockout_dates(destination_id='DLR',product_types=['believe-key-pass'],num_months=1)
pprint(process_calendar_availabilities(response[0]))
# DisneyReservation().print_dates()