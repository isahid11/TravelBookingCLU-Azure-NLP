# Conversational Language Understanding — Travel Booking Bot
### SIG788 — Engineering AI Solutions | Deakin University

## Overview
This project builds and evaluates a **Conversational Language Understanding (CLU)** model using **Azure Language Studio** for a travel booking domain. The model classifies user intents and extracts key entities from natural language input, forming the NLP layer of a travel booking assistant.

Built as part of the Master of Data Science program at Deakin University.

---

## Model Design

### Intents
| Intent | Description |
|---|---|
| `BookFlight` | User wants to book a flight |
| `SearchFlights` | User wants to search/browse available flights |
| `CancelBooking` | User wants to cancel an existing booking |
| `None` | Input is out of scope or unrecognised |

### Entities
| Entity | Description |
|---|---|
| `Destination` | Travel destination city or location |
| `TravelDate` | Date or relative time of travel (e.g. "tomorrow", "next week") |
| `PassengerCount` | Number of passengers travelling |

### Sample Utterances
```
"Book a flight to Delhi tomorrow"
→ Intent: BookFlight | Destination: Delhi | TravelDate: tomorrow

"I want to travel to Mumbai next week"
→ Intent: SearchFlights | Destination: Mumbai | TravelDate: next week

"Cancel my booking"
→ Intent: CancelBooking
```

---

## Tech Stack
- **Azure Language Studio** — CLU model authoring, training, and deployment
- **Azure AI Language Service** — REST API for inference
- **Azure Bot Service** — Bot integration layer
- **Python** — CLU endpoint querying and testing

---

## Files
```
├── TravelBookingCLU.json        # CLU model export (intents, entities, utterances)
├── query_clu.py                 # Python script to query the deployed CLU endpoint
├── sample_queries.json          # Sample test utterances with expected outputs
├── .env.example                 # Template for credentials
├── .gitignore
└── README.md
```

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/isahid11/TravelBookingCLU-Azure-NLP.git
cd TravelBookingCLU-Azure-NLP
```

### 2. Install dependencies
```bash
pip install requests python-dotenv
```

### 3. Configure credentials
Create a `.env` file:
```
AZURE_LANGUAGE_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_LANGUAGE_KEY=your_api_key_here
CLU_PROJECT_NAME=TravelBookingCLU
CLU_DEPLOYMENT_NAME=production
```

### 4. Run the query script
```bash
python query_clu.py
```

---

## How to Import the Model
1. Go to [language.cognitive.azure.com](https://language.cognitive.azure.com)
2. Create a new **Conversational Language Understanding** project
3. Click **Import** and upload `TravelBookingCLU.json`
4. Train and deploy the model
5. Update your `.env` file with the new endpoint and key

---

## Key Findings
- CLU successfully classified all three primary intents with high confidence on test utterances
- Entity extraction accurately identified `Destination` and `TravelDate` across varied phrasings
- Model struggled with ambiguous utterances combining multiple intents — highlighted need for more diverse training data
- Confidence thresholds and the `None` intent are critical for handling out-of-scope queries gracefully

---

## Skills Demonstrated
- NLP model design: intent schema, entity extraction, utterance engineering
- CLU model training, evaluation, and deployment on Azure Language Studio
- REST API integration with Azure AI Language Service
- Model performance analysis and failure mode identification
- Technical documentation and academic report writing
