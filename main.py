cpu_threshold = 85 #bugfix -> highest is 100 -> fixed now
memory_threshold = 80 
disk_threshold = 90
check_interval = 10 #bugfix -> negative interval not possible ->fixed now

print("Code using Vim")
print("Running health check")
print(f"Checking every {check_interval} seconds")
