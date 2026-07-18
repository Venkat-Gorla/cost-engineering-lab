"""
uv run tools/list_metrics.py
"""
import boto3

NAMESPACE = "AWS/Lambda"


def main() -> None:
    client = boto3.client("cloudwatch")
    response = client.list_metrics(Namespace=NAMESPACE,)

    unique_metric_names = {
        metric["MetricName"]
        for metric in response["Metrics"]
    }

    print("\nPrinting Lambda metric names:")
    print("=============================")
    for name in sorted(unique_metric_names):
        print(name)


if __name__ == "__main__":
    main()
