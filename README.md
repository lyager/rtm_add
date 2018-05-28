## Intro

Simple program to add task to [Remember The Milk](https://rmilk.com). I used it
from [Alfred](https://www.alfredapp.com/), but you can call it from console too.

## Using

Call `rtm_add.py` like:

    ./rtm_add.py <Task> [auth token]

if no `auth token` is specified a browser window will open up and ask you to
authenticate. Subsequent `rtm_add.py` should be called with the token returned
and printed to the console.