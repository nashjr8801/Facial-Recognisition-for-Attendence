from flask import Flask, render_template , request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///table.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Table(db.Model):
    sno =db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable =False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
alltable = Table.query.all()
print(alltable[0].title)
# alltable = Table.query.delete()
# db.session.commit()
# print(alltable)