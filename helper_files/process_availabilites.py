def process_calendar_availabilities(data):
    processed_data = {}
    for entry in data['calendar-availabilities']:
        if entry['availability'] != 'cms-key-no-availability':
            date_key = entry.pop('date')  # Remove the date and use it as the key
            processed_data[date_key] = entry  # Assign the rest of the dictionary to the date key
    return processed_data