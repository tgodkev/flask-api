from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

# need to run this in terminal for virtual environment
# source venv/bin/activate

app = Flask(__name__)

def get_recipes():
    url = 'https://www.allrecipes.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    recipe_cards = soup.select('span.card__title')
    recipes = [card.text.strip() for card in recipe_cards]
    
    return recipes




@app.route('/api/recipes', methods=['GET'])
def get_recipe_list():
    recipes = get_recipes()
    return jsonify({"message": "Recipes fetched successfully", "recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)


