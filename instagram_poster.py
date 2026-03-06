from instagrapi import Client

cl = Client()

cl.login("your.tensura1","a1m2@rit")

def post(image, caption):

    cl.photo_upload(image, caption)