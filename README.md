# Flask API
## An API that returns "Next to jump" races





This repository was developed in order to create an API that returns data from horse races. The app was developed in Python with the Flask framework. 


### Dataset - race_dataset.csv
The dataset was generated synthetically using python (not in this repository) just for demonstration purposes.  
The columns are the following:

`raceType`: Type of race - information sampled from a list from wikipedia \
`raceNumber`:numbers sampled randomly from 1:25 \
`raceName`: Names generated artificially on a website \
`venue`: List from wikipedia \
`raceStartTime`: Numbers randomly sampled between 12:00 and 24:00 


### Application - app.py
This is file is key to the API. Using pandas, It reads the race_dataset.csv file and returns requested data. 

The methods list (methods=['GET']) is central to the file. It allows HTTP requests that send data from the application to the user. In following line of code the `\` means the path used to make the request. 
`@app.route('/', methods=['GET'])`


### Set Up 
To interact with the application:
1. Clone the repo
2. install flask `pip install flask`
3. Move to the directory code-challenge and run `python app.py`


### Request Data
Once the application is the running, just go to python localhost and make a request. Examples:

`http://127.0.0.1:5000/?dayTime=12.00`
`http://127.0.0.1:5000/?dayTime=16.35`
`http://127.0.0.1:5000/?dayTime=21.12`

All of these requests should return data in a JSON format. This is what a typical return would be like:

```
{"raceName":{"0":"Immortal Fiends","1":"Immortal Fiends","2":"Forest Angels","3":"Shore Undine","4":"Immortal Fiends"},"raceNumber":{"0":9,"1":7,"2":2,"3":22,"4":18},"raceStartTime":{"0":12.1,"1":12.11,"2":12.11,"3":12.12,"4":12.14},"raceType":{"0":"Saddle Trotting","1":"Saddle Trotting","2":"Jump racing","3":"Saddle Trotting","4":"Harness racing"},"venue":{"0":"Ladbrokes Park,\u00a0Melbourne,\u00a0Victoria\u00a0(formerly Sandown Racecourse)","1":"Doomben Racecourse,\u00a0Brisbane, Queensland","2":"Wangaratta Racecourse,\u00a0Wangaratta, Victoria","3":"Warrnambool Racecourse,\u00a0Warrnambool, Victoria","4":"Wyong Race Club,\u00a0Wyong, New South Wales"}}
```

### Reference
Flask API: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
