from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os 

# Init app 
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db 
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

# Recipe Class/Model 
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500))
    image = db.Column(db.String)
    time = db.Column(db.Integer)
    servings = db.Column(db.Integer)
    course = db.Column(db.String)
    cuisine = db.Column(db.String)
    ingredients = db.Column(db.String)
    author = db.Column(db.String)
    source = db.Column(db.String)

    def __init__(self, title, description, image, time, servings, course, cuisine, ingredients, author, source):
        self.title = title 
        self.description = description
        self.image = image
        self.time = time 
        self.servings = servings
        self.course = course 
        self.cuisine = cuisine 
        self.ingredients = ingredients
        self.author = author 
        self.source = source 

# Recipe Schema 
class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'image', 'time', 'servings', 'course', 'cuisine', 'ingredients','author', 'source')

# Init schema 
recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

# Create a Recipe 
@app.route('/recipe', methods=['POST'])
def add_recipe():
    title = request.json['title']
    description = request.json['description']
    image = request.json['image']
    time = request.json['time']
    servings = request.json['servings']
    course = request.json['course']
    cuisine = request.json['cuisine']
    ingredients = request.json['ingredients']
    author = request.json['author']
    source = request.json['source']

    new_recipe = Recipe(title, description, image, time, servings, course, cuisine, ingredients, author, source)

    db.session.add(new_recipe)
    db.session.commit()

    return recipe_schema.jsonify(new_recipe)

# Get All Recipes 
@app.route('/recipe', methods=['GET'])
def get_recipes():
    all_recipes = Recipe.query.all()
    result = recipes_schema.dump(all_recipes)
    return jsonify(result)

# Get Single Recipe 
@app.route('/recipe/<id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return recipe_schema.jsonify(recipe)

# Update a Recipe 
@app.route('/recipe/<id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get(id)

    title = request.json['title']
    description = request.json['description']
    image = request.json['image']
    time = request.json['time']
    servings = request.json['servings']
    course = request.json['course']
    cuisine = request.json['cuisine']
    ingredients = request.json['ingredients']
    author = request.json['author']
    source = request.json['source']

    recipe.title = title 
    recipe.description = description
    recipe.image = image
    recipe.time = time 
    recipe.servings = servings
    recipe.course = course 
    recipe.cuisine = cuisine 
    recipe.ingredients = ingredients
    recipe.author = author 
    recipe.source = source 

    db.session.commit()

    return recipe_schema.jsonify(recipe)

# Delete Recipe 
@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    
    return recipe_schema.jsonify(recipe)

# Run Server 
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)