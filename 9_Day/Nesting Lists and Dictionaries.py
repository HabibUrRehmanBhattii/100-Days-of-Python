# Nesting Lists and Dictionaries
#  is a list that can hold dictionaries like this:

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

#  Nesting Dictionaries inside a List
travel_log = {
    "Freance" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# OR

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },  
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

# Nesting Dictionaries inside a Dictionary

travel_logs = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visted": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 5,
        },
    }

# Nesting Lists inside a Dictionary

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
    },
]


