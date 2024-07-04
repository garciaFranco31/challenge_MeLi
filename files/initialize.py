from pydrive2.auth import GoogleAuth

def initialize():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()