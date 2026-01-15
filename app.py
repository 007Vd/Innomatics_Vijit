from flask import Flask,render_template,request,jsonify
import re

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/match",methods=['POST'])
def match_regex():
    data=request.json
    test_string=data.get('test_string',"")
    pattern=data.get('pattern',"")

    try:
        regex=re.compile(pattern)
        matches=regex.findall(test_string)
        return jsonify({
            "matches":matches,
            "error":None
        })
    except re.error:
        return jsonify({
            "matches":[],
            "error":str(re.error)
        })
if __name__=="__main__":
    app.run(debug=True)

    
