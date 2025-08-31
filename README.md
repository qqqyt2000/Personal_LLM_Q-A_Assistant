# Personal_LLM_Q-A_Assistant
You can use this Agent to Ask Deepseek simple questions and search by keywords in your own knowledge base

# AI 知识问答与个人知识库系统

## 项目简介

为了解决现有AI问答工具无法用关键词搜索定位到具体对话问题与答案的痛点（deepseek没有关键词搜索功能，腾讯元宝仅可以定位到对话）
这是一个基于 Flask 的智能问答系统，集成了 AI 对话和个人知识库管理功能。系统包含两个主要模块：
1. AI 问答对话（`app.py`，在第一个文件夹中）
2. 个人知识库搜索（`app_2.py`，在第二个文件夹中）
<img width="723" height="488" alt="a9346b3b77e34d22755eac4550c05b8" src="https://github.com/user-attachments/assets/b83eb3a9-9935-4663-a694-20fb78bca02a" />
<img width="774" height="787" alt="89e7aed30640adf19522f58f44aaacf" src="https://github.com/user-attachments/assets/928dc20e-83d1-442d-9731-2eec4939c5e4" />

## 主要功能

### AI 问答对话
- 与 AI 助手进行实时对话
- 自动保存所有对话记录
- 支持问答历史的自动备份

### 个人知识库搜索
- 关键词搜索历史问答记录
- 点击问题查看详细答案
- 支持模糊匹配搜索

## 环境要求

- Python 3.8+
- Flask
- OpenAI
- Pandas
- openpyxl

## 安装依赖

```bash
pip install flask openai pandas openpyxl
```

## 使用说明

### 1. 配置 API 密钥
在项目根目录创建 `config_new.py` 文件，配置你的 OpenAI API 密钥：

```python
OPENAI_API_KEY = "你的API密钥"
```

### 2. 运行 AI 问答系统
```bash
python app.py
```
然后访问 http://localhost:5000 开始与 AI 对话

### 3. 运行知识库搜索系统
```bash
cd qa-web-app/src
python app_2.py
```
然后访问 http://localhost:5001 搜索历史问答记录

## 文件结构

```
AI_Note_Agent/
├── app.py                  # AI 问答主程序
├── config_new.py          # 配置文件
├── templates/             # 前端模板
│   └── index.html
├── chat_history.xlsx     # 对话历史记录
└── qa-web-app/
    ├── src/
    │   └── app_2.py      # 知识库搜索程序
    └── data/
        └── knowledge_base.xlsx  # 知识库备份

```

## 注意事项

1. 请确保 API 密钥配置正确
2. 运行程序前请确认相关依赖已安装
3. 首次运行时系统会自动创建必要的文件和目录
4. 建议定期备份 knowledge_base.xlsx 文件

## 常见问题

Q: 找不到模板文件？
A: 确保 templates 目录存在且包含所需的 HTML 模板文件。

Q: API 调用失败？
A: 检查 config_new.py 中的 API 密钥是否正确配置。

## 开发计划

- [ ] 添加用户认证系统
- [ ] 支持知识库数据导出
- [ ] 优化搜索算法
- [ ] 添加更多 AI 模型支持
