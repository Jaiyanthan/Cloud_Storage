from os import access
import dropbox

class TransferData:
    def __init__(self, access_token): 
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox (self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        print("Uploaded")
def main():
    access_token = "sl.BDUfpei8CIhE3w1uuS7RDWg6UONgoVQ_7k8x-cDcp7UyIS7JesJq3RiMp4VOeHgXultCTqqdeluf3qHEwoA6iYV2mjFT77EAUhyBSmz_8l5I4ZdHyiKqB2ktyU0uPSJC6Vwo8Tg"
    transfer = TransferData(access_token)

    file_from = input("Enter the exact path of the file to be uploaded")
    file_to = input("Enter the dropbox path")
    
    transfer.upload_file(file_from, file_to) 

main()    

  