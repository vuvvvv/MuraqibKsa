import importlib.util
import sys

from arabic_text import reshape_arabic_text


def check_library_installed(package_name):
    return importlib.util.find_spec(package_name) is not None


def check_requirements():
    required_packages = ["selenium", "arabic_reshaper", "bidi"]
    missing_packages = []

    for pkg in required_packages:
        if not check_library_installed(pkg):
            missing_packages.append(pkg)

    if missing_packages:
        print(
            f"\033[91m[-] {reshape_arabic_text('المكتبات التالية غير مثبّتة:')}\033[0m"
        )
        for pkg in missing_packages:
            print(f"    - {pkg}")
        print(
            f"\033[91m[-] {reshape_arabic_text('يمكنك تثبيتها بالأمر التالي:')}\033[0m"
        )
        print(f"    pip install {' '.join(missing_packages)}")
        sys.exit(1)
    else:
        print(
            f"\033[92m[+] {reshape_arabic_text('جميع المكتبات المطلوبة مثبّتة وجاهزة.')} \033[0m"
        )
