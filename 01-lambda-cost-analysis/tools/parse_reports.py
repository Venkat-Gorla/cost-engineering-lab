"""
uv run tools/parse_reports.py
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterator
import re

import boto3

LOG_GROUP_NAME = "/aws/lambda/cost-engineering-lab-01-lambda"

REPORT_PATTERN = re.compile(
    r"REPORT RequestId: (?P<request_id>\S+)\s+"
    r"Duration: (?P<duration>[0-9.]+) ms\s+"
    r"Billed Duration: (?P<billed>[0-9]+) ms\s+"
    r"Memory Size: (?P<memory>[0-9]+) MB\s+"
    r"Max Memory Used: (?P<used>[0-9]+) MB"
    r"(?:\s+Init Duration: (?P<init>[0-9.]+) ms)?"
)


@dataclass
class LambdaExecutionReport:
    request_id: str
    duration_ms: float
    billed_duration_ms: int
    memory_size_mb: int
    max_memory_used_mb: int
    init_duration_ms: float | None


def get_log_stream_names(
    logs_client,
    log_group_name: str,
) -> Iterator[str]:
    paginator = logs_client.get_paginator("describe_log_streams")

    for page in paginator.paginate(logGroupName=log_group_name):
        for stream in page.get("logStreams", []):
            yield stream["logStreamName"]


def get_log_events(
    logs_client,
    log_group_name: str,
    log_stream_name: str,
) -> Iterator[dict]:
    response = logs_client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        startFromHead=True,
    )

    yield from response.get("events", [])


def extract_execution_reports(
    logs_client,
    log_group_name: str,
) -> list[LambdaExecutionReport]:
    reports: list[LambdaExecutionReport] = []

    for log_stream_name in get_log_stream_names(
        logs_client=logs_client,
        log_group_name=log_group_name,
    ):
        for event in get_log_events(
            logs_client=logs_client,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        ):
            match = REPORT_PATTERN.search(event["message"])

            if not match:
                continue

            reports.append(
                LambdaExecutionReport(
                    request_id=match["request_id"],
                    duration_ms=float(match["duration"]),
                    billed_duration_ms=int(match["billed"]),
                    memory_size_mb=int(match["memory"]),
                    max_memory_used_mb=int(match["used"]),
                    init_duration_ms=(
                        float(match["init"])
                        if match["init"] is not None
                        else None
                    ),
                )
            )

    return reports


def print_summary(
    reports: list[LambdaExecutionReport],
) -> None:
    if not reports:
        print("No execution reports found.")
        return

    print("Execution Report Summary")
    print("========================")

    print(f"Invocations     : {len(reports)}")
    print(
        f"Cold Starts     : "
        f"{sum(r.init_duration_ms is not None for r in reports)}"
    )
    print(
        f"Warm Starts     : "
        f"{sum(r.init_duration_ms is None for r in reports)}"
    )

    average_duration = sum(
        r.duration_ms for r in reports
    ) / len(reports)

    average_billed = sum(
        r.billed_duration_ms for r in reports
    ) / len(reports)

    total_billed = sum(
        r.billed_duration_ms for r in reports
    )

    memory_mb = reports[0].memory_size_mb

    print(f"Memory Size     : {memory_mb} MB")
    print(f"Avg Duration    : {average_duration:.2f} ms")
    print(f"Avg Billed      : {average_billed:.2f} ms")
    print(f"Total Billed    : {total_billed} ms")


def main() -> None:
    logs_client = boto3.client("logs")

    reports = extract_execution_reports(
        logs_client=logs_client,
        log_group_name=LOG_GROUP_NAME,
    )

    print_summary(reports)


if __name__ == "__main__":
    main()
