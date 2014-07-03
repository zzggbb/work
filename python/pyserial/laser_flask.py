from flask import Flask
app = Flask(__name__)

@app.route("/laser")
def test():
	return str(555923934)

if __name__ == "__main__":
	app.run()
