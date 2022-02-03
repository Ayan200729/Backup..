import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BA1SsoH3foTMR-HUCAjK88XzpjxowWqaREVQigQUkf8p-cRrriwVXsKwtlEtvbXOEXnXW23MAJQD9XYlP48iaHy34OKIv_zcbvj_HPWn0pUNiwHhuy3qxWUOtJKbUrqGV8KrxrEuKFA"
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer")
    file_to = input("Enter the full path to upload to Dropbox")
    transferData.upload_file(file_from, file_to)
    print("File has been moved!")

main()

