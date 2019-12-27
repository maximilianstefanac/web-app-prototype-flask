from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from flask_json import FlaskJSON, json_response
from shapely_geojson import dumps, Feature

POSTGRES = {
    'user': 'geoapp',
    'pw': 'Welcome1!',
    'db': 'geoapp',
    'host': 'postgis',
    'port': '5432'
}



#db = SQLAlchemy()

app = Flask(__name__)

#app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
FlaskJSON(app)

class Tree(db.Model):
    tree_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(Geometry("POINT"))


@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/trees')
def trees():
    trees_simplified_array = []
    trees = Tree.query.all()

    for tree in trees:
        trees_simplified_array.append({
            'tree_id' : tree.tree_id,
            'position' : dumps(Feature(to_shape(tree.position)))
        })
    return json_response(trees=trees_simplified_array)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0',port=8080)