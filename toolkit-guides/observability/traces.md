# Traces

> The ComUnity Developer Toolkit offers tracing capabilities through the integration of [Jaeger](https://www.jaegertracing.io/docs/1.55/) and [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/), providing a robust and user-friendly interface for monitoring and troubleshooting your projects. This integration provides a rich set of features to enhance your observability strategy, particularly in identifying and resolving issues efficiently.



The ComUnity Developer Toolkit offers powerful tracing capabilities through the integration of [Jaeger](https://www.jaegertracing.io/docs/1.23/architecture/apis/) and [OpenTelemetry](https://opentelemetry.io/), providing a robust and intuitive interface for monitoring and troubleshooting your projects.

Tracing is a key part of the ComUnity Platform's Observability framework, complementing Metrics (system performance data) and Client Analytics (user activity insights).

While [Metrics](https://comunity.gitbook.io/learning.comunityplatform/toolkit-guides/observability/metrics) present aggregated performance indicators, Traces capture the complete journey of individual requests across the system, from the user interface through backend services, giving teams detailed visibility into how each component interacts during execution.

## Types of Traces in the Toolkit

The ComUnity Developer Toolkit provides two distinct Traces interfaces depending on your access level and what you're investigating:

| Type                | Scope                                                      | Access Required                    | Navigation Path                  |
| ------------------- | ---------------------------------------------------------- | ---------------------------------- | -------------------------------- |
| **Platform Traces** | All platform infrastructure components across all projects | Toolkit Administrator              | Sidebar → Observability → Traces |
| **Project Traces**  | Single project's application request flows                 | Project User (with project access) | Project → Observability → Traces |

## Platform Traces

Platform Traces capture request flows across the ComUnity Platform's core infrastructure components. Use Platform Traces for:

* Infrastructure monitoring and health checks
* Cross-project debugging and investigation
* Platform service performance analysis
* DevOps troubleshooting

**What you'll see:** Core platform services such as `core_web.vm_dev`, `core_availability.vm_dev`, and other infrastructure components.

## Project Traces

Project Traces are scoped to a single project and display tracing specific to that project's application operations. Use Project Traces for:

* Application-level debugging
* Project-specific performance analysis
* Custom application request flows
* End-user request troubleshooting

**What you'll see:** Request flows through your project's application code and services.

{% hint style="info" %}
This page documents both interfaces. The interface sections below focus primarily on **Platform Traces**, which includes the enhanced Search Options. Project Traces follow a similar pattern but are scoped to your specific project.&#x20;
{% endhint %}

### Key Benefits

1. **Detailed Insight**: Obtain a granular view of your application's transactions and workflows. Tracing allows you to follow individual requests as they travel through your application, providing visibility into the lifecycle of each request and how different components interact.
2. **Performance Optimisation**: Identify performance bottlenecks and inefficiencies within your application. By visualising the flow and duration of requests, you can pinpoint areas where latency occurs, enabling targeted optimisations to improve overall performance.
3. **Error Identification and Troubleshooting**: Quickly detect and diagnose issues within your application. The traces dashboard highlights errors and exceptions, allowing you to trace them back to their source, understand the context, and resolve issues more efficiently.
4. **Root Cause Analysis**: Delve into the specifics of any issue or anomaly in your application. Tracing provides the detailed context necessary for comprehensive root cause analysis, helping you understand not just what went wrong, but why.
5. **Collaboration and Communication**: Share insights and findings with your team. The dashboard's visual representations and detailed trace data facilitate clearer communication, enabling teams to collaborate effectively on diagnosing and resolving issues.

### Further Reading

* [OpenTracing Data Model](https://github.com/opentracing/specification/blob/master/specification.md#the-opentracing-data-model)

## Accessing the Traces Dashboard

### Platform Traces Access

**Required Role:** Toolkit Administrator

1. Log in to the Toolkit with Toolkit Administrator credentials.
2. From the left sidebar, select **Observability** (under the Platform context).
3. Select the **Traces** tab.
4. Choose your target environment from the **Environment** dropdown (Development, QA, or Production).

{% hint style="info" %}
If you see a white screen or cannot access Platform Traces, verify that your account has the Toolkit Administrator role assigned.
{% endhint %}

### Project Traces Access

**Required Access:** Project User with project permissions

1. Log in to the Toolkit.
2. Open your project from the project list.
3. Navigate to **Observability** in the main menu.
4.  Select the **Traces** tab.<br>

    <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Traces</p></figcaption></figure>

## Platform Traces - Interface

The Platform Traces interface provides comprehensive search and filtering capabilities for locating traces across all platform components.

<figure><img src="../../.gitbook/assets/image (541).png" alt=""><figcaption><p>Platform Traces</p></figcaption></figure>

### Query Controls

The top section provides controls for managing your trace query:

| Control           | Description                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Time range**    | Filter traces by time period. Options include preset ranges (e.g., "Last 15 minutes") or custom date/time ranges. |
| **Traces limit**  | Maximum number of traces to retrieve. Default is 20. Increase this value to review more traces.                   |
| **Refresh**       | Execute the current query and reload trace results.                                                               |
| **Records found** | Displays the count of traces matching your current filters.                                                       |

### Search Options

The **Search options** panel provides advanced filtering capabilities. Click the panel header to expand or collapse the search options.

The panel includes utility icons:

* **Clear (⊗)** — Reset all search filters to default values
* **Refresh (↻)** — Re-execute the search with current filter settings

**Component**

Filter traces by the originating platform service or component.

| Field        | Description                      |
| ------------ | -------------------------------- |
| **Dropdown** | Select from available components |

The component list is **environment-specific**. When viewing the Development environment, only components that have generated traces in Development are shown. The same applies to QA and Production environments.

**Example platform components:**

* `core_web.vm_dev` — Core web service (Development)
* `core_web.vm_prod` — Core web service (Production)
* `core_availability.vm_dev` — Availability monitoring service (Development)

\{% hint style="info" %\} Component names include environment suffixes (e.g., `.vm_dev` for Development, `.vm_prod` for Production) to help identify the source environment. \{% endhint %\}

**Span Name**

Filter traces containing specific span names. Spans represent individual units of work within a trace.

| Field        | Description                      |
| ------------ | -------------------------------- |
| **Dropdown** | Select from available span names |

**Common span names:**

* `handler` — Request handler entry point
* `incoming_request` — Incoming HTTP request processing
* `handle` — Core request handling logic
* `brand` — Branding/theming operations
* `watch` — Monitoring/polling operations
* `GET /o/comcity/Campaign` — Specific HTTP endpoint operations

**Duration**

Filter traces based on execution time. This helps identify slow-performing requests or verify that operations complete within expected thresholds.

| Field              | Options               | Description                                        |
| ------------------ | --------------------- | -------------------------------------------------- |
| **Scope**          | `span`                | The scope to apply duration filtering              |
| **Operator (min)** | `>`                   | Greater than — find traces exceeding this duration |
| **Value (min)**    | e.g., `100ms`, `1.2s` | Minimum duration threshold                         |
| **Operator (max)** | `<`                   | Less than — find traces under this duration        |
| **Value (max)**    | e.g., `100ms`, `1.2s` | Maximum duration threshold                         |

**Duration format examples:**

* `100ms` — 100 milliseconds
* `1.2s` — 1.2 seconds
* `5s` — 5 seconds

**Common filter configurations:**

| Filter               | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| `> 1s`               | Find slow requests taking longer than 1 second |
| `< 100ms`            | Verify fast operations complete quickly        |
| `> 500ms` AND `< 2s` | Find requests in a specific performance range  |

**Tags**

Perform advanced filtering using metadata tags associated with trace spans. Different services and operations expose different tags.

| Field        | Options               | Description                              |
| ------------ | --------------------- | ---------------------------------------- |
| **Scope**    | `span`                | The scope to search for tags             |
| **Tag**      | Select a tag          | Choose from available tag names          |
| **Operator** | `=`                   | Equality operator for tag value matching |
| **Value**    | Select or enter value | The tag value to match                   |

\{% hint style="info" %\} If "No values found" appears in the value dropdown, the selected tag may not have indexed values, or no traces with that tag exist in the current time range. \{% endhint %\}

**Common tags in ComUnity Platform traces:**

| Tag                    | Description            | Example Values                 |
| ---------------------- | ---------------------- | ------------------------------ |
| `request.verb`         | HTTP method            | `GET`, `POST`, `PUT`, `DELETE` |
| `request.url`          | Request URL path       | `/o/comcity/Campaign`          |
| `response.status_code` | HTTP response code     | `200`, `404`, `500`            |
| `User`                 | Authenticated user     | `admin@example.com`            |
| `AppName`              | Application identifier | `comcity`                      |

### Trace Results List

The trace results display in a table format with the following columns:

| Column           | Description                                                        |
| ---------------- | ------------------------------------------------------------------ |
| **Trace ID**     | Unique identifier for the trace. Click to expand trace details.    |
| **Start time**   | Timestamp when the trace began (format: `YYYY-MM-DD HH:MM:SS.mmm`) |
| **Service name** | The primary service that handled the request                       |
| **Name**         | The operation or endpoint name                                     |
| **Duration**     | Total trace duration                                               |

**Visual indicators:**

* **Highlighted row** (green background) — Currently selected/expanded trace
* **Duration values** — Displayed in appropriate units (ms, s)

### Expanded Trace View

Click on any trace row to expand the detailed trace visualization below the results list.

#### Trace Header

The expanded view header displays:

* **Trace ID** with full identifier (e.g., `Trace - 7a5f87c25c4a97da918211ce7f2720ce`)
* **Service and operation summary** (e.g., `core_availability.vm_dev: watch (10.1 s)`)
* **Start timestamp**
* **Fullscreen toggle** icon (⤢) — Expand trace visualization to full screen

#### Timeline Header

The horizontal timeline shows time markers in milliseconds:

* Timeline progresses left to right
* Markers indicate elapsed time from trace start (e.g., `17.55 ms`, `35.09 ms`, `52.64 ms`, `70.18 ms`)

#### Service & Operation Breakdown

The waterfall visualization displays:

| Element             | Description                                             |
| ------------------- | ------------------------------------------------------- |
| **Service rows**    | Expandable rows showing service name and operation      |
| **Nested spans**    | Indented rows showing child operations within a service |
| **Duration bars**   | Green horizontal bars showing relative duration         |
| **Duration values** | Precise timing displayed to the right of each bar       |

**Example span hierarchy:**

```
▼ core_web.vm_dev  GET /o/comcity/Campaign     ████████ 5.94 ms
    ▼ handler                                   █ 12.03 µs
        ▼ incoming_request                      ██████ 5.93 ms
            handle                              ███ 1.31 ms
            brand                               █ 5.89 µs
```

**Duration units:**

* `µs` — Microseconds (millionths of a second)
* `ms` — Milliseconds (thousandths of a second)
* `s` — Seconds

## Understanding Traces: The Complete Request Journey

A trace shows the path a single request takes through your system, from start to finish.

**Example:** When a user clicks "Submit Payment"

A trace captures:

1. Web app receives click → sends API request (10ms)
2. API validates payment details (5ms)
3. API calls payment gateway (200ms) ← **This is slow!**
4. Payment gateway responds (50ms)
5. API updates database (15ms)
6. API returns success to web app (5ms)

**Total time:** 285ms, with payment gateway being the bottleneck (200ms out of 285ms)

Without a trace, you'd only know the request took 285ms—you wouldn't know WHERE the time was spent.

#### When to Use Traces

Use traces to answer these questions:

1. _**"Why is this request slow?"**_ — Trace shows which operation took the longest time
2. _**"Where did this error occur?"**_ — Trace highlights the failed step and shows what happened before/after
3. _**"Which services are involved in this workflow?"**_ — Trace visualises the complete dependency chain
4. _**"What's the normal flow for this request?"**_ — Trace shows the expected path through your system

## Finding a Trace

There are three main ways to locate a specific trace depending on what you're investigating.

### Method 1: From an Error Log (Most Common)

When investigating an issue, start by finding the relevant error in your logs. Every log entry in the ComUnity Platform includes a `trace_id` that links it to the complete request flow.

**Steps:**

1.  Search for errors in Logs:

    ```
    {service_name="payment-api"} |= "ERROR"
    ```
2. Click on an error log to expand it
3. Look for the `trace_id` field (e.g., `trace_id: "c33aa305656ce5f7b71db7bb85e54494"` or in headers as `x-b3-traceid`)
4. Copy the `trace_id`
5. Navigate to **Observability** → **Traces**
6. Paste the `trace_id` in the search box
7. Click **Search**

You'll see the complete flow of that failed request.

### Method 2: Browse Recent Traces

When you don't have a specific `trace_id` but want to explore system behavior or investigate patterns:

1. Navigate to **Observability** → **Traces**
2. Recent traces are displayed automatically
3. Use Search Options to filter by:
   * Component/Service name
   * Time range
   * Duration (find only slow traces)
   * Tags (e.g., status codes for errors only)

## Reading a Trace Visualisation

When you open a trace, you'll see a waterfall-style visualisation.

<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### The Timeline (Horizontal Axis)

* **Left to right** = Time progressing
* **Total duration** shown at the top (e.g., "494ms")
* Each bar represents one operation (called a "span")
* **Wider bars** = Longer duration = Potential problem

#### The Services (Vertical Sections)

* Each service gets its own horizontal section
* Bars within a section are operations within that service
* Nested bars show sub-operations (e.g., database query within an API call)

#### The Colours

Different colors indicate different states:

* **Blue/Green** — Successful operation
* **Red** — Error occurred in this operation
* **Yellow/Orange** — Warning or slower than expected

#### The Spans (Individual Bars)

Each bar is a "span" representing one operation.

**Click on any span to see:**

* Operation name (e.g., "database query", "HTTP request")
* Duration (how long it took)
* Status (success/error)
* Tags/attributes (additional context like query parameters, user ID)
* Error messages (if the span failed)

### Real Example: ComUnity Platform Request Trace

Here's an actual trace from the ComUnity Platform showing a News data request:

#### Trace Overview

* **Trace ID:** `c33aa305656ce5f7b71db7bb85e54494`
* **Request:** GET /o/testcampaigns0842042025/News
* **Total Duration:** \~492ms
* **Services Involved:** 2 (runtime, core\_web)
* **Status:** Success (200)

#### Request Flow Breakdown

```
Timeline (milliseconds):
0ms    ├─ GET /o/.../News (client-side)
       │  Service: runtime
       │  
687ms  ├─ GET /o/.../News (server receives)
       │  Service: core_web.vm_dev
       │  ├─ handler (0.009ms)
       │  │  └─ incoming_request (1.959ms)
       │  │     └─ handle (1.604ms)
       │  │        ├─ brand (0.025ms) [FAST]
       │  │        └─ process (1.549ms)
       │  │           ├─ auth (0.008ms) [FAST]
       │  │           └─ data_service (1.534ms)
       │  │              └─ request (401ms) ← **Slowest operation**
       │  │                 └─ client_http_session (401ms)
       │  │                    └─ Database call to localhost:82
       │  │
1089ms └─ response (402ms)

Total: 492ms (client perspective)
```

#### What This Trace Tells Us

**System is healthy:**

* Most operations complete in under 10ms
* Authentication and authorization are fast (< 1ms)
* No errors in the flow

**Potential optimization:**

* Database request takes 401ms out of 492ms total (81% of time)
* This is the bottleneck — if we need to improve performance, start here

#### Trace Attributes You'll See

In ComUnity Platform traces, you'll find these useful attributes:

**Request Information:**

* `request.verb`: HTTP method (GET, POST, etc.)
* `request.url`: Full request URL
* `Authorization`: Authentication header
* `User`: Logged-in user email
* `AppName`: Which application is being accessed

**Response Information:**

* `response.status_code`: HTTP status (200, 404, 500, etc.)
* `response.size`: Response body size in bytes
* `response.body`: Actual response content (in some spans)

**Code Location:**

* `code.file`: Source file where span was created
* `code.line`: Line number in source file

#### Finding Trace IDs in Your System

ComUnity Platform uses **B3 propagation** for trace IDs. You'll find them in:

**1. HTTP Headers:**

```
x-b3-traceid: c33aa305656ce5f7b71db7bb85e54494
x-b3-spanid: FFE22E60C089F488
x-b3-parentspanid: (parent span ID)
```

**2. Log Entries:**

```json
{
  "trace_id": "c33aa305656ce5f7b71db7bb85e54494",
  "span_id": "FFE22E60C089F488",
  "message": "Request processed successfully"
}
```

**3. Error Messages:** Trace IDs are automatically included in error logs for correlation.

### Example: Debugging a Slow API Request

**Problem:** Users report that the payment confirmation page is slow

#### Step 1: Find the Slow Request

From the Metrics dashboard, you notice P99 latency for the payment API is 5 seconds (normally 500ms).

#### Step 2: Get a Trace

Option A: Find an error log with a trace ID Option B: Browse recent traces and filter to payment-api with duration > 4 seconds

#### Step 3: Open the Trace

You see the timeline shows a total duration of 5.2 seconds.

#### Step 4: Identify the Bottleneck

Scanning the visualization, you notice:

* Most spans are under 50ms (green/blue, thin bars)
* ONE span is 4.8 seconds wide (much wider than others)
* It's labeled "database query: SELECT \* FROM orders WHERE..."

#### Step 5: Examine the Details

Click on the slow span to see:

```
Operation: database.query
Duration: 4,832ms
Status: Success
Query: SELECT * FROM orders WHERE customer_id = ? AND status = 'pending'
```

#### Step 6: Take Action

**Now you know:**

* The slow operation is a specific database query
* It's taking 4.8 seconds (out of 5.2 total)
* The query searches for pending orders by customer ID

**Next steps:**

* Check if the orders table has an index on customer\_id
* Consider caching frequent queries
* Optimize the query or add database indexes

#### Step 7: Verify the Fix

After implementing the fix:

1. Wait for new requests to generate new traces
2. Search for recent traces to the same endpoint
3. Verify the database query span is now under 100ms

### Common Trace Patterns

#### Healthy Trace

**Characteristics:**

* Total duration within acceptable range (e.g., <500ms for API)
* All spans are green/blue (no errors)
* Time distributed evenly across operations
* No single operation dominates

#### Slow External Dependency

**Characteristics:**

* Total duration is high
* One span (usually an external API call) is very wide
* Other operations are fast

**What this means:** Your code is fast, but you're waiting on an external service

**Actions:**

* Check if the external service is experiencing issues
* Consider adding timeout limits
* Implement caching if appropriate
* Add retry logic with exponential backoff

#### Error in Request Flow

**Characteristics:**

* One or more spans are red
* Trace may stop abruptly (if error caused request to fail)
* Error span shows error message in details

**Actions:**

* Check database connectivity
* Review error message in span details
* Look for related errors in Logs
* Check if database is overloaded (see Metrics)

#### Sequential Operations That Could Be Parallel

**Characteristics:**

* Multiple operations happen one after another
* Each waits for the previous to complete
* Total duration is the sum of all operations

**What this means:** Optimisation opportunity — refactor code to fetch data concurrently

### Linking Traces to Other Data

#### Trace → Logs

**When:** You see an error span in a trace **Action:** Look for log entries with the same trace\_id

#### Logs → Trace

**When:** You find an error in logs **Action:** Copy the trace\_id from the log and search for it in Traces

#### Metrics → Traces

**When:** Dashboard shows increased latency **Action:** Find traces from that time period with high duration

### Tips for Trace Analysis

**DO:**

* Start with the longest spans — they're usually the problem
* Check error spans first — errors often cause cascading slowness
* Compare to successful traces — see what's different
* Look for patterns — one slow request might be random; many indicate a real issue
* Use trace IDs from logs — they provide the most relevant context

**DON'T:**

* Assume one trace tells the whole story — look at multiple traces
* Ignore fast operations — sometimes the problem is something that should happen but doesn't
* Forget about sampling — not every request generates a trace
* Overlook nested spans — the real problem might be hidden in a sub-operation

### Common Trace Investigation Questions

_**"This trace looks normal, but users say it's slow"**_

Possible causes:

* Network latency between user and server (not captured in trace)
* Client-side rendering time (trace only shows server-side)
* Multiple sequential requests (each fast, but total UX is slow)

Action: Check Client Analytics for client-side performance data

_**"I see the error, but why did it happen?"**_

Look at:

* Tags/attributes on the error span — may include error details
* Spans before the error — what was the application doing just before failure?
* Logs with the same trace\_id — often have more detailed error messages

_**"The trace has many services - which one is the problem?"**_

Strategy:

1. Sort spans by duration (if visualization allows)
2. Identify the longest span
3. That service/operation is where to start investigation
4. Check if that service's Metrics show issues

### Next Steps

* **Found a slow operation?** → Check if Metrics show a pattern
* **See an error?** → Search Logs for detailed error messages
* **Need to be notified of trace errors?** → Set up Alerts _(coming soon)_

### Technical Details

The tracing system uses:

* **Jaeger** for trace visualisation
* **OpenTelemetry** for trace collection and instrumentation
* **Tempo** for trace storage
* **B3 Propagation** for trace context across services
