from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file. The ,env file contains the GROQ_API_KEY variable.
# Make sure to have a .env file with the GROQ_API_KEY variable
load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

def scrape_imdb_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the main content text from the page
        page_text = soup.get_text(separator=' ', strip=True)
        
        # Limit the text length to avoid token limits
        if len(page_text) > 10000:
            page_text = page_text[:10000]
            
        return page_text
    except Exception as e:
        print(f"Error scraping IMDB page: {e}")
        return None

def extract_data(imdb_movie_url):
    # First, scrape the actual content from the IMDB page
    page_content = scrape_imdb_page(imdb_movie_url)
    if not page_content:
        return None
        
    prompt = '''
    You are an expert data extractor. Your task is to extract specific information from the given IMDB movie page content.
    The content from an IMDB movie page will be provided below, and you need to extract the following information:
    - Title
    - Year
    - Rating
    - Genre
    - Director
    - Cast (as a list of actor names)
    - Plot
    - Runtime
    - Language
    
    Extract only the information specified above, and format it as a JSON object containing the keys:
    "title", "year", "rating", "genre", "director", "cast", "plot", "runtime", "language".
    
    For the cast, return it as a list of strings (actor names).
    Do not extract any other information or provide any additional commentary or preamble.
    
    IMDB Movie Page Content: {input}
    '''

    prompt_template = PromptTemplate.from_template(prompt)
    global llm
    chain = prompt_template | llm
    output_parser = JsonOutputParser()

    try:
        response = chain.invoke({"input": page_content})
        parsed_response = output_parser.parse(response.content)
        return parsed_response
    except OutputParserException as e:
        print(f"Error parsing output: {e}")
        return None