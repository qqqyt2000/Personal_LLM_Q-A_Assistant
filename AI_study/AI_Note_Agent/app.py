from flask import Flask, render_template, request, jsonify
import openai
import pandas as pd
import os
import shutil  # 导入 shutil 模块
import sys
from config_new import OPENAI_API_KEY

# 添加当前目录到模块搜索路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder='templates')

# 设置 OpenAI API 密钥
client = openai.OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.deepseek.com/v1")

# Excel 文件路径
EXCEL_FILE = 'chat_history.xlsx'

# 副本文件路径
BACKUP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../qa-web-app/data'))
BACKUP_FILE = os.path.join(BACKUP_DIR, 'knowledge_base.xlsx')

# 检查 Excel 文件是否存在，如果不存在则创建
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Question', 'Answer'], dtype=str)  # 显式指定 dtype 为 str
    df.to_excel(EXCEL_FILE, index=False)

    # 确保目标目录存在
    os.makedirs(BACKUP_DIR, exist_ok=True)
    # 保存副本
    shutil.copy(EXCEL_FILE, BACKUP_FILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    try:
        # 调用 OpenAI API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        # 提取 AI 的回复
        ai_message = response.choices[0].message.content

        # 将问题和答案添加到 Excel 表格
        df = pd.read_excel(EXCEL_FILE)
        new_row = pd.DataFrame([{'Question': user_message, 'Answer': ai_message}])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)

        # 保存副本到目标目录
        os.makedirs(BACKUP_DIR, exist_ok=True)
        shutil.copy(EXCEL_FILE, BACKUP_FILE)

        return jsonify({'ai_message': ai_message})
    except openai.error.OpenAIError as e:
        # 返回 JSON 格式的错误信息
        return jsonify({'error': f"OpenAI API Error: {str(e)}"}), 500
    except Exception as e:
        # 捕获其他异常并返回 JSON 格式的错误信息
        return jsonify({'error': f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # 将端口设置为 5000