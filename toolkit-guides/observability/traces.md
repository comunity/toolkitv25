# Traces

> The ComUnity Developer Toolkit offers tracing capabilities through the integration of [Jaeger](https://www.jaegertracing.io/docs/1.55/) and [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/), providing a robust and user-friendly interface for monitoring and troubleshooting your projects. This integration provides a rich set of features to enhance your observability strategy, particularly in identifying and resolving issues efficiently.

The ComUnity Developer Toolkit offers powerful tracing capabilities through the integration of [Jaeger ](https://www.jaegertracing.io/docs/1.23/architecture/apis/)and [OpenTelemetry](https://opentelemetry.io/), providing a robust and intuitive interface for monitoring and troubleshooting your projects.

Tracing is a key part of the ComUnity Platform’s Observability framework, complementing Metrics (system performance data) and Client Analytics (user activity insights).

While [Metrics](metrics.md) present aggregated performance indicators, Traces capture the complete journey of individual requests across the system, from the user interface through backend services, giving teams detailed visibility into how each component interacts during execution.

## **Key Benefits**

1. **Detailed Insight**: Obtain a granular view of your application's transactions and workflows. Tracing allows you to follow individual requests as they travel through your application, providing visibility into the lifecycle of each request and how different components interact.
2. **Performance Optimisation**: Identify performance bottlenecks and inefficiencies within your application. By visualising the flow and duration of requests, you can pinpoint areas where latency occurs, enabling targeted optimisations to improve overall performance.
3. **Error Identification and Troubleshooting**: Quickly detect and diagnose issues within your application. The traces dashboard highlights errors and exceptions, allowing you to trace them back to their source, understand the context, and resolve issues more efficiently.
4. **Root Cause Analysis**: Delve into the specifics of any issue or anomaly in your application. Tracing provides the detailed context necessary for comprehensive root cause analysis, helping you understand not just what went wrong, but why.
5. **Collaboration and Communication**: Share insights and findings with your team. The dashboard's visual representations and detailed trace data facilitate clearer communication, enabling teams to collaborate effectively on diagnosing and resolving issues.

## Further Reading

* [OpenTracing Data Model](https://github.com/opentracing/specification/blob/master/specification.md#the-opentracing-data-model)

## Accessing the Traces Dashboard in Your Project

To fully utilise the Traces dashboard for your project, please adhere to the following instructions:

1.  **Access the Dashboard**: Navigate to the "**Observability**" menu item in the Toolkit. Here, select the "**Traces**" tab. You will then be presented with the Traces dashboard, which provides a comprehensive view of your project's trace data.\


    <figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption><p>Traces</p></figcaption></figure>
