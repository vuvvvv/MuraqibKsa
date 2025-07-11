import arabic_reshaper
from bidi.algorithm import get_display


def reshape_arabic_text(text):
    return get_display(arabic_reshaper.reshape(text))
