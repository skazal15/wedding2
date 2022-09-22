import requests
from odm.wish import Wish

api_wish_post = 'http://localhost:8004/nikah/wedding.php'
api_wish_get = 'http://localhost:8004/nikah/wedding_getdata.php'

class WishPost():
    def __init__(self,nama,doa,hadir) -> None:
        body={
            "nama":nama,
            "doa":doa,
            "hadir":hadir
        }
        requests.post(api_wish_post,json=body)

class WishGet():
    def getData(self):
        Response=requests.get(api_wish_get)
        wish = Response.json()

        return wish
