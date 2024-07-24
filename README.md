## Summarize Me: A Streamlit Summarization App

Welcome to the Summarize Me app! This application uses advanced language models to provide concise summaries of YouTube videos, news articles, and PDF documents. It's designed to help you quickly grasp the essential information from various content sources.

### Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

### Project Overview

The Summarize Me app leverages the power of large language models to process and summarize content from different media formats. Whether it's a lengthy YouTube video, an extensive news article, or a detailed PDF document, this app provides clear and concise summaries to save your time and enhance your productivity.

### Features

- **YouTube Video Summarization:** Extracts and summarizes the transcript of YouTube videos.
- **News Article Summarization:** Summarizes the content of online news articles.
- **PDF Document Summarization:** Provides summaries of PDF documents by extracting and analyzing their text content.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/summarize-me.git
   cd summarize-me
   ```

2. **Install the Required Packages:**
   Ensure you have Python 3.7+ installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory of the project and add your HuggingFace API token:
   ```env
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
   ```

### Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the App:**
   - **YouTube Summarization:** Enter the YouTube video URL and get the summarized transcript.
   - **News Article Summarization:** Enter the URL of the news article to get a summary.
   - **PDF Summarization:** Upload your PDF files and click "Process" to get summaries.

### Technologies Used

- **Streamlit:** For creating the web application.
- **HuggingFace Transformers:** For leveraging large language models.
- **Python Libraries:** Including Pandas, NumPy, and others for data processing and manipulation.


### Contact

If you have any questions or feedback, please feel free to reach out.
Email - loviaeb@gmail.com
LinkedIn - https://www.linkedin.com/in/lovia-edassery/
