from flask import Blueprint, request, jsonify
from app.models import Expense
from app.utils.database import db

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/expenses', methods=['POST'])
def create_expense():
    data = request.get_json()
    new_expense = Expense(
        name=data['name'],
        amount=data['amount'],
        date=data['date'],
        category=data['category']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense created successfully'}), 201

@expenses_bp.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    expenses_list = [{'id': exp.id, 'name': exp.name, 'amount': exp.amount, 'date': exp.date, 'category': exp.category} for exp in expenses]
    return jsonify(expenses_list), 200

@expenses_bp.route('/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    expense = Expense.query.get_or_404(id)
    expense_data = {'id': expense.id, 'name': expense.name, 'amount': expense.amount, 'date': expense.date, 'category': expense.category}
    return jsonify(expense_data), 200

@expenses_bp.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    data = request.get_json()
    expense = Expense.query.get_or_404(id)
    expense.name = data['name']
    expense.amount = data['amount']
    expense.date = data['date']
    expense.category = data['category']
    db.session.commit()
    return jsonify({'message': 'Expense updated successfully'}), 200

@expenses_bp.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted successfully'}), 200