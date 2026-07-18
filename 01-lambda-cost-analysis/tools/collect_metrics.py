"""
uv run tools/collect_metrics.py
"""
from __future__ import annotations

from datetime import UTC, datetime, timedelta
import boto3
from pprint import pprint

FUNCTION_NAME = "cost-engineering-lab-01-lambda"
NAMESPACE = "AWS/Lambda"


def print_lambda_metrics(response) -> None:
    print("Lambda Metrics")
    print("==============")

    for result in response["MetricDataResults"]:
        value = result["Values"][0] if result["Values"] else 0

        if result["Id"] == "duration":
            print(f"Duration    : {value:.2f} ms")
        else:
            print(f"{result['Id'].capitalize():12}: {value}")


def main() -> None:
    client = boto3.client("cloudwatch")

    end_time = datetime.now(UTC)
    start_time = end_time - timedelta(minutes=30)

    response = client.get_metric_data(
        MetricDataQueries=[
            {
                "Id": "invocations",
                "MetricStat": {
                    "Metric": {
                        "Namespace": NAMESPACE,
                        "MetricName": "Invocations",
                        "Dimensions": [
                            {
                                "Name": "FunctionName",
                                "Value": FUNCTION_NAME,
                            }
                        ],
                    },
                    "Period": 60,
                    "Stat": "Sum",
                },
            },
            {
                "Id": "duration",
                "MetricStat": {
                    "Metric": {
                        "Namespace": NAMESPACE,
                        "MetricName": "Duration",
                        "Dimensions": [
                            {
                                "Name": "FunctionName",
                                "Value": FUNCTION_NAME,
                            }
                        ],
                    },
                    "Period": 60,
                    "Stat": "Average",
                },
            },
            {
                "Id": "errors",
                "MetricStat": {
                    "Metric": {
                        "Namespace": NAMESPACE,
                        "MetricName": "Errors",
                        "Dimensions": [
                            {
                                "Name": "FunctionName",
                                "Value": FUNCTION_NAME,
                            }
                        ],
                    },
                    "Period": 60,
                    "Stat": "Sum",
                },
            },
            {
                "Id": "throttles",
                "MetricStat": {
                    "Metric": {
                        "Namespace": NAMESPACE,
                        "MetricName": "Throttles",
                        "Dimensions": [
                            {
                                "Name": "FunctionName",
                                "Value": FUNCTION_NAME,
                            }
                        ],
                    },
                    "Period": 60,
                    "Stat": "Sum",
                },
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
    )

    print_lambda_metrics(response)


if __name__ == "__main__":
    main()
