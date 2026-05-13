from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/korol/Labs/Sem2/Lab9/chat/messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'created_at': self.created_at.strftime('%H:%M')
        }


NAMES = ['Artem', 'Sanya', 'Misha', 'Danya', 'Ilya']
TEXTS = [
    'Понял, принял.',
    'Скиньте мем срочно.',
    'Чисто я в понедельник.',
    'Базу выдал, уважаю.',
    'А минусы будут?'
]


def add_sample_messages():
    if Message.query.count() == 0:
        for _ in range(5):
            db.session.add(Message(
                author=random.choice(NAMES),
                text=random.choice(TEXTS)
            ))
        db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/messages')
def get_messages():
    messages = Message.query.order_by(Message.created_at).all()
    return jsonify([message.to_dict() for message in messages])


@app.route('/api/message', methods=['POST'])
def add_message():
    message = Message(
        author=random.choice(NAMES),
        text=random.choice(TEXTS)
    )
    db.session.add(message)
    db.session.commit()
    return jsonify(message.to_dict())


@app.route('/api/clear', methods=['POST'])
def clear_messages():
    Message.query.delete()
    db.session.commit()
    return jsonify({'success': True})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_sample_messages()

    app.run(debug=True, port=8000)
