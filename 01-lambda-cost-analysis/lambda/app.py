import time
from typing import Any


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    Simple Lambda workload used for cost analysis.

    Event Parameters
    ----------------
    sleep_ms:
        Time in milliseconds to sleep before returning.
    """

    sleep_ms = int(event.get("sleep_ms", 100))

    start = time.perf_counter()
    time.sleep(sleep_ms / 1000)
    elapsed_ms = (time.perf_counter() - start) * 1000

    return {
        "status": "success",
        "sleep_ms": sleep_ms,
        "elapsed_ms": round(elapsed_ms, 2),
    }
