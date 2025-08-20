# 🎬 Movie Recommendation System (Flask + Machine Learning)

A simple yet powerful **content-based Movie Recommendation System**
built using **Flask, Pandas, and Scikit-learn**.\
This project recommends movies similar to a user-selected movie based on
**genre, director, and description** using **TF-IDF vectorization** and
**cosine similarity**.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 Search and select movies from dropdown
-   🎥 View detailed movie information (title, genre, director, rating,
    description)
-   🤖 Get top-5 recommended movies similar to the selected one
-   ⚡ Clean and modern UI with responsive design
-   📊 Machine learning powered by **TF-IDF + Cosine Similarity**

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Frontend:** HTML, CSS, JavaScript\
-   **Backend:** Flask (Python)\
-   **Libraries:** Pandas, Scikit-learn, Scipy\
-   **Dataset:** `movies.csv` (movie metadata), `ratings.csv` (ratings
    data)

------------------------------------------------------------------------

## 📂 Project Structure

    movie-recommendation-flask/
    │
    ├── app.py               # Main Flask app
    ├── requirement.txt      # Python dependencies
    ├── static/
    │   └── style.css        # CSS styling
    ├── templates/
    │   └── index.html       # Frontend template
    ├── data/
    │   ├── movies.csv       # Movie dataset
    │   └── ratings.csv      # Ratings dataset

------------------------------------------------------------------------

## ⚙️ Installation & Setup

1.  **Clone the repository**

    ``` bash
    git clone https://github.com/yourusername/movie-recommendation-flask.git
    cd movie-recommendation-flask
    ```

2.  **Create a virtual environment (optional but recommended)**

    ``` bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3.  **Install dependencies**

    ``` bash
    pip install -r requirement.txt
    ```

4.  **Run the Flask app**

    ``` bash
    python app.py
    ```

5.  **Open in browser**

        http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📊 How It Works

1.  Load movies dataset (`movies.csv`).\
2.  Create a **feature vector** combining `genre`, `director`, and
    `description`.\
3.  Apply **TF-IDF Vectorization** to convert text into numerical
    features.\
4.  Compute **cosine similarity** between movies.\
5.  When a user selects a movie, return the **Top-5 most similar
    movies**.

------------------------------------------------------------------------

## 🖼️ Screenshots

### 🎥 Home Page

> Dropdown to select movies & button to fetch recommendations.

### 📊 Recommendations

> Displays selected movie details and recommended movies.

------------------------------------------------------------------------

## ✅ Requirements

-   Python 3.8+\
-   Flask\
-   Pandas\
-   Scikit-learn\
-   Scipy

(Already listed in `requirement.txt`)

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add **collaborative filtering** (user-based recommendations)
-   Include **movie posters & images**
-   Deploy to **Heroku / Render**
-   Add user login and personalized recommendations

------------------------------------------------------------------------

## 👨‍💻 Author

-   Developed by *\[Kavya Oza\]*\
-   ✉️ Contact: kavyaoza54@gmail.com\
-   🌐 Portfolio/GitHub: \[your-link-here\]
