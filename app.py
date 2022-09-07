from flask import Flask,render_template,request
from flask_caching import Cache
import os

root_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(root_dir,'templates')
static_dir = os.path.join(root_dir,'static')
config = {'CACHE_TYPE':'SimpleCache'}
male="Muhammad Sai'd Fadhiil,S.T."
female = "Dyah Puspita Sari,S.P.,M.P"
couple = "Said & Dyah"
date = "16 Oktober 2022"
pfemale = "Putri pertama dari Bapak Sugiyono, S.Pd., M.Pd & Ibu Dewi Variyanti, S.Pd"
pmale = "Putra pertama dari Bapak Andi Setiawan, S.E. & Ibu Aini Almadany, S.E."
day = "Minggu"
atime = "Pukul 08:00 WIB"
start = "10:00"
end = "Selesai"
nameplace = "Gedung Institut Agama Islam Muhammad Azim (IAIMA)"
address =  "Jl. Fatah Laside No. 68 Kel. Kebun Handil, Kec. Jelutung, Kota Jambi"
rekening1 = "Muhammad Sai'd Fadhiil"
datadate = "1665854396"
norekening1 = "0700009709259"
rekening = "Dyah Puspita Sari"
norekening = "025601081686503"
app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/',methods=['POST','GET'])
@cache.cached(timeout=50)
def home():
    receive = request.args.get('kepada')
    return render_template('index444b.html',datadate=datadate,receive=receive,male=male,female=female,couple=couple,date=date,pfemale=pfemale,pmale=pmale,day=day,atime=atime,start=start,end=end,nameplace=nameplace,address=address,rekening1=rekening1,norekening1=norekening1,rekening=rekening,norekening=norekening)
