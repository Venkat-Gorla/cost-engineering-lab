# Lambda Cost Analysis

## Problem

AWS Lambda provides a simple pay-per-use pricing model, but the actual cost of a workload depends on multiple runtime characteristics.

While deploying Lambda functions is straightforward, understanding the relationship between execution behavior, CloudWatch metrics, and AWS billing is considerably less obvious.

This lab investigates the primary factors that influence Lambda cost and builds an intuition for explaining AWS billing.

## Goal

Build a repeatable experiment that measures and explains the cost of AWS Lambda workloads.

The objective is to understand **why** a Lambda workload costs what it does, rather than simply calculating its price.

## 🧱 Architecture

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

## 🛠 Tech Stack

| **Category**      | Technology        |
| ----------------- | ----------------- |
| **Language**      | Python            |
| **Compute**       | AWS Lambda        |
| **Monitoring**    | Amazon CloudWatch |
| **Cost Analysis** | AWS Cost Explorer |

## Success Criteria

- Deploy and execute a representative AWS Lambda workload.
- Measure the runtime characteristics of the workload.
- Correlate runtime metrics with AWS billing data.
- Explain the primary factors that contribute to Lambda cost.
- Document findings and key engineering insights.
