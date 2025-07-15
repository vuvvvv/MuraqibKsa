import arabic_reshaper
from bidi.algorithm import get_display

# reshaping arabic text
def reshape_arabic_text(text):
    return get_display(arabic_reshaper.reshape(text))
