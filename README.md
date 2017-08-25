# dynamic-ui-boilerplate
Shows how to use flask, redis, and html5 events to update a dynamic UI in a few lines of code.


## Install Redis

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04

Ensure it's running.

## Install dependencies

pip install -r requirements.txt

## Run the server

python server.py

## Open the UI

http://127.0.0.1:31337/

## Send events and update div elements on the UI

http://127.0.0.1:31337/send?id=one&html=test1

http://127.0.0.1:31337/send?id=two&html=test2
