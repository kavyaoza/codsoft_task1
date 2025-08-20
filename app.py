from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load movie data
movies = pd.read_csv('data/movies.csv')

# Prepare content-based features
movies['features'] = movies['genre'] + ' ' + movies['director'] + ' ' + movies['description']
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

@app.route('/')
def home():
    return render_template('index.html', movies=movies.to_dict('records'))

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_id = int(request.json['movieId'])
    method = request.json['method']
    
    # Get movie index
    idx = movies.index[movies['id'] == movie_id].tolist()[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5 similar
    
    # Get movie indices and similarity percentages
    recommendations = []
    for i, score in sim_scores:
        movie = movies.iloc[i].to_dict()
        movie['similarity'] = float(score * 100)  # Convert to percentage
        recommendations.append(movie)
    
    return jsonify(recommendations)

@app.route('/movie/<int:movie_id>')
def get_movie(movie_id):
    movie = movies[movies['id'] == movie_id].iloc[0].to_dict()
    return jsonify(movie)

if __name__ == '__main__':
    app.run(debug=True)