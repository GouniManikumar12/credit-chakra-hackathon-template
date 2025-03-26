"""
Credit Chakra Hackathon Template
==============================

This template helps you build a FastAPI application for MSME digital data collection.
Follow these steps to complete your hackathon project:

1. SETUP:
   - Install dependencies: pip install -r requirements.txt
   - Copy .env.example to .env and configure settings
   - Run the app: uvicorn app.main:app --reload

2. IMPLEMENTATION STEPS:
   a) Choose 3 out of 4 data extraction tracks:
      - Google Maps (Reviews, Ratings, Photos)
      - Instagram (Followers, Engagement)
      - Website (Domain age, SSL, Product pages)
      - JustDial/IndiaMART (Listings, Ratings)

   b) For each track, implement:
      - Data extraction logic in separate modules
      - FastAPI endpoint for the track
      - Data validation and formatting
      - Error handling

   c) Create a unified scoring system:
      - Combine data from different tracks
      - Implement scoring algorithm
      - Generate final credit score

3. EXAMPLE STRUCTURE:
   - /app/
     ├── main.py (this file)
     ├── website.py (website scraping)
     ├── listing.py (data storage)
     └── scoring.py (credit scoring logic)
   - /data/
     └── output.json (scraped data)
   - /tests/
     └── test_*.py (unit tests)

4. API ENDPOINTS TO IMPLEMENT:
   - GET /api/v1/website/{business_name}
   - GET /api/v1/google-maps/{business_name}
   - GET /api/v1/instagram/{business_name}
   - GET /api/v1/justdial/{business_name}
   - GET /api/v1/score/{business_name}

5. EVALUATION CRITERIA:
   - Code quality and organization
   - Error handling and robustness
   - Data validation and cleaning
   - API documentation
   - Test coverage
"""

from fastapi import FastAPI, HTTPException
from typing import Dict
from .website import WebsiteScraper
from .listing import ListingManager

app = FastAPI(
    title="Credit Chakra MSME Data Collector",
    description="API for collecting and analyzing MSME digital presence data",
    version="1.0.0"
)

# Initialize components
website_scraper = WebsiteScraper()
listing_manager = ListingManager()

@app.get("/")
async def root():
    """Welcome message and API documentation"""
    return {
        "message": "Welcome to Credit Chakra MSME Data Collector",
        "documentation": "/docs",
        "endpoints": {
            "/api/v1/website/{business_name}": "Get website data",
            "/api/v1/score/{business_name}": "Get credit score"
        }
    }

@app.get("/api/v1/website/{business_name}")
async def get_website_data(business_name: str):
    """
    Get website data for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing website analysis
    """
    try:
        # Get website data
        data = website_scraper.analyze_website(business_name)
        
        # Save to storage
        listing_manager.save_listing(business_name, data)
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/score/{business_name}")
async def get_credit_score(business_name: str):
    """
    Get credit score for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing credit score
    """
    try:
        # Get stored data
        listing = listing_manager.get_listing(business_name)
        if not listing:
            raise HTTPException(status_code=404, detail="Business not found")
            
        # For now, return a simple score based on website data
        website_data = listing['data']
        score = website_data.get('total_score', 0)
        
        return {
            "business_name": business_name,
            "credit_score": score,
            "max_score": 30,
            "timestamp": listing['timestamp']
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 