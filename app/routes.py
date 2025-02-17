from flask import Blueprint, request, jsonify
from app import db
from app.models import Order, OrderItem, Customer, MenuItem

# Create a Blueprint instead of a Flask app instance
main = Blueprint('main', __name__)

# Customer Endpoints
@main.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'first_name': c.first_name, 'last_name': c.last_name, 'email': c.email} for c in customers])

@main.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer = Customer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone_number=data.get('phone_number')
    )
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer created', 'id': customer.id})

# Order Endpoints
@main.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': o.id, 'customer_id': o.customer_id, 'order_date': o.order_date, 'total_amount': o.total_amount} for o in orders])

@main.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(
        customer_id=data['customer_id'],
        total_amount=data['total_amount']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order created', 'id': order.id})

# Menu Endpoints
@main.route('/menu', methods=['GET'])
def get_menu_items():
    menu_items = MenuItem.query.all()
    return jsonify([{'item_id': m.item_id, 'name': m.name, 'price': m.price} for m in menu_items])

@main.route('/menu', methods=['POST'])
def create_menu_item():
    data = request.json
    menu_item = MenuItem(
        name=data['name'],
        description=data.get('description'),
        category=data.get('category'),
        price=data['price'],
        size_options=data.get('size_options'),
        ingredients=data.get('ingredients'),
        image_url=data.get('image_url'),
        availability_status=data.get('availability_status', True),
        calories=data.get('calories'),
        preparation_time=data.get('preparation_time')
    )
    db.session.add(menu_item)
    db.session.commit()
    return jsonify({'message': 'Menu item created', 'item_id': menu_item.item_id})
