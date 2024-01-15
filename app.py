# import requests
from gradio_client import Client
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        # input_text = """
        #                 Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde in reiciendis, inventore dolores dicta
        #                 repellendus cumque quas doloremque ea corporis qui ab, maiores perspiciatis quod facilis, cum
        #                 deleniti debitis iusto.
        #             """
        # input_text = "Hello World!!"
        input_text = request.form['input_text']

        
        outputs = categorize_keywords(input_text=input_text)
        
        # print(outputs)
        
        # output_text = "HELLO WORLD THIS IS THE WORLD"
        
        output_text = outputs

        # print(f"This is the output: {type(output_text)}")
        
        return render_template("classifier.html", input_text = input_text, output_text = output_text)
    else:
        return render_template("index.html")
    # print(output)
        
def categorize_keywords(input_text):
    # response = requests.post("https://nelbarman053-multilabel-book-genre-classifier-2.hf.space/run/predict", json={
    #     "data": [
    #         input_text
    #     ]
    # }).json()

    # response_data = response['data'][0]['confidences']
    # keywords = [data['label'] for data in response_data if data['confidence'] >= 0.5]

    # return keywords
    client = Client("https://nelbarman053-scientific-paper-keyword-categorization.hf.space/--replicas/2zaem/")

    response = client.predict(
		input_text,	# str  in 'abstract' Textbox component
		api_name="/predict"
    )

    # print(response)

    response_data = response['confidences']

    # print(response_data)
    
    keywords = [data['label'] for data in response_data if data['confidence'] >= 0.5]

    # print(f"This is the keywords: {keywords}")

    return keywords

if __name__ == "__main__":
    app.run(debug=True)