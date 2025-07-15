# MuraqibKSA KSAمراقب

<br><br>

![لقطة شاشة ](img/capture_250713_220525.png "logo")
<br><br>
<br><br>

# Description

This is an open-source, command-line interface (CLI) tool designed to help users identify callers in Saudi Arabia by their mobile phone number.
<br><br>

# Installation

## **For windows**

- Download`git clone https://github.com/vuvvvv/MuraqibKsa.git`
  <br><br>

- Install requirements.txt
  `pip install -r requirements.txt`
  <br><br>

- Run
  `python .\MuraqibKsa.py  `
  Or
  `python .\MuraqibKsa.py Number phone `

### There are issues in Windows with Arabic language support. Follow these steps to make it work

<br><br>

- Before run `python .\MuraqibKsa.py` in your cmd to supports UTF-8 encoding to correctly display Arabic text use `chcp 65001`
  <br><br>
- And change font from cmd to
  `Simsun-ExtB`

  _Font_
  <br><br>

<br><br>

![لقطة شاشة ](img/capture_250713_210225.jpg "logo")
<br><br>
<br><br>

![لقطة شاشة ](img/capture_250713_222135.png "logo")
<br><br>

## **For Linux**

- Download
  `git clone https://github.com/vuvvvv/MuraqibKsa.git`
  <br><br>

- install requirements.txt
  `pip install -r requirements.txt`
  <br><br>

- Run
  `python .\MuraqibKsa.py  `
  or
  `python .\MuraqibKsa.py Number phone `
  <br><br>
  <br><br>
  <br><br>

![لقطة شاشة ](img/56.gif "logo")
<br><br>

## **For Mac Os**

**_Not yet_**

## **For Termux**

**_Not supported_**

<br><br>
<br><br>

| Operating System | Support Status |
| ---------------- | -------------- |
| Windows          | Supported      |
| Linux            | Supported      |
| macOS            | Not Yet Tested |
| Termux           | Not Supported  |

<br><br>
<br><br>
<br><br>

# Compile

<br><br>

Windows

- Install Python `https://www.python.org/downloads/release/python-3110/` recommend Python 3.11.0

&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;

Linux

- **Debian**
  Install Python `sudo apt install python3`
  <br><br>
- **Arch**
  Install Python `sudo pacman -S python`
  <br><br>
- **OpenSUSE**
  install Python `sudo zypper install python3`

<br><br>
<br><br>

### **Library**

- The `check_requirements.py` file uses the `check_library_installed` function to verify the installation status of packages

<br><br>

- Or install the required Python packages from the `requirements.txt` file, use `pip install -r requirements.txt`

<br><br>
<br><br>
<br><br>
<br><br>

| Library         | Description                                                                                                                     | Version | Support Status |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------- |
| selenium        | For browser automation, helping with UI testing, web automation, and data scraping.                                             | 4.33.0  | Supported      |
| arabic_reshaper | For processing and reshaping Arabic text to ensure correct display in environments that may not natively support Arabic script. | 3.0.0   | Supported      |
| python-bidi     | For handling bidirectional text (like Arabic and Hebrew), ensuring its proper rendering and orientation.                        | 0.6.6   | Supported      |

<br><br>
<br><br>
<br><br>

### **pip**

Sometimes, when you use `pip install <library>` to install a package, you may encounter the error message: `error: externally-managed-environment`.
<br><br>
<br><br>

![لقطة شاشة ](img/3.jpg "logo")

<br><br>

<_solutions_>

1. Use `install pipx` and then use `pipx install <librlai-name>`
   <br><br>

2. Use `pip install <librlai-name> --break-system-packages` easy solution and is to directly.
   <br><br>

3. Use `python3 -m venv .venv`then run `source .venv/bin/activate` now you are in a real environment and you can use `pip install <librlai-name>`

<br><br>
<br><br>
<br><br>

# Developers

**If you have any ideas or improvements that could benefit the project, feel free to**
<br><br>
Open an Issue to share your suggestions or report bugs.
<br><br>
Fork the repository, make your changes, and submit a Pull Request.
<br><br>
Contact me directly on GitHub for any questions or support.
<br><br>

[Discussions](https://github.com/vuvvvv/MuraqibKsa/discussions)

<br><br>

[@vuvvvv](https://github.com/vuvvvv)
