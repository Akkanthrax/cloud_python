from flask import Blueprint, request, jsonify
from app.models import db, Objective

objectives_bp = Blueprint('objectives', __name__)

@objectives_bp.route('/objectives', methods=['GET'])
def get_objectives():
    objectives = Objective.query.all()
    return jsonify([objective.to_dict() for objective in objectives])

@objectives_bp.route('/objectives', methods=['POST'])
def create_objective():
    data = request.get_json()
    new_objective = Objective(
        name=data['name'],
        description=data['description'],
        target_amount=data['target_amount'],
        current_amount=data['current_amount']
    )
    db.session.add(new_objective)
    db.session.commit()
    return jsonify(new_objective.to_dict()), 201

@objectives_bp.route('/objectives/<int:id>', methods=['PUT'])
def update_objective(id):
    data = request.get_json()
    objective = Objective.query.get_or_404(id)
    objective.name = data['name']
    objective.description = data['description']
    objective.target_amount = data['target_amount']
    objective.current_amount = data['current_amount']
    db.session.commit()
    return jsonify(objective.to_dict())

@objectives_bp.route('/objectives/<int:id>', methods=['DELETE'])
def delete_objective(id):
    objective = Objective.query.get_or_404(id)
    db.session.delete(objective)
    db.session.commit()
    return '', 204