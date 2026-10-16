# FindrAI — AI-Powered Lost & Found Matching Platform

FindrAI is an intelligent, full-stack Lost & Found platform that automatically detects and pairs lost items with found items using a multi-modal similarity matrix (NLP text analysis, visual image perceptual hashing, GPS spatial proximity, and timeline decay).

---

## 🌟 Key Features

1. **Multi-Modal AI Matching Engine**:
   - **Text & Semantic NLP**: Item category classification, keyword & attribute extraction (colors, materials, item nouns), synonym mapping (e.g., "wallet" ~ "cardholder" ~ "purse"), and title/description similarity.
   - **Visual Image Fingerprinting**: Perceptual hashing (`pHash`, `dHash`) and dominant RGB color histogram analysis to pair photos even across varying camera angles.
   - **Location Proximity**: Great-circle Haversine GPS distance calculation + fuzzy campus landmark text matching (e.g., "college cafeteria", "library 2nd floor").
   - **Temporal Proximity**: Timeline decay scoring ensuring found events logically align with or succeed lost events.
   - **Explainable AI (XAI)**: Generates human-readable evidence badges explaining why pairs were matched (e.g., *"95% text match on 'black wallet' • 88% visual color match • Located within 80m of Cafeteria"*).

2. **Claim & Verification System**:
   - Finders can attach security verification challenges (e.g., *"What initials or bank cards are inside?"*, *"What custom engraving or lock screen is on the device?"*).
   - Claimants submit proof without disclosing confidential information publicly.
   - Finders can review, approve, or reject claims with instant status progression.

3. **Anonymous Protected Messaging**:
   - End-to-end pseudonymous in-app chat between item owners and finders.
   - Protects users from publicly sharing phone numbers or personal emails.
   - Built-in safety warnings advising users to arrange hand-offs at secure public locations (e.g., campus security desks).

4. **Interactive Campus Map & Modern UI**:
   - Leaflet.js interactive map for dropping pins and selecting campus landmarks.
   - Live AI Match Radar with circular similarity gauges and subscore breakdowns.
   - Preloaded with realistic college demo data for instant testing.

---

## 🚀 How to Run

### Quick Start (Windows)
Simply double-click the **`start.bat`** file in this folder. It will start the server and automatically launch the website in your browser!

### Manual Start via Command Line
Run the following command in PowerShell or Command Prompt:

```powershell
python run.py
```

The application will launch at:
👉 **`http://127.0.0.1:8000`**

---

## 🧪 Testing the AI Matching

Try this realistic scenario:
1. Click **"Load College Demo"** in the top navigation bar.
2. Go to **"AI Match Radar"** to see the system's pairing of:
   - *"Black wallet lost near college cafeteria"*
   - *"Found black leather wallet"*
   - **Match Confidence**: **88%** with breakdown of text, image, location, and timeline scores.
3. Click **"Claim & Verify"** to submit proof or **"Anonymous Chat"** to send real-time secure messages.
4. Try reporting a new lost or found item with a photo to see the AI radar scan the database in real-time!
