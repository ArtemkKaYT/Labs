from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/korol/Labs/Sem2/Lab9/portfolio/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(300), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        link = request.form.get('link').strip()

        if title and link:
            project = Project(title=title, link=link)

            db.session.add(project)
            db.session.commit()

        return redirect(url_for('index'))

    projects = Project.query.order_by(Project.id.desc()).all()

    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
