import argparse
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from arabic_text import reshape_arabic_text
from check_requirements import check_requirements
from firefox import create_driver
from intro import show_intro
from loding_main import loading_progress, Lodding


def search_ksa_number(number):
    try:
        driver = create_driver()
       

        driver.get(Lodding())

        stop_loading = threading.Event()
        loader_thread = threading.Thread(target=loading_progress, args=(stop_loading,))
        loader_thread.start()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "snumber"))
        )
        stop_loading.set()
        loader_thread.join()

        input_box = driver.find_element(By.ID, "snumber")
        input_box.clear()
        input_box.send_keys(number)
        driver.find_element(By.ID, "sbutton").click()

        stop_loading.clear()
        loader_thread = threading.Thread(target=loading_progress, args=(stop_loading,))
        loader_thread.start()

        WebDriverWait(driver, 15).until(
            lambda d: len(
                d.find_element(By.ID, "tf_body").find_elements(By.TAG_NAME, "tr")
            )
        )

        stop_loading.set()
        loader_thread.join()

        tbody = driver.find_element(By.ID, "tf_body")
        rows = tbody.find_elements(By.TAG_NAME, "tr")

        if not rows:
            print("\033[93m[+] لا توجد نتائج. قد يكون الرقم جديدًا.\033[0m")
            driver.quit()
            return

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if not cells:
                continue

            img = cells[0].find_elements(By.TAG_NAME, "img")
            if img:
                continue

            cell_texts = [cell.text.strip() for cell in cells]

            if any("ﺎﺘﻗﺆﻣ" in cell for cell in cell_texts):
                print("\033[91m[-] تم الحظر مؤقتًا من الموقع.\033[0m")
                driver.quit()
                return

            reshaped_cells = [reshape_arabic_text(cell) for cell in cell_texts]
            print(f"\033[92m[+] {' | '.join(reshaped_cells)} \033[0m")

    except Exception as e:
        print(f"\033[91m[-] حصل خطأ: {e}\033[0m")

    finally:
        try:
            driver.quit()
        except:
            pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f"{reshape_arabic_text('تعليمات')}")
    parser = argparse.ArgumentParser(
        description=reshape_arabic_text("اداة للبحث برقم الجوال ** مراقب KSA **"),
        epilog="\n  python3 MuraqibKsa.py +966500000000 |OR| 0500000000",
    )

    parser.add_argument(
        "number",
        help=reshape_arabic_text(
            "رقم الجوال للبحث عنه (مثال: 0500000000 أو +966500000000)"
        ),
    )
    args = parser.parse_args()
    show_intro()
    check_requirements()

    search_ksa_number(args.number)
