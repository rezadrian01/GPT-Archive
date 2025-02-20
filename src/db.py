import mysql.connector
from json import dumps
from config import DB_CONFIG

def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table():
    """Create Conversations table if doesnt exist"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Conversations (
                conversation_id INT AUTO_INCREMENT PRIMARY KEY,
                link TEXT,
                title VARCHAR(255),
                text LONGTEXT,
                lowercased_text LONGTEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Conversations table succesfully created.")

def insert_conversation(title, link, text, lowercased_text):
    """Add conversation to database"""
    text = dumps(text)
    lowercased_text = dumps(lowercased_text)
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Conversations (title, link, text, lowercased_text) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, link, text, lowercased_text))
        conn.commit()
        cursor.close()
        conn.close()
        print("Conversation succesfully inserted.")

def get_conversations():
    """Get all conversations from database"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Conversations")
        conversations = cursor.fetchall()
        cursor.close()
        conn.close()
        return conversations

def get_conversation_by_id(conversation_id):
    """Get a single conversation by ID from the database"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Conversations WHERE conversation_id = %s"
        cursor.execute(query, (conversation_id,))
        conversation = cursor.fetchone()
        cursor.close()
        conn.close()
        return conversation

def update_conversation_by_id(conversation_id, title):
    """Update a single conversation by ID"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE Conversations SET title = %s WHERE conversation_id = %s"
        cursor.execute(query, (title, conversation_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Conversation succesfully updated.")

def delete_conversation_by_id(conversation_id):
    """Delete a single conversation by ID"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM Conversations WHERE conversation_id = %s"
        cursor.execute(query, (conversation_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Conversation succesfully deleted.")