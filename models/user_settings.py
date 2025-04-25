from models.database import Session
from models.user_language import UserLanguage

async def get_user_language(user_id: int):
    session = Session()
    lang_entry = session.query(UserLanguage).filter_by(user_id=user_id).first()
    session.close()
    return lang_entry.language if lang_entry else "en"

def set_user_language(user_id: int, language: str):
    session = Session()
    existing = session.query(UserLanguage).filter_by(user_id=user_id).first()
    if existing:
        existing.language = language
    else:
        new_lang = UserLanguage(user_id=user_id, language=language)
        session.add(new_lang)
    session.commit()
    session.close()
