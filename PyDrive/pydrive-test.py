import os
import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

print(type(drive))

# 特定フォルダ下へのUpload
## フォルダの作成
# f_folder = drive.CreateFile({'title': 'sample_folder',
#                              'mimeType': 'application/vnd.google-apps.folder'})
# f_folder.Upload()
# pprint.pprint(f_folder)
# f_folder_id = f_folder.get('id')
# print(f_folder_id)

## フォルダIDの取得
folder_id = drive.ListFile({'q': 'title="sample_folder"'}).GetList()[0].get('id')
print(folder_id)
query = "'{}' in parents and mimeType='application/vnd.google-apps.folder'".format(folder_id)
child_folder_id = drive.ListFile({'q': query}).GetList()
pprint.pprint(child_folder_id)

## ファイルのUpload
# f = drive.CreateFile({'parents': [{'id': folder_id}]})
# f.SetContentFile('sample.txt')
# f.Upload()
# pprint.pprint(f)