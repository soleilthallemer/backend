from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() 

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id}>'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.item_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # Store price at order time

    def __repr__(self):
        return f'<OrderItem {self.id}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)  # Required first name
    last_name = db.Column(db.String(50), nullable=False)   # Required last name
    email = db.Column(db.String(120), unique=True, nullable=False) # Required and unique email
    phone_number = db.Column(db.String(20))  # Optional phone number
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of account creation
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp of last update

    orders = db.relationship('Order', backref='customer', lazy=True) # Relationship to orders

    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'  
   

class MenuItem(db.Model): 
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(255))
    price = db.Column(db.Float)
    size_options = db.Column(db.String(255))
    ingredients = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    availability_status = db.Column(db.Boolean)
    calories = db.Column(db.Integer)
    preparation_time = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<MenuItem {self.name}>'

