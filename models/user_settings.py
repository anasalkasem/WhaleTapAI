async def get_user_language(user_id: int):
    session = Session()
    lang_entry = session.query(UserLanguage).filter_by(user_id=user_id).first()
    session.close()
    return lang_entry.language if lang_entry else "en"
