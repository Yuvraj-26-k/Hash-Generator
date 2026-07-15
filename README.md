# 🔐 Hash Generator

A Python-based Command Line Interface (CLI) application that generates secure SHA-256 hashes from user-provided text. The tool provides an interactive terminal interface with loading animations, progress bars, colored output, and report generation.

---

## 📌 Overview

Hash Generator is a beginner-friendly cybersecurity project built to understand how cryptographic hashing works using Python's `hashlib` module.

The application converts plain text into a SHA-256 hash, displays detailed information about the generated hash, and optionally saves the report to a text file.

---

## ✨ Features

- 🔐 Generate SHA-256 hashes
- 📝 Accept custom user input
- 📏 Display hash length
- 📅 Display generation date & time
- 💾 Save generated reports
- 🎨 Colored terminal interface
- ⏳ Loading animations
- 📊 Progress bar
- ⚠️ Input validation
- 📂 Display saved report location

---

## 🛠 Technologies Used

- Python 3
- hashlib
- os
- datetime
- time
- ANSI Terminal Colors

---

## 📂 Project Structure

```text
Hash-Generator/
│
├── hash_generator.py
├── README.md
├── report.txt
├── .gitignore
└── LICENSE (Optional)
```

---

## 📸 Project Demonstration

### 🔐 SHA-256 Hash Generation

> Demonstrates the successful generation of a SHA-256 hash from user input along with hash details, date, and time.
<img width="687" height="761" alt="hash_generator" src="https://github.com/user-attachments/assets/aab39b11-9c06-442e-9393-d032f8f823f3" />





---

## 📋 Example Output

```text
==============================
       HASH GENERATOR
==============================

Initializing..........
Loading Modules..........

Enter Text:
Hare Krishna

Generating SHA-256 Hash...

████████████████████ 100%

Hash Generated Successfully!

==============================
       HASH REPORT
==============================

Original Text   : Hare Krishna
Algorithm        : SHA-256
Hash Length      : 64 Characters

Generated Hash :

6d8e1d5f7a3c9e4b8f2d1e7c4a9f6b3d5f1c8e9a2d4b6c7f8a9b0c1d2e3f4a5

Date : 15-07-2026
Time : 15:42:10
```

---

## 🚀 Future Improvements

- Support multiple hashing algorithms
- File hashing
- Hash verification
- Drag-and-drop file support
- Export reports as CSV
- Export reports as JSON
- Better terminal UI using Rich
- Progress spinner using tqdm

---

## 📚 Learning Outcomes

This project helped me practice:

- Cryptographic Hashing
- SHA-256
- hashlib Module
- String Encoding
- File Handling
- Report Generation
- Terminal UI Design
- Progress Bars
- Python Modules

---

## 👨‍💻 Author

**Yuvraj Singh**

🎓 Computer Science (AI & ML) Student

🛡️ Aspiring Cybersecurity Professional

🐍 Python Developer

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
