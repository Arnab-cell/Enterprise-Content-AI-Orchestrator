
def check_brand_voice(content):

    issues = []

    if "guaranteed profit" in content.lower():
        issues.append("Unrealistic claim")

    if "free forever" in content.lower():
        issues.append("Potential misleading claim")

    if issues:
        return {"status": "flagged", "issues": issues}

    return {"status": "approved"}
