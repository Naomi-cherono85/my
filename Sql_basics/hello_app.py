from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/example'
db= SQLAlchemy(app)

print(f'table created successfully {db.metadata.tables.values()}')
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f'{self.name}'

@app.route('/')
def index():
    person=Person.query.first()
    if not Person.query.first():
        person=Person(name='Naomi')
        db.session.add(person)
        db.session.commit()
    return f'Hello {person.name}'

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)

