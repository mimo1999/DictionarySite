import json 
from difflib import get_close_matches
from flask import Flask, render_template  
 
app = Flask(__name__, template_folder='templates') 

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search/<t>")
def searcher(t):
    return render_template("searchpage.html", value=t)

@app.route('/find/<w>')
def translate(w):
    # converts to lower case 
    w = w.lower() 
  
    if w in data: 
        return data[w] 
    # for getting close matches of word 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) 
        yn = yn.lower() 
        if yn == "y": 
            return data[get_close_matches(w, data.keys())[0]] 
        elif yn == "n": 
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your entry."
    else: 
        return "The word doesn't exist. Please double check it."
	

if __name__ == '__main__':
	data = json.load(open("dictionary.json")) 
	app.run(debug="False", port=6080, host='127.0.0.1')