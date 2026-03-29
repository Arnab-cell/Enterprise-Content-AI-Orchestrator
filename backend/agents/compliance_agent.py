
from langchain.chat_models import ChatOpenAI
from backend.config import MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)

def review_content(content):
    prompt = f"""
Review this content for:
- Legal compliance
- Brand safety
- False claims

Return PASS or FAIL with feedback.

Content:
{content}
"""

    return llm.predict(prompt)
