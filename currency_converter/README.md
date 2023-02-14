# README.md

**REQUEST DATA**

Use the following URL pattern:

http://localhost:8000/convert/<from_currency>/<to_currency>//

For example, to convert 100 US dollars to euros, the URL would be: 

http://localhost:8000/convert/USD/EUR/100/ 

This would return the result in an HTML template that displays the converted amount in euros.

**RECEIVE DATA** 

Make a GET request to the URL, then parse the response. 

For example, if we are using Python:

```jsx
import requests

url = "http://localhost:8000/convert/USD/EUR/100/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Do something with the data
else:
    # Handle error
```

**UML Sequence Diagram**

![Untitled](README%20md/Untitled.png)
![image](https://user-images.githubusercontent.com/76701215/218653716-42df7cb9-2f61-4ebe-8723-369784f0663b.png)

