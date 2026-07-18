# Lambda Cost Analysis

## Problem

AWS Lambda is widely used for building serverless applications because of its automatic scaling and pay-per-use pricing model. While the pricing model appears simple, the actual cost of a Lambda workload depends on multiple factors including invocation count, execution duration, allocated memory, and generated logs.

Engineers often know how to deploy Lambda functions but lack an intuitive understanding of which runtime characteristics have the greatest impact on cost.

This lab investigates the relationship between Lambda execution behavior, CloudWatch metrics, and AWS billing.

## Goal

Build a repeatable experiment that measures the cost of running AWS Lambda workloads under different execution characteristics.

The experiment will:

- Deploy a simple Lambda function.
- Execute controlled workloads.
- Collect CloudWatch metrics.
- Correlate runtime metrics with AWS Cost Explorer.
- Document the observed billing behavior.

The objective is to understand **why** a Lambda workload costs what it does rather than simply calculating its final price.

## Architecture

```text
                Invoke Workload
                       │
                       ▼
                AWS Lambda Function
                       │
      ┌────────────────┴────────────────┐
      ▼                                 ▼
CloudWatch Metrics             CloudWatch Logs
      │
      ▼
AWS Cost Explorer
      │
      ▼
Python Analysis
      │
      ▼
Findings
```

## Technology Stack

- Python
- AWS Lambda
- Amazon CloudWatch
- AWS Cost Explorer API
- boto3

## Success Criteria

- Deploy and invoke a Lambda function programmatically.
- Generate multiple workload scenarios.
- Retrieve execution metrics from CloudWatch.
- Retrieve billing information from Cost Explorer.
- Explain how invocation count, execution duration, memory allocation, and logging contribute to overall Lambda cost.
- Document all findings with reproducible experiments.
