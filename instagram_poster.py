from instagrapi import Client

cl = Client()

cl.login("amrityadav82224@gmail.com","a1m2@rit")

def post(image, caption):

    cl.photo_upload(image, caption)