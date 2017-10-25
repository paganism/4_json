# Prettify JSON

This script allows to make the JSON data readable and pretty looking.

# Quickstart

Linux:

    [user@server ]$ python3.5 pprint_json.py <path to file>
    <path to file> - path to file, which contain JSON data


# Output example

    {
      "orderID": 12345,
      "shopperName": "John Smith",
      "shopperEmail": "johnsmith@example.com",
      "contents": [
        {
          "productID": 34,
          "productName": "SuperWidget",
          "quantity": 1
        },
        {
          "productID": 56,
          "productName": "WonderWidget",
          "quantity": 3
        }
      ],
      "orderCompleted": true
    }

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
