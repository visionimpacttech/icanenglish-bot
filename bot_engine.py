
from content_manager import get_daily_word

def get_response(user_input, user_profile):
    text = user_input.lower()
    if "word" in text or "day" in text:
        return get_daily_word(user_profile.level)
    return "Hi {name}! Ready to learn English today? 😊 Type 'word' to get started.".format(name=user_profile.name)
