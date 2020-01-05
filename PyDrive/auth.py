import os
import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
