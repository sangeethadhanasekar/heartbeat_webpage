from flask import Flask,render_template,request
from heartbeat import  heart_beat
from werkzeug.utils import secure_filename
app=Flask(
          __name__,
          template_folder='client/template',
          static_folder='client/static',

)



@app.route('/', methods = ['GET', 'POST'])
def upload_file():
     if request.method=='GET':
        bpm="upload video in step1"
        return render_template("page1.html",bpm=bpm)

     else:
      f = request.files['video']
      f.save(secure_filename(f.filename))
      video=f.filename
      bpms=heart_beat(video)
      bpm=bpms+" BPM"

      return render_template("page1.html", bpm=bpm)

#@app.route("/user/<name>")
#def webpage(name):
#

if __name__=="__main__":
    app.run(debug=True)