"""
uv run tools/invoke.py
uv run tools/invoke.py --count 100
uv run tools/invoke.py --count 200
"""

import argparse
import json
import boto3


FUNCTION_NAME = "cost-engineering-lab-02-lambda"


def invoke(function_name: str, count: int) -> None:
    client = boto3.client("lambda")

    succeeded = 0
    failed = 0

    progress_interval = None
    next_progress = None

    if count > 100:
        progress_interval = max(1, count // 10)
        next_progress = progress_interval

    for i in range(1, count + 1):
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

        if next_progress is not None and (i >= next_progress or i == count):
            percent = int(i * 100 / count)
            print(f"Progress: {percent}% ({i}/{count})")
            next_progress += progress_interval

    print("\nInvocation Summary")
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
