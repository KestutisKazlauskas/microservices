
class ValidationError(Exception):
    """Raise validation errors"""

    def __init__(self, message):
        self.message = message