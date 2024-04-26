from pprint import pprint
from server.src.helpers.process_park_data import fetch_all_calendar_dates, ProcessParkCalendar
from common.consts import Parks


response = fetch_all_calendar_dates(dest_enum=Parks.WDW, product_types=['disney-incredi-pass'], num_months=1)

print(ProcessParkCalendar(data=response).process_api_response())
