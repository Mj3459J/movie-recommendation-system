# Movie Recommendation System
This project is a **Content-Based Movie Recommendation System** that recommends movies similar to a user-selected movie.  
The system analyzes movie metadata and suggests the **top 5 most relevant movies** using **cosine similarity**.

The application is built using **Streamlit** and fetches movie posters dynamically using the **TMDB API**, making the recommendations more interactive and user-friendly.

---

## Dataset Used
- **tmdb_5000_movies.csv**
- **tmdb_5000_credits.csv**

These datasets contain information such as:
- Movie titles
- Overview
- Genres
- Keywords
- Cast
- Crew

---

## Technologies & Tools Used
- Python  
- Pandas & NumPy  
- Scikit-learn  
- NLTK (for stemming)  
- Streamlit  
- TMDB API  
- Jupyter Notebook  

---

## Project Workflow
1. **Data Loading**
   - Loaded movie and credits datasets
   - Merged both datasets based on movie ID

2. **Data Preprocessing**
   - Selected important features (overview, genres, keywords, cast, crew)
   - Cleaned and transformed text data
   - Converted text to lowercase
   - Applied **stemming** to reduce words to their root form

3. **Feature Engineering**
   - Used **Bag of Words (BOW)** to convert text into numerical vectors
   - Created a feature vector for each movie

4. **Similarity Calculation**
   - Used **Cosine Similarity** to measure similarity between movies
   - Generated a similarity matrix for recommendations

5. **Recommendation Logic**
   - Given a movie name, the system:
     - Finds similar movies
     - Returns the **top 5 recommended movies**

6. **Web Application**
   - Built a simple UI using **Streamlit**
   - Integrated **TMDB API** to fetch movie posters
   - Displays recommended movies along with their posters

---

## Features
- Content-based movie recommendations
- Top 5 similar movies for any selected movie
- Real-time movie poster fetching using TMDB API
- Simple and interactive Streamlit UI

---

## Algorithms Used
- Bag of Words (BOW)
- Cosine Similarity
- Stemming (NLP preprocessing)

---

## How to Run the Project
1. Clone the repository
   ```bash
   git clone <your-repository-link>
