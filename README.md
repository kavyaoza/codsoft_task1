# 🎬 CODSOFT Internship -- Task: Movie Recommendation System

This project is created as part of my **CODSOFT AI/ML Internship**.\
It is a **Content-Based Movie Recommendation System** built using
**Flask, Pandas, and Scikit-learn**.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 Select a movie from dropdown
-   🎥 View detailed information:
    -   Title
    -   Genre
    -   Director
    -   Rating
    -   Description
-   🤖 Get **Top-5 recommended movies** based on similarity
-   ⚡ Clean and responsive UI

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend:** Flask (Python)\
-   **Frontend:** HTML, CSS, JavaScript\
-   **Libraries:** Pandas, Scikit-learn, Scipy\
-   **Dataset:** `movies.csv` & `ratings.csv`

------------------------------------------------------------------------

## 📂 Project Structure

    Task1_MovieRecommendation/
    │
    ├── app.py               # Flask backend
    ├── requirement.txt      # Dependencies
    ├── static/
    │   └── style.css        # CSS styling
    ├── templates/
    │   └── index.html       # Frontend
    └── data/
        ├── movies.csv       # Movie dataset
        └── ratings.csv      # Ratings dataset

------------------------------------------------------------------------

## ⚙️ Installation & Setup

1.  Clone this repository

    ``` bash
    git clone https://github.com/yourusername/codsoft_taskno.git
    cd codsoft_taskno/Task1_MovieRecommendation
    ```

2.  Create a virtual environment (optional)

    ``` bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3.  Install dependencies

    ``` bash
    pip install -r requirement.txt
    ```

4.  Run the Flask app

    ``` bash
    python app.py
    ```

5.  Open in browser

        http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📊 How It Works

1.  Load movies dataset (`movies.csv`)\
2.  Create a **feature vector** combining `genre`, `director`, and
    `description`\
3.  Apply **TF-IDF Vectorization** → convert text into numbers\
4.  Compute **cosine similarity** between movies\
5.  Recommend the **Top-5 most similar movies**

------------------------------------------------------------------------

## ✅ Internship Requirement

-   Task completed as part of **CODSOFT AI/ML Internship**\
-   Maintained proper **GitHub repository (codsoft_taskno)**\
-   To be shared on **LinkedIn** tagging `@codsoft`

------------------------------------------------------------------------

## 👨‍💻 Author

-   Name: *Kavya Oza*\
-   Email: *kavyaoza54@gmail.com*\
-   GitHub: [yourusername](https://github.com/yourusername)\
-   LinkedIn: [your-linkedin-profile](https://linkedin.com/in/your-link)

------------------------------------------------------------------------
