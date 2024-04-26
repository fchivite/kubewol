from flask import Blueprint, render_template, request, jsonify
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("dashboard.html")


@views.route('/add-wol', methods=['GET', 'POST'])
def add_wol():
    if request.method == 'POST':
        wol_data = json.loads(request.data)
        return jsonify({})
    
    return render_template("addwol.html")