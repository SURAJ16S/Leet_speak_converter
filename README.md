# 👾 Leet Speak Converter (`1337 5P34K`)

![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

Welcome to the **Leet Speak Converter**! This is a dynamic, lightweight Python utility that transforms standard English text into stylized "Leet-Speak" (1337). 

Leet (or "1337") is a system of modified spellings primarily used on the internet, where standard alphabet characters are replaced by numerals or special character combinations that visually resemble the original letters.

---

## ✨ Features
- **Dynamic Randomization**: Translates characters dynamically! Every time you translate the same string, the output changes because the script selects from multiple possible character replacements (e.g., the letter `E` can become `3`, `€`, `£`, or `Ǝ`).
- **Full Alphanumeric Support**: Converts both letters (`A-Z`) and numbers (`0-9`).
- **Interactive CLI**: Runs in a continuous loop, allowing you to convert sentences on the fly directly from the terminal.

---

## 🚀 Getting Started

### Prerequisites
All you need is Python 3.x installed on your machine. No external dependencies or libraries are required!

### Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/SURAJ16S/Leet_speak_converter.git
   cd Leet_speak_converter
   ```

2. **Run the script:**
   ```bash
   python leet.py
   ```

3. **Convert your text!**
   The terminal will prompt you. Simply type your standard string and hit `Enter` to see the magic happen.
   
   *Example Session:*
   ```text
   Enter a string: Hello World
   Leet-Speak Code :  #311() vv()1210
   
   Enter a string: Hello World
   Leet-Speak Code :  H£!!<> \/V02L0
   ```

---

## 🛠️ How it Works under the Hood
The script utilizes a hardcoded `leet_dict` dictionary containing lists of corresponding visual replacements for every letter and number. 

When you enter a string:
1. It iterates through every character.
2. Checks if the lowercase version of the character exists in the `leet_dict`.
3. If it exists, it imports Python's native `random` module to execute `random.choice()`, picking a random symbol out of the available list for that specific character.
4. If it doesn't exist (like punctuation), it leaves the character entirely intact.

---

> *Note: This script is continuously updated to expand the dictionary and introduce more complex Leet variations!*
