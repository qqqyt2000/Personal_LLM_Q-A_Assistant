import pandas as pd

def load_knowledge_base(file_path):
    """Load the knowledge base from an Excel file."""
    df = pd.read_excel(file_path)
    return df

def search_knowledge_base(df, keyword):
    """Search for questions and answers that contain the given keyword."""
    results = df[df['问题'].str.contains(keyword, case=False, na=False)]
    return results[['问题', '答案']].to_dict(orient='records')