from uuid import uuid4
from datetime import datetime, UTC
import json


def lambda_handler(event, context):
    item = {
        "id": str(uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "message": "Hello from Lambda!",
        "source": "cost-engineering-lab",
    }

    return {
        "statusCode": 200,
        "body": json.dumps(item),
    }
