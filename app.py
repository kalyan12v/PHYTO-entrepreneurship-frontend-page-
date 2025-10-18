from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(
    __name__,
    template_folder='accessible-navbar',  # Tells Flask to look for HTML files here
    static_folder='accessible-navbar'   # Tells Flask to look for CSS/JS here
)
# Set a secret key for sessions and flashing messages
app.secret_key = 'kalyan@12v'

# --- Mock Database for Demo Login ---
# In a real application, this would be a database query
MOCK_USERS = {
    "user1": "password123",
    "admin": "securepass",
}

# ----------------- Routes for HTML Pages -----------------

@app.route('/')
def home():
    """Serves the main index page."""
    # The template references static files using Jinja2's url_for
    return render_template('index.html')

@app.route('/about')
def about():
    """Serves the about page."""
    return render_template('about.html')

@app.route('/features')
def features():
    """Serves the features page."""
    return render_template('features.html')

@app.route('/pricing')
def pricing():
    """Serves the pricing page."""
    return render_template('pricing.html')

# ----------------- Login Route -----------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the display and submission of the login form."""
    
    # If the user is already logged in, redirect them (e.g., to a dashboard)
    if 'logged_in' in session and session['logged_in']:
        # For this demo, we'll just redirect to the home page if logged in
        flash('You are already logged in!', 'info')
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Get data from the submitted form
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember') # Not fully implemented, but captured

        # Mock authentication logic
        if username in MOCK_USERS and MOCK_USERS[username] == password:
            # Successful login
            session['logged_in'] = True
            session['username'] = username
            flash(f'Login successful! Welcome, {username}.', 'success')
            
            # Redirect to the home page after successful login
            return redirect(url_for('home'))
        else:
            # Failed login
            flash('Invalid username or password. Please try again.', 'error')
            # Stay on the login page, allowing the user to try again
            # The 'show_error=True' parameter is removed as the error is handled by the flash message block.
            return render_template('login.html') 

    # For GET requests, just display the login form
    return render_template('login.html')

# ----------------- Logout Route (Optional but Recommended) -----------------

@app.route('/logout')
def logout():
    """Handles user logout."""
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# ----------------- Running the Application -----------------

if __name__ == '__main__':
    # Use 0.0.0.0 for compatibility, debug=True for development
    app.run(debug=True, host='0.0.0.0', port=5000)