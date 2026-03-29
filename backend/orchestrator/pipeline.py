
from backend.agents.content_agent import generate_content
from backend.agents.compliance_agent import review_content
from backend.agents.localization_agent import localize_content
from backend.agents.governance_agent import check_brand_voice

def run_pipeline(topic, audience):

    content = generate_content(topic, audience)

    compliance = review_content(content)

    if "FAIL" in compliance:
        return {"status": "rejected", "reason": compliance}

    brand = check_brand_voice(content)

    if brand["status"] == "flagged":
        return brand

    spanish = localize_content(content, "Spanish")
    hindi = localize_content(content, "Hindi")

    return {
        "status": "approved",
        "content": content,
        "spanish": spanish,
        "hindi": hindi
    }
