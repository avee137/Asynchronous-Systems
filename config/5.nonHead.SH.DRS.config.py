# test case name.  can be used to trigger test case specific code in client,
# e.g., to generate special request sequences or validate intermediate or
# final values of object state. [2017-09-12: added this item]
test_case_name = failure_at_head_change_operation

# logfile_path=/Users/adityatomer/Desktop/Asynchronous-Systems/
logfile_name=run_system
logfile_path=/Users/adityatomer/Desktop/Asynchronous-Systems/logs/

# number of failures to tolerate.  number of replicas is 2t+1.
t = 1
# number of clients
num_client = 1
num_replica = 3
# client timeout, in milliseconds.  if timer expires, resend request 
# to all replicas, as described in section 3.3.
client_timeout = 10
retransmission_case_replica_sleep_time=0
# timeout, in seconds, for head and non-head servers, respectively:
# if timer expires, send reconfiguration request to Olympus, as described 
# in section 3.3.
head_timeout = 5
nonhead_timeout = 5
max_retransmission_counter=1
client_retransmission_timeout=10
# MAPPING OF PROCESSES TO HOSTS
# to simplify changing the hosts, we first specify a semicolon-separated
# list of hosts, and then use 0-based indices into that list to specify the
# host on which each process runs.
# list of hosts used in this scenario
#192.168.0.3; 192.168.0.4
hosts = localhost; localhost;localhost
# host on which each client runs.  in this example, client 0 runs 
# on host 1, clients 1 and 2 run on host 0.
client_hosts = 1; 0; 0
# host on which each replica runs.  same in all configurations.
replica_hosts = 0; 1; 2

# CLIENT WORKLOAD
workload[1] = put('movie','star'); append('movie','wars'); slice('movie':'4:7');get('movie')
result[1] = "{'movie':'star'}"
# FAILURE SCENARIO
# failures(c,r) is the failure scenario for replica r in configuration c.
# configurations are numbered starting with 0.  replicas are numbered by
# position in the chain, starting from 0.  replicas without a specified
# failure scenario are failure-free.
failures[0,1] = shuttle(0,1),DropResultStatement();shuttle(0,1),change_operation()



