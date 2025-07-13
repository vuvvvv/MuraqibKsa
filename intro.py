import os
import shutil
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
            "\n \033[93m[*] This tool was developed by @vuvvvv\033[0m"
            "\n \033[93m[*] This tool works only with Saudi mobile numbers\033[0m"
            "\n \033[91m[*] Do not use it for any illegal purposes\033[0m"
        )
    except Exception as e:
        print(f"\033[91m[!] error  {e}\033[0m")

    finally:
        stop_loading.set()
        loader_thread.join()

    time.sleep(4)
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """    +========================================================+
    |███╗   ███╗██╗   ██╗██████╗  █████╗  ██████╗ ██╗██████╗ |
    |████╗ ████║██║   ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗|
    |██╔████╔██║██║   ██║██████╔╝███████║██║   ██║██║██████╔╝|
    |██║╚██╔╝██║██║   ██║██╔══██╗██╔══██║██║▄▄ ██║██║██╔══██╗|
    |██║ ╚═╝ ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝██║██████╔╝|
    |██╗  ██╗███████╗═█████╗  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝ ╚═╝╚═════╝ |
    |██║ ██╔╝██╔════╝██╔══██╗                                |
    |█████╔╝ ███████╗███████║                                |
    |██╔═██╗ ╚════██║██╔══██║                                |
    |██║  ██╗███████║██║  ██║                                |
    |╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝github.com/vuvvvv/MuraqibKsa    |
    +========================================================+
    """
    )
