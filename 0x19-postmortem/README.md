Duration of the Outage:

Start: 2024-06-20 14:30 UTC
End: 2024-06-20 16:00 UTC
Impact:

The outage affected our e-commerce platform's checkout service.
Users were unable to complete purchases, resulting in a 100% checkout failure rate.
Approximately 65% of our active users during this period were impacted.
Root Cause:

A database connection pool exhaustion caused by an unhandled increase in concurrent transactions.
Timeline
14:30 UTC: Issue detected via monitoring alert indicating a spike in checkout failures.
14:32 UTC: On-call engineer notified and began investigation.
14:35 UTC: Initial investigation pointed towards possible database performance issues.
14:45 UTC: Database queries and logs reviewed; no immediate issues found.
15:00 UTC: Noticed increased error rates in the application logs related to database connections.
15:10 UTC: Assumed issue might be related to a recent application deployment; rolled back the deployment.
15:25 UTC: Rollback did not resolve the issue; escalated to the database team.
15:35 UTC: Database team identified connection pool exhaustion.
15:40 UTC: Temporary increase in connection pool size applied to mitigate immediate issue.
15:50 UTC: Confirmed that checkout service was restoring functionality.
16:00 UTC: Full service restored and monitored for stability.
Root Cause and Resolution
Root Cause:

The primary cause was the exhaustion of the database connection pool. A sudden increase in concurrent transactions led to more connections being requested than the pool could handle. This was due to a promotional event that led to higher-than-expected traffic.
Resolution:

The immediate fix involved increasing the size of the connection pool to handle the unexpected traffic surge.
In the long term, we will implement rate limiting on the checkout service and optimize database queries to reduce the number of connections required.
Corrective and Preventative Measures
Improvements:

Implement more robust traffic monitoring and alerting to predict and manage high load scenarios.
Conduct load testing more frequently, especially before promotional events.
Optimize database queries and application logic to reduce dependency on high numbers of database connections.
Improve error handling to degrade gracefully instead of outright failing under load.
