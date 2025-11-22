from app import app, db

with app.app_context():
    db.create_all()
    print("✅ دیتابیس با موفقیت ساخته شد!")
