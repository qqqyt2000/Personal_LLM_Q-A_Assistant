from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__, template_folder='templates')

# Load the knowledge base from the Excel file
def load_knowledge_base():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/knowledge_base.xlsx'))
    df = pd.read_excel(file_path)
    return df

# Search for questions based on the keyword
def search_questions(keyword):
    df = load_knowledge_base()
    results = df[df['Question'].str.contains(keyword, case=False, na=False)]
    return results[['Question']].to_dict(orient='records')

# Get the answer for a specific question
def get_answer(question):
    df = load_knowledge_base()
    result = df[df['Question'] == question]
    if not result.empty:
        return result.iloc[0]['Answer']
    return "未找到答案"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    results = search_questions(query)
    return jsonify(results)

@app.route('/get_answer', methods=['GET'])
def fetch_answer():
    question = request.args.get('question', '')
    answer = get_answer(question)
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # 将端口设置为 5001