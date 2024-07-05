from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def get_headers(self):
        return [column.name for column in self.__table__.columns]


class AddForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Cafe Location on Google Maps(url)', validators=[DataRequired(), URL()])
    sockets = BooleanField('Does the cafe have sockets?', validators=[DataRequired()])
    toilet = BooleanField('Does the cafe have a toilet?', validators=[DataRequired()])
    wifi = BooleanField('Does the cafe have Wifi?', validators=[DataRequired()])
    calls = BooleanField('Does the cafe allow calls?', validators=[DataRequired()])
    seats = SelectField('How many seats does the cafe have?', choices=['0-10', '10-20', '20-30', '30-40', '40-50', '50+'], validators=[DataRequired()])
    price = StringField('Coffe Price', validators=[DataRequired()])
    submit = SubmitField('Add!')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    headers = all_cafes[0].get_headers()
    return render_template('cafes.html', cafes=all_cafes, headers=headers)

@app.route('/one_cafe/<int:cafe_id>')
def one_cafe(cafe_id):
    req_cafe = db.get_or_404(Cafe, cafe_id)
    return render_template('one_cafe.html', cafe=req_cafe)

@app.route('/add')
def add():
    form = AddForm()
    return render_template('add.html', form=form)

if __name__=='__main__':
    app.run(debug=True)