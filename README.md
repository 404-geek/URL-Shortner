# URL-Shortening API Service (Simple) 

## Prerequisites

- Install Redis server ([Redis Installation in Linux](https://redis.io/topics/quickstart))

## Setup

- Create a Virtual Environment `virtualenv -p python3 venv`
- Install the requirements `pip install -r requirements.txt`
- Run the app with `python shorten.py`

## Services
- [Shorten the URLs](http://127.0.0.1:5000/shorten) [POST]
    
    > `url` is to be provided in the form-data
                                                             
-  [Stats Info](http://127.0.0.1:5000/info/<url-id>) [POST] [GET]
    
    >`url id` is to be appended in the url

## Features that can be included

- Web Platform for these APIs.
- URL privacy can be implemented by saving user data and specific origins.
- More stats can be populated for tracking.
- Open API specs to generate stubs.
