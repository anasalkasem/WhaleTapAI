from models import User  # أو أي موديل للمستخدمين عندك
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session  # جلسة الاتصال بقاعدة البيانات

async def update_user_setting(user_id: int, setting_key: str, new_value: str) -> bool:
    try:
        async with async_session() as session:  # افتح جلسة قاعدة بيانات
            user = await session.get(User, user_id)
            if not user:
                return False

            setattr(user, setting_key, new_value)  # عدّل الإعداد
            await session.commit()
            return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
