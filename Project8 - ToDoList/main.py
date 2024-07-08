from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    tasklist = db.session.execute(db.select(Task).order_by(Task.done)).scalars().all()
    return render_template('index.html', tasklist=tasklist)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task_name = request.form.get('todoitem')
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/done/<int:task_id>')
def done(task_id):
    task = db.get_or_404(Task, task_id)
    task.done = True
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
