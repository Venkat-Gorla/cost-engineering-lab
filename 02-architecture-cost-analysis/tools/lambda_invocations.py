"""
uv run tools/lambda_invocations.py
"""

from datetime import UTC, datetime
import boto3


FUNCTION_NAME = "cost-engineering-lab-02-lambda"

START_TIME = datetime(2026, 7, 19, tzinfo=UTC)
PERIOD = 86400  # 1 day


def get_total_invocations(function_name: str) -> int:
    cloudwatch = boto3.client("cloudwatch")

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/Lambda",
        MetricName="Invocations",
        Dimensions=[
            {
                "Name": "FunctionName",
                "Value": function_name,
            }
        ],
        StartTime=START_TIME,
        EndTime=datetime.now(UTC),
        Period=PERIOD,
        Statistics=["Sum"],
    )

    total = sum(
        int(datapoint["Sum"])
        for datapoint in response.get("Datapoints", [])
    )

    return total


def main() -> None:
    total = get_total_invocations(FUNCTION_NAME)

    TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"

    print("Lambda Invocations")
    print("-" * 40)
    print(f"Function   : {FUNCTION_NAME}")
    print(f"Start Time : {START_TIME.strftime(TIME_FORMAT)}")
    print(f"End Time   : {datetime.now(UTC).strftime(TIME_FORMAT)}")
    print()
    print(f"Total Invocations : {total}")


if __name__ == "__main__":
    main()
