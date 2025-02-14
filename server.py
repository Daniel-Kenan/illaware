from flask import Flask, render_template, url_for,send_from_directory , request, session,redirect,flash

app = Flask(__name__,template_folder="templates")
app.secret_key = "7u11t@nk"


def render(url,title="null",user=None,inland={},coastal={}): 
    return render_template(url,title=title)

@app.route("/")
def home():
    return render("Home.html",title="Fulltanksa - Home")

if __name__ == "__main__":
    app.run( host='0.0.0.0', port=8765)