# Control Structures / Control Flow
#instance_running = "broken"

# If Statements
#if instance_running == "running":
#    print("The EC2 is running.")
#elif instance_running == "stopped":
#    print("The EC2 is stopped.....")
#else:
#    print("The EC2 is in an unknown state.")

public_access_block = "true"

# Write the If Statement
#If condition
if public_access_block == "false":
    print("The S3 bucket is secure.")
#Else condition
else:
    print("The S3 bucket is not secure.")