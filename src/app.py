from flask import Flask, render_template

from db import create_table, insert_conversation, get_conversations

app = Flask(__name__)

@app.route('/')
def index():
    conversations = get_conversations()
    print(conversations)
    return render_template('index.html', text='Hello World')

if __name__ == '__main__':
    create_table()
    app.run(debug = True)