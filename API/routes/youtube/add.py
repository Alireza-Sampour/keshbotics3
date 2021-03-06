import falcon

from middleware.auth import auth
from classes.youtube.youtube_management import youtube_management

@falcon.before(auth())
class youtube_add(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):

        # Retrieve the Discord channel ID and the YouTube channel URL from the headers
        disc_channel_id  = req.get_header('discord-channel-id')
        yt_channel_url   = req.get_header('youtube-channel-url')

        # If either of the two required headers are missing, return bad request
        if(disc_channel_id == None or yt_channel_url == None):
            raise falcon.HTTPBadRequest('Missing Requried Headers', 'Required headers: discord_channel_id and youtube_channel_url')

        # Using the youtube_management class add the subscription to the database
        resp.body = youtube_management().subscribe(yt_channel_url, disc_channel_id)
