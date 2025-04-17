from utils.database import Base, engine

# هذا ينشئ كل الجداول المعرّفة في Base
Base.metadata.create_all(bind=engine)

print("✅ تم إنشاء الجداول بنجاح")
