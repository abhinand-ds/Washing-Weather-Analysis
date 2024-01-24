23-01-2024
Python Code Output:
```Bash
(venv) [abhi@archlinux Washing-Weather-Analysis]$ python extractor.py 
Loading took too much time!

Washer 1
Frontload Washer
Complete


Washer 2
Frontload Washer
Available


Washer 3
Frontload Washer
Available


Washer 4
Frontload Washer
Available


Dryer 5
Single Dryer
Available


Dryer 6
Single Dryer
In Use
54 min. left
Create Alert

Dryer 7
Single Dryer
In Use
14 min. left
Create Alert

Dryer 8
Single Dryer
In Use
57 min. left
Create Alert
```

- I was able to get the following output used Stackoverflow for the most of the part nearly 4-5 Errors solved.

---

24-01-2024
Python Output:
`extractor.py`
```bash
(venv) [abhi@archlinux Washing-Weather-Analysis]$ python extractor.py 
Loading took too much time!
[['Washer 1', 'Frontload Washer', 'Available'], ['Washer 2', 'Frontload Washer', 'Available'], ['Washer 3', 'Frontload Washer', 'Available'], ['Washer 4', 'Frontload Washer', 'Available'], ['Dryer 5', 'Single Dryer', 'Available'], ['Dryer 6', 'Single Dryer', 'Available'], ['Dryer 7', 'Single Dryer', 'Available'], ['Dryer 8', 'Single Dryer', 'Available']]
```
- Provides me output of data in the correct manner without empty list and empty values in the list.

`weather_data.py`
```bash
(venv) [abhi@archlinux Washing-Weather-Analysis]$ python weather_data.py 
['5.48 C', '3.66 C', '1022 hPa ', '2.28 m/s']
```
- This provides me few parameters like temprature, feels like, pressure and wind speed.

I believe recording of the following data will enable me to understand the pattern of the usage of washing machine and dryer and the temprature.
I hope I will prepare the project before 1st of February analysing the usage pattern of the students in case of using washing machine.