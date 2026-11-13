# AWS EC2 Start and Stop Automation using Lambda and EventBridge

## Project Overview
This project automates the starting and stopping of Amazon EC2 instances using AWS Lambda, Amazon EventBridge Scheduler, IAM, and Python Boto3.

The objective is to reduce unnecessary EC2 running time and automate cloud resource management.

## Architecture
EventBridge Scheduler → AWS Lambda → IAM Execution Role → Amazon EC2

## AWS Services Used
- Amazon EC2 – Virtual server
- AWS Lambda – Executes Python automation code
- Amazon EventBridge Scheduler – Triggers Lambda at scheduled times
- AWS IAM – Manages permissions
- Amazon CloudWatch – Stores Lambda execution logs
- Boto3 – AWS SDK for Python

## How It Works
1. EventBridge Scheduler invokes the Lambda function at the configured time.
2. EventBridge passes a JSON payload containing the requested action.
3. Lambda reads the action from the event.
4. Boto3 calls the EC2 StartInstances or StopInstances API.
5. EC2 starts or stops based on the requested action.

## Sample Event Payloads

**Start EC2**
```json
{
  "action": "start"
}
```

**Stop EC2**
```json
{
  "action": "stop"
}
```

## Key Learnings
- Creating IAM roles and least-privilege policies.
- Writing AWS Lambda functions using Python.
- Using Boto3 to manage EC2 instances.
- Configuring EventBridge schedules.
- Passing JSON event payloads to Lambda.
- Automating cloud infrastructure operations.

## Security Notes
- Use IAM permissions scoped to the required EC2 instance.
- Never upload AWS access keys, secret keys, passwords, or account credentials.
- Replace example instance IDs and account IDs with your own values when configuring AWS.
- Review AWS billing and remove unused resources after testing.