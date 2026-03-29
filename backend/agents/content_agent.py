
from langchain.chat_models import ChatOpenAI
from backend.config import MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)

def generate_content(topic, audience):
    prompt = f"""
Generate enterprise marketing content.

Topic: {topic}
Audience: {audience}

Output:
1 Blog article
1 LinkedIn post
1 Twitter thread
"""

    return llm.predict(prompt)
