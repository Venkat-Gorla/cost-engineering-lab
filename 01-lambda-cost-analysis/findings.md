# Findings

- **2026-07-18** – The AWS Cost Explorer API is a billable service. Programmatic cost analysis should avoid unnecessary API requests and retrieve billing data only when needed.

- **2026-07-18** – During a cold start, the Lambda billed duration included both the initialization time and the function execution time. Subsequent warm invocations did not include an initialization phase, resulting in billed duration closely matching the function execution duration.

- **2026-07-19** – Validated that Lambda compute usage (GB-seconds) can be accurately derived from the configured memory allocation and the billed duration reported in Lambda `REPORT` logs. The calculated value (0.9625 GB-seconds) matched the AWS Billing dashboard (0.962 GB-seconds).
