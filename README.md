# 👾 Leet Speak Converter (`1337 5P34K`)

![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

Welcome to the **Leet Speak Converter**! This is a dynamic, lightweight Python utility that transforms standard English text into stylized "Leet-Speak" (1337). 

Leet (or "1337") is a system of modified spellings primarily used on the internet, where standard alphabet characters are replaced by numerals or special character combinations that visually resemble the original letters.

---

## ✨ Features
- **Dynamic Randomization**: Translates characters dynamically! Every time you translate the same string, the output changes because the script selects from multiple possible character replacements using Python's `random.choice()`.
- **Full Alphanumeric Support**: Converts both letters (`A-Z`) and numbers (`0-9`). It even handles whitespace transformation!
- **Interactive CLI**: Runs in an infinite continuous loop, allowing you to convert sentences on the fly directly from the terminal without restarting the script.
- **Preserves Unmapped Characters**: Any character not explicitly defined in the leet dictionary (like standard punctuation `!`, `?`, `.`) is safely ignored and preserved in the final output.

---

## 🛠️ Complete Character Mapping Dictionary
The script uses a highly extensive mapping dictionary to ensure visually striking variations. Here is the complete list of character conversions the script is capable of:

| Standard Character | Leet Conversions | Standard Character | Leet Conversions |
|:---:|:---|:---:|:---|
| **A** | `4`, `@`, `∆`, `^`, `∀`, `A`, `a` | **N** | `N`, `n` |
| **B** | `8`, `3`, `13`, `6`, `B`, `b` | **O** | `0`, `()`, `<>`, `O`, `o` |
| **C** | `(`, `[`, `<`, `C`, `c` | **P** | `9`, `P`, `p` |
| **D** | `0`, `D`, `d` | **Q** | `9`, `0`, `Q`, `q` |
| **E** | `3`, `€`, `£`, `Ǝ`, `E`, `e` | **R** | `2`, `12`, `R`, `r` |
| **F** | `ƒ`, `F`, `f` | **S** | `5`, `$`, `Z`, `z`, `S`, `s` |
| **G** | `6`, `9`, `G`, `g` | **T** | `7`, `T`, `t` |
| **H** | `#`, `H`, `h` | **U** | `v`, `U`, `u` |
| **I** | `1`, `!`, `\|`, `I`, `i` | **V** | `\/`, `V`, `v` |
| **J** | `;`, `J`, `j`, `]` | **W** | `vv`, `W`, `w` |
| **K** | `\|<`, `/<`, `K`, `k` | **X** | `><`, `}{`, `)(`, `X`, `x` |
| **L** | `1`, `\|`, `\|_`, `!`, `L`, `l` | **Y** | `` `/ ``, `Y`, `y` |
| **M** | `\|\\/\|`, `^^`, `\|V\|`, `[V]`, `M`, ` m` | **Z** | `2`, `Z`, `z` |

### Number & Space Mappings
| Standard | Leet Conversions |
|:---:|:---|
| **1** | `I`, `\|`, `!`, `1`, `l` |
| **2** | `Z`, `z`, `2` |
| **3** | `E`, `3`, `Ǝ` |
| **4** | `A`, `4` |
| **5** | `S`, `s`, `5` |
| **6** | `G`, `b`, `6` |
| **7** | `T`, `7`, `+` |
| **8** | `B`, `8`, `I3` |
| **9** | `g`, `9`, `q` |
| **0** | `O`, `o`, `0`, `()`, `*`, `[]` |
| **Space** | `_`, `-`, ` ` |

---

## 💻 Code Architecture Overview
The script is contained entirely within `leet.py` and is divided into two primary functions:

1. **`cnvrt_to_leet(str)`**:
   - The core engine. It defines the `leet_dict` dictionary.
   - It iterates over the inputted string `char` by `char`.
   - It converts the character to lowercase to match the dictionary keys.
   - It utilizes `random.choice(leet_dict[char.lower()])` to append a random variation to the final string `leet_text`.

2. **`main()`**:
   - Acts as the CLI wrapper.
   - Implements a `while True:` loop to continuously ask the user for an input string using `input()`.
   - Prints the returned processed string in a formatted layout.

---

## 🚀 Getting Started

### Prerequisites
All you need is Python 3.x installed on your machine. The script uses the native `random` module, so **no external dependencies or libraries are required!**

### Installation & Execution
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
   Enter a string: Hack the planet!
   Leet-Speak Code :  #4<k_7#€_p14N37!
   
   Enter a string: Hack the planet!
   Leet-Speak Code :  H@C|</#3-91@n£+!
   
   Enter a string: 123456
   Leet-Speak Code :  !zE4S6
   ```

> *Tip: To exit the infinite loop in your terminal, press `CTRL+C`.*
