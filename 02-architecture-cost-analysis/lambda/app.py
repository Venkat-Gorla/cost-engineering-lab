from uuid import uuid4
from datetime import datetime, UTC
import json

import boto3


TABLE_NAME = "cost-engineering-lab-02-events"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def write_event(item: dict) -> None:
    table.put_item(Item=item)


def lambda_handler(event, context):
    item = {
        "id": str(uuid4()),
        "timestamp": datetime.now(UTC).isoformat(),
        "message": "Hello from Lambda!",
        "source": "cost-engineering-lab",
    }

    write_event(item)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Event written successfully.",
                "id": item["id"],
            }
        ),
    }
