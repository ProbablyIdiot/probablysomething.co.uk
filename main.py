from flask import *

app = Flask(__name__)

#app.add_url_rule("/images/cloudsBg.webp", endpoint="/")
recentBlogs = [["img", "Test Title", "The quick brown fox jumps over the lazy dog, the quick brown fox jumps over the lazy dog, the quick brown fox jumps over the lazy dog."],["","",""],["","",""],["","",""],["","",""]]

@app.route("/")
def home():
	return render_template("home.htm", recentBlogs = recentBlogs)
