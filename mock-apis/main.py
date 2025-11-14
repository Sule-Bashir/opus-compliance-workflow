from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Mock Sanctions API
@app.route('/sanctions/check', methods=['POST'])
def sanctions_check():
    data = request.json
    print(f"Sanctions check for: {data}")
    
    # Mock logic - 5% chance of match
    match = random.random() < 0.05
    return jsonify({
        "match": match,
        "confidence": 0.95,
        "similar_entities": ["John Doe Similar"] if match else [],
        "timestamp": datetime.now().isoformat()
    })

# Mock Credit Check API
@app.route('/credit/score', methods=['POST'])
def credit_score():
    data = request.json
    customer_id = data.get('customer_id', 'unknown')
    
    # Mock credit score 300-850
    score = random.randint(300, 850)
    return jsonify({
        "customer_id": customer_id,
        "score": score,
        "factors": ["payment_history", "credit_utilization"],
        "risk_level": "low" if score > 700 else "medium" if score > 600 else "high"
    })

# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
