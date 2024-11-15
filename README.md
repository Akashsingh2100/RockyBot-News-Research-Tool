# RockyBot: News Research Tool 🤖📈

RockyBot is a powerful AI-powered news research tool that leverages OpenAI's language models to analyze financial articles and provide intelligent insights. Built with Streamlit and LangChain, it enables users to extract, process, and query information from multiple news sources simultaneously.

![RockyBot Interface](rockybot.jpg)

## 🌟 Key Features

- **Intelligent Article Processing**: Automatically extracts and processes content from multiple URLs
- **Advanced Natural Language Understanding**: Powered by OpenAI's GPT models
- **Fast Similarity Search**: Utilizes FAISS (Facebook AI Similarity Search) for efficient information retrieval
- **Source Attribution**: Provides source URLs for all information retrieved
- **User-Friendly Interface**: Built with Streamlit for seamless interaction

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: 
  - OpenAI GPT Models
  - LangChain Framework
  - FAISS Vector Database
- **Data Processing**: 
  - UnstructuredURL Loader
  - RecursiveCharacterTextSplitter
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Sufficient storage for FAISS indexes
- Internet connection for URL processing

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone using link 
   cd rockybot
   ```

2. **Create and Activate Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure OpenAI API Key**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## 🚀 Usage

1. **Start the Application**
   ```bash
   streamlit run main.py
   ```

2. **Process Articles**
   - Enter up to 3 news article URLs in the sidebar
   - Click "Process URLs" to begin analysis
   - Wait for the processing indicators to complete

3. **Query Information**
   - Type your question in the main input field
   - Get AI-generated answers with source attribution
   - View related sources for fact-checking

## 📁 Project Structure

```
rockybot/
│
├── main.py                 # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .env                   # Environment variables
├── faiss_store_openai.pkl # FAISS index storage
├── README.md              # Project documentation
└── rockybot.jpg          # Project screenshot
```

## 📦 Dependencies

```text
streamlit>=1.24.0
langchain>=0.0.200
openai>=0.27.8
faiss-cpu>=1.7.4
python-dotenv>=1.0.0
beautifulsoup4>=4.12.2
requests>=2.31.0
```

## 🔧 Configuration

The application can be configured through the following environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- Additional configuration can be modified in `main.py`

## 🚧 Error Handling

RockyBot includes robust error handling for:
- Invalid URLs
- Failed content extraction
- API failures
- Empty or invalid content
- FAISS indexing issues

## 🔍 Advanced Features

- **Intelligent Text Splitting**: Optimized chunk sizes for better context preservation
- **Embedding Management**: Efficient storage and retrieval of document embeddings
- **Source Tracking**: Maintains links between answers and source documents
- **Memory Management**: Efficient handling of large documents through FAISS


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- OpenAI for providing the GPT models
- Facebook Research for FAISS
- LangChain community for the framework
- Streamlit team for the awesome web framework

## 📧 Contact

For questions and feedback:
- Create an issue in this repository
- Contact: akashsingh80029@gmail.com

---
Built with ❤️ by [Akash Singh]