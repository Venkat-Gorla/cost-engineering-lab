"""
uv run tools/invoke.py
uv run tools/invoke.py --count 5
"""
import argparse
import json
import boto3


FUNCTION_NAME = "cost-engineering-lab-02-lambda"


def print_response_payload(response_payload: dict) -> None:
    status_code = response_payload.get("statusCode")
    print(f"\nStatus Code: {status_code}")

    body = response_payload.get("body")
    if isinstance(body, str):
        body = json.loads(body)

    print("\nResponse:")
    print(json.dumps(body, indent=2))


def invoke(function_name: str, count: int) -> None:
    client = boto3.client("lambda")

    for i in range(count):
        response = client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
        )

        response_payload = json.loads(response["Payload"].read())

        print(f"Invocation {i + 1}")
        print_response_payload(response_payload)
        if i < count - 1:
            print("\n" + "-" * 40)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    args = parser.parse_args()

    invoke(FUNCTION_NAME, args.count)


if __name__ == "__main__":
    main()
