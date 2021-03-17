from flask import Flask, render_template,request#,url_for
# import os
import roulette as rol

app = Flask(__name__)


@app.route("/")
def index():
    menues = rol.momokara_roulette("単品の1000円")
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,attribute="メニュー")

@app.route("/tp500",methods=["GET"])
def ac1():
    menues = rol.momokara_roulette("単品の500円")
    title = "500円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="単品")

@app.route("/tp750",methods=["GET"])
def ac2():
    menues = rol.momokara_roulette("単品の750円")
    title = "750円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="単品")

@app.route("/tp1000",methods=["GET"])
def ac3():
    menues = rol.momokara_roulette("単品の1000円")
    title = "1000円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="単品")

@app.route("/TB500",methods=["GET"])
def TB500():
    menues = rol.momokara_roulette("定食の500円")
    title = "500円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="定食・弁当")

@app.route("/TB750",methods=["GET"])
def TB750():
    menues = rol.momokara_roulette("定食の750円")
    title = "750円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="定食・弁当")

@app.route("/TB1000",methods=["GET"])
def TB1000():
    menues = rol.momokara_roulette("定食の1000円")
    title = "1000円"
    total = menues[-1]
    menues = menues[:-1]
    return render_template("index.html",menues=menues,total=total,title=title,attribute="定食・弁当")

if __name__ == "__main__":
    app.run(debug=True)