import pickle
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

def print_text(text):
    print("Your original text file is\n\n")
    return text

@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form.get('text')
        print_text(text)
        summarization = pickle.load(open('summarize_model.pkl','rb'))
        processed_text = summarization(text, min_length=100, max_length=500)
        return processed_text[0]['summary_text']
    return render_template('summarize.html', title='Summarized Text', text=text)