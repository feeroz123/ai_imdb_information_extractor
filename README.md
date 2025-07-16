# IMDB Movie Data Extractor

A sample Streamlit web application that extracts movie information from IMDB pages using web scraping and AI-powered data extraction.

## Features

- Extract comprehensive movie information from IMDB URLs
- Clean and structured data presentation
- AI-powered data parsing using Groq's LLaMA model
- User-friendly web interface built with Streamlit

## Extracted Information

The application extracts the following movie details:

- **Title**: Movie title
- **Year**: Release year
- **Rating**: IMDB rating
- **Genre**: Movie genre(s)
- **Director**: Director name
- **Cast**: List of main actors
- **Plot**: Movie plot summary
- **Runtime**: Movie duration in minutes
- **Language**: Original language

## Prerequisites

- Python 3.7 or higher
- Groq API key (free tier available)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/feeroz123/ai_imdb_information_extractor.git
cd ai_imdb_information_extractor
```

2. Install required dependencies:

```bash
pip install streamlit pandas langchain-groq requests beautifulsoup4 python-dotenv
```

3. Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the Streamlit application:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter a valid IMDB movie URL in the text area (e.g., `https://www.imdb.com/title/tt31216548/`)

4. Click "Extract Data" to retrieve and display the movie information

## Example

Try with this IMDB URL: `https://www.imdb.com/title/tt31216548/?ref_=nv_srb_trend_title_4`

## Project Structure

```text
imdb_information_extractor/
├── main.py              # Streamlit web application
├── data_extractor.py    # Core data extraction logic
├── README.md           # Project documentation
└── __pycache__/        # Python cache files
```

## How It Works

1. **Web Scraping**: The application uses BeautifulSoup to scrape content from IMDB movie pages
2. **Data Processing**: Raw HTML content is cleaned and processed
3. **AI Extraction**: Groq's LLaMA model analyzes the content and extracts structured information
4. **Data Display**: Extracted information is presented in a clean table format using Streamlit

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and display
- **LangChain**: AI framework for LLM integration
- **Groq**: AI inference platform
- **BeautifulSoup**: HTML parsing and web scraping
- **Requests**: HTTP library for web requests

## API Key Setup

To get your free Groq API key:

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file

## Limitations

- The application is designed for IMDB movie pages only
- Content extraction is limited to 10,000 characters to avoid token limits
- Requires a stable internet connection for web scraping and API calls

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## License

This project is open source and available under the MIT License.

## Troubleshooting

- **"Failed to extract data"**: Check if the IMDB URL is valid and accessible
- **API errors**: Verify your Groq API key is correctly set in the `.env` file
- **Installation issues**: Ensure all dependencies are properly installed using the provided pip command