from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'})
    else:
        return jsonify({'error': 'Missing username or password'}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        # You can implement a session management system or token-based authentication here
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in (you can implement this based on session or token)
        # For demo purposes, we'll assume the user is logged in
        return f(*args, **kwargs)
    return decorated_function

@app.route('/habits', methods=['GET'])
@login_required
def get_user_habits():
    # Get the logged-in user's habits
    # For demo purposes, we'll return sample habits
    user_habits = {
        "running": {
            "goal": 3,
            "planned_days": ["Monday", "Wednesday", "Saturday"],
            "occurrences": [
                {"date": "2024-04-15", "completed": True},
                {"date": "2024-04-17", "completed": False}
            ]
        },
        "training": {
            "goal": 2,
            "planned_days": ["Tuesday", "Friday"],
            "occurrences": []
        }
    }
    
    return jsonify(user_habits)


@app.route('/habits', methods=['GET'])
@login_required
def get_user_habits():
    # Get the logged-in user's habits
    # For demo purposes, we'll return sample habits
    user_habits = {
        "running": {
            "goal": 3,
            "planned_days": ["Monday", "Wednesday", "Saturday"],
            "occurrences": [
                {"date": "2024-04-15", "completed": True},
                {"date": "2024-04-17", "completed": False}
            ]
        },
        "training": {
            "goal": 2,
            "planned_days": ["Tuesday", "Friday"],
            "occurrences": []
        }
    }
    
    return jsonify(user_habits)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)