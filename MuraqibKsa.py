import argparse  # Used for parsing command-line arguments.
import sys  # Provides access to system-specific parameters and functions, like checking the OS.
import threading  # Used for running tasks in parallel (like the loading animation).

from selenium.webdriver.common.by import (  # Used to specify how to locate elements (e.g., by ID, by tag name).
    By,
)
from selenium.webdriver.support import (
    expected_conditions as EC,  # Provides common conditions to wait for in web automation.
)
from selenium.webdriver.support.ui import (  # Used to wait for specific conditions to be met before proceeding.
    WebDriverWait,
)

from arabic_text import (  # Custom module to handle Arabic text shaping for correct display.
    reshape_arabic_text,
)
from check_requirements import (  # Custom module to verify necessary dependencies or conditions.; Custom class/function from check_requirements to get a URL or check something.
    Check,
    check_requirements,
)
from firefox import (  # Custom module to initialize and configure the Selenium Firefox WebDriver.
    create_driver,
)
from intro import (  # Custom module to display an introductory message or banner.
    show_intro,
)
from loding_main import (  # Custom module for displaying a loading animation.
    loading_progress,
)


def search_ksa_number(number):
    """
    Searches for a given Saudi Arabian (KSA) mobile number .

    Args:
        number (str): The mobile number to search for.
    """
    try:
        driver = (
            create_driver()
        )  # Initializes the Selenium WebDriver (Firefox in this case).
        driver.get(
            Check()
        )  # Navigates the browser to the URL retrieved from the Check function.

        # --- Loading Animation Setup (Initial Load) ---
        stop_loading = (
            threading.Event()
        )  # Event to signal the loading animation thread to stop.
        loader_thread = threading.Thread(
            target=loading_progress, args=(stop_loading,)
        )  # Creates a thread for the loading animation.
        loader_thread.start()  # Starts the loading animation thread.

        # --- Wait for Search Input Field ---
        WebDriverWait(
            driver, 15
        ).until(  # Waits up to 15 seconds for a specific condition.
            EC.presence_of_element_located(
                (By.ID, "snumber")
            )  # Waits until the element with ID "snumber" is present on the page.
        )
        stop_loading.set()  # Signals the loading animation thread to stop.
        loader_thread.join()  # Waits for the loading animation thread to finish.

        # --- Enter Number and Perform Search ---
        input_box = driver.find_element(
            By.ID, "snumber"
        )  # Finds the input field by its ID.
        input_box.clear()  # Clears any existing text in the input field.
        input_box.send_keys(number)  # Types the provided number into the input field.
        driver.find_element(By.ID, "sbutton").click()  # Clicks the search button.

        # --- Loading Animation Setup (After Search) ---
        stop_loading.clear()  # Resets the event for a new loading animation.
        loader_thread = threading.Thread(
            target=loading_progress, args=(stop_loading,)
        )  # Creates a new thread for the loading animation.
        loader_thread.start()  # Starts the loading animation thread again.

        # --- Wait for Search Results ---
        WebDriverWait(
            driver, 15
        ).until(  # Waits up to 15 seconds for search results to appear.
            lambda d: len(  # Custom lambda function to check the condition.
                d.find_element(By.ID, "tf_body").find_elements(
                    By.TAG_NAME, "tr"
                )  # Checks if there are any table rows within the element with ID "tf_body".
            )
        )
        stop_loading.set()  # Signals the loading animation thread to stop.
        loader_thread.join()  # Waits for the loading animation thread to finish.

        # --- Process Search Results ---
        tbody = driver.find_element(
            By.ID, "tf_body"
        )  # Finds the table body element where results are displayed.
        rows = tbody.find_elements(
            By.TAG_NAME, "tr"
        )  # Gets all table rows within the table body.

        if not rows:  # Checks if no rows were found.
            print(
                "\033[93m[+] No results found\033[0m"
            )  # Prints a message in yellow (using ANSI escape codes).
            driver.quit()  # Closes the browser.
            return  # Exits the function.

        all_rows_text = []  # List to store extracted text from all valid rows.
        for row in rows:  # Iterates through each found row.
            cells = row.find_elements(
                By.TAG_NAME, "td"
            )  # Gets all table data cells within the current row.
            if not cells or cells[0].find_elements(
                By.TAG_NAME, "img"
            ):  # Skips rows that have no cells or the first cell contains an image (e.g., headers or irrelevant rows).
                continue  # Continues to the next row.
            cell_texts = [
                cell.text.strip() for cell in cells
            ]  # Extracts and strips whitespace from text of each cell.
            all_rows_text.append(
                cell_texts
            )  # Adds the list of cell texts to all_rows_text.

        if not all_rows_text:  # Checks if no valid results were extracted.
            print(
                "\033[93m[+] No valid results found\033[0m"  # Prints a message in yellow.
            )
            driver.quit()  # Closes the browser.
            return  # Exits the function.

        single_word_rows = []  # List to store rows that contain only one word.
        multi_word_rows = []  # List to store rows that contain multiple words.

        for row in all_rows_text:  # Iterates through the extracted text rows.
            full_row_text = " ".join(
                row
            )  # Joins all cell texts in a row into a single string.
            words_in_row = full_row_text.split()  # Splits the row text into words.
            if len(words_in_row) == 1:  # Checks if the row contains only one word.
                single_word_rows.append(row)  # Adds to single_word_rows.
            elif (
                len(words_in_row) > 1
            ):  # Checks if the row contains more than one word.
                multi_word_rows.append(row)  # Adds to multi_word_rows.

        rows_to_print = []  # List to store the rows that will actually be printed.
        if len(single_word_rows) >= 2:  # Conditional logic to filter results.
            # If there are 2 or more "single-word" rows, it suggests they might be irrelevant,
            # so only "multi-word" rows are considered for printing.
            rows_to_print = multi_word_rows

        else:  # If less than 2 "single-word" rows, all valid rows are printed.
            rows_to_print = all_rows_text

        if (
            not rows_to_print
        ):  # Checks if there are any rows to display after filtering.
            print(
                "\033[93m[+] No results to display\033[0m"  # Prints a message in yellow.
            )
            driver.quit()  # Closes the browser.
            return  # Exits the function.

        # --- Print Results Based on OS ---
        if sys.platform.startswith("linux"):  # Checks if the operating system is Linux.
            # For Linux, Arabic text might display correctly without reshaping.
            for row in rows_to_print:  # Iterates through rows to print.
                print(
                    f"\033[92m[+] {' | '.join(row)} \033[0m"
                )  # Prints the row with green color and cells separated by '|'.
        else:
            # For other OS (like Windows), Arabic text often needs reshaping for proper display in console.
            for row in rows_to_print:  # Iterates through rows to print.
                reshaped = [
                    reshape_arabic_text(cell) for cell in row
                ]  # Reshapes Arabic text in each cell.
                print(
                    f"\033[92m[+] {' | '.join(reshaped)} \033[0m"
                )  # Prints the reshaped row in green.

    except (
        Exception
    ) as e:  # Catches any general exceptions that occur during the process.
        print(
            "\033[91m[-] Incorrect number or no results found \033[0m"
        )  # Prints an error message in red.

    finally:  # This block always executes, regardless of whether an exception occurred.
        try:
            driver.quit()  # Attempts to close the browser cleanly.
        except:
            pass  # Ignores any errors if the driver couldn't be closed (e.g., if it was never initialized).


if (
    __name__ == "__main__"
):  # This block runs only when the script is executed directly (not imported as a module).
    # --- Argument Parser Setup ---
    # The reshape_arabic_text in the argparse description and epilog will still apply
    # regardless of OS, as argparse processes arguments before the OS check
    parser = argparse.ArgumentParser(  # Creates an ArgumentParser object to handle command-line arguments.
        description=reshape_arabic_text(  # Description of the script, with Arabic text reshaped.
            "A tool for mobile number search in **Muraqib KSA**"
        ),
        epilog="\n   python3 MuraqibKsa.py +966500000000 |OR| 0500000000",  # Example usage displayed at the end of help message.
    )

    parser.add_argument(  # Adds a command-line argument.
        "number",  # Name of the argument (positional).
        nargs="?",  # Makes the argument optional (0 or 1 occurrence).
        help="Mobile number to search for (e.g., 0500000000 or +966500000000)",  # Help message for the argument.
    )
    args = (
        parser.parse_args()
    )  # Parses the command-line arguments provided by the user.

    show_intro()  # Displays the introductory message.
    check_requirements()  # Runs the requirements check.

    number_to_search = None  # Initializes variable to store the number to search.
    if args.number:  # Checks if a number was provided via command-line argument.
        number_to_search = (
            args.number
        )  # Assigns the command-line argument to number_to_search.
    else:  # If no number was provided via command-line, prompt the user.
        number_to_search = input(  # Prompts the user to enter the number.
            "\033[94m[**] Enter the number to search for (e.g., 0500000000 or +966500000000): \033[0m \033[94m\n[**]\033[0m"  # Prompt message in blue.
        )

    if not number_to_search:  # Checks if the user provided no number.
        print(
            "\033[91m[-] No number provided. Exiting.\033[0m"
        )  # Prints an error message in red.
    else:
        search_ksa_number(
            number_to_search
        )  # Calls the main search function with the provided number.
