# Findings

- **2026-07-20** – For Amazon DynamoDB, the `DescribeTable` API's `ItemCount` did **not** immediately reflect recently written items during the experiment. To accurately verify the number of records persisted by the workload, the experiment used `Scan` with `Select=COUNT`, which returned the current item count.

- **2026-07-20** – A controlled workload of 1,000 successful `PutItem` operations resulted in 1,000 consumed write capacity units for the dataset used in this experiment, establishing a direct correlation between the application workload and the measured DynamoDB write capacity consumption.

- **2026-07-20** – Amazon DynamoDB request-unit metrics returned to zero after the measurement window elapsed, confirming that the CloudWatch metrics reflected recent request activity within the selected time window rather than cumulative request-unit consumption.
