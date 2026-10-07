from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/categories', methods=['GET'])
def get_categories():
    data = load_config()
    return jsonify(list(data.keys()))

@app.route('/api/add-link', methods=['POST'])
def add_link():
    data = load_config()
    req = request.json
    
    category = req.get('category', '').strip()
    if not category:
        return jsonify({"success": False, "error": "Category is required"}), 400
    if not category.endswith('/'):
        category += '/'
        
    filename = req.get('filename', '').strip()
    if not filename:
        return jsonify({"success": False, "error": "Filename is required"}), 400
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    url = req.get('url', '').strip()
    if not url.startswith('http'):
        return jsonify({"success": False, "error": "Invalid Flipkart URL"}), 400
        
    force = 1 if req.get('force') else 0
    notassured = True if req.get('notassured') else False
    
    if category not in data:
        data[category] = []
        
    new_task = {
        "filename": filename,
        "force": force,
        "notassured": notassured,
        "url": url,
        "source_script": "web_ui"
    }
    
    existing_index = next((i for i, t in enumerate(data[category]) if t['filename'] == filename), -1)
    if existing_index >= 0:
        data[category][existing_index] = new_task
    else:
        data[category].append(new_task)
        
    save_config(data)
    return jsonify({"success": True, "message": f"Successfully mapped '{filename}' to '{category}'"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
