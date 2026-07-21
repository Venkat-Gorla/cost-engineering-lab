# Lambda Cost Analysis

## Problem

AWS Lambda provides a simple pay-per-use pricing model, but the actual cost of a workload depends on multiple runtime characteristics.

While deploying Lambda functions is straightforward, understanding the relationship between execution behavior, CloudWatch metrics, and AWS billing is considerably less obvious.

This lab investigates the primary factors that influence Lambda cost and builds an intuition for explaining AWS billing.

## Goal

Build a repeatable experiment that measures and explains the cost of AWS Lambda workloads.

The objective is to understand how Lambda execution characteristics translate into AWS charges, rather than simply reading the final cost from AWS billing.

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
      │                                 │
      └────────────────┬────────────────┘
                       ▼
                Python Analysis
                       │
                       ▼
               AWS Cost Explorer
                       │
                       ▼
                    Findings
```

## Success Criteria

| Check                                   | Status |
| --------------------------------------- | ------ |
| Representative Lambda workload executed | ✅     |
| Runtime metrics collected               | ✅     |
| Lambda REPORT logs analyzed             | ✅     |
| Runtime correlated with AWS billing     | ✅     |
| Primary Lambda cost drivers explained   | ✅     |
| Findings documented                     | ✅     |
