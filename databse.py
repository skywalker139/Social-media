from app import posts, db, Post
from flask import Flask

app = Flask(__name__)
from app import User, Post  # Import your models

# ... other Flask app code

@app.before_first_request  # Run this code before the first request
def create_dummy_data():
    # Create some dummy users (assuming you have a way to generate usernames, emails, passwords)
    user1 = User(username="user1", email="user1@example.com", password="password1")
    user2 = User(username="user2", email="user2@example.com", password="password2")

    # Create some dummy posts with the generated users
    post1 = Post(title="Welcome Post", content="This is the first post!", author=user1)
    post2 = Post(title="Another Post", content="Sharing some dummy content.", author=user2)

    db.session.add_all([user1, user2, post1, post2])
    db.session.commit()  # Commit the data to the database

# ... other Flask routes


for post_data in posts:
        post = Post(title=post_data['title'], id=post_data['id'], content=post_data['content'])
        db.session.add(post)
    
db.session.commit()
print('Dummy posts added to the database.')