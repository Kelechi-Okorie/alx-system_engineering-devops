# Explanation of concepts about this infrastructure

## Why additional elements were added

- A load balancer was added so to distribute the incoming request to different servers
- Two more web servers and application server were added to increase the throughput of the system
- A replicate MySQL server was added so that failure in one server would not cause a downtime in the system


## The distribution algorithm of the load balancer
The load balancer uses the Round Robin distribution algorithm - This works by distributing the incoming requests to every other server

## Is the load balancer Active-Active or Active-Passive
- In active-active setup, both load balancers are actively distributing traffic simultaneously
- In active-passive setup, one load balancer is active and actively distributing traffic, while the other is passive and only takes over when the active one fails  

Only one single load balancer is used in this infrastructure design, as such, it is neither active-active nor active-passive

## How database primary-replica (master-slave) cluster work
- This is common setup where primary database (master) and one or more replica databases (slaves) work to maintain data consistency
- The primary database is the authoritative source of data,handling all read and write operations
- The replica database are read-only copies of the primary database, they are typically used for read-heavy operations

## Difference between primary node and replica node in regard to application
- The primary node of a database is responsible for all write and data modification operations
- the replica node is responsible primarily for read operations

## Issue with this infrastructure
- The Single Point Of Failure exist in the load balancer. Since there's only one load balancer, if it were to fail, the entire system would fail
- The system does not have firewall so it is open to all sorts of traffics
- There is no monitoring in the system, so it is hard to measure what is happening
