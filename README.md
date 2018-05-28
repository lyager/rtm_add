## Intro

Simple program to add task to [Remember The Milk](https://rmilk.com) (Rmilk). I use it
from [Alfred](https://www.alfredapp.com/), but you can call it from console too,
and probably should do the first time, to extract the authentication token from RMilk.

## Using

Call `rtm_add.py` like:

    ./rtm_add.py <Task> [auth token]

if no `auth token` is specified a browser window will open up and ask you to
authenticate. Subsequent `rtm_add.py` should be called with the token returned
and printed to the console.