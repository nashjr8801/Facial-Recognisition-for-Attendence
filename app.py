from flask import Flask, render_template , request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///table.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# get the standard UTC time
UTC = pytz.utc


IST = pytz.timezone('Asia/Kolkata')


datetime_ist = datetime.now(IST)

class Table(db.Model):
    sno =db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable =False)
    desc=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime_ist)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"




@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title = request.form['title']
        desc = "..."
        table=Table(title=title, desc=desc)
        db.session.add(table)
        db.session.commit()
    alltable = Table.query.all()
    print(alltable)
    return render_template('index.html',alltable=alltable)


@app.route('/update')
def update():
    alltable = Table.query.all()
    print(alltable)
    return 'This is products page'

@app.route('/delete/<int:sno>')
def delete(sno):
    table = Table.query.filter_by(sno=sno)
    db.session.delete(table)
    return 'This is products page'

if __name__=="__main__":
    Table.query.delete()
    db.session.commit()
    app.run(debug=True, port=8000)
