from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/home/<int:age>")
def homepage(age):
    if age>=20:
        return render_template("home.html",title="home")
    else:
        return "<h1>hello all welocme to the page</h1>"


if __name__=="__main__":
    app.run(debug=True)