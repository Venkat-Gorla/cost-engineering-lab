"""
uv run tools/dynamodb_item_count.py
"""

import boto3


TABLE_NAME = "cost-engineering-lab-02-events"


def get_item_count(table_name: str) -> int:
    dynamodb = boto3.client("dynamodb")

    response = dynamodb.scan(
        TableName=table_name,
        Select="COUNT",
    )

    return response["Count"]


def main() -> None:
    count = get_item_count(TABLE_NAME)

    print("DynamoDB Item Count")
    print("-" * 40)
    print(f"Table      : {TABLE_NAME}")
    print()
    print(f"Total Items: {count}")


if __name__ == "__main__":
    main()
