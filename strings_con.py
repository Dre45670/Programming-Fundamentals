# Define the AWS account ID
account_id = "123456789012"

# Define the project name
project_name = "cloud engineering project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + "-" + project_name + "-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")

# Exercise EC2 String Concatenation

# Environment name, production, staging, or development
environment_name = "production"

# Application name
application_name = "EC2"

# Instance number
instance_number = "01"

# Concatenate
instance_name = environment_name + "-" + application_name + "-instance-" + instance_number

# Print
print(f"EC2 Instance Name: {instance_name}")
# Print