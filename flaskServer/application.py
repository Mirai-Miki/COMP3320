from flask import Flask, render_template, request, redirect, url_for
import yaml

app = Flask(__name__)

uploaded_file = {}
yamlObj = {}

@app.route("/")
def index():
	return render_template("index.html", upload=uploaded_file, yaml=yamlObj)

@app.route("/", methods=["POST"])
def upload_file():
	file = request.files['file']
	if (file.filename != ''):
		uploaded_file["file"] = file.read()
		uploaded_file["name"] = file.filename
		
	return redirect(url_for('index'))

@app.route("/load")
def load():
	if uploaded_file["file"]:
		yamlObj.clear()
		try:
			yamlObj["file"] = yaml.load(uploaded_file["file"])
		except yaml.YAMLError as e:
			yamlObj["error"] = e

	return redirect(url_for('index'))

@app.route("/full_load")
def full_load():
	if uploaded_file["file"]:
		yamlObj.clear()
		try:
			yamlObj["file"] = yaml.full_load(uploaded_file["file"])
		except yaml.YAMLError as e:
			yamlObj["error"] = e

	return redirect(url_for('index'))

@app.route("/safe_load")
def safe_load():
	if uploaded_file["file"]:
		yamlObj.clear()
		try:
			yamlObj["file"] = yaml.safe_load(uploaded_file["file"])
		except yaml.YAMLError as e:
			yamlObj["error"] = e

	return redirect(url_for('index'))

@app.route("/unsafe_load")
def unsafe_load():
	if uploaded_file["file"]:
		yamlObj.clear()
		try:
			yamlObj["file"] = yaml.unsafe_load(uploaded_file["file"])
		except yaml.YAMLError as e:
			yamlObj["error"] = e

	return redirect(url_for('index'))

@app.route("/unload")
def unload():
	uploaded_file.clear()
	yamlObj.clear()
	return redirect(url_for('index'))

@app.route("/clear")
def clear():
	yamlObj.clear()
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()