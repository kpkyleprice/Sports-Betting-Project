from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema, Bet, bet_schema, bets_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/contacts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    name = request.json['name']
    email = request.json['email']
    age = request.json['age']
    sport = request.json['sport']
    team = request.json['team']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    contact = Contact(name, email, age, sport, team, user_token = user_token )

    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route('/contacts', methods = ['GET'])
@token_required
def get_contact(current_user_token):
    a_user = current_user_token.token
    contacts = Contact.query.filter_by(user_token = a_user).all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)

@api.route('/contacts/<id>', methods = ['GET'])
@token_required
def get_contact_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        contact = Contact.query.get(id)
        response = contact_schema.dump(contact)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

@api.route('/contacts/<id>', methods = ['POST','PUT'])
@token_required
def update_contact(current_user_token,id):
    contact = Contact.query.get(id) 
    contact.name = request.json['name']
    contact.email = request.json['email']
    contact.age = request.json['age']
    contact.sport = request.json['sport']
    contact.team = request.json['team']
    contact.user_token = current_user_token.token

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)


@api.route('/contacts/<id>', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

    # 
@api.route('/bets', methods=['POST'])
@token_required
def create_bet(current_user_token):
    id = request.json['ID']
    Amount = request.json['Amount']
    Team = request.json['Team']
    Odds = request.json['Odds']
    user = User.query.get(current_user_token.id)

    bet = Bet(ID=ID, Bet=Bet, Team=Team, Odds=Odds, user_id=user.id)

    db.session.add(bet)
    db.session.commit()

    response = bet_schema.dump(bet)
    return jsonify(response)

@api.route('/bets', methods=['GET'])
@token_required
def get_bets(current_user_token):
    user_id = current_user_token.id
    bets = Bet.query.filter_by(user_id=user_id).all()
    response = bets_schema.dump(bets)
    return jsonify(response)


@api.route('/bets/<id>', methods=['GET'])
@token_required
def get_bet(current_user_token, id):
    wager = current_user_token.token
    if wager == current_user_token.token:
        bet = Bet.query.get(id)
        response = bet_schema.dump(bet)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"})


@api.route('/bets/<id>', methods=['POST', 'PUT'])
@token_required
def update_bet(current_user_token, id):
    bet = Bet.query.get(id)
    bet.ID = request.json['ID']
    bet.Amount = request.json['Amount']
    bet.Team = request.json['Team']
    bet.Odds = request.json['Odds']
    bet.user_id = current_user_token.id

    db.session.commit()
    response = bet_schema.dump(bet)
    return jsonify(response)


@api.route('/bets/<id>', methods=['DELETE'])
@token_required
def delete_bet(current_user_token, id):
    bet = Bet.query.get(id)
    db.session.delete(bet)
    db.session.commit()
    response = bet_schema.dump(bet)
    return jsonify(response)