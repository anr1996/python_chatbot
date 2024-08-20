import sqlite3
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('chatbot.db') # creates or opens a file named chatbot.db
cursor = conn.cursor() # Get a cursor object to execute SQL commands

# Creates a table for storing facts
cursor.execute('''
   CREATE TABLE IF NOT EXISTS facts (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
)
''')

# Insert some initial data
cursor.execute('''
INSERT INTO facts (question, answer) VALUES
('What is Python?', 'Python is a programming language.'),
('What is AI?', 'AI stands for Artificial Intelligence.')
''')
 

# commit the changes and close the connection
conn.commit() # save (commit) the changes
conn.close() # close the connection to the database.

