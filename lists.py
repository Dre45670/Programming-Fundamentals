# List of EC2 instance
instance_id = ["i-1234", "i-5678", "i-9012"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]

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

# Remove EC2 instance ID from the list
instance_id.remove("i-1234")
print ("After removing an instance ID")
print (f"EC2 Instances: {instance_id}")

# Check if an instance ID is in the list
if "10.0.0.4" in ip_addresses:
    print("Yes, 10.0.0.4 is in the list.")
else: 
    print("No, 10.0.0.4 is not in the list.")
    print(f"IP Addresses: {ip_addresses}")

# Slicing a list
# First 2 AZs
first_two_azs = availability_zones[:2]
print("First 2 Availability Zones:", first_two_azs)

#Sorting a list
instance_id.sort()
print("Sorted EC2 Instance IDs:", instance_id)

# Finding the length of a list
number_of_ips = len(ip_addresses)
print(f"Number of IP addresses: {number_of_ips}")

# Accessing a list of items by index
first_az = availability_zones[0]
last_az = availability_zones[-1]
print(f"First Availability Zone: {first_az}")
print(f"Last Availability Zone: {last_az}")