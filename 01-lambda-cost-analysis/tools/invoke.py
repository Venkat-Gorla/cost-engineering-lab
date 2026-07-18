"""
uv run tools/invoke.py
"""
from __future__ import annotations

import json
import boto3

FUNCTION_NAME = "cost-engineering-lab-01-lambda"


def main() -> None:
    client = boto3.client("lambda")

    response = client.invoke(
        FunctionName=FUNCTION_NAME,
        Payload=json.dumps({"sleep_ms": 100}),
    )

    response_payload = json.loads(response["Payload"].read())
    print(json.dumps(response_payload, indent=2))


if __name__ == "__main__":
    main()
