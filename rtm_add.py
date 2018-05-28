#!/usr/bin/env python3
import webbrowser
import sys
from rtmapi import Rtm

def main():
    api_key = "910f700cc0ff23ed2462312c250bc560"
    shared_secret = "b7be4d2a824b42b1"

    token = sys.argv[2] if len(sys.argv) == 3 else None
    task_name = sys.argv[1]

    api = Rtm(api_key, shared_secret, "delete", token)

    if not api.token_valid():
        url, frob = api.authenticate_desktop()

        webbrowser.open(url)
        input("Continue?")

        # Get the token for the frob
        assert(api.retrieve_token(frob))

        print("New token: {}".format(api.token))

    result = api.rtm.timelines.create()
    timeline = result.timeline.value

    # Add task - default is Inbox
    result = api.rtm.tasks.add(timeline = timeline, parse = "1", name = task_name)

    task_id = result.list.taskseries.id
    print("Create task, id: {}".format(task_id))

if __name__ == '__main__':
    # Call with <taskname> [token]
    #
    # If token not provided, webprowser will open in order to acquire one
    # Tasks a always added to 'Inbox' in true GTD style.
    main()