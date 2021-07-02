from flask import Flask,render_template,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app =Flask(__name__)
@app.route('/',methods=["POST","GET"])
def main():
    print("inp")
    if request.method == "POST":
        inp = request.form.get("inp")
        sid =SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        print(score)
        if score["neg"] !=0:
            return render_template('home.html',message="negative")
        else:
            return render_template('home.html',message="positive")    
    return render_template('home.html')