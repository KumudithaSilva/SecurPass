# 🔐 SecurPass — Password Manager & Generator  

<p align="center">
<img src="https://img.shields.io/badge/Tech-Python-306998" />
<img src="https://img.shields.io/badge/License-MIT-4caf50" />
<img src="https://img.shields.io/badge/CI-Passing-brightgreen" />
<img src="https://img.shields.io/badge/OOP-Yes-orange" />
<img src="https://img.shields.io/badge/SOLID-Principles-purple" />
<img src="https://img.shields.io/badge/Code%20Style-PEP8-yellow" />
<img src="https://img.shields.io/badge/Maintained-Yes-brightgreen" />
<img src="https://img.shields.io/badge/Version-0.1.2-blue" />
</p>

<hr style="border: 0; border-top: 1px solid #ddd; height: 1px; margin: 8px 0;">

**SecurPass** is a lightweight, secure, and user-friendly **password management application** developed in **Python** with a **Tkinter** GUI. It is designed to assist users in generating, storing, and retrieving passwords securely, thereby promoting strong password practices and reducing the cognitive burden of managing multiple credentials.

The project is architected using **Object-Oriented Programming (OOP)** principles and adheres to **SOLID design practices**, ensuring that the software is:


- 🛠️ **Well-Structured** — the codebase is organized into clearly defined modules such as password generation, data management, configuration, and message handling. This modular structure ensures that each part of the system has a single responsibility, making the application easy to understand, maintain, and extend.

- 🔄 **Adaptive & Reusable** — each component is designed to operate independently, allowing reuse across the application. For example, the password generator and data retrieval modules can be invoked from multiple parts of the program without duplication, ensuring consistency and reducing maintenance overhead.

- 🧩 **Extensible** — the architecture allows new functionalities to be added seamlessly. Features like configurable password complexity, flexible JSON-based data storage, and modular UI controls can be enhanced or expanded without altering existing modules, preserving system stability.

- ✅ **User-Centric Feedback** — the message and alert system guides users in real time, providing validation for missing fields or weak passwords, which improves usability and reduces errors.

- 📂 **Structured Data Handling** — all credentials are stored in a well-organized JSON format, making data retrieval reliable and consistent, while keeping the storage system lightweight.

- ⚙️ **Configurable & Flexible** — system parameters, such as password length and complexity, are centralized in a configuration module, allowing easy adjustments without touching core logic.

- 🎨 **Minimal & Clear UI** — the Tkinter-based interface is simple, intuitive, and designed to minimize user errors while maintaining full functionality.

- 🧪 **Testable Modules** — each core component (password generation, data management, UI) is modular and testable, facilitating unittesting and ensuring reliability of key functionalities.

---

## 🎓 Purpose  

- 🔑 **Securely store passwords** — maintain credentials in a structured and easily retrievable format.  
- ⏱️ **Generate strong, random passwords** — produce complex passwords with configurable length and character sets.  
- 📂 **Organize credentials** — associate passwords with websites and email addresses for clear, structured management.  
- 🧠 **Promote cybersecurity awareness** — guide users towards safer password practices through validation and feedback.  
- 🛠️ **Demonstrate real-world software engineering principles** — applying **OOP, SOLID design patterns, modularity, and PEP8 compliance**.  
- ✅ **Enable maintainable and testable code** — architecture allows for isolated module testing, easy debugging, and future extension.  
- 🎨 **Provide a user-friendly experience** — a clean, minimal Tkinter interface ensures accessibility for all users.  

---

## 🧠 Key Features  

- 📝 **Password Storage** — securely save website, email, and password in a structured CSV file for easy retrieval.  
- 🔐 **Password Generation** — automatically generate strong passwords combining letters, numbers, and symbols.  
- 🎨 **Minimal Tkinter UI** — intuitive interface with clear input forms and controls.  
- ⚙️ **Validation & Alerts** — prevents missing fields, duplicates, or weak passwords with real-time user feedback.  
- 📝 **Logging** — track application events and actions in `app.log` for maintainability and debugging.  
- 🔄 **Modular Architecture** — separate modules for UI, password generation, data management, and configuration ensure maintainability and scalability.  
- 🧩 **Extensible Design** — flexible structure allows future enhancements like additional password rules, UI tweaks, or configurable settings without impacting existing modules.  
- ✅ **Testable Components** — modules are designed to support unit testing, ensuring reliability and robustness of the application.  
- ⚡ **Lightweight & Efficient** — no heavy dependencies; runs efficiently using Python standard libraries and Tkinter.  


---

## 📸 SecurPass UI Preview  

<img width="370" height="370" alt="image" src="https://github.com/user-attachments/assets/d3a19224-b6d0-4e6a-baed-0df721f46dc8" />


---
## ✨ Features  

- 🔑 **Password Generator** — Configurable length and complexity.  
- 🏷️ **Save & Retrieve** — Manage multiple accounts efficiently.  
- ⚠️ **Error Handling & Validation** — Warns if a password is too short or fields are empty.  
- 📦 **Lightweight** — Pure Python, no heavy dependencies.  
- 📝 **Activity Logging** — Tracks events and user actions.  
- 🔄 **Reusable Modules** — Components can be utilized across the application.  
- 🧩 **Extensible Architecture** — Easy to add new functionalities or adjust settings.  

---

## 📌 How It Works  

1. **Enter Credentials** — Input website, email, and password.  
2. **Generate Password** — Automatically create a strong password based on configurable criteria (letters, numbers, symbols).  
3. **Save Credentials** — Validate inputs and store securely in `data.json`.  
4. **Retrieve Passwords** — Search for saved passwords by website for quick access.  
5. **Receive Feedback** — Alerts notify users of missing, weak, or duplicate passwords to ensure security compliance.  

---

## 🎯 Application Flow  

- ✏️ **Input Form** → Users enter website and email.  
- ⏱️ **Password Generation** → Randomly generates secure passwords with configurable complexity.  
- 💾 **Save Action** → Validates data and writes to storage.  
- 🔍 **Search Functionality** → Retrieves stored credentials efficiently.  
- ⚠️ **Validation & Alerts** → Ensures completeness, uniqueness, and strength of passwords.  
- 📝 **Activity Logging** → Tracks user actions and warnings in `app.log`.  

---

## 🔧 Core Components  

SecurPass is built with **modular, independent components** following **OOP and SOLID principles**, with each module responsible for a specific aspect of the application:

- `config.py`  
  — Stores configurable parameters for password rules and system behavior, enabling easy adjustments without modifying core logic.  

- `data_retrieval.py`  
  — Provides structured retrieval of saved credentials by website or email, ensuring data integrity and reliable access.  

- `data_save.py`  
  — Encapsulates the logic for writing credentials safely to CSV, including input validation checks.  

- `main.py`  
  — Serves as the **application entry point**, initializing core components and launching the UI.  

- `messagebox.py`  
  — Centralizes all **user messaging**, including warnings, errors, and confirmations, enhancing usability and security awareness.  

- `password_generator.py`  
  — Implements the **password creation logic**, supporting configurable length and character complexity for strong credentials.  

- `resources.py`  
  — Loads and manages static assets such as icons or images, maintaining modularity and separation of concerns.  

- `SecurePassController.py`  
  — Acts as the **core coordinator**, linking UI interactions with backend operations (data storage, retrieval, and password generation).  

- `ui.py`  
  — Constructs the **graphical interface**, managing inputs, buttons, alerts, and overall user experience in a clean, intuitive design.  

- `errors.py`  
  — Defines **custom exceptions** such as PasswordTooShortError and EmptyWebsiteError to standardize error handling across the project.

Each component is **independent yet cohesive**, making the system **maintainable, testable, and extensible**. The modular design allows **easy updates and feature expansion** without affecting other parts of the application.
 


---

## 🖥️ System Requirements

- Python **3.8+**  
- Dependencies:  
  - `tkinter` (built-in)  
- Optional: `pyperclip` for clipboard functionality  

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Project Structure  

```bash

SecurPass/
├── securpass/                           # Main application package
│   ├── __init__.py                      # Package initializer
│   ├── main.py                          # Entry point; initializes modules and launches UI
│   ├── SecurePassController.py          # Core coordinator linking UI, password generation, and data storage
│   ├── password_generator.py            # Strong password generation logic
│   ├── data_save.py                     # Saves credentials securely to CSV
│   ├── data_retrieval.py                # Retrieves credentials from CSV storage
│   ├── ui.py                            # Tkinter-based user interface
│   ├── messagebox.py                    # Handles user alerts, warnings, and confirmations
│   ├── config.py                        # Configurable parameters for password rules and system behavior
│   ├── resources.py                     # Manages static resources like icons/images
│   ├── errors.py                        # Manages custom exceptions
│   └── assets/                          # Static files
│       └── images/                       # Icon/image assets
│
├── tests/                               # Unit tests
│   └── test_main.py                      # Tests core functionalities
│
├── .github/                              # GitHub Actions workflows
│   └── workflows/
│       └── securpass-tests.yml           # CI/CD configuration
│
├── .flake8                               # Python style checking configuration
├── .gitignore                             # Ignore build files, __pycache__, etc.
├── LICENSE                                # MIT License
├── MANIFEST.in                            # Includes assets in Python package
├── pyproject.toml                         # Modern build system configuration
└── README.md                              # Project overview, setup, and usage

```

---

## 📦 Future Enhancements

- 🔐 Encryption — Encrypt saved passwords for enhanced security

- 📊 Analytics Dashboard — Track password strength & usage

---

## 🤝 Contributing

- 🍴 Fork the repo
- 🌱 Create a feature branch
- 🛠️ Commit changes
- 📤 Push branch & open Pull Request

- We welcome UI tweaks, new features, bug fixes, and documentation improvements!

---

## 🔀 Git Flow Workflow

The development process follows a **Git Flow** style workflow to keep development organized and efficient. Currently, it uses these branches:

- 🌿 **`master`** — Stable, production-ready code (released versions)  
- 🌱 **`develop`** — Main development branch for ongoing work  
- ✨ **`feature/*`** — For developing new features, branched off `develop`  
- 🛠️ **`release/*`** — For preparing releases, branched off `develop`  
- 🩹 **`hotfix/*`** — For urgent bug fixes, branched off `master`

---

## 💡 Inspiration

>SecurPass was created to provide secure, easy-to-use password management in everyday life while showcasing OOP and SOLID principles in Python. The project demonstrates a modular, maintainable, and extensible design with clean coding practices, combining practical cybersecurity needs with professional software engineering.
