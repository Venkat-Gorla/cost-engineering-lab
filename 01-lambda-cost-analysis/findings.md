# Findings

- **2026-07-18** – The AWS Cost Explorer API is a billable service. Programmatic cost analysis should avoid unnecessary API requests and retrieve billing data only when needed.

- **2026-07-18** – During a cold start, the Lambda billed duration included both the initialization time and the function execution time. Subsequent warm invocations did not include an initialization phase, resulting in billed duration closely matching the function execution duration.
