#!/usr/bin/python3

class Review(BaseModel):
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
    text
    user_id
    place_id
    """
    text = ""
    user_id = ""
    place_id = ""
