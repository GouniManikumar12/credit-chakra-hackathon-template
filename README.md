# Credit Chakra MSME Digital Presence Analyzer

## 🧩 Problem Statement

Build a FastAPI application that collects publicly available digital data of MSMEs in India across multiple platforms.

Your goal is to simulate how a credit scoring engine might assess a small business's credibility based on their online presence. You'll be working with real-world businesses — from your city, locality, or anywhere in India — and building APIs to extract and format relevant digital signals.

## 🎯 What You Need To Do

1. Choose **3 out of 4 real-world data extraction tracks**
2. Build a **FastAPI-based Python app**
3. Each track should have its own **API endpoint**
4. Output data for **at least 2 MSMEs per track** in JSON format
5. Submit your GitHub repo with clean code + documentation

## 🛠️ Platforms You'll Work With

| Track | Platform | What You'll Extract | Points |
|-------|----------|---------------------|--------|
| 1. Google Maps | Reviews, Ratings, Photos | Local reputation | 40 |
| 2. Instagram | Followers, Engagement | Digital reach | 30 |
| 3. Website | Domain age, SSL, Products | Trustworthiness | 30 |
| 4. JustDial / IndiaMART | Listings, Ratings | Local verification | 30 |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Setup Instructions

1. Clone this repository:
```bash
git clone <repository-url>
cd credit-chakra-hackathon-template
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

5. Access the API documentation:
- Open http://localhost:8000/docs in your browser

## 📝 Implementation Tasks

### 1. Choose Your Tracks
Select 3 platforms from the available tracks. For each track:
- Create a new Python module in the `app` directory
- Implement data extraction logic
- Create FastAPI endpoints
- Add data validation
- Implement error handling

### 2. Data Extraction Implementation
For each track, implement:

#### Website Analysis (30 points)
- Domain age checking
- SSL certificate verification
- Mobile responsiveness
- Content quality analysis
- Contact information extraction

#### Google Maps (40 points)
- Business search functionality
- Reviews and ratings extraction
- Photos count and analysis
- Business details scraping
- Location data processing

#### Instagram (30 points)
- Profile data extraction
- Follower count tracking
- Post frequency analysis
- Engagement rate calculation
- Content type analysis

#### JustDial/IndiaMART (30 points)
- Business listing extraction
- Ratings and reviews collection
- Service/product categorization
- Contact information validation
- Business age verification

### 3. Credit Scoring System
Implement a scoring algorithm that:
- Weighs different factors from each platform
- Calculates a unified credit score
- Provides score breakdown
- Generates score explanations

## 📊 Scoring Criteria

Your implementation will be evaluated on:

1. **Code Quality (30%)**
   - Clean, well-organized code
   - Proper error handling
   - Input validation
   - Documentation
   - Type hints

2. **Functionality (40%)**
   - Successful data extraction
   - Accurate scoring system
   - API reliability
   - Error handling
   - Response format

3. **Technical Design (30%)**
   - Code structure
   - Scalability
   - Maintainability
   - Testing coverage
   - Documentation quality

## 📚 API Documentation

### Base URL
`http://localhost:8000`

### Endpoints

1. Website Data
```
GET /api/v1/website/{business_name}
```

2. Google Maps Data
```
GET /api/v1/google-maps/{business_name}
```

3. Instagram Data
```
GET /api/v1/instagram/{business_name}
```

4. JustDial Data
```
GET /api/v1/justdial/{business_name}
```

5. Credit Score
```
GET /api/v1/score/{business_name}
```

## 🔍 Testing

1. Create test cases in the `tests` directory
2. Test with real MSME data
3. Validate scoring accuracy
4. Check error handling
5. Verify API responses

## 📦 Project Structure
```
credit-chakra-hackathon-template/
├── app/
│   ├── main.py           # FastAPI application
│   ├── website.py        # Website scraping
│   ├── google_maps.py    # Google Maps scraping
│   ├── instagram.py      # Instagram scraping
│   ├── justdial.py       # JustDial scraping
│   ├── scoring.py        # Credit scoring logic
│   └── listing.py        # Data storage
├── data/
│   └── output.json       # Scraped data storage
├── tests/
│   └── test_*.py         # Unit tests
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## ⚠️ Important Notes

1. Use only publicly available data
2. Implement proper rate limiting
3. Handle errors gracefully
4. Document your code
5. Follow Python best practices
6. Add proper logging
7. Include error handling
8. Write unit tests

## 🏁 Submission Guidelines

1. Clean and documented code
2. Working API endpoints
3. Test data for at least 2 MSMEs
4. README with setup instructions
5. Requirements.txt with dependencies
6. Unit tests
7. API documentation

## 🤝 Need Help?

- Check the FastAPI documentation: https://fastapi.tiangolo.com/
- Review Python scraping best practices
- Study the provided template code
- Ask questions in the discussion forum

Good luck with your implementation! 🚀
