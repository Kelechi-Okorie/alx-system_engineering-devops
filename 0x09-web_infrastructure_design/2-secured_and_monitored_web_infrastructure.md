# Some resources used in this infrastructure

## Additional elements to this infrastructure
- Monitoring client is used for monitoring operations
- SSL Certificate is used to make sure the traffic is served over https
- Firewall - Is used to filter unauthorized traffics

## What firewall used for
Firewall is used for filtering unauthourized traffics

## Why is the traffic served over https
The traffic is served over https to provide encryption to the packets sent over the network

## Why monitoring is used
This is for measuring and collecting data

## How the monitoring tool is collecting data
- The monitoring tool collects data on the performance of the application and server resource utilization

## What to do if you want to monitor your seb server QPS
To monitor the QPS (Query Per Second) of a server
1. Select a monitoring tool
2. Intrument/integrate your web server with the monitoring tool by adding appropriate instrumentation or agens
3. Define metrics - Identify the specific QPS-related metrics you want to monitor
4. Configure alert - Set up alerts for QPS to receive notifications when it crosses certain thresholds
5. Dashbaord creation - create a monitoring dashboard to visualize QPS and other relted metrics
6. Collect and analyze data
7. Scale as needed
8. Logging - enable server access and error logging

## Why terminating SSL at the load balancer level is an issue
- Security issue - when ssl is terminated at the load balancer, decrypted traffic is then transmitted within the internal network. This means anyone with access to internal network can potentially intercept unencrypted traffic, unless other measures are taken to ensure that does not happen

## Why having only one MySQL server capable of accepting writes is an issue
- This can cause Single Point of Failure

Why having server with all same components might be an issue
- Uniform vulnerability - If all server have same components they share the same vulnerabilities