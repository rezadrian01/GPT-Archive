import mysql.connector
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
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Conversations table succesfully created.")

def insert_conversation(title, link, chat_json):
    """Add conversation to database"""
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO Conversations (title, link, text) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, link, chat_json))
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
