from teapotai import TeapotAI
from pydantic import BaseModel

# Sample text for information extraction
apartment_description = """
This spacious 2-bedroom apartment is available for rent in downtown New York. The monthly rent is $2500.
It includes 1 bathrooms and a fully equipped kitchen with modern appliances.

Pets are welcome!

Please reach out to us at 555-123-4567 or john@realty.com
"""

# Define Pydantic model for structured data extraction
class ApartmentInfo(BaseModel):
    rent: float = Field(..., description="the monthly rent in dollars")
    bedrooms: int = Field(..., description="the number of bedrooms")
    bathrooms: int = Field(..., description="the number of bathrooms")
    phone_number: str

# Initialize TeapotAI
teapot_ai = TeapotAI()

# Extract the apartment details
extracted_info = teapot_ai.extract(
    ApartmentInfo, 
    context=apartment_description
)
print(extracted_info) # => ApartmentInfo(rent=2500.0 bedrooms=2 bathrooms=1 phone_number='555-123-4567')
