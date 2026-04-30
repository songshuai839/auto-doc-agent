
def analyze_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    return f"""
代码分析：
函数数量：{code.count('def ')}
类数量：{code.count('class ')}

代码片段：
{code[:500]}
"""
