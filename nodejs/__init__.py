from flask import Flask, render_template 
import os 
DIR = os.path.dirname(__file__) or '.' 
DIR += '/' 
 
app = Flask(__name__) 
 
@app.route('/') 
def main(): 
	return render_template('index.html') 
 
if __name__ == '__main__': 
	app.debug = True 
	app.run()
