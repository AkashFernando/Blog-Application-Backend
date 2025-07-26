from flask import Flask
from database import db

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/blog_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
