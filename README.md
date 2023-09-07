# catalyst-count

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


