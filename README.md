# Message Dashboard Django
The Message Dashboard project is a web application built using the Django framework that combines messaging functionality with a comprehensive dashboard interface.
It serves as a centralized platform for managing and interacting with messages.

# What this project does?
* The frontend of the application provides a user-friendly messaging interface. Users can compose and send messages.
* The messages are categorized as read or pending, allowing users to easily identify new messages. 
* The dashboard prominently displays key metrics, such as the total number of messages and the number of messages sent today, giving users an overview of their messaging activity.
* To enhance usability, a global search bar is implemented, enabling users to search for specific messages based on different criteria such as sender name, keywords, or message content. This search functionality allows users to quickly find relevant messages within their inbox.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

1. First of all create a isolated environment in your folder using following commands

```bash
i) virtualenv env
ii) env\Scripts\activate

```

2. Then install tools using  

 ```python
 pip install -r requirements.txt
```
3. To get the API Key you need to create an account on [WeatherAPI](https://www.weatherapi.com/). 
4. Then, copy your API key and paste it in `.env` file replacing <Your_Weather_API_Key> with your API key.
5. Then use

```python
 python manage.py makemigration
 python manage.py migrate
 python manage.py runserver
 ```

6. Copy the url(127.0.0.1:8000) and open it into your browser.
7. You must see this screen
![weather_app_django (2)](https://github.com/Krish123-lang/Weather_App_GUI_Django/assets/56486342/6c48dd54-7732-400d-b314-efb5cd337b4f)


THANK YOU 🙏
