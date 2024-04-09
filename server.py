from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_model', methods=['POST'])
def run_model():
    input_data = request.form['input_data']
    # Pass the input data to your Python script for processing
    # Replace the following line with your actual script execution logic
    result = f"Python script executed successfully with input: {input_data}"
    return result

if __name__ == '__main__':
    app.run(debug=True)

