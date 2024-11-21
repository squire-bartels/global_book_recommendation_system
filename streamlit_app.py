import streamlit as st
import pickle
import numpy as np

# Add custom CSS styling for UI improvements
st.markdown("""
    <style>
    .main {
        background-color: #F5F5F5;
        padding: 10px;
        border-radius: 10px;
    }
    .title {
        font-size: 2rem;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description of the app
st.title("Global Book Recommendation System")
st.subheader("Find similar books based on your favorite reads!")

# Load the saved model and data
model = pickle.load(open('./data/artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('./data/artifacts/books_name.pkl', 'rb'))
final_ratings = pickle.load(open('./data/artifacts/final_ratings.pkl', 'rb'))
book_pivot = pickle.load(open('./data/artifacts/book_pivot.pkl', 'rb'))

# Function to fetch posters for the recommended books
def fetch_poster(suggestions):
    books_name_list = []
    poster_url = []
    for book_id in suggestions:
        # Find the book name for each suggestion
        books_name_list.append(book_pivot.index[book_id])
    
    # Find the poster URL for each book name
    for name in books_name_list:
        try:
            book_info = final_ratings[final_ratings['title'] == name]
            url = book_info['img_url'].values[0]  # Fetching the first match for the poster URL
            poster_url.append(url)
        except IndexError:
            poster_url.append('https://via.placeholder.com/150')  # Placeholder image if no poster found
    
    return poster_url

# Function to recommend books based on the selected book
def recommended_books(book_name, min_rating=None):
    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
    except IndexError:
        st.error(f"Book '{book_name}' not found in the database.")
        return [], []

    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    book_list = []
    include_book = True  # Initialize this variable

    for i in range(1, len(suggestions[0])):
        book = book_pivot.index[suggestions[0][i]]

        if min_rating:
            book_rating = final_ratings[final_ratings['title'] == book]['rating'].values
            include_book = len(book_rating) > 0 and book_rating[0] >= min_rating

        if include_book:
            book_list.append(book)

    poster_url = fetch_poster(suggestions[0][1:len(book_list)+1])

    return book_list, poster_url
