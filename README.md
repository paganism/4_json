# Форматирование

Скрипт возвращает получаемые из файла данные в читабельном виде PrettyPrint в формате json.

# Как запустить

Запуск на Linux:

    [user@server ]$ python3.5 pprint_json.py <path to file>
    <path to file> - путь к файлу с исходными данными

Запуск на Windows происходит аналогичным образом

# Пример вывода:

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


# Цель проекта

Код написан в образовательных целях
[DEVMAN.org](https://devman.org)
