from flask import Flask, render_template, request, jsonify
import requests
import openai

app = Flask(__name__)

# Constants
API_KEY_GPT = 'sk-proj-d9qB0TG9mcfGkXXE7eFKT3BlbkFJKUIN3AwxO3FrvuhinjBP'
API_KEY_NEWS = 'hdy1tiwQG2ct7YeB7RFZx06hywk9seeFEpIFK01B'
BASE_URL = 'https://api.thenewsapi.com/v1/news/top'
COMPANIES = ["Apple Inc.", "LinkedIn", "Tesla"]
TAGS = ["CXO News", "Cybersecurity", "AI", "Finance", "Tech"]

openai.api_key = API_KEY_GPT

def fetch_news_for_company(company):
    params = {
        'api_token': API_KEY_NEWS,
        'search': company,
        'language': 'en',
        'limit': 10,
        'categories': 'general'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json().get('data', []) if response.status_code == 200 else []

def fetch_all_news():
    all_news = []
    for company in COMPANIES:
        all_news.extend(fetch_news_for_company(company))
    return all_news

def tag_and_categorize_article(description, url):
    if not description:
        description = f"Please check the URL for content: {url}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a highly trained AI capable of understanding complex topics and providing insights."},
            {"role": "user", "content": f"Please tag the following news article description with one of these categories and only give one tag: CXO News, Cybersecurity, AI, Finance, Tech.\nDescription: {description}"}
        ]
    )
    tag = response.choices[0].message['content'].strip()
    tag = tag.replace('Category: ', '').replace('This news article falls under the category of ', '').replace('This news article description would be best tagged as "', '').replace('"', '')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a highly trained AI capable of understanding complex topics and providing insights."},
            {"role": "user", "content": f"Please categorize the following news article description as either 'Business' or 'Consumer' in one word.\nDescription: {description}"}
        ]
    )
    category = response.choices[0].message['content'].strip()
    category = category.replace('Category: ', '').replace('This news article falls under the category of ', '').replace('This news article description would be best categorized as "', '').replace('"', '')

    return tag, category

@app.route('/')
def index():
    return render_template('index.html', tags=TAGS)

@app.route('/fetch_news', methods=['POST'])
def fetch_news_route():
    data = request.get_json()
    tag_filter = data.get('tag')

    print(f"Received request for tag: {tag_filter}")

    news_articles = fetch_all_news()
    filtered_articles = []

    for article in news_articles:
        title = article.get('title')
        description = article.get('description', '')
        url = article.get('url')
        image_url = article.get('image_url')
        tag, category = tag_and_categorize_article(description, url)

        if tag == tag_filter and category.lower() == 'business':  # Filter to only show Business category
            filtered_articles.append({
                'title': title,
                'description': description,
                'url': url,
                'image_url': image_url,
                'category': category
            })

    print(f"Filtered articles: {filtered_articles}")
    return jsonify(filtered_articles)

if __name__ == '__main__':
    app.run(debug=True)
