"""
uv run tools/invoke.py
uv run tools/invoke.py --count 5
uv run tools/invoke.py --count 100 --sleep-ms 500
"""
from __future__ import annotations

import argparse
import json
import boto3

FUNCTION_NAME = "cost-engineering-lab-01-lambda"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Invoke an AWS Lambda function.")

    parser.add_argument(
        "--sleep-ms",
        type=int,
        default=100,
        help="Sleep duration inside the Lambda function (milliseconds).",
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of invocations.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    client = boto3.client("lambda")

    for i in range(args.count):
        response = client.invoke(
            FunctionName=FUNCTION_NAME,
            Payload=json.dumps({"sleep_ms": args.sleep_ms}),
        )

        response_payload = json.loads(response["Payload"].read())

        print(f"Invocation {i + 1}/{args.count}")
        print(json.dumps(response_payload, indent=2))
        print()


if __name__ == "__main__":
    main()
