# Findings

- **2026-07-20** – For Amazon DynamoDB, the `DescribeTable` API's `ItemCount` did **not** immediately reflect recently written items during the experiment. To accurately verify the number of records persisted by the workload, the experiment used `Scan` with `Select=COUNT`, which returned the current item count.
