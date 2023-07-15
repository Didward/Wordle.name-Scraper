# main.py
import requests
from data import my_list

# Function to check the endpoint of a URL
def check_url_endpoint(url):
    response = requests.get(url)
    # Process the response and extract the desired value
    # For example, if the response is JSON, you can use response.json()
    value = response.json()['value']
    return value

# Get the URL based on the index and check its endpoint
def check_endpoint_by_index(index):
    url = f"https://www.wordle.name/en/{index}"
    value = check_url_endpoint(url)
    return value

# Example usage
index = 0
result = check_endpoint_by_index(index)
print(my_list[result])
