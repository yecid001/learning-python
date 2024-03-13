from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_option', methods=['POST'])
def process_option():
    option = request.form.get('option')
    if option == '1':
        # Create a new user
        pass
    elif option == '2':
        # List users
        pass
    elif option == '3':
        # Search user
        pass
    elif option == '4':
        # Update user
        pass
    elif option == '5':
        # Delete user
        pass
    else:
        # Invalid option
        pass

if __name__ == '__main__':
    app.run(debug=True)