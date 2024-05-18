# Cloud_optimization
In this GitHub README file, we'll document the project titled "Cloud Cost Optimization for AWS", which aims to automate the process of identifying and deleting stale EBS snapshots in AWS, thereby optimizing storage costs. This project leverages AWS Lambda for automation and Amazon EventBridge for scheduling the cleanup process.

# Project Overview
Our goal was to develop a system that automatically manages AWS EBS snapshots to prevent unnecessary storage costs. By identifying and removing snapshots that are no longer associated with any active EC2 instances, we aim to streamline our cloud infrastructure and maintain optimal resource utilization.

# Architecture
The project consists of three primary components integrated within the AWS ecosystem:

# AWS Lambda Function: 
Acts as the core component responsible for listing all EBS snapshots owned by the account, checking for those not associated with any active EC2 instances, and deleting them.
# Amazon EventBridge: 
Serves as the scheduler, triggering the Lambda function at predefined intervals (e.g., daily) to ensure regular cleanup of stale snapshots.
# AWS IAM Roles and Policies: 
Ensures that the Lambda function has the necessary permissions to list and delete EBS snapshots and that EventBridge can invoke the Lambda function.

# Detailed Steps and Code Explanation
# Step 1: Setting Up the AWS Environment
Before diving into coding, we ensured our AWS account was properly configured with an IAM user having the necessary permissions to manage EC2 instances and EBS snapshots.

# Step 2: Creating the AWS Lambda Function
We navigated to the AWS Lambda console and created a new function, selecting Python 3.8 as the runtime. We assigned an IAM role with permissions to interact with EC2 and EBS services.

# Step 3: Writing the Lambda Function Code
The Lambda function begins by initializing clients for EC2 and EBS services. It then retrieves all snapshots owned by the account and filters them to find those that are stale (not associated with any active EC2 instances). Finally, it deletes these identified snapshots.

# Step 4: Configuring the Lambda Function
We ensured the Lambda function had the necessary IAM permissions and configured it to be triggered by Amazon EventBridge.

# Step 5: Scheduling with Amazon EventBridge
We set up an EventBridge rule to trigger the Lambda function at regular intervals, ensuring the cleanup process runs automatically.

# Testing and Monitoring
After deployment, we tested the Lambda function manually to verify its operation and monitored its execution via CloudWatch Logs to ensure it was successfully identifying and deleting stale snapshots.

# Conclusion
Through this project, we've implemented a robust solution for managing AWS EBS snapshots, significantly contributing to our cloud cost optimization efforts. By leveraging AWS services like Lambda and EventBridge, we've automated a critical aspect of our cloud infrastructure management, ensuring efficient use of resources and cost savings.
