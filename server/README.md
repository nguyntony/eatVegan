# eatVegan Recipe API

## Usage

API will host list of curated recipes from various vegan blogs. API is built with Flask, SQLAlchemy, and Flask-Mashmallow for serialization.

All responses will have the form

```json
{
	"data": "Mixed type holding the content of the response",
	"message": "Description of request status"
}
```

To access API:

`cd server`

Create pip environment:
`pip3 install pipenv`

Install pip dependcies:
`pipenv install`

## Testing API with Postman

### List all recipes

**Method**

`GET /recipe`

**Response**

- `200 OK` on success

```json
[
	{
		"id": "recipe identifier",
		"title": "recipe title",
		"description": "recipe description from author",
		"image": ["url image 1", "url image 2", "url image 3"],
		"time": "total cooking time (prep + cook times combined)",
		"servings": "total recipe yield",
		"course": "meal category",
		"cuisine": "particular country, region, or style of cooking",
		"ingredients": ["ingredient 1", "ingredient 2", "ingredient 3"],
		"author": "Blog author",
		"source": "recipe url"
	},
	{
		"id": "1",
		"title": "Crispy Falafel",
		"description": "These vegan and gluten-free falafels are golden brown and crispy on the outside, while tender, delicious and full of fresh herbs on the inside! They are baked instead of fried and are a fantastic protein-rich option to keep on hand for future salads and pita sandwhiches!",
		"image": [
			"https://cookieandkate.com/images/2018/05/falafel-salad-550x822.jpg",
			"https://cookieandkate.com/images/2018/05/falafel-ingredients-550x378.jpg",
			"https://cookieandkate.com/images/2012/05/baked-falafel-out-of-oven-550x399.jpg"
		],
		"total_time": "50 minutes",
		"servings": "12 falafels",
		"course": "appetizer",
		"cuisine": "Middle Eastern",
		"ingredients": [
			"extra-virgin olive oil",
			"chickpeas",
			"red onion",
			"parsley",
			"cilantro",
			"garlic",
			"sea salt",
			"cumin",
			"cinnamon",
			"black pepper"
		],
		"author": "Kathryne Taylor",
		"source": "https://cookieandkate.com/crispy-falafel-recipe/"
	}
]
```

### Adding a new recipe

**Method**

`POST /recipe`

**Arguments**

- `"id": string` a globally unique identifier for recipe
- `"title": string`
- `"description": string`
- `"image": string` url image or array if multiple images
- `"total_time": string` total prep + cook minutes
- `"servings": integer`
- `"course": string`
- `"cuisine": string`
- `"ingredients": string` format as array
- `"author": string`
- `"source": string`

If a recipe with the given identifier already exists, response will be an error

- `400 Bad Request`

## Look up recipe

**Method**

`GET /recipe/<id>`

**Response**

- `404 Not Found` if the recipe does not exist
- `200 OK` on success

```json
{
	"id": "recipe identifier",
	"title": "recipe title",
	"description": "recipe description from author",
	"image": ["url image 1", "url image 2", "url image 3"],
	"total_time": "total cooking time (prep + cook times combined)",
	"servings": "total recipe yield",
	"course": "meal category",
	"cuisine": "particular country, region, or style of cooking",
	"ingredients": ["ingredient 1", "ingredient 2", "ingredient 3"],
	"author": "Blog author",
	"source": "recipe url"
}
```

## Delete a recipe

**Method**

`DELETE /recipe/<id>`

**Response**

- `404 Not Found` if the recipe does not exist
- `200 OK` deletion was successful

## Updating a recipe

**Method**

`PUT /recipe<id>`

**Response**

- `200 OK` Update was successful
