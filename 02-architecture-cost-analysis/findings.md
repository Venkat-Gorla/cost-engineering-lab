# Findings

- **2026-07-20** – For Amazon DynamoDB, the `DescribeTable` API's `ItemCount` did **not** immediately reflect recently written items during the experiment. To accurately verify the number of records persisted by the workload, the experiment used `Scan` with `Select=COUNT`, which returned the current item count.

- **2026-07-20** – A controlled workload of 1,000 successful `PutItem` operations resulted in 1,000 consumed write capacity units for the dataset used in this experiment, establishing a direct correlation between the application workload and DynamoDB write capacity consumption.

- **2026-07-20** – Amazon DynamoDB request-unit metrics returned to zero after the measurement window elapsed, confirming that the CloudWatch metrics reflected recent request activity within the selected time window rather than cumulative request-unit consumption.

- **2026-07-21** – AWS Cost Explorer reported **1,005 DynamoDB write request units**, matching the cumulative workload applied to the table (5 baseline items and 1,000 experimental writes), validating the measured write capacity consumption against AWS billing.

- **2026-07-21** – AWS Cost Explorer reported **25 DynamoDB read request units**. The experiment measured 17 request units during the observation window, with the remaining request units attributable to read activity outside the measurement window, demonstrating the difference between windowed operational metrics and daily billing totals.

- **2026-07-21** – AWS Cost Explorer reported **1,036 Lambda requests**, matching the cumulative invocations generated across the experiments (16 baseline invocations and 1,020 architecture workload invocations), validating the measured Lambda request activity against AWS billing.
