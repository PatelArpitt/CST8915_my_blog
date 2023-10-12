# comment_service.py

from flask import Flask, jsonify
import requests

app = Flask(__name__)

comments = {
    '1': {'user_id': '1', 'comment': 'Hello, world!'},
    '2': {'user_id': '2', 'comment': 'My first blog comment'}
}

@app.route('/comment/<id>')
def comment(id):

    comment_info = comments.get(id, {})
    
    # Get user info from User Service
    if comment_info:
        response = requests.get(f'http://localhost:5000/user/{comment_info["user_id"]}')
        if response.status_code == 200:
            comment_info['user'] = response.json()

    return jsonify(comment_info)

if __name__ == '__main__':
    app.run(port=5002)