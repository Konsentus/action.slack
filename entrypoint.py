#!/usr/bin/env python

import requests
import json
import os
import sys


def main():
    token = getInput('INPUT_SLACK_TOKEN')
    data = json.loads(getInput('INPUT_DATA'))

    postMessage(data, token)


def getInput(var):
    try:
        return os.environ[var]
    except KeyError:
        print(f'"{var[6:].lower()}" has not been provided')
        sys.exit(2)


def postMessage(messageData, token):

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json;charset=utf-8',
    }
    data = {
        'channel': None,
        'text': None,
        'icon_emoji': ':slack:',
        'username': 'Slack',
        'attachments': None,
    }
    data.update(messageData)

    return requests.post(
        'https://slack.com/api/chat.postMessage',
        data=json.dumps(data),
        headers=headers
    )


main()
