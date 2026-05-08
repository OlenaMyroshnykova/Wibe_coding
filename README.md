# 🦇 Gothic Team Vibe Dashboard

A gothic-style Streamlit dashboard for tracking the daily mood and energy level of a team.

The app allows users to register their current "vibe", save the history locally, visualize the team's energy level, and remove records when needed.

---

## 🌙 Project Overview

**Gothic Team Vibe Dashboard** is a small interactive web app built with **Python**, **Streamlit**, **Pandas**, and **Altair**.

The goal of the project is to practice:

- Building interactive web applications with Streamlit
- Managing user input
- Saving and loading data from a CSV file
- Visualizing data with charts
- Organizing Python code into clean and reusable modules
- Applying custom CSS styles to a Streamlit interface

---

## ✨ Features

- 🖤 Gothic visual design with custom CSS
- 🦇 Animated gothic effects
- 🕷️ White spider animation when the page is refreshed
- 📋 User form for registering team mood
- ⚡ Energy level slider
- 💾 Local data persistence using CSV
- 📊 Dark themed Altair bar chart
- 🗑️ Delete individual records
- 🧹 Clear the full history
- 🧩 Modular project structure following cleaner code organization

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Altair
- HTML/CSS for custom styling

---

## 📁 Project Structure

```text
Wibe_coding/
│
├── app.py                 # Main Streamlit application
├── config.py              # Global configuration and constants
├── storage.py             # CSV data loading and saving
├── effects.py             # Visual effects and animations
├── charts.py              # Altair chart generation
├── components.py          # UI components and layout blocks
├── styles.py              # Custom CSS styles
├── requirements.txt       # Project dependencies
├── historial_vibe.csv     # Local data file
└── .gitignore             # Files ignored by Git
```

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/OlenaMyroshnykova/Wibe_coding.git
cd Wibe_coding
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Git Bash:

```bash
source .venv/Scripts/activate
```

On Windows PowerShell:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Streamlit app

```bash
python -m streamlit run app.py
```

The app will open in your browser at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

```txt
streamlit
pandas
altair
```

---

## 💾 Data Storage

The app stores registered team vibe records in a local CSV file:

```text
historial_vibe.csv
```

This file is used to keep the history after refreshing the page or restarting the app.

For a production version, this could be replaced with a real database such as:

- SQLite
- PostgreSQL
- MySQL
- Firebase
- Supabase

---

## 📊 Main Functionality

Users can register:

- Their name
- Their current mood
- Their energy level

The app then calculates the average team energy and shows a message depending on the result:

- High energy → positive feedback
- Medium energy → stable team rhythm
- Low energy → coffee break recommendation

---

## 🧹 Clean Code Organization

The project was refactored into several files to make the code easier to read and maintain.

Instead of keeping everything inside one large `app.py`, the logic is separated into modules:

| File | Responsibility |
|---|---|
| `app.py` | Main application flow |
| `config.py` | Constants and configuration |
| `storage.py` | Data persistence |
| `effects.py` | Visual effects |
| `charts.py` | Data visualization |
| `components.py` | UI components |
| `styles.py` | CSS styling |

This structure makes it easier to update one part of the app without breaking the rest.

---

## 🌐 Deployment

This project can be deployed with **Streamlit Community Cloud**.

Basic deployment steps:

1. Push the project to GitHub.
2. Go to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select the branch `main`.
5. Set the main file path as:

```text
app.py
```

6. Deploy the app.

---

## 🎯 Learning Goals

This project was created as a learning exercise for practicing:

- Python basics
- Streamlit app development
- Working with CSV files
- Data visualization
- UI customization
- Git and GitHub workflow
- Project organization and clean code principles

---

## 🖤 Author

Created by **Olena Myroshnykova** as part of a Python / Streamlit learning project.

GitHub: [OlenaMyroshnykova](https://github.com/OlenaMyroshnykova)

---

## 📌 Future Improvements

Possible future improvements:

- Add user authentication
- Add a real database
- Add date and time for each record
- Add filters by name or mood
- Add export to Excel
- Add deployment link
- Improve responsive mobile layout
- Add unit tests

---

## 🦇 Preview

A dark gothic dashboard with team energy metrics, visual effects, and a mood history chart.

```text
🦇 Gothic Team Vibe Dashboard
🕯️ ¿Cómo late hoy el alma del equipo?
```

---

## 📄 License

This project is for educational purposes.
