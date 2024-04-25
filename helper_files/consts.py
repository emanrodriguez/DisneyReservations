DISNEY_API_URL = "https://disneyland.disney.go.com/passes/blockout-dates/api/get-availability/"

NUM_MONTH_AVAILABILITY = 2


DISNEY_PARK_LOCATIONS = {
    'California Disneyland Resort' : 'DLR',
    'Walt Disney World' : 'WDW'
}

DISNEY_LOCATION_SUBPARKS = {
    'WDW': {
        'WDW_ALL':{
            'parkType': 'All Parks'
        },
        'WDW_AK':{
            'parkType': 'Animal Kingdom'
        },
        'WDW_EP':{
            'parkType': 'Epcot'
        },
        'WDW_HS':{
            'parkType': 'Hollywood Studios'
        },
        'WDW_MK':{
            'parkType': 'Magic Kingdom'
        }
    }
}


DISNEY_PARK_PASSES = {
    'DLR' : ('inspire-key-pass','believe-key-pass','enchant-key-pass','imagine-key-pass','dream-key-pass'),
    'WDW' : ('disney-incredi-pass','disney-sorcerer-pass','disney-pirate-pass','disney-pixie-dust-pass')
}


DISNEY_PARK_DETAILS = {
    'DLR' : {
        'LOCATION_NAME' : 'California Disneyland Resort',
        'ANNUAL_PASSES' : DISNEY_PARK_PASSES['DLR'],
        'SUB_PARKS' : None
    },
    'WDW' : {
        'LOCATION_NAME' : 'Walt Disney World',
        'ANNUAL_PASSES' : DISNEY_PARK_PASSES['WDW'],
        'SUB_PARKS' : DISNEY_LOCATION_SUBPARKS['WDW']
    }
}


DISNEY_API_HEADERS = {
    "Dnt": "1",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}