
def generate_uml(text):
    return """
graph TD
A[Upload] --> B[Analyzer]
B --> C[Planner Agent]
C --> D[Doc Generator]
D --> E[Output Docs]
"""
