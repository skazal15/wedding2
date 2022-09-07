import requests
from models.wish import Wish

api_wish_post = 'http://localhost/nikah/wedding.php'
api_wish_get = 'http://localhost/nikah/wedding_getdata.php'

class WishPost():
    def __init__(self,nama,doa,hadir) -> None:
        body={
            "nama":nama,
            "doa":doa,
            "hadir":hadir
        }
        requests.post(api_wish_post,json=body)

class WishGet():
    def __init__(self) -> None:
        Response=requests.get(api_wish_get)
        wish = Response.json()
        Wish.nama = wish['nama']
        Wish.doa = Wish['doa']
        Wish.hadir = Wish['hadir']