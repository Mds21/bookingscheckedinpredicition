# import subprocess
# import sys
# subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirement.txt"])
# from distutils.log import debug
from flask import Flask,render_template,redirect, url_for, request
from keras.models import load_model

app = Flask(__name__)


model = load_model('./model.h5')
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        nationality=request.form.get("nationality")
        age=request.form.get("age")
        daysincecreation=request.form.get("daysincecreation")
        averageleadtime=request.form.get("averageleadtime")
        lodgingrevenue=request.form.get("lodgingrevenue")
        otherrevenue=request.form.get("otherrevenue")
        bookingcanceled=request.form.get("bookingcanceled")
        bookingnoshowed=request.form.get("bookingnoshowed")
        personsnights=request.form.get("personsnights")
        roomnights=request.form.get("roomnights")
        dayssincelaststay=request.form.get("dayssincelaststay")
        dayssincefirststay=request.form.get("dayssincefirststay")
        distributionchannel=request.form.get("distributionchannel")
        marketsegment=request.form.get("marketsegment")
        srhighfloor=request.form.get("srhighfloor")
        srlowfloor=request.form.get("srlowfloor")
        sraccessibleroom=request.form.get("sraccessibleroom")
        srmediumfloor=request.form.get("srmediumfloor")
        srbathtub=request.form.get("srbathtub")
        srshower=request.form.get("srshower")
        srcrib=request.form.get("srcrib")
        srkingsizebed=request.form.get("srkingsizebed")
        srtwinbed=request.form.get("srtwinbed")
        srwearelevator=request.form.get("srwearelevator")
        srawayfromelevator=request.form.get("srawayfromelevator")
        srnoalcoholinminibar=request.form.get("srnoalcoholinminibar")
        srquietroom=request.form.get("srquietroom")

        prediction=int(model.predict([[float(nationality),float(age),float(daysincecreation),float(averageleadtime),float(lodgingrevenue),
        float(otherrevenue),float(bookingcanceled),float(bookingnoshowed),float(personsnights),float(roomnights),float(dayssincelaststay),
        float(dayssincefirststay),float(distributionchannel),float(marketsegment),float(srhighfloor),float(srlowfloor),
        float(sraccessibleroom),float(srmediumfloor),float(srbathtub),float(srshower),float(srcrib),float(srkingsizebed),
        float(srtwinbed),float(srwearelevator),float(srawayfromelevator),float(srnoalcoholinminibar),float(srquietroom)]])[0][0])

        if prediction:
            print("Prediction : ",prediction)
            return render_template("predict.html",output=prediction)
        else:
            return "some Exception occured during prediction"





    return render_template('index.html') 
   

if __name__ == "__main__":
    app.run(debug=True)
