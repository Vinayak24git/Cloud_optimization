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
This foundational step ensures that our AWS environment is correctly configured to support the project. It involves:

- Creating an AWS Account: If not already done, setting up an AWS account is crucial. This account will house all the resources   and configurations for the project.
- Setting Up IAM Users and Roles: We create an IAM user with sufficient permissions to manage EC2 instances and EBS snapshots. -  - This includes permissions to list, describe, and delete snapshots, as well as to list and stop/start EC2 instances. The IAM role attached to the Lambda function grants it the necessary permissions to execute these operations.

# Step 2: Creating the AWS Lambda Function
This step involves setting up the AWS Lambda service to host our custom code:

- Navigating to the AWS Lambda Console: We access the Lambda service within the AWS Management Console.
- Creating a New Lambda Function: We initiate the creation of a new Lambda function, specifying Python 3.8 as the runtime since   our code is written in Python. This choice allows us to leverage Python's extensive libraries and ease of use.
- Assigning an IAM Role: During the creation process, we assign an IAM role to the Lambda function. This role must have policies  granting it permissions to call AWS APIs related to EC2 and EBS services.

# Step 3: Writing the Lambda Function Code
The core logic of our project resides here:

- Initializing Clients: Our code initializes clients for both EC2 and EBS services using Boto3, the AWS SDK for Python. These clients enable our function to interact with AWS services programmatically.
- Retrieving Snapshots and Instances: The function retrieves all EBS snapshots owned by the account and lists all active EC2 instances (both running and stopped). This dual retrieval is crucial for comparing snapshots against active instances.
- Filtering Stale Snapshots: The function iterates over the snapshots, filtering out those that are not associated with any active EC2 instances. This association check is vital for identifying snapshots that are no longer needed.
- Deleting Stale Snapshots: Finally, the function deletes the identified stale snapshots, freeing up storage space.

# Step 4: Configuring the Lambda Function
Post-creation, we need to ensure the Lambda function is correctly configured:

- Setting Environment Variables: Although our initial implementation doesn't require external configuration through environment - variables, it's good practice to prepare for future enhancements or changes in AWS service endpoints.
- Testing the Function Locally: Before deploying, we test the Lambda function locally using the AWS SAM CLI or another local testing tool. This step helps catch any syntax errors or logical issues early.

# Step 5: Scheduling with Amazon EventBridge
To automate the snapshot cleanup process:

- Creating an EventBridge Rule: We navigate to the EventBridge service in the AWS Management Console and create a new rule. This rule specifies the Lambda function as its target and defines a schedule (e.g., daily) for triggering the function.
- Configuring the Rule Details: We specify the event pattern to match the schedule and ensure the rule is enabled. This setup ensures our Lambda function runs automatically according to the defined schedule.

# Testing and Monitoring
After deployment, we:

- Manually Invoke the Lambda Function: To confirm everything is set up correctly, we manually invoke the Lambda function once or twice. This step helps verify that the function executes without errors and performs the intended operations.
- Monitor Execution with CloudWatch Logs: We use Amazon CloudWatch Logs to monitor the execution of our Lambda function. This monitoring provides insights into the function's behavior, including successful deletions and any errors encountered during execution.


# Conclusion
Through this project, we've implemented a robust solution for managing AWS EBS snapshots, significantly contributing to our cloud cost optimization efforts. By leveraging AWS services like Lambda and EventBridge, we've automated a critical aspect of our cloud infrastructure management, ensuring efficient use of resources and cost savings.
