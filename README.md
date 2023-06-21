# Message Dashboard Django
The Message Dashboard project is a web application built using the Django framework that combines messaging functionality with a comprehensive dashboard interface.
It serves as a centralized platform for managing and interacting with messages.

# What this project does?
* The frontend of the application provides a user-friendly messaging interface. Users can compose and send messages.
![1](https://github.com/Krish123-lang/Message_Dashboard_Django/assets/56486342/15427a9d-d75a-46e4-aac5-d66482f47bf7)

* Send message using Message icon.
![2](https://github.com/Krish123-lang/Message_Dashboard_Django/assets/56486342/0fb3aa0c-5813-4b31-b15f-9798e8728fde)

* Login Form
![3](https://github.com/Krish123-lang/Message_Dashboard_Django/assets/56486342/bf49e44e-59e7-48c5-b2c9-dc2f06956b11)

* The messages are categorized as read or pending, allowing users to easily identify new messages.
* The dashboard also includes a table that lists all message senders.
* Each row in the table provides options to delete and mark as read the messages.
* This table is paginated to accommodate a large number of senders and ensure efficient navigation.
![4](https://github.com/Krish123-lang/Message_Dashboard_Django/assets/56486342/a65021af-6d73-43db-ab73-c4df8eb4b833)

  
* The dashboard prominently displays key metrics, such as the total number of messages and the number of messages sent today, giving users an overview of their messaging activity.
* To enhance usability, a global search bar is implemented, enabling users to search for specific messages based on different criteria such as sender name, keywords, or message content. This search functionality allows users to quickly find relevant messages within their inbox.
![5](https://github.com/Krish123-lang/Message_Dashboard_Django/assets/56486342/23c313d1-de4e-4b80-82c5-64bfdb89f35c)

* Additionally, the project includes an admin dashboard that provides administrative functionalities. The admin dashboard is accessible to authorized personnel and allows them to manage system settings, user permissions, and perform administrative tasks specific to the messaging functionality.
* Finally, the project incorporates a logout functionality, ensuring that users can securely terminate their sessions and protect their data.

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
