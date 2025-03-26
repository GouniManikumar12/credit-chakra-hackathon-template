"""
Credit Chakra MSME Digital Presence Analyzer
=========================================

This FastAPI application helps analyze MSME digital presence across multiple platforms.
Students need to implement the data collection and scoring logic for each track.

Available Tracks:
1. Google Maps (Reviews, Ratings, Photos)
2. Instagram (Followers, Engagement)
3. Website (Domain age, SSL, Product pages)
4. JustDial/IndiaMART (Listings, Ratings)

Students must implement 3 out of 4 tracks and the final scoring system.
"""

from fastapi import FastAPI, HTTPException
from typing import Dict
from datetime import datetime

app = FastAPI(
    title="Credit Chakra MSME Digital Presence Analyzer",
    description="API for analyzing MSME digital presence across multiple platforms",
    version="1.0.0"
)

# Initialize components
from .website import WebsiteScraper
from .listing import ListingManager
from .scoring import CreditScorer

website_scraper = WebsiteScraper()
listing_manager = ListingManager()
credit_scorer = CreditScorer()

@app.get("/")
async def root():
    """Welcome message and API documentation"""
    return {
        "message": "Welcome to Credit Chakra MSME Digital Presence Analyzer",
        "documentation": "/docs",
        "available_endpoints": {
            "/api/v1/google-maps/{business_name}": "Get Google Maps data",
            "/api/v1/instagram/{business_name}": "Get Instagram data",
            "/api/v1/website/{business_name}": "Get website analysis",
            "/api/v1/justdial/{business_name}": "Get JustDial/IndiaMART data",
            "/api/v1/score/{business_name}": "Get final credit score"
        }
    }

@app.get("/api/v1/google-maps/{business_name}")
async def get_google_maps_data(business_name: str):
    """
    Get Google Maps data for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing:
        - Business name
        - Address/location
        - Average rating
        - Number of reviews
        - Sample reviews (2-3)
        - Number of photos
        - (Optional) Review sentiment
    """
    try:
        # TODO: Implement Google Maps data collection
        # This is where students will implement their Google Maps scraping logic
        raise NotImplementedError("Google Maps data collection not implemented")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/instagram/{business_name}")
async def get_instagram_data(business_name: str):
    """
    Get Instagram data for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing:
        - Username/handle
        - Number of followers
        - Number of posts
        - Likes/comments on last 5 posts
        - Engagement rate
        - (Optional) Bio and tags
    """
    try:
        # TODO: Implement Instagram data collection
        # This is where students will implement their Instagram scraping logic
        raise NotImplementedError("Instagram data collection not implemented")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/website/{business_name}")
async def get_website_data(business_name: str):
    """
    Get website analysis for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing:
        - Domain age (via whois)
        - SSL certificate status
        - Product/services page existence
        - Mobile responsiveness check (Optional)
    """
    try:
        # Get website data
        data = website_scraper.analyze_website(business_name)
        
        # Save to storage
        listing_manager.save_listing(business_name, data)
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/justdial/{business_name}")
async def get_justdial_data(business_name: str):
    """
    Get JustDial/IndiaMART data for a business
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing:
        - Is business listed?
        - Ratings/review count
        - Contact info (if available)
        - Listing verification (photos)
    """
    try:
        # TODO: Implement JustDial/IndiaMART data collection
        # This is where students will implement their JustDial/IndiaMART scraping logic
        raise NotImplementedError("JustDial/IndiaMART data collection not implemented")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/score/{business_name}")
async def get_credit_score(business_name: str):
    """
    Get credit score for a business based on available data
    
    Args:
        business_name: Name of the business to analyze
        
    Returns:
        Dictionary containing:
        - Business name
        - Final score (out of 100)
        - Score breakdown per platform
        - Score explanation
    """
    try:
        # Get stored data
        listing = listing_manager.get_listing(business_name)
        if not listing:
            raise HTTPException(status_code=404, detail="Business not found")
            
        # Calculate scores for each available track
        scores = {}
        if 'website' in listing:
            scores['website'] = credit_scorer.calculate_website_score(listing['website'])
        if 'google_maps' in listing:
            scores['google_maps'] = credit_scorer.calculate_local_score(listing['google_maps'])
        if 'instagram' in listing:
            scores['instagram'] = credit_scorer.calculate_social_score(listing['instagram'])
        if 'justdial' in listing:
            scores['justdial'] = credit_scorer.calculate_local_score(listing['justdial'])
            
        # Calculate final score
        final_score = credit_scorer.calculate_final_score(scores)
        
        # Add explanation
        final_score['explanation'] = credit_scorer.get_score_explanation(final_score['final_score'])
        
        return final_score
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 