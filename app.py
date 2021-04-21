import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accesstoken = 'gHY3yNiqSbwAAAAAAAAAATgGQ4zMOEaOb_2Psk88TrdFqgfriEunlboVJn5xmVmg'
    transferData = TransferData(accesstoken)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("Enter the dropox path")

    transferData.upload_file(file_from, file_to)


main()