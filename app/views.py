from flask import Flask


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


from flask import render_template

@app.route('/')
def home():
    return render_template('landing_page.html')
 #    return """
 #    <!doctype html>
	# <h1>hello world!<h1>
	# """


if __name__ == "__main__":
    app.run(debug=True)
