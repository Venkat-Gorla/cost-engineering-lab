# Architecture Cost Analysis

## Problem

Cloud architectures are composed of multiple AWS services, each with its own pricing model. While the cost of an individual service can be understood in isolation, the total cost of an architecture is determined by the workload generated across its participating services.

This lab investigates how a serverless architecture generates costs across multiple AWS services and builds an intuition for analyzing architecture-level costs.

## Goal

Build a repeatable experiment that explains the cost of a simple AWS architecture.

The objective is to identify the cost contribution of each AWS service, independently validate its primary cost drivers, and explain how the combined service costs produce the overall architecture cost.

## 🧱 Architecture

```text
            Client
               │
               ▼
        AWS Lambda
               │
               ▼
      Amazon DynamoDB
               │
      ┌────────┴────────┐
      ▼                 ▼
 Amazon CloudWatch   DynamoDB APIs
      │                 │
      └────────┬────────┘
               ▼
      Engineering Analysis
               │
               ▼
      AWS Cost Explorer
               │
               ▼
          Validation
               │
               ▼
            Findings
```

## 🛠 Tech Stack

| **Category**      | **Technology**    |
| ----------------- | ----------------- |
| **Language**      | Python            |
| **Compute**       | AWS Lambda        |
| **Database**      | Amazon DynamoDB   |
| **Monitoring**    | Amazon CloudWatch |
| **Cost Analysis** | AWS Cost Explorer |

## Success Criteria

| **Check**                                       | **Status** |
| ----------------------------------------------- | ---------- |
| Architecture deployed                           | ✅         |
| Controlled workload generated                   | ✅         |
| Lambda cost drivers measured                    | ✅         |
| DynamoDB cost drivers measured                  | ✅         |
| Architecture cost validated against AWS billing | ⏳ Pending |
| Findings documented                             | ⏳ Pending |
