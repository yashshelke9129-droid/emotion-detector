import requests


def emotion_detector(text_to_analyse):
    """
    Analyze emotions from text and return emotion scores
    plus dominant emotion.
    """

    if not text_to_analyse or text_to_analyse.strip() == "":
        return None

    url = "https://example.com/emotion-api"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "text": text_to_analyse
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        emotions = data.get("emotion", {})

        result = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

        result["dominant_emotion"] = max(
            result,
            key=result.get
        )

        return result

    except Exception:
        return None