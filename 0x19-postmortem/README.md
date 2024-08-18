Duration:
The outage lasted from 10:15 AM to 11:45 AM UTC on August 16, 2024, resulting in a total downtime of 1 hour and 30 minutes.

Impact:
During the outage, the primary service affected was our e-commerce platform’s checkout process. Customers experienced delays and failures while trying to complete purchases, with approximately 75% of users being impacted. This led to a significant drop in conversion rates and a substantial number of abandoned carts.

Root Cause:
The root cause of the outage was a misconfiguration in the load balancer settings that caused traffic to be unevenly distributed across our backend servers, leading to server overload and failure.

Timeline
10:15 AM: Issue detected via monitoring alert indicating a spike in 5xx errors from the checkout API.
10:20 AM: On-call engineer notified and began initial investigation, suspecting a database performance issue.
10:30 AM: Further investigation revealed no abnormalities in database metrics. Focus shifted to application servers.
10:40 AM: Misleading path: Engineers investigated recent code deployments, suspecting a bug in the latest release. No issues were found in the code.
10:50 AM: Escalation to the infrastructure team after noticing uneven traffic distribution across servers.
11:00 AM: Root cause identified as a misconfigured load balancer after inspecting the load balancer logs and settings.
11:10 AM: Configuration updated to balance traffic correctly. Servers began recovering gradually.
11:45 AM: Full recovery confirmed; all services were functioning normally.
Root Cause and Resolution
Root Cause:
The outage was caused by a misconfiguration in the load balancer settings, specifically an incorrect algorithm used for traffic distribution. The round-robin algorithm, which was intended to evenly distribute traffic, was accidentally replaced with a sticky session configuration that directed all user traffic to a limited subset of backend servers. This resulted in the overloaded servers failing under the excessive load while others remained underutilized.

Resolution:
The issue was resolved by reconfiguring the load balancer to use the correct round-robin algorithm. Once the load balancer was reconfigured, traffic was evenly distributed across all available backend servers, allowing them to handle the incoming requests efficiently. The servers that had failed due to overload were restarted and returned to normal operation.

Corrective and Preventative Measures
Improvements:

Implement a stricter review process for changes to critical infrastructure components like the load balancer.
Enhance monitoring to include alerts for uneven traffic distribution across servers.
Conduct training sessions for engineers to understand the implications of different load balancer configurations.
