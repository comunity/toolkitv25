# Traces

> The ComUnity Developer Toolkit offers tracing capabilities through the integration of [Jaeger](https://www.jaegertracing.io/docs/1.55/) and [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/), providing a robust and user-friendly interface for monitoring and troubleshooting your projects. This integration provides a rich set of features to enhance your observability strategy, particularly in identifying and resolving issues efficiently.

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

1. **Enable Observability**: Activate the observability feature in your project. For detailed instructions on enabling observability within the Toolkit, refer to the [Observability Integration](./#observability-integration) guide.
2.  **Access the Dashboard**: Once observability is enabled, navigate to the "**Observability**" tab. Here, select the "**Traces**" tab. You will then be presented with the Traces dashboard, which provides a comprehensive view of your project's trace data.\


    <figure><img src="../../.gitbook/assets/image (392).png" alt=""><figcaption><p>Traces</p></figcaption></figure>
