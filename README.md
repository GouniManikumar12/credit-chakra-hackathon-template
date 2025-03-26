
# 🧠 Credit Chakra Hackathon – Data Engineer Intern

Welcome to the Credit Chakra Hackathon Challenge! This is your chance to showcase your coding skills by extracting real-world digital presence data of MSMEs in India.

You must complete **at least 3 out of the 4 tracks** using **Python and FastAPI** and structure your output clearly.

---

## 🚀 Objective
Build a FastAPI application with endpoints that extract public digital data for Indian MSMEs from:
- Google Maps
- Instagram
- Business Websites
- JustDial / IndiaMART

---

## ✅ Your Mission
Complete **3 out of 4 Tracks** below:

### 📍 Track 1: Google Maps Review Scraper
`GET /google-maps?business=Triveni%20Store&city=Hyderabad`
- Google rating
- Review count
- Top 3 review texts
- Photo count
- Last photo upload date

### 📍 Track 2: Instagram Profile Analyzer
`GET /instagram?handle=stylehub_mumbai`
- Follower count
- Post count
- Avg likes/comments on last 5 posts
- Engagement rate

### 📍 Track 3: Website & Domain Checker
`GET /website?url=https://www.sargamfashion.in`
- SSL valid?
- Domain age
- Mobile responsiveness (optional)
- Product/services page present?

### 📍 Track 4: JustDial / IndiaMART Listing
`GET /listing?business=Ramdev%20Hardware&city=Ahmedabad`
- Listing present?
- Rating
- Phone number present?
- Photos present?

---

## 📦 Project Structure
```
credit-chakra-hackathon/
├── app/
│   ├── main.py
│   ├── google_maps.py
│   ├── instagram.py
│   ├── website.py
│   ├── listing.py
├── data/
│   └── output.json / output.csv
├── requirements.txt
├── .env.example
└── README.md
```

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📤 Submission Format
Send an email to `contact@creditchakra.in` with:
- Subject: `Credit Chakra Hackathon Submission – [Your Name] – [College Name]`

**Email Body:**
```
Name: [Your Full Name]  
College: [Your College Name]  
Year: [2nd / 3rd / Final Year]  
Track(s) Completed: [Google Maps, Instagram, Website]  
GitHub Repo Link: [Paste your public repo URL here]

Notes (optional):
- Any assumptions or workarounds
- Tools/libraries used
- Bonus features (if any)
```

📞 Contact: contact@creditchakra.in  
📍 Available for in-person meetups in Bangalore

---

## 🏁 Deadline
Submit within **48 hours** of receiving this challenge.

Good luck and build something real 💪
