
from langchain.chat_models import ChatOpenAI
from backend.config import MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)

def localize_content(content, language):
    prompt = f"""
Translate and localize the following content for {language}.

Content:
{content}
"""
    return llm.predict(prompt)
