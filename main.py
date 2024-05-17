import datetime
import io 

import pytesseract
from PIL import Image
from flask import Flask, request, render_template, url_for , redirect, session

#Instanciating app
#-----------------

app = Flask(__name__)


app.secret_key= b'_4#y1L"F4Q8z\n\xec]/'

#Routes
#-----------------

@app.route('/')
def root(): 
    return render_template("index.html",title="OCR App")


@app.route('/scanner',methods=['GET','POST'])
def scan(): 
    if request.method == 'POST':

        time_track = datetime.datetime.now()
        image_data = request.files['file'].read()

        scanned_image = pytesseract.image_to_string(Image.open(io.BytesIO(image_data)))

        print(scanned_image)
        session['data'] = {
            "text" : scanned_image,
            "time" : str((datetime.datetime.now() - time_track).total_seconds())
        }

        return redirect(url_for('output'))


@app.route('/output')
def output():
    if "data" in session: 

        data = session ['data']
        return render_template(

            "output.html",
            title="Output",
            time=data["time"],
            text =data["text"],
            words = len(data["text"].split(" "))

        )
    else:
        return "Bad methode call."



# Start main.py
#-----------------
if __name__ == '__main__': 

    app.run('0.0.0.0',port=5000)