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

## Run in Production

- Install Docker Engine ([Docker Installation in Debian](https://docs.docker.com/engine/install/debian/))
- Build Docker image of the app `docker build -t urlservice .` in the project directory.
- Run the application `docker run -d -p 5000:5000 urlservice`                                                                           
                                                                          
## Features that can be included

- Web Platform for these APIs.
- URL privacy can be implemented by saving user data and specific origins.
- More stats can be populated for tracking.
- Open API specs to generate stubs.
