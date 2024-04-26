"""
Contains all the constants needed for:
    1. Disney's API Responses, URL, and Params
    2. Any other constant lol
"""
from enum import Enum

class Parks(Enum):
    DLR = 'DLR'
    WDW = 'WDW'

CALENDAR_API_ENDPOINT = "/passes/blockout-dates/api/get-availability/"


NUM_MONTH_AVAILABILITY = 3

DISNEY_PARK_LOCATIONS = {
    'California Disneyland Resort': Parks.DLR,
    'Walt Disney World': Parks.WDW
}

DISNEY_PARK_FACILITIES = {
    Parks.WDW: {
        'WDW_ALL': {
            'parkType': 'All Parks'
        },
        'WDW_AK': {
            'parkType': 'Animal Kingdom'
        },
        'WDW_EP': {
            'parkType': 'Epcot'
        },
        'WDW_HS': {
            'parkType': 'Hollywood Studios'
        },
        'WDW_MK': {
            'parkType': 'Magic Kingdom'
        }
    },

    Parks.DLR: {
        'DLR_CA': {
            'parkType': 'California Adventure'
        },
        'DLR_DP': {
            'parkType': 'Disney Park'
        }
    }
}

DISNEY_PARK_PASSES = {
    Parks.DLR: ('inspire-key-pass', 'believe-key-pass',
            'enchant-key-pass', 'imagine-key-pass', 'dream-key-pass'),

    Parks.WDW: ('disney-incredi-pass', 'disney-sorcerer-pass',
            'disney-pirate-pass', 'disney-pixie-dust-pass')
}

DISNEY_PARKS_API_URLS = {
    Parks.DLR: 'https://disneyland.disney.go.com' + CALENDAR_API_ENDPOINT,
    Parks.WDW: 'https://disneyworld.disney.go.com' + CALENDAR_API_ENDPOINT
}

DISNEY_PARK_DETAILS = {
    Parks.DLR: {
        'LOCATION_NAME': 'California Disneyland Resort',
        'ANNUAL_PASSES': DISNEY_PARK_PASSES[Parks.DLR],
        'FACILITIES': None
    },
    Parks.WDW: {
        'LOCATION_NAME': 'Walt Disney World',
        'ANNUAL_PASSES': DISNEY_PARK_PASSES[Parks.WDW],
        'FACILITIES': DISNEY_PARK_FACILITIES[Parks.WDW]
    }
}


DISNEY_API_HEADERS = {
    "Priority": "u=0, i",
    "User-Agent": "Mozilla/5.0"
}
