# 🔍 Mini Search Engine (Python)

A simple command-line search engine built with Python that allows users to search the web directly from the terminal. It retrieves search results using the **DDGS (DuckDuckGo Search)** library and lets users open any result in their default web browser.

---

## ✨ Features

* 🔎 Search the web from the terminal
* 📄 Displays the top search results
* 📝 Shows the title, URL, and description for each result
* 🌐 Open any search result in your default web browser
* 🔁 Perform multiple searches without restarting the program
* ❌ Graceful handling of invalid input and search errors
* 💻 Lightweight and easy to use

---

## 📸 Example

```text
================================================================================
             MINI SEARCH ENGINE
================================================================================

Search (or type 'exit'): python

================================================================================
Searching for: python
================================================================================

[1] Welcome to Python.org
URL : https://www.python.org/
Info: The official home of the Python Programming Language.

[2] Python Tutorial - W3Schools
URL : https://www.w3schools.com/python/
Info: Learn Python with examples.

Enter result number to open (0 = Back, q = Quit): 1
Opening browser...
```

---

## 🛠️ Technologies Used

* Python 3
* DDGS (DuckDuckGo Search)
* Webbrowser (Python Standard Library)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mini-search-engine.git
```

### 2. Navigate to the project folder

```bash
cd mini-search-engine
```

### 3. Install the required package

```bash
pip install -U ddgs
```

---

## ▶️ Usage

Run the program using:

```bash
python search.py
```

Type anything you want to search.

Example:

```text
Search (or type 'exit'): artificial intelligence
```

After the results are displayed, enter the corresponding number to open a result in your browser.

---

## 📂 Project Structure

```text
Mini-Search-Engine/
│
├── search.py
├── README.md
└── requirements.txt
```

---

## 📄 Requirements

* Python 3.8 or later
* Internet connection
* DDGS package

Install dependencies:

```bash
pip install -U ddgs
```

---

## 🚀 Future Improvements

* 🎨 Colored terminal interface
* 📜 Search history
* ⭐ Bookmarks
* 🖼️ Image search
* 📰 News search
* 🎤 Voice search
* 📄 Pagination (Next/Previous pages)
* 🌙 Dark mode
* 🖥️ GUI version using PyQt6
* ⚡ Faster search performance

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project, feel free to fork the repository, make your changes, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with ❤️ using Python.
