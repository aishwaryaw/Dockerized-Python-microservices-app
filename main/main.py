from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy import UniqueConstraint
from flask_cors import CORS
import requests
from producer import publish


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@postgres/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id : int
    title : str
    image : str
    likes: int

    id = db.Column(db.Integer, primary_key= True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    likes = db.Column(db.Integer, default=0)

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    db.UniqueConstraint(user_id,product_id)


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/product/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://backend:8000/api/user')
    json = req.json()
    print(json)
    try:
        productuser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productuser)
        product = Product.query.get(id)
        product.likes = product.likes + 1
        db.session.commit()
        publish('Product liked',id)
        
    except:
        abort(400,'You already liked this product')
        
    return jsonify({
            'message':'success'
    })
   
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

