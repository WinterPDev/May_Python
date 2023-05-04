from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/home')
def home():
    return 'This is the Home Page! 🎃'

# butkus
@app.route('/hello/<petname>/<favFood>')
def petname(petname, favFood):
    return f"Hello to {petname}! Their favorite food is {favFood}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

