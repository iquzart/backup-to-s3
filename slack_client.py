#!/usr/bin/python
import os
import slack

slack_token = os.environ["SLACK_API_TOKEN"]
client = slack.WebClient(token=slack_token)

client.chat_postEphemeral(
  channel="App-x",
  text="The backup has been failed",
  user="UN231"
)
