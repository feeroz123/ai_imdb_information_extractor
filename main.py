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
            # st.table(dataframe)
            st.dataframe(
                dataframe, 
                use_container_width=True,
                column_config={
                    "Title": st.column_config.TextColumn("Title", width="medium"),
                    "Plot": st.column_config.TextColumn("Plot", width="large"),
                    "Cast": st.column_config.TextColumn("Cast", width="large"),
                    "Genre": st.column_config.TextColumn("Genre", width="small"),
                    "Director": st.column_config.TextColumn("Director", width="medium"),
                    "Year": st.column_config.NumberColumn("Year", width="small"),
                    "Rating": st.column_config.NumberColumn("Rating", width="small"),
                    "Runtime (mins)": st.column_config.NumberColumn("Runtime (mins)", width="small"),
                    "Language": st.column_config.TextColumn("Language", width="small")
                }
            )
        else:
            st.error("Failed to extract data. Please check the URL and try again.")
    else:
        st.warning("Please enter a valid IMDB movie URL.")
