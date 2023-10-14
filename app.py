from flask import Flask,render_template

# Create a Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def index():
    return render_template('html/mainhp.html')

@app.route('/aboutus')
def aboutus():
    return render_template('html/about us.html')

@app.route('/contact')
def contact():
    return render_template('html/contact.html')

@app.route('/signup')
def signup():
    return render_template('html/sign up.html')

@app.route('/feedback')
def feedback():
    return render_template('html/follow us.html')

@app.route('/signin')
def signin():
    return render_template('html/FIRST PAGE .HTML')

@app.route('/ownersignup')
def ownersignup():
    return render_template('html/owner sign up.html')

@app.route('/ownership')
def ownership():
    return render_template('html/ownershp.html')

@app.route('/upload')
def upload():
    return render_template('html/upload.html')

# Run the Flask app
if __name__ == '__main__':
    app.run()
