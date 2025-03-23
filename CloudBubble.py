#code was first from https://github.com/zaid-ahmed1/Hack-the-Bias-Web-App-Template/blob/main/app.py

import streamlit as st
import pandas as pd

#st.header('Display image using st.image')



#from chatgpt to change the background colour of the webpage



# Read the data
df = pd.read_csv('Book2.csv')

#image import
st.image('./media/header.jpg',caption = 'All your sites - in one place',width=550)
# Set page title
st.title('Cloud Bubble')

#audio file
audio_file = open('./media/dawnofchange.mp3','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/ogg')

st.image('./media/chocolate.jpeg')

url = "https://www.sciencefocus.com/science/fun-facts"

st.markdown(f"[![Click here for a surprise](./media/Untitled96.jpg)]({url})", unsafe_allow_html=True)

#st.markdown(f'<a href="{url}" target="_blank"><img src="./media/Untitled96.jpg" alt="Click here for a surprise" width="300"></a>', unsafe_allow_html=True)

# Make the image clickable by wrapping it with a markdown link
#st.markdown(f'<a href="{url}" target="_blank"><img src="./media/Untitled96.jpg" alt="Click here for a surprise" width="300"></a>', unsafe_allow_html=True)


# Create sidebar filters
st.sidebar.header('What would you like to learn about today?')


# Genre filter
all_genres = [genre.strip() for genres in df['Genre'].str.split(',') for genre in genres]
unique_genres = sorted(list(set(all_genres)))
selected_genre = st.sidebar.selectbox('Select Topic', unique_genres)

# Director filter
all_directors = [director.strip() for directors in df['Director'].str.split(',') for director in directors]
unique_directors = sorted(list(set(all_directors)))
selected_director = st.sidebar.selectbox('Select Type', ['All'] + unique_directors)



# Rating filter
rating_range = st.sidebar.slider(
    'Select Difficulty level: ',
    min_value=float(df['IMDB_Rating'].min()),
    max_value=float(df['IMDB_Rating'].max()),
    value=(float(df['IMDB_Rating'].min()), float(df['IMDB_Rating'].max()))
)

# Filter the dataframe
filtered_df = df[
    (df['IMDB_Rating'].between(rating_range[0], rating_range[1])) &
    (df['Genre'].str.contains(selected_genre, case=False)) &
    (df['Director'].str.contains(selected_director, case=False) if selected_director != 'All' else True)
]

# Display results
st.subheader(f'Found {len(filtered_df)} resources matching your criteria')

# Show movies in a simpler format
for idx, row in filtered_df.iterrows():
    st.markdown("---")  # Add a separator between movies
    
    # Movie title and rating in a header
    st.header(f"{row['Series_Title']} ({row['Released_Year']})")
    st.markdown(f"⭐ **Difficulty level:** {row['IMDB_Rating']}")
    
    # Two columns: Image and Basic Info
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(row['Poster_Link'], width=200)
    
    with col2:
        st.markdown(f"📚 **Topic:** {row['Genre']}")
        st.markdown(f"📖 **Type:** {row['Director']}")
        st.markdown(f"🔗 **Link:** {row['Runtime']}")


