from sqlalchemy import Column, String, Integer
from models.database import Base, Session

class UserSettings(Base):
    __tablename__ = "user_settings"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    language = Column(String)

# دالة جلب اللغة
async def get_user_language(user_id: int):
    session = Session()
    lang_entry = session.query(UserSettings).filter_by(user_id=user_id).first()
    session.close()
    return lang_entry.language if lang_entry else "en"

# دالة حفظ أو تعديل اللغة
def set_user_language(user_id: int, language: str):
    session = Session()
    existing = session.query(UserSettings).filter_by(user_id=user_id).first()
    if existing:
        existing.language = language
    else:
        new_lang = UserSettings(user_id=user_id, language=language)
        session.add(new_lang)
    session.commit()
    session.close()
