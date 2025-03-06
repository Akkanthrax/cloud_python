from flask import Blueprint, jsonify
from app.models import Expense, Objective
from app.utils.database import db

financial_overview_bp = Blueprint('financial_overview', __name__)

@financial_overview_bp.route('/financial_overview', methods=['GET'])
def financial_overview():
    total_expenses = db.session.query(db.func.sum(Expense.amount)).scalar() or 0
    total_objectives = db.session.query(db.func.sum(Objective.amount)).scalar() or 0

    overview = {
        'total_expenses': total_expenses,
        'total_objectives': total_objectives,
        'balance': total_objectives - total_expenses
    }

    return jsonify(overview)