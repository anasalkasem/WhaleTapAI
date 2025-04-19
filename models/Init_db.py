from models.database import Base, engine

# إنشاء الجداول إذا لم تكن موجودة مسبقاً
Base.metadata.create_all(bind=engine)

print("✅ تمت مزامنة الجداول مع قاعدة البيانات.")
