# Credit Chakra MSME Digital Presence Analyzer

A FastAPI application for analyzing MSME (Micro, Small, and Medium Enterprises) digital presence across multiple platforms.

## 🎯 Project Overview

This project helps evaluate MSMEs' digital presence by analyzing their online footprint across multiple platforms. Students must implement at least 2 out of 4 available tracks (3 tracks recommended for better scoring).

## ⏰ Timeline Recommendation

We recommend completing and submitting your project within 48 hours of receiving this template.


## 🛠️ Available Tracks

1. **Google Maps Analysis**
   - Scrape business information from Google Maps
   - Collect ratings, reviews, and photos
   - Optional: Analyze review sentiment

2. **Instagram Analysis**
   - Analyze business Instagram profile
   - Collect follower count, engagement metrics
   - Analyze recent posts and engagement

3. **Website Analysis**
   - Check domain age using whois
   - Verify SSL certificate status
   - Check for product/services pages
   - Optional: Mobile responsiveness check

4. **JustDial/IndiaMART Analysis**
   - Check business listing status
   - Collect ratings and reviews
   - Verify listing details and photos

## 🛠️ Tools & Resources

Feel free to use any of the following but not limited to help with your implementation:

1. **Open Source Libraries**
   - BeautifulSoup4 for web scraping
   - Selenium for dynamic content
   - Requests for API calls
   - Pandas for data processing
   - NLTK for text analysis

2. **AI Tools**
   - ChatGPT for code assistance
   - GitHub Copilot for code suggestions
   - AI-powered code editors
   - AI tools for data analysis

3. **Development Tools**
   - VS Code with Python extensions
   - Postman for API testing
   - Git for version control
   - Docker for containerization

Remember to:
- Document any third-party tools you use
- Follow the tools' licenses and terms of use
- Give credit to open source projects
- Keep your code original and unique

## 🚀 Getting Started

1. **Setup Environment**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd credit-chakra-hackathon-template

   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   ```bash
   # Copy example environment file
   cp .env.example .env

   # Edit .env with your configuration
   # Add any required API keys or credentials
   ```

3. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📦 Project Structure

```
credit-chakra-hackathon-template/
├── app/
│   ├── main.py           # FastAPI application and endpoints
│   ├── website.py        # Website analysis logic
│   ├── listing.py        # Data storage management
│   └── scoring.py        # Credit scoring logic
├── data/
│   └── output.json       # Stored analysis results
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## 📝 Implementation Steps

1. **Choose Your Tracks**
   - Select at least 2 out of 4 available tracks (3 tracks recommended)
   - Implement the corresponding endpoints in `app/main.py`
   - Each track should have its own data collection module
   - More tracks = Better scoring potential

2. **Implement Track Endpoints**
   - Each track has its own endpoint in `app/main.py`
   - Replace `NotImplementedError` with your implementation
   - Follow the specified return format for each endpoint
   - Implement proper error handling and validation

3. **Implement Scoring System**
   - Update `app/scoring.py` with your scoring logic
   - Implement track-specific scoring methods
   - Create a final score calculation
   - Ensure scoring reflects the importance of each track

## 🔍 API Endpoints

### Track-Specific Endpoints
```http
GET /api/v1/website/{business_name}
GET /api/v1/google-maps/{business_name}
GET /api/v1/instagram/{business_name}
GET /api/v1/justdial/{business_name}
```

### Scoring Endpoint
```http
GET /api/v1/score/{business_name}
```

## 📊 Expected Response Formats

### Website Analysis
```json
{
    "domain_age": "2 years",
    "ssl_status": true,
    "has_product_pages": true,
    "mobile_responsive": true
}
```

### Google Maps Data
```json
{
    "business_name": "Example Business",
    "address": "123 Main St",
    "rating": 4.5,
    "review_count": 100,
    "sample_reviews": [
        {"text": "Great service!", "rating": 5},
        {"text": "Good products", "rating": 4}
    ],
    "photo_count": 25
}
```

### Instagram Data
```json
{
    "username": "example_business",
    "followers": 1000,
    "post_count": 150,
    "recent_posts": [
        {"likes": 100, "comments": 10},
        {"likes": 85, "comments": 8}
    ],
    "engagement_rate": 0.05
}
```

### Final Score
```json
{
    "business_name": "Example Business",
    "score": 81,
    "breakdown": {
        "website": 25,
        "google_maps": 34,
        "instagram": 22
    },
    "explanation": "Good reviews and website trust; average engagement on Instagram."
}
```

## 📋 Evaluation Criteria

1. **Code Quality**
   - Clean, well-documented code
   - Proper error handling
   - Type hints and validation

2. **Functionality**
   - Accurate data collection
   - Reliable scoring system
   - Proper data storage

3. **API Design**
   - Clear endpoint structure
   - Consistent response formats
   - Good error messages

4. **Documentation**
   - Clear code comments
   - API documentation
   - Setup instructions

## 📧 Submission Email Template

Use the following template for your submission email:

```
Hi Credit Chakra Team,

I'm submitting my project for the Credit Chakra MSME Digital Presence Analyzer Hackathon.  
Please find the details below:

🔹 **Name**: John Doe  
🔹 **College**: [Your College Name]  
🔹 **Year & Branch**: 3rd Year, B.Tech in [Your Branch]  
🔹 **GitHub Repo Link**: https://github.com/your-username/credit-chakra-msme-analyzer  
🔹 **Tracks Implemented**: Google Maps, Instagram, Website  
🔹 **Bonus Features (if any)**:
- Review sentiment analysis using TextBlob
- Engagement rate calculation on Instagram
- Domain trustworthiness logic
- Clean scoring breakdown endpoint

📝 Notes:
- Fully working FastAPI backend with 3 tracks  
- Real data for 2+ MSMEs per track  
- Scoring system with breakdown  
- Sample outputs in `data/output.json`  
- Basic test cases  
- Setup instructions in the README

Looking forward to your feedback!

Thanks and regards,  
**John Doe**  
[Your Phone Number (Optional)]  
[Your LinkedIn (Optional)]
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
