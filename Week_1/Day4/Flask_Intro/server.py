from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keepitsecret' # We'll need this for our sessions! It's a lightweight cookie encryption

@app.route('/')
def home():
    return render_template('index.html', phrase='hello', times=10)

@app.route('/hello/<petname>/<favfood>')
def petname(petname, favFood):
    return f"Hello to {petname}! Their favorite food is {favFood}"

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    andrew_data = {
        'first_name' : 'Andrew',
        'last_name' : 'Tran',
        'education' : 'Coding Dojo Bootcamp!',
        'projects' : 'TBD',
        'contact' : 'andrew@tran.com'
    }

    return render_template("lists.html", andrew_data=andrew_data, bg_color='teal')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

