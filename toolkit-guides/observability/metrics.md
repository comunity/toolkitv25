---
description: >-
  The ComUnity Platform's metrics functionality is a crucial component for
  monitoring your project's performance, providing an in-depth view of various
  operational aspects through the Metrics dashboard.
---

# Metrics

The ComUnity Platform’s metrics functionality is a crucial component for monitoring your project’s performance, providing an in-depth view of various operational aspects through the Metrics dashboard. This dashboard presents critical data points and trends that are vital for maintaining and optimising your project’s health and performance.

The Metrics dashboard is one of four core components of the ComUnity Platform’s Observability framework, alongside [Traces](traces.md), [Client Analytics](client-analytics.md) and [Logs](logs.md).

While metrics focus on system performance, traces provide detailed request-level insights, and client analytics capture user behaviour and interaction data.

## **Key Benefits**

* **Comprehensive Performance Monitoring**: Gain insights into key performance indicators such as server response times, enabling you to detect and address performance issues proactively.
* **Informed Decision-Making**: Leverage detailed metrics to make informed decisions, ensuring your project's resources are optimised for peak performance.
* **Enhanced System Reliability**: Monitor system health and performance trends over time, aiding in the prevention of potential issues and ensuring system stability.

### **Detailed Insights Available on the Metrics Dashboard**

1. **Server Response Time**: This graph provides a real-time view of your server's response times, helping you identify trends and potential performance bottlenecks.
2. **Concurrent Responses**: Monitor the number of concurrent responses your server is handling to understand the load and performance under various conditions.
3. **Accumulative Users**: Track the growth of user engagement by viewing the cumulative number of users interacting with your project over time.
4. **Requests per Day (7 Days)**: Analyse the daily request volume over a week to identify usage patterns, peak times, and potential stress points on your infrastructure.

## **Accessing Your Project's Metrics Dashboard**

By default, the Metrics dashboard includes a set of standard panels that provide insights such as cumulative users and system performance statistics.

The available dashboards may change over time as new metrics are introduced or existing ones are refined. Some metrics may be temporarily disabled to reduce data noise or improve performance.

Metrics are configured and visualised through [Grafana](https://grafana.com/).

The default dashboards are automatically generated, but additional or customised dashboards can be created directly in[ Grafana](https://grafana.com/) where access permissions allow.

In shared or hosted environments, users may not have rights to modify or add dashboards.

Alerts can be configured in [Grafana](https://grafana.com/)  to notify your team when key thresholds are reached, for example, when disk usage or response times exceed defined limits.

Future updates will expand available dashboards and may allow users to select or configure which metrics are displayed directly within the platform.

1.  &#x20;Access the "**Metrics**" tab in the **Observability** section. The Metrics dashboard will automatically display, offering a detailed overview of your project's key performance metrics.\
    <br>

    <figure><img src="../../.gitbook/assets/image (393).png" alt=""><figcaption><p>Metrics </p></figcaption></figure>

### Understanding Your Metrics Dashboard

When you open the Metrics tab, you'll see your service's health dashboard with several panels showing different aspects of performance.

#### What the Metrics Tell You

**Server Response Time**

**What it shows:** How long your server takes to respond to requests

**Healthy range:**

* APIs: Under 500ms
* Web pages: Under 2 seconds
* Background processes: Depends on the task

**When to investigate:**

* Sudden spikes (may indicate performance issue)
* Gradual increase over time (may indicate resource exhaustion)
* Response time consistently above your target

**What to check:** If response time is high, look at the trace data to identify slow operations.

**Concurrent Responses**

**What it shows:** Number of requests being handled simultaneously

**What's normal:** Varies by service and traffic patterns

**When to investigate:**

* Unusually high (may indicate slow processing or stuck requests)
* Drops to zero during business hours (service may be down)

**What to check:** Compare with Request Rate - if requests are coming in but concurrent responses are low, check for errors.

**Accumulative Users**

**What it shows:** Total number of unique users who have accessed your application over time

**Use this to:**

* Track user growth trends
* Identify successful features or campaigns
* Compare across time periods

**Requests per Day (7 Days)**

**What it shows:** Daily volume of requests over the past week

**Use this to:**

* Identify usage patterns (weekday vs weekend)
* Spot unusual traffic spikes
* Capacity planning

**What's normal:** Consistent patterns with predictable peaks

**When to investigate:**

* Unexpected spikes (potential attack or viral content)
* Sudden drops (service issues or deployment problems)

### Reading the Graphs

#### Time Series Graphs

Most metrics are displayed as line graphs showing values over time.

**How to use them:**

1. **Hover over the line** to see exact values at specific times
2. **Click and drag** to zoom into a specific time period
3. **Compare patterns** - Does today look different from yesterday?

**What to look for:**

* **Spikes** - Sudden increases may indicate problems or unusual events
* **Drops** - Sudden decreases may indicate service outages
* **Trends** - Gradual changes over days/weeks indicate capacity needs

#### Understanding Percentiles&#x20;

You may see metrics labeled P99 or P95 - these are **percentiles**.

**P99 Latency = 500ms** means:

* 99% of requests complete in under 500ms
* Only 1% of requests are slower

**Why this matters:** Average response time can be misleading. If most requests are fast (50ms) but a few are very slow (10 seconds), the average might look okay while users are experiencing problems.

**Rule of thumb:**

* Focus on P99 for user-facing services (represents worst-case user experience)
* P95 is useful for understanding typical performance
* P50 (median) shows what "most users" experience

### Common Investigation Patterns

#### Pattern 1: Error Rate Increases

**You notice:** Error percentage panel shows 5% (was normally <1%)

**Steps:**

1. Note the time when errors started
2.  Navigate to Logs and search for errors during that time:

    ```
    {service_name="your-service"} |= "ERROR"
    ```
3. Examine error messages to identify the cause
4. If logs show a trace\_id, view the trace for detailed flow

#### Pattern 2: Latency Spike

**You notice:** Server Response Time suddenly increases

**Steps:**

1. Check if error rate also increased (errors often cause latency)
2. Look at Concurrent Responses - are requests backing up?
3. View traces from the spike period to identify slow operations
4. Common causes:
   * Slow database queries
   * External API timeouts
   * Memory/CPU exhaustion

#### Pattern 3: Traffic Drop

**You notice:** Requests per Day shows sudden decrease

**Steps:**

1. Check if service is actually down (Concurrent Responses = 0?)
2. Look for deployment events at that time
3. Check logs for startup errors or crashes
4. Verify with team if intentional (maintenance, feature flag change)

### Using Time Controls

#### Selecting Time Ranges

The time range selector (top right of dashboard) lets you focus on specific periods:

**Quick ranges:**

* Last 5 minutes - Real-time monitoring
* Last 1 hour - Recent issue investigation
* Last 24 hours - Daily pattern analysis
* Last 7 days - Weekly trend comparison

**Custom range:** Click the time range and select specific start/end dates

**Tip:** Use the refresh interval dropdown to auto-update dashboards every 5-30 seconds when actively monitoring.

#### Comparing Time Periods

To compare current performance to a baseline:

1. Note current metrics (e.g., response time = 800ms)
2. Change time range to yesterday at the same time
3. Compare values
4. Look for differences in patterns

**Example:** If latency is high now but was normal yesterday at the same time, it's likely a new issue (not normal load).

### When to Create an Alert

Dashboards are great for investigation, but you can't watch them 24/7. Create alerts for:

**Critical issues:**

* Error rate > 5%
* Server response time > 2 seconds for 5+ minutes
* Service becomes unreachable

**Capacity planning:**

* Database connections approaching limit
* Disk space < 20%
* Memory usage > 85%

**Business metrics:**

* Payment processing rate drops
* User signups below threshold

See Alerts for how to configure notifications.

### Tips for Daily Monitoring

#### ✅ DO:

* **Check dashboards regularly** (daily for production services)
* **Compare to historical data** - Is this normal for this time/day?
* **Investigate gradual changes** - Slow degradation is easy to miss
* **Use multiple metrics together** - Latency + Errors + Requests tells the full story

#### ❌ DON'T:

* **Panic at single spikes** - Brief anomalies are normal
* **Ignore sustained issues** - If it lasts >10 minutes, investigate
* **Forget about off-peak hours** - Problems can start when traffic is low
* **Rely only on dashboards** - Use logs and traces for root cause

### Next Steps

* **See elevated errors?** → Search Logs to find specific error messages
* **Identify slow requests?** → View Traces to see detailed request flow
* **Need to be notified?** → Set up Alerts for automatic notifications
* **Want custom metrics?** → Learn about Instrumentation

### Technical Details

The metrics system uses:

* [Grafana](https://grafana.com/docs/loki/latest/?pg=oss-loki\&plcmt=quick-links) for visualisation and dashboards
* [ Prometheus](https://prometheus.io/) for metrics collection and storage
* [Thanos](https://thanos.io/) for long-term metric retention

