import argparse
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from arabic_text import reshape_arabic_text
from check_requirements import check_requirements
from firefox import create_driver
from intro import show_intro
from loding_main import loading_progress
from check_requirements import Check


def search_ksa_number(number):
    try:
        driver = create_driver()
        driver.get(Check())

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
            print("\033[93m[+] No results found\033[0m")
            driver.quit()
            return

        all_rows_text = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if not cells or cells[0].find_elements(By.TAG_NAME, "img"):
                continue
            cell_texts = [cell.text.strip() for cell in cells]
            all_rows_text.append(cell_texts)

        if not all_rows_text:
            print(
                "\033[93m[+] No valid results found\033[0m"
            )
            driver.quit()
            return

        single_word_rows = []
        multi_word_rows = []

        for row in all_rows_text:
            full_row_text = " ".join(row)
            words_in_row = full_row_text.split()
            if len(words_in_row) == 1:
                single_word_rows.append(row)
            elif (
                len(words_in_row) > 1
            ):  
                multi_word_rows.append(row)

        rows_to_print = []
        if len(single_word_rows) >= 2:

            rows_to_print = multi_word_rows

        else:

            rows_to_print = all_rows_text

        if not rows_to_print:
            print(
                "\033[93m[+] No results to display\033[0m"
            )
            driver.quit()
            return

        for row in rows_to_print:
            reshaped = [reshape_arabic_text(cell) for cell in row]
            print(f"\033[92m[+] {' | '.join(reshaped)} \033[0m")

    except Exception as e:
        print("\033[91m[-] Incorrect number or no results found \033[0m")

    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=reshape_arabic_text(
            "A tool for mobile number search in **Muraqib KSA**"
        ),
        epilog="\n  python3 MuraqibKsa.py +966500000000 |OR| 0500000000",
    )

    parser.add_argument(
        "number",
        nargs="?",  
        help="Mobile number to search for (e.g., 0500000000 or +966500000000)",
    )
    args = parser.parse_args()

    show_intro()
    check_requirements()

    number_to_search = None
    if args.number: 
        number_to_search = args.number
    else: 
        number_to_search = input(
            "\033[94m[**] Enter the number to search for (e.g., 0500000000 or +966500000000): \033[0m \033[94m\n[**]\033[0m"
        )

    if not number_to_search:
        print("\033[91m[-] No number provided. Exiting.\033[0m")
    else:
        search_ksa_number(number_to_search)
