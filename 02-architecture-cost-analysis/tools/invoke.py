"""
uv run tools/invoke.py
uv run tools/invoke.py --count 100
"""

import argparse
import json
import boto3


FUNCTION_NAME = "cost-engineering-lab-02-lambda"


def invoke(function_name: str, count: int) -> None:
    client = boto3.client("lambda")

    succeeded = 0
    failed = 0

    for _ in range(count):
        response = client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
        )

        response_payload = json.loads(response["Payload"].read())

        if (
            response.get("FunctionError") is None
            and response_payload.get("statusCode") == 200
        ):
            succeeded += 1
        else:
            failed += 1

    print("Invocation Summary")
    print("-" * 40)
    print(f"Total Invocations : {count}")
    print(f"Succeeded         : {succeeded}")
    print(f"Failed            : {failed}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()

    invoke(FUNCTION_NAME, args.count)


if __name__ == "__main__":
    main()
