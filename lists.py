# List of EC2 instance
instance_id = ["i-1234", "i-5678", "i-9012"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

# List of availability zones in a region
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Print the lists
print(f"EC2 Instances to terminate: {instance_id}")
print(f"IP Addresses for security group: {ip_addresses}")
print(f"Availability Zones: {availability_zones}")

# Add new EC2 instance ID to the list
instance_id.append("i-3456")
print ("After adding a new instance ID")
print(f"EC2 Instances: {instance_id}")
