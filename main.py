from flask import *

app = Flask(__name__)

#app.add_url_rule("/images/cloudsBg.webp", endpoint="/")

@app.route("/")
def home():
	return render_template("home.htm")
