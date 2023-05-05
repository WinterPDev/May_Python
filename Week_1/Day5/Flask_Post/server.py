from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# Create a home form route
@app.route('/') # Display the form!
def show_form():
    return render_template('form.html')


# Create a Route to POST the data to
@app.route('/submit_form', methods=['POST']) # Action Route to submit the form!
def submit_form():
    session['title'] = request.form['title']
    session['genre'] = request.form['genre']
    session['release_year'] = request.form['release_year']
    session['movie_length'] = request.form['movie_length']
    '''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    DO NOT RENDER ON A POST ROUTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    return redirect('/display')

@app.route('/clear') # Action Route
def clear():
    session.clear()
    return redirect('/')

# Create a destination Route to send the POST-ed Data
@app.route('/display') # Display Route!
def display():

    return render_template('display.html')


# Transfer the data using Session to the display route so it isn't lost between pages!



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.