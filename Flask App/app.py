
from flask import Flask , render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('carco2new.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/login', methods = ["POST"])
def login():
    BRAND=request.form["BRAND"]
    CM=request.form["CM"]
    MY=request.form["MY"]
    VC=request.form["VC"]
    FT=request.form["FT"]
    if(FT =="Z"):
        s1,s2,s3,s4 = 0,0,0,1
    if(FT =="D"):
        s1,s2,s3,s4 = 0,0,1,0
    if(FT =="E"):
        s1,s2,s3,s4 = 0,1,0,0
    if(FT =="X"):
        s1,s2,s3,s4 = 1,0,0,0
    ES=request.form["ES"]
    C=request.form["C"]
    T=request.form["T"]
    FCC=request.form["FCC"]
    FCHWY=request.form["FCHWY"]
    FCCC=request.form["FCCC"]
    FCCMPG=request.form["FCCMPG"]
    
    total = [[s1,s2,s3,s4,float(ES),int(C),int(T),float(FCC),float(FCHWY),float(FCCC),int(FCCMPG)]]
    
    p = model.predict(total)
    
    if(p>256.2286785379569):
        return render_template('details.html',label1 = "CO2 EMISSION OF THE VEHICLE = "+str(p), label2 ="THRESHOLD VALUE : 256.2286785379569", label3 ="Car Company : "+str(BRAND), label4 ="Car Model : "+str(CM), label5 ="Model Year : "+str(MY), label6 ="Vechile Class Type : "+str(VC), label7 =" Your Vehicle is Siezed Because CO2 Emission From Your Vehicle is Greater Than the THRESHOLD VALUE",label8=1)
    else:
        return render_template('details.html',label1 = "CO2 EMISSION OF THE VEHICLE = "+str(p), label2 ="THRESHOLD VALUE : 256.2286785379569", label3 ="You Are Safe!!! ",label8=0)
  
       

if __name__=='__main__':
    app.run(debug=True,port=9000)