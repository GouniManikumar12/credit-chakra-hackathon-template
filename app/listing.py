from typing import Dict, List
import json
import os
from datetime import datetime

class ListingManager:
    def __init__(self):
        """Initialize the listing manager"""
        self.output_file = os.path.join('data', 'output.json')
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Ensure the data directory exists"""
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

    def save_listing(self, business_name: str, data: Dict) -> None:
        """
        Save business data to storage
        
        Args:
            business_name: Name of the business
            data: Business data to save
        """
        listings = self.load_listings()
        
        # Add or update listing
        listing = {
            'business_name': business_name,
            'data': data,
            'timestamp': datetime.now().isoformat()
        }
        
        # Update if exists, append if new
        updated = False
        for i, existing in enumerate(listings):
            if existing['business_name'] == business_name:
                listings[i] = listing
                updated = True
                break
                
        if not updated:
            listings.append(listing)
            
        # Save to file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(listings, f, indent=2, ensure_ascii=False)

    def load_listings(self) -> List[Dict]:
        """
        Load all business listings
        
        Returns:
            List of business listings
        """
        if not os.path.exists(self.output_file):
            return []
            
        try:
            with open(self.output_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def get_listing(self, business_name: str) -> Dict:
        """
        Get a specific business listing
        
        Args:
            business_name: Name of the business
            
        Returns:
            Business listing data
        """
        listings = self.load_listings()
        for listing in listings:
            if listing['business_name'] == business_name:
                return listing
        return None

    def update_listing(self, listing_id: str, updated_data: Dict) -> None:
        """
        Update an existing listing
        
        Args:
            listing_id: ID of the listing to update
            updated_data: Dictionary containing updated information
        """
        listings = self.load_listings()
        
        # Find and update the listing
        for i, listing in enumerate(listings):
            if listing.get('id') == listing_id:
                # Preserve original timestamp
                original_timestamp = listing.get('timestamp')
                
                # Update listing data
                listings[i] = updated_data
                
                # Add update timestamp
                listings[i]['timestamp'] = original_timestamp
                listings[i]['last_updated'] = datetime.now().isoformat()
                
                # Save updated listings
                with open(self.output_file, 'w', encoding='utf-8') as f:
                    json.dump(listings, f, indent=2, ensure_ascii=False)
                return
                
        print(f"Listing with ID {listing_id} not found") 