# Dictionaries
# - Store and retrieve information
# - Key And Vaules

# EC2
ec2_instance = {
    "instanceid": "i-123456abcdef",
    "instance_type": "t3.micro",
    "State": "running",
    "PublicIPAddress": "203.0.113.1"
}

instance_type = ec2_instance["instanceid"]
print(f"This is a {instance_type} instance.")

public_ip = ec2_instance.get("PublicIPAddress", "No public IP address assigned.")
print(f"The instance's Public IP Address: {public_ip}")

# Adding a new key-value pair to the dictionary
ec2_instance["AvailabilityZone"] = "us-east-1a"
ec2_instance["State"] = "stopped"
print(ec2_instance)

# Using pop()
rm_instance_type = ec2_instance.pop("instance_type")
print(f"removed instance type: {rm_instance_type}")
print(ec2_instance)

# Using Del
del ec2_instance["AvailabilityZone"]
print(ec2_instance)

