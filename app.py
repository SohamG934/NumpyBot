import bot
from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['userInput']
    
    # Call your Python script to generate AI response
    bot_response = bot.generate_response(user_input)  # Replace with the actual function call

    return jsonify({'bot_response': bot_response})

if __name__=='__main__':
    app.run() 