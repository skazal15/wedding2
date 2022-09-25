from flask import Flask,render_template,request
from flask_caching import Cache
import os
from odm.data import WishPost,WishGet

root_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(root_dir,'templates')
static_dir = os.path.join(root_dir,'static')
#config = {'CACHE_TYPE':'SimpleCache'}
male=["Muhammad Sai'd Fadhiil,S.T.","Bapak Andi Setiawan, S.E. & Ibu Aini Almadany, S.E.","Muhammad Sai'd Fadhiil","0700009709259"]
female = ["Dyah Puspita Sari,S.P.,M.P","Bapak Sugiyono, S.Pd., M.Pd & Ibu Dewi Variyanti, S.Pd","Dyah Puspita Sari","025601081686503"]
other = ["Said & Dyah","16 Oktober 2022","Minggu","08:00 WIB","10:00","Selesai","Gedung Institut Agama Islam Muhammad Azim (IAIMA)",
"1665854396","pernikahan kami","pernikahan putra putri kami","Kami yang berbahagia","Hormat Kami yang Menanti","male.png","malenew.png",
"female.png","femalenew.png"]

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)
#app.config.from_mapping(config)
#cache = Cache(app)

@app.route('/our',methods=['POST','GET'])
#@cache.cached(timeout=1)
def our():
    receive = request.args.get('kepada')
    records = WishGet().getData()
    return render_template('index444b.html',datadate=other[7],receive=receive,male=male[0],
    female=female[0],couple=other[0],date=other[1],pfemale=female[1],pmale=male[1],day=other[2],
    atime=other[3],start=other[4],end=other[5],nameplace=other[6],rekening1=male[2],
    norekening1=male[3],rekening=female[2],norekening=female[3],acara=other[8],redax=other[10],fotomale=other[12],fotofemale=other[14], view='kami', records=records)

@app.route('/ortu',methods=['POST','GET'])
#@cache.cached(timeout=1)
def home():
    receive = request.args.get('kepada')
    records = WishGet().getData()
    return render_template('index444b.html',datadate=other[7],receive=receive,male=male[0],
    female=female[0],couple=other[0],date=other[1],pfemale=female[1],pmale=male[1],day=other[2],
    atime=other[3],start=other[4],end=other[5],nameplace=other[6],rekening1=male[2],norekening1=male[3],
    rekening=female[2],norekening=female[3],acara=other[9],redax=other[11],fotomale=other[13],fotofemale=other[15], view='ortu',records=records)

@app.route('/post',methods=['POST','GET'])
def post():
    nama = request.form.get('nama')
    doa = request.form.get('doa')
    hadir = request.form.get('hadir')
    WishPost(nama,doa,hadir)