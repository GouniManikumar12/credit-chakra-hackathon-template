# Credit Chakra MSME Digital Presence Analyzer

A FastAPI application for analyzing MSME (Micro, Small, and Medium Enterprises) digital presence across multiple platforms.

## 🎯 Project Overview

This project helps evaluate MSMEs' digital presence by analyzing their online footprint across multiple platforms. Students need to implement data collection and scoring logic for 3 out of 4 available tracks.

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

## 📝 Implementation Steps

1. **Choose Your Tracks**
   - Select 3 out of 4 available tracks
   - Implement the corresponding endpoints in `app/main.py`
   - Each track should have its own data collection module

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

## 🐛 Testing

1. **Run Tests**
   ```bash
   pytest
   ```

2. **Test Coverage**
   ```bash
   pytest --cov=app tests/
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
├── tests/
│   └── test_*.py         # Test files
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## ⚠️ Important Notes

1. **API Keys and Credentials**
   - Never commit API keys to the repository
   - Use environment variables for sensitive data
   - Document required credentials in .env.example

2. **Rate Limiting**
   - Implement rate limiting for external APIs
   - Handle API quotas and limits
   - Cache responses when appropriate

3. **Error Handling**
   - Handle network errors gracefully
   - Provide meaningful error messages
   - Log errors for debugging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
