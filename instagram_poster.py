from instagrapi import Client

cl = Client()

cl.login("USERNAME","PASSWORD")

def post(image, caption):

    cl.photo_upload(image, caption)