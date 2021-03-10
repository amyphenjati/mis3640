"""
----------------------------------------------------------------------
Q1. Please complete the following function to use your APIKEY to
get current temperature (in Fahrenheit) in your current place
from openweathermap.org.
If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below,
but you will lose 10 points.
APIKEY = '8f62260aa7890d58d9a026e2810341ea'
----------------------------------------------------------------------
"""

import urllib.request
import json


def get_current_temp():
    """
    Returns current temperature in Fahrenheit in your current place
    from api.openweathermap.org
    Notice: the temperature returned from the API is in Kelvin.
    Below is the conversion formula form Kelvin to Fahrenheit:
    T(°F) = T(°K) × 9/5 - 459.67
    """
    APIKEY = "22499eddd60c8b6d76550fa01c151bcc"
    city = "Bangkok"
    country_code = "th"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}"

    print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    faranheit = (response_data["main"]["temp"]) * 9 / 5 - 459.67

    return faranheit


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(get_current_temp())

## Expected output: 87.44


"""
----------------------------------------------------------------------
Q2. complete the following function
----------------------------------------------------------------------
"""
rules = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 7}


def replace_vowels(data):
    """
    Given a string, replace vowels in the string with numbers based on rules
    defined above, and return the new string
    """
    for output in rules:
        rules[output] = str(rules[output])  # change given output numbers into strings
    for vowels in data:
        if vowels in rules.keys():  # get the letters from the dictionary
            data = data.replace(vowels, rules[vowels])  # replace by the rule
    return data


# # # Uncomment the following lines to test
# s1 = "babson college"
# s2 = "how are you?"
# print(replace_vowels(s1))
# print(replace_vowels(s2))

# # Expected output:
# # b4bs0n c0ll3g3
# # h0w 4r3 y07?


"""
---------------------------------------------------------------------------------
Q3. covid-19-vaccine.json is a JSON file that contains vaccine information in MA.
 Please complete the function to read the city names into a list. Each city name 
 will be one item in the list. 
 
 Part of function is given. The JSON data is loaded into a variable, data, which is 
 a dictionary. Please do not change the existing code. 
---------------------------------------------------------------------------------
"""


def read_cities_to_list():
    """
    Return: a list of city names
    """
    import json
    import pprint

    # Make sure covid-19-vaccine.json is under "data" folder
    with open("data/covid-19-vaccine.json") as f:
        data = json.load(f)  # load json file into a dictionary named data
        pprint.pprint(data)
    # You can write code below
    cities = []  # new list
    MA_set = data["responsePayloadData"]["data"]["MA"]  # narrow down to only MA
    for i in MA_set:
        cities.append(i["city"])  # add city name into list
    return cities


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(read_cities_to_list())


## Expected output:
# ['ABINGTON', 'AGAWAM', 'ALLSTON', 'AMHERST', 'ARLINGTON', 'ASHLAND', 'ATTLEBORO', 'BEDFORD', 'BELCHERTOWN', 'BELMONT', 'BILLERICA', 'BOSTON', 'BOURNE', 'BRAINTREE', 'BRIGHTON', 'BROCKTON', 'BROOKLINE', 'BURLINGTON', 'CAMBRIDGE', 'CHATHAM', 'CHELSEA', 'CHESTNUT HILL', 'CHICOPEE', 'COHASSET', 'CONCORD', 'DANVERS', 'DEDHAM', 'DORCHESTER', 'EAST BOSTON', 'EAST BRIDGEWATER', 'EAST FALMOUTH', 'EAST HARWICH', 'EVERETT', 'FALL RIVER', 'FOXBOROUGH', 'FRAMINGHAM', 'GEORGETOWN', 'GLOUCESTER', 'GRANBY', 'GREAT BARRINGTON', 'GREENFIELD', 'HADLEY', 'HANOVER', 'HANSON', 'HARWICHPORT', 'HAVERHILL', 'HINGHAM', 'HOLBROOK', 'HOLLISTON', 'HOLYOKE', 'HOPKINTON', 'HUDSON', 'HYANNIS', 'HYDE PARK', 'IPSWICH', 'KINGSTON', 'LANESBOROUGH', 'LAWRENCE', 'LEOMINSTER', 'LEXINGTON', 'LONGMEADOW', 'LOWELL', 'LYNN', 'MALDEN', 'MARBLEHEAD', 'MARLBOROUGH', 'MASHPEE', 'MAYNARD', 'MEDFIELD', 'MEDFORD', 'METHUEN', 'MIDDLEBOROUGH', 'MIDDLETON', 'MILFORD', 'MILLBURY', 'MILLIS', 'NEEDHAM', 'NEW BEDFORD', 'NEWTON', 'NORTH ANDOVER', 'NORTH ATTLEBOROUGH', 'NORTH DARTMOUTH', 'NORTH EASTON', 'NORTH GRAFTON', 'NORTHAMPTON', 'NORWELL', 'ORLEANS', 'OXFORD', 'PALMER', 'PEABODY', 'PLAINVILLE', 'PROVINCETOWN', 'QUINCY', 'RANDOLPH', 'READING', 'REVERE', 'ROSLINDALE', 'ROWLEY', 'SALEM', 'SALISBURY', 'SANDWICH', 'SAUGUS', 'SEEKONK', 'SHARON', 'SOMERVILLE', 'SOUTH EASTON', 'SOUTH HAMILTON', 'SOUTH WEYMOUTH', 'SOUTH YARMOUTH', 'SOUTHWICK', 'SPRINGFIELD', 'STONEHAM', 'STOUGHTON', 'STURBRIDGE', 'SWANSEA', 'TAUNTON', 'WALTHAM', 'WAREHAM', 'WATERTOWN', 'WAYLAND', 'WELLESLEY', 'WEST BRIDGEWATER', 'WEST NEWTON', 'WEST SPRINGFIELD', 'WESTBOROUGH', 'WESTFORD', 'WESTWOOD', 'WEYMOUTH', 'WILBRAHAM', 'WILMINGTON', 'WINCHENDON', 'WINCHESTER', 'WINTHROP', 'WOBURN', 'WORCESTER', 'WRENTHAM']


"""
--------------------------------------------------------------------------
Q4. Please complete the function that takes a list of city names, returns
a dictionary - in this dictionary, key is a letter and value is a list of 
city names that start with that letter. You can find example from the expected 
output below
--------------------------------------------------------------------------
"""


def first_letters(cities):
    """
    cities: a list of city names
    Return: a dictionary of letter: city pairs
    """
    dic = {}  # new dictionary
    for city in city_names:
        if city[0] not in dic.keys():
            dic[city[0]] = []  # add alphabet to beginning of the list
            dic[city[0]].append(city)  # add city name for that alphabet
        else:
            if (
                city not in dic[city[0]]
            ):  # if the first alphabet already in the dictionary
                dic[city[0]].append(city)  # add the city name ot the list
    return dic


# When you've completed your function, uncomment the
# following lines and run this file to test!

# city_names = read_cities_to_list()
# print(first_letters(city_names))

## Expected output:
# {'A': ['ABINGTON', 'AGAWAM', 'ALLSTON', 'AMHERST', 'ARLINGTON', 'ASHLAND', 'ATTLEBORO'], 'B': ['BEDFORD', 'BELCHERTOWN', 'BELMONT', 'BILLERICA', 'BOSTON', 'BOURNE', 'BRAINTREE', 'BRIGHTON', 'BROCKTON', 'BROOKLINE', 'BURLINGTON'], 'C': ['CAMBRIDGE', 'CHATHAM', 'CHELSEA', 'CHESTNUT HILL', 'CHICOPEE', 'COHASSET', 'CONCORD'], 'D': ['DANVERS', 'DEDHAM', 'DORCHESTER'], 'E': ['EAST BOSTON', 'EAST BRIDGEWATER', 'EAST FALMOUTH', 'EAST HARWICH', 'EVERETT'], 'F': ['FALL RIVER', 'FOXBOROUGH', 'FRAMINGHAM'], 'G': ['GEORGETOWN', 'GLOUCESTER', 'GRANBY', 'GREAT BARRINGTON', 'GREENFIELD'], 'H': ['HADLEY', 'HANOVER', 'HANSON', 'HARWICHPORT', 'HAVERHILL', 'HINGHAM', 'HOLBROOK', 'HOLLISTON', 'HOLYOKE', 'HOPKINTON', 'HUDSON', 'HYANNIS', 'HYDE PARK'], 'I': ['IPSWICH'], 'K': ['KINGSTON'], 'L': ['LANESBOROUGH', 'LAWRENCE', 'LEOMINSTER', 'LEXINGTON', 'LONGMEADOW', 'LOWELL', 'LYNN'], 'M': ['MALDEN', 'MARBLEHEAD', 'MARLBOROUGH', 'MASHPEE', 'MAYNARD', 'MEDFIELD', 'MEDFORD', 'METHUEN', 'MIDDLEBOROUGH', 'MIDDLETON', 'MILFORD', 'MILLBURY', 'MILLIS'], 'N': ['NEEDHAM', 'NEW BEDFORD', 'NEWTON', 'NORTH ANDOVER', 'NORTH ATTLEBOROUGH', 'NORTH DARTMOUTH', 'NORTH EASTON', 'NORTH GRAFTON', 'NORTHAMPTON', 'NORWELL'], 'O': ['ORLEANS', 'OXFORD'], 'P': ['PALMER', 'PEABODY', 'PLAINVILLE', 'PROVINCETOWN'], 'Q': ['QUINCY'], 'R': ['RANDOLPH', 'READING', 'REVERE', 'ROSLINDALE', 'ROWLEY'], 'S': ['SALEM', 'SALISBURY', 'SANDWICH', 'SAUGUS', 'SEEKONK', 'SHARON', 'SOMERVILLE', 'SOUTH EASTON', 'SOUTH HAMILTON', 'SOUTH WEYMOUTH', 'SOUTH YARMOUTH', 'SOUTHWICK', 'SPRINGFIELD', 'STONEHAM', 'STOUGHTON', 'STURBRIDGE', 'SWANSEA'], 'T': ['TAUNTON'], 'W': ['WALTHAM', 'WAREHAM', 'WATERTOWN', 'WAYLAND', 'WELLESLEY', 'WEST BRIDGEWATER', 'WEST NEWTON', 'WEST SPRINGFIELD', 'WESTBOROUGH', 'WESTFORD', 'WESTWOOD', 'WEYMOUTH', 'WILBRAHAM', 'WILMINGTON', 'WINCHENDON', 'WINCHESTER', 'WINTHROP', 'WOBURN', 'WORCESTER', 'WRENTHAM']}


"""
--------------------------------------------------------------------------
Q5.(20 bonus points) Write a function that prints the dictionary from Q4. 
Your function should first print the longest list of cities with same first 
letter, followed by the second longest, and so on.
--------------------------------------------------------------------------
"""


def print_longer_list():
    """sort dictionary from Q4:
    from alphabet with the longest list of cities"""
    dic = {}  # new dictionary
    for city in city_names:
        if city[0] not in dic.keys():
            dic[city[0]] = []  # add alphabet to beginning of the list
            dic[city[0]].append(city)  # add city name for that alphabet
        else:
            if (
                city not in dic[city[0]]
            ):  # if the first alphabet already in the dictionary
                dic[city[0]].append(city)  # add the city name ot the list

    new_longest_list = sorted(dic, key=lambda s: len(dic.get(s)), reverse=True) # new way to sort the dictionary
    for i in range(len(new_longest_list)):
        print("{}: {}".format(new_longest_list[i], dic[new_longest_list[i]]))


city_names = read_cities_to_list()
first_letters(city_names)
print_longer_list()
