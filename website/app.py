import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = "Hello World"
        outputs = categorize_keywords(input_text=input_text)
        print(outputs)
        output_text = "HELLO WORLD THIS IS THE WORLD"
        return render_template("classifier.html", input_text = input_text, output_text = output_text)
    else:
        render_template("index.html")
    # print(output)
        
def categorize_keywords(input_text):
    response = requests.post("https://nelbarman053-multilabel-book-genre-classifier-2.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()

    response_data = response['data'][0]['confidences']
    keywords = [data['label'] for data in response_data if data['confidence'] >= 0.5]

    return keywords

if __name__ == "__main__":
    app.run(debug=True)

# def main():
#     input_text = "https://nelbarman053-multilabel-book-genre-classifier-2.hf.space/run/predict"

#     keywords = categorize_keywords(input_text=input_text)

#     print(keywords)

if __name__ == "__main__":
    main()