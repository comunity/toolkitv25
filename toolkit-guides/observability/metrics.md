# Metrics



> The ComUnity Platform's metrics functionality is a crucial component for monitoring your project's performance, providing an in-depth view of various operational aspects through the Metrics dashboard. This dashboard presents critical data points and trends that are vital for maintaining and optimising your project's health and performance.

The ComUnity Platform’s metrics functionality is a crucial component for monitoring your project’s performance, providing an in-depth view of various operational aspects through the Metrics dashboard. This dashboard presents critical data points and trends that are vital for maintaining and optimising your project’s health and performance.

The Metrics dashboard is one of three core components of the ComUnity Platform’s Observability framework, alongside [Traces](traces.md) and [Client Analytics](client-analytics.md).

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
