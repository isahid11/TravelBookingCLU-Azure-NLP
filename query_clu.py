"""
query_clu.py
------------
Query a deployed Azure Conversational Language Understanding (CLU) model.

Setup:
    1. Create a .env file with your credentials (see .env.example)
    2. pip install requests python-dotenv
    3. python query_clu.py
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ENDPOINT     = os.getenv("AZURE_LANGUAGE_ENDPOINT")
API_KEY      = os.getenv("AZURE_LANGUAGE_KEY")
PROJECT_NAME = os.getenv("CLU_PROJECT_NAME", "TravelBookingCLU")
DEPLOYMENT   = os.getenv("CLU_DEPLOYMENT_NAME", "production")

if not ENDPOINT or not API_KEY:
    raise ValueError("Missing credentials. Set AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY in your .env file.")

URL = f"{ENDPOINT.rstrip('/')}/language/:analyze-conversations?api-version=2022-10-01-preview"

HEADERS = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}


def query_clu(utterance: str) -> dict:
    """Send an utterance to the CLU model and return the parsed result."""
    payload = {
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "participantId": "user",
                "text": utterance
            }
        },
        "parameters": {
            "projectName": PROJECT_NAME,
            "deploymentName": DEPLOYMENT,
            "stringIndexType": "Utf16CodeUnit"
        }
    }

    response = requests.post(URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()


def display_result(utterance: str, result: dict):
    """Print a clean summary of the CLU prediction."""
    prediction = result["result"]["prediction"]
    top_intent = prediction["topIntent"]
    confidence = next(
        (i["confidenceScore"] for i in prediction["intents"] if i["category"] == top_intent),
        None
    )
    entities = prediction.get("entities", [])

    print(f"\nUtterance : {utterance}")
    print(f"Top Intent: {top_intent} (confidence: {confidence:.2%})")
    if entities:
        print("Entities  :")
        for ent in entities:
            print(f"  - {ent['category']}: '{ent['text']}' (confidence: {ent.get('confidenceScore', 'N/A')})")
    else:
        print("Entities  : None detected")
    print("-" * 60)


# Sample test utterances
TEST_UTTERANCES = [
    "Book a flight to Delhi tomorrow",
    "I want to travel to Mumbai next week",
    "Cancel my booking",
    "Find me flights to Bangalore for 2 passengers",
    "What's the weather like in Goa?",   # Out-of-scope — should map to None
]

if __name__ == "__main__":
    print("=" * 60)
    print("TravelBookingCLU — Model Query Test")
    print(f"Project   : {PROJECT_NAME}")
    print(f"Deployment: {DEPLOYMENT}")
    print("=" * 60)

    for utterance in TEST_UTTERANCES:
        try:
            result = query_clu(utterance)
            display_result(utterance, result)
        except requests.exceptions.HTTPError as e:
            print(f"\n[ERROR] {utterance}")
            print(f"  HTTP {e.response.status_code}: {e.response.text}")
        except Exception as e:
            print(f"\n[ERROR] {utterance}: {e}")
