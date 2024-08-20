from flask import Flask, request, jsonify # Import Flask and necessary modules for handling requests and JSON
import spacy # import spaCy for NLP tasks
import sqlite3 # Import SQLite3 for database interaction
import requests #Import the Requests library for external API calls.


#Initialize the Flask application
app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

#Placeholder function to process user input
def process_input(user_input):
    """
    Process the user input using spaCy for NLP tasks. 
    Here, we simply convert the input lowercase.

    Args:
        user_input (str): The user's input test.

        Returns:
        str: Processed input text.
        doc: The processed spaCy document.
    """
    doc = nlp(user_input)
    return doc

# Function to fetch data (placeholder)
def fetch_data(query):

    """
    Fetch data based on the user's query from the database.
  

    Args:
        query (str): The processed user query.

    Returns:
        str: Fetched data or response.

    """

    conn = sqlite3.connect('chatbot.db') # connect to the database
    cursor = conn.cursor() # Get a cursor object to execute SQL commands
    cursor.execute("Select answer FROM facts WHERE question LIKE ?", ('%' + query + '%',)) # Execute a query
    result = cursor.fetchone() # Fetch the first result
    conn.close()
    if result:
        return result[0] # Return the answer if found
    else:
        return "I don't know the answer to that question. " # Return a default response if not found
    


#Function to generate a response based on user input

def get_response(user_input):
    """
        Generate a response to the user's input by processing the input and fetching relevant data.

        Args:
            User_input (str): The user's input text.

        Returns:
            str: Response text.
    """

    doc = process_input(user_input) # Process the user input
    entities = [(ent.text, ent.label_) for ent in doc.ents] # Extract entities

    response = fetch_data(user_input)
    return f"{response}\Entities: {entities}" # Return the generated response.

# Define a route for the chatbot API

@app.route('/chatbot', methods=['POST'])

def chatbot():
    """
    Handle POST requests to the /chatbot endpoint.
    This function extracts the user's message from the request, generates a response, and returns it.

    Returns:
        Response: JSON response containing the chatbot's reply.
    """

    user_input = request.json.get("message") # Extract user input from the requesti JSON
    response = get_response(user_input) # Generate a response to user input
    return jsonify({"response": response}) # Return the response as JSON

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode for easier development and debugging




    

