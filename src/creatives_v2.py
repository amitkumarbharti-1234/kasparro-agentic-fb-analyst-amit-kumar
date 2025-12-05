import json
from typing import List, Dict
from utils.logging_utils import get_logger

logger = get_logger("creatives_v2")

def generate_creatives_from_hypotheses(hypotheses: List[Dict]) -> List[Dict]:
    creatives = []

    for h in hypotheses:
        evidence = h.get("evidence", {})
        segment = evidence.get("segment", "overall")
        rel_delta = evidence.get("ctr_delta_relative", 0.0)

        if rel_delta < 0:
            headline = f"Rebuild Engagement for {segment}"
            primary_text = (
                f"CTR dropped significantly in {segment}. Consider stronger hooks, product benefits, "
                f"tighter messaging, and testing urgency or offer-led creatives."
            )
            cta = "Explore Collection"
        else:
            headline = f"Increase Spend in Winning Segment {segment}"
            primary_text = (
                f"{segment} is showing improved CTR. Increase budget allocation and create creative variants "
                f"based on current high-performing message direction."
            )
            cta = "Shop Now"

        creatives.append({
            "segment": segment,
            "linked_hypothesis": h.get("hypothesis", ""),
            "impact": h.get("impact", ""),
            "confidence": h.get("confidence", 0.5),
            "suggested_headline": headline,
            "suggested_primary_text": primary_text,
            "suggested_call_to_action": cta
        })

    logger.info("Generated creatives from hypotheses", extra={"count": len(creatives)})

    return creatives


def save_creatives(creatives: List[Dict], path: str):
    with open(path, "w") as f:
        json.dump(creatives, f, indent=4)
