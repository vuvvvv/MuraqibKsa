import os
import threading
import time

from arabic_text import reshape_arabic_text
from loding_main import loading_progress


def show_intro():
    try:
        stop_loading = threading.Event()
        loader_thread = threading.Thread(target=loading_progress, args=(stop_loading,))
        loader_thread.start()

        print(
            f"\n \033[93m[*] {reshape_arabic_text('هذي الاداة تم تطويرها من قبل @vuvvvv')}\033[0m"
            f"\n \033[93m[*] {reshape_arabic_text('هذه الأداة تعمل فقط على **أرقام الجوال السعودية**')}\033[0m"
            f"\n \033[93m[*] {reshape_arabic_text('الأداة لا تدعم أرقام دول أخرى')}\033[0m"
            f"\n \033[93m[*] {reshape_arabic_text('لا تستخدمها في الأمور المخالفة للقانون')}\033[0m"
            f"\n \033[91m[*] {reshape_arabic_text('لا يجوز استخدامها لأغراض التجسس أو الإزعاج أو انتهاك الخصوصية')}\033[0m"
        )
    except Exception as e:
        print(f"\033[91m[!] {reshape_arabic_text('حدث خطأ ما')} {e}\033[0m")

    finally:
        stop_loading.set()
        loader_thread.join()

    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

    print(
        f"""*************** MuraqibKsa ******************
╔════════════════════════════════════╗
║           📒  MuraqibKsa           ║
║              {reshape_arabic_text('مراقب KSA')}             ║ 
║    github.com/vuvvvv/MuraqibKsa    ║
╚════════════════════════════════════╝
************** {reshape_arabic_text('مراقب KSA')} ********************
"""
    )
