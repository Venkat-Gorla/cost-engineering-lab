"""
uv run tools/dynamodb_metrics.py
"""

from datetime import UTC, datetime, timedelta
import boto3


TABLE_NAME = "cost-engineering-lab-02-events"
NAMESPACE = "AWS/DynamoDB"


def get_metric_sum(cloudwatch, metric_name, start_time, end_time) -> float:
    response = cloudwatch.get_metric_statistics(
        Namespace=NAMESPACE,
        MetricName=metric_name,
        Dimensions=[
            {
                "Name": "TableName",
                "Value": TABLE_NAME,
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=60,
        Statistics=["Sum"],
    )

    return sum(
        datapoint["Sum"]
        for datapoint in response["Datapoints"]
    )


def main() -> None:
    cloudwatch = boto3.client("cloudwatch")

    end_time = datetime.now(UTC)
    start_time = end_time - timedelta(minutes=10)

    consumed_writes = get_metric_sum(
        cloudwatch,
        "ConsumedWriteCapacityUnits",
        start_time,
        end_time,
    )

    consumed_reads = get_metric_sum(
        cloudwatch,
        "ConsumedReadCapacityUnits",
        start_time,
        end_time,
    )

    print("DynamoDB Metrics")
    print("-" * 40)
    print(f"Table      : {TABLE_NAME}")
    print("Time Window: Last 10 minutes")
    print()
    print(f"Consumed Write Capacity Units: {consumed_writes:.2f}")
    print(f"Consumed Read Capacity Units : {consumed_reads:.2f}")


if __name__ == "__main__":
    main()
