from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# تنظیمات دیتابیس SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# مدل رزرو وقت
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)

# صفحه اصلی
@app.route('/')
def index():
    return render_template('index.html')

# پردازش فرم رزرو
@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    service = request.form['service']
    date = request.form['date']
    time = request.form['time']

    new_booking = Booking(name=name, phone=phone, service=service, date=date, time=time)
    db.session.add(new_booking)
    db.session.commit()

    return redirect(url_for('success'))

# صفحه موفقیت
@app.route('/success')
def success():
    return render_template('success.html')

# اجرای سرور
if __name__ == "__main__":
    app.run(debug=True)
