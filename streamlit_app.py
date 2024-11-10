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
        book_info = final_ratings[final_ratings['title'] == name]
        url = book_info['img_url'].values[0]  # Fetching the first match for the poster URL
        poster_url.append(url)

    return poster_url

# Function to recommend books based on the selected book
def recommend_books(books_name, genre=None, min_rating=None):
    book_list = []
    
    # Filter the book list based on genre and rating
    filtered_books = books_name
    if genre:
        filtered_books = [book for book in books_name if book in final_ratings['title'].values and final_ratings[final_ratings['title'] == book]['genre'].values[0] in genre]
    if min_rating:
        filtered_books = [book for book in filtered_books if book in final_ratings['title'].values and final_ratings[final_ratings['title'] == book]['rating'].values[0] >= min_rating]
    
    # Finding the index of the selected book in the pivot table
    book_id = np.where(book_pivot.index == books_name)[0][0]

    # Finding distances and indices of similar books using KNN model
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    # Fetch posters for the recommended books
    poster_url = fetch_poster(suggestions[0])

    for i in range(len(suggestions[0])):
        book = book_pivot.index[suggestions[0][i]]  # Fetching the book name
        book_list.append(book)

    return book_list, poster_url

# Select a book from the dropdown
selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    books_name
)

# Recommend books when a button is clicked
if st.button('Show Recommendations'):
    if selected_books:
        st.write(f"Books similar to '{selected_books}':")

        # Get the recommended books and posters
        recommended_books, posters = recommend_books(selected_books, genre=genres, min_rating=ratings)
        
        # Display the recommended books and their posters
        cols = st.columns(5)
        for i in range(1, len(recommended_books)):
            with cols[i-1]:
                st.text(recommended_books[i])
                st.image(posters[i])

# Feedback form
st.subheader("Give Feedback")
feedback = st.text_area("How can we improve?")
if st.button("Submit Feedback"):
    # Save feedback to a log file or a database
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")
    st.success("Thank you for your feedback!")
