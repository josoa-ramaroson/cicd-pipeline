from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Sample data
items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': f"An item with name '{name}' already exists."}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

# Default route
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Item Store API!',
        'endpoints': {
            'GET /items': 'Get a list of all items',
            'GET /item/<name>': 'Get a specific item by name',
            'POST /item/<name>': 'Create a new item with a given name and price (provided in the JSON body)',
            'PUT /item/<name>': 'Update an existing item or create it if it doesn\'t exist',
            'DELETE /item/<name>': 'Delete an item by name'
        }
    })

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True, port=2121)
