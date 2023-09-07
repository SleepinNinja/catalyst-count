# catalyst-count

For running the project.

1. Create a virtual environment and activate it.
2. Install all the dependencies using pip install -r requirements.txt
3. Create a .env file inside the main project app i.e catalyst_count.
4. Inside .env file Provide django SECRET_KEY, and NAME, USER, PASSWORD, HOST and PORT for postgres.
5. Make migrations using commands:
  a. python manage.py makemigrations
  b. python manage.py migrate
7. Finally run the project using command python manage.py runserver.



API

The url for getting the filtered company data is http://127.0.0.1:8000/api/query_builder/,
This API only accepts GET request, we need to send filters in request body in json format as shown below.

![image](https://github.com/SleepinNinja/catalyst-count/assets/88624644/77bc3cd8-123c-41f1-8589-653efdd287d2)

The list of filters are:
1. country
2. industy
3. city
4. state
5. year_founded

The value for all these filters should be of type string.

For a successful API call we need to pass alteast one filter.
On a successfully request call number of matches, and serialized matching results are retuend with status code 200.
![image](https://github.com/SleepinNinja/catalyst-count/assets/88624644/b1846ae7-796e-4e55-901b-0176d261eeb7)

If we don't pass any filter then status code 400 is returned.
![image](https://github.com/SleepinNinja/catalyst-count/assets/88624644/6892a503-4791-47d0-9795-d9ab8735f82d)

