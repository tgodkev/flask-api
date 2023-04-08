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
    
    # Updated CSS selector
    recipe_cards = soup.select('a.comp.card--image-top.mntl-card-list-items.mntl-document-card.mntl-card.card.card--no-image')

    recipes = []
    for card in recipe_cards:
        link = card['href']
        title_element = card.find('span', class_='card__titleText')

        if title_element and link:
            title = title_element.text.strip()
            recipes.append({'title': title, 'link': link})
    
    return recipes




@app.route('/api/recipes', methods=['GET'])
def get_recipe_list():
    recipes = get_recipes()
    return jsonify({"message": "Recipes fetched successfully", "recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)


