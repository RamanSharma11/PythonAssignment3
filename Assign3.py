from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    # Retrieve News API key from environment variable
    # api_key = os.environ.get('NEWS_API_KEY')

    api_key = "eb2e159326544f0497fa68bff4e1afff"

    # Get the 'country' parameter from the request
    country = request.args.get('country', 'us')

    # News API base URL for top headlines
    base_url = 'https://newsapi.org/v2/top-headlines'

    # Parameters for the API request
    params = {'apiKey': api_key, 'country': country}

    try:
        # Make a request to the News API
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Extract relevant information from the response
            articles = [{'title': article['title'], 'url': article['url']} for article in data.get('articles', [])]
            return jsonify({'articles': articles})
        else:
            # Return an error message if the response is not successful
            return jsonify({'error': data}), response.status_code

    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)