# Findings

- **2026-07-18** – The AWS Cost Explorer API is a billable service. Programmatic cost analysis should avoid unnecessary API requests and retrieve billing data only when needed.

- **2026-07-18** – During a cold start, the Lambda billed duration included both the initialization time and the function execution time. In this experiment, an execution duration of approximately 102 ms and an initialization duration of approximately 68 ms resulted in a billed duration of 171 ms.
