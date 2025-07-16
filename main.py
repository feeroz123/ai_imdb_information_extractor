import streamlit as st
import pandas as pd
from data_extractor import extract_data

st.title("IMDB Movie Data Extractor")
imdb_url = st.text_area("Enter IMDB Movie URL")

if st.button("Extract Data"):
    if imdb_url:
        extracted_data = extract_data(imdb_url)
        if extracted_data:
            st.success("Data extracted successfully!")
            data = {
                   "Title": extracted_data["title"],
                   "Year": extracted_data["year"],
                   "Rating": extracted_data["rating"],
                   "Genre": extracted_data["genre"],
                   "Director": extracted_data["director"],
                   "Cast": ", ".join(extracted_data["cast"]) if isinstance(extracted_data["cast"], list) else extracted_data["cast"],
                    "Plot": extracted_data["plot"],
                    "Runtime (mins)": extracted_data["runtime"],
                    "Language": extracted_data["language"]
                }

            dataframe = pd.DataFrame(data, index=[0])
            st.table(dataframe)
        else:
            st.error("Failed to extract data. Please check the URL and try again.")
    else:
        st.warning("Please enter a valid IMDB movie URL.")
