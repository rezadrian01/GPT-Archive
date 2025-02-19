
from flask import Flask, render_template, request
from db import create_table, insert_conversation, get_conversations, get_conversation_by_id
import json
from scrape import scrape

app = Flask(__name__)

@app.route('/')
def index():
    conversations = get_conversations()
    for conversation in conversations:
        conversation['text'] = json.loads(conversation['text'])
    
    # print(json.loads(conversations[0]['text']))
    
    return render_template('index.html', conversations=conversations, home = True)

@app.route('/conversations/<int:conversation_id>', methods = ['GET'])
def get_conversation(conversation_id):
    conversations = get_conversations()
    for conversation in conversations:
        conversation['text'] = json.loads(conversation['text'])
    conversation = next((conversation for conversation in conversations if conversation['conversation_id'] == conversation_id))

    if not conversation:
        return "Conversation not found"
    
    return render_template('index.html', conversations = conversations, conversation=conversation, home = False)
    

@app.route('/insert', methods = ["POST"])
def insert_conversation_route():
    req_data = request.get_json()
    title = req_data['title']
    link = req_data['link']
    user_chat, assitant_chat =  scrape(link, headless=True)
    text = []
    lowercased_text = []

    if not title or not link:
        return "Error: Title or link is empty"

    if len(user_chat) != len(assitant_chat):
        return "Error: User and assistant chat length mismatch"
    
    for i in range(len(user_chat)):
        text.append({"user": user_chat[i], "assistant": assitant_chat[i]})
        lowercased_text.append({"user": user_chat[i].lower(), "assistant": assitant_chat[i].lower()})
    
    insert_conversation(title, link, text, lowercased_text)
    return "Conversation inserted"

if __name__ == '__main__':
    create_table()
    app.run(debug = True)