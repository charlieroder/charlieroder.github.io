from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python_script():
    input_data = request.json['input']
    
    # Process input_data and execute your Python script here

    # For demonstration, let's just return the input data reversed
    output_data = input_data[::-1]

    return jsonify({'output': output_data})

if __name__ == '__main__':
    app.run(debug=True)  # Remove debug=True in production


