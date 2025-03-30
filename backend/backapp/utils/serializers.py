from django.core.serializers.json import DjangoJSONEncoder
from datetime import date

class DateAwareJSONEncoder(DjangoJSONEncoder):
    """Custom JSON encoder that properly handles date objects"""
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()  # Convert dates to 'YYYY-MM-DD' strings
        return super().default(obj)  # Default handling for other types