# Company News Curation and Tagging Algorithm

## Overview
This repository contains the implementation of a sophisticated algorithm designed to curate and tag real-time news articles for business purposes. The algorithm utilizes two main techniques:
- **Word2Vec**: This method involves a machine learning model that leverages word embeddings to analyze textual data.
- **Pretrained Large Language Model (LLM)**: This approach uses a pre-trained model to enhance the accuracy and relevance of tagging and categorization of news articles.

Additionally, a Flask-based web application is included, which serves as a user interface for the real-time curation and tagging system.

## Repository Structure
- **BusinessCase.ipynb**: Contains the detailed implementation of the Word2Vec and Pretrained LLM techniques used for news tagging and categorization.
- **newsapp/**: Directory containing the Flask web application files for the user interface.

## User Interface
The Flask web application provides a dynamic interface for users to interact with the system. Features include:
- **Tag Selection**: Users can filter news by selecting tags such as CXO News, Cybersecurity, AI, Finance, and Tech.
- **Business Category Focus**: Automatically filters out non-business news, ensuring only business-relevant articles are shown.

### UI Screenshot
![UI Screenshot](https://github.com/komal-akhlaq/Company-News-Curation-and-Tagging-Algorithm/blob/main/UI.PNG)  <!-- Ensure the link points to an actual image in your repository -->

## Installation and Setup
Follow these steps to get the application running on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/komal-akhlaq/Company-News-Curation-and-Tagging-Algorithm.git

2. **Install Dependencies**:  
Install the required Python libraries by running:
  
   ```bash
   pip install -r requirements.txt

3. **Run the Flask App**:  
Start the Flask application with the following command:
   ```bash
   python app.py
