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

1. **Access the Dashboard**: Navigate to the "**Observability**" menu item in the Toolkit. Here, select the "**Traces**" tab. You will then be presented with the Traces dashboard, which provides a comprehensive view of your project's trace data.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption><p>Traces</p></figcaption></figure>

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

### When to Use Traces

Use traces to answer these questions:

1. **"**_**Why is this request slow?**_**"** - Trace shows which operation took the longest time
2. **"**_**Where did this error occur?**_**"** - Trace highlights the failed step and shows what happened before/after
3. **"**_**Which services are involved in this workflow?**_**"** - Trace visualises the complete dependency chain
4. **"**_**What's the normal flow for this request?**_**"** - Trace shows the expected path through your system

### Find a Traces&#x20;

There are three main ways to locate a specific trace depending on what you're investigating. The most common approach is starting from an error log, but you can also browse recent traces or navigate directly from dashboard metrics.

#### _Method 1_: From an Error Log (Most Common)

When investigating an issue, start by finding the relevant error in your logs. Every log entry in the ComUnity Platform includes a `trace_id`. that links it to the complete request flow.

**Steps:**

1.  Search for errors in Logs:

    ```
    {service_name="payment-api"} |= "ERROR"
    ```
2. Click on an error log to expand it
3. Look for the `trace_id` field (e.g., `trace_id: "c33aa305656ce5f7b71db7bb85e54494"` or in headers as `x-b3-traceid`)
4. Copy the `trace_id`.
5. Navigate to _**Observability**_ > _**Traces.**_
6. Paste the `trace_id`. in the search box.
7. Click _**Search**_

You'll see the complete flow of that failed request.

_<mark style="color:red;">**Screenshot needed:**</mark> <mark style="color:red;"></mark><mark style="color:red;">Log entry with trace\_id field highlighted</mark>_

#### _Method 2_: Browse Recent Traces

When you don't have a specific `trace_id` but want to explore system behavior or investigate patterns, you can browse recent traces directly in the dashboard.

1. Navigate to _**Observability**_ > _**Traces**_
2. Recent traces are displayed automatically (as shown in the screenshot above)
3. You can filter by:
   * Service name
   * Time range
   * Duration (find only slow traces)
   * Status (errors only)

### Reading a Trace Visualisation

When you open a trace, you'll see a waterfall-style visualisation.

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

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

* **Blue/Green** - Successful operation
* **Red** - Error occurred in this operation
* **Yellow/Orange** - Warning or slower than expected

#### The Spans (Individual Bars)

Each bar is a "span" representing one operation.

**Click on any span to see:**

* Operation name (e.g., "database query", "HTTP request")
* Duration (how long it took)
* Status (success/error)
* Tags/attributes (additional context like query parameters, user ID)
* Error messages (if the span failed)

**Screenshot needed:** Expanded span details view

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
* This is the bottleneck - if we need to improve performance, start here

**Service breakdown:**

* Client-side: 687ms (initial processing + network)
* Server-side processing: \~2ms (very fast)
* Database fetch: 401ms (main delay)
* Response assembly: <1ms

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
* Helpful for developers who need to fix issues

**Performance Data:**

* `startTimeUnixNano`: When operation started
* `endTimeUnixNano`: When operation completed
* Duration is calculated from these values

#### Finding Trace IDs in Your System

ComUnity Platform uses **B3 propagation** for trace IDs. You'll find them in:

**1. HTTP Headers:**

```
x-b3-traceid: c33aa305656ce5f7b71db7bb85e54494
x-b3-spanid: FFE22E60C089F488
x-b3-parentspanid: (parent span ID)
```

**2. Log Entries:** Look for fields like:

```json
{
  "trace_id": "c33aa305656ce5f7b71db7bb85e54494",
  "span_id": "FFE22E60C089F488",
  "message": "Request processed successfully"
}
```

**3. Error Messages:** Trace IDs are automatically included in error logs for correlation.

#### How to Use This Information

**Scenario: User reports slow page load**

1. **Find the trace ID** from the browser network tab or logs
2. **Open the trace** in Observability → Traces
3. **Identify the slowest span:**
   * In this example: `data_service → request` (401ms)
4. **Check the attributes:**
   * `request.url` shows which database endpoint was called
   * `code.file` and `code.line` show where in code this happens
5. **Take action:**
   * Database query might need optimization
   * Consider adding caching
   * Check if database is under load

### Example: Debugging a Slow API Request

**Problem:** Users report that the payment confirmation page is slow

#### Step 1: Find the Slow Request

From the Metrics dashboard, you notice P99 latency for the payment API is 5 seconds (normally 500ms).

**Screenshot needed:** Metrics dashboard showing high latency

#### Step 2: Get a Trace

Option A: Find an error log with a trace ID\
Option B: Browse recent traces and filter to payment-api with duration > 4 seconds

#### Step 3: Open the Trace

You see the timeline shows a total duration of 5.2 seconds.

**Screenshot needed:** Trace showing 5.2 second total duration

#### Step 4: Identify the Bottleneck

Scanning the visualization, you notice:

* Most spans are under 50ms (green/blue, thin bars)
* ONE span is 4.8 seconds wide (much wider than others)
* It's labeled "database query: SELECT \* FROM orders WHERE..."

**Screenshot needed:** Trace with one very wide span highlighted

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

**Result:** Problem identified and resolved using trace analysis

### Common Trace Patterns

#### Healthy Trace

**Characteristics:**

* Total duration within acceptable range (e.g., <500ms for API)
* All spans are green/blue (no errors)
* Time distributed evenly across operations
* No single operation dominates

**Example:**

* Request received: 5ms
* Business logic: 50ms
* Database query: 80ms
* Response serialization: 10ms
* **Total: 145ms** \[HEALTHY]

_<mark style="color:$danger;">**Screenshot needed:**</mark> <mark style="color:$danger;"></mark><mark style="color:$danger;">Example of healthy trace</mark>_

#### Slow External Dependency

**Characteristics:**

* Total duration is high
* One span (usually an external API call) is very wide
* Other operations are fast

**Example:**

* Request received: 5ms
* Business logic: 10ms
* **External payment gateway: 2,800ms** \[SLOW]
* Database update: 15ms
* **Total: 2,830ms**

**What this means:** Your code is fast, but you're waiting on an external service

**Actions:**

* Check if the external service is experiencing issues
* Consider adding timeout limits
* Implement caching if appropriate
* Add retry logic with exponential backoff

**Screenshot needed:** Trace showing slow external call

#### Error in Request Flow

**Characteristics:**

* One or more spans are red
* Trace may stop abruptly (if error caused request to fail)
* Error span shows error message in details

**Example:**

* Request received: 5ms
* Validate user: 10ms
* **Database query: ERROR - Connection timeout** \[ERROR]
* (Request ends here - no further operations)

**What this means:** The request failed during database access

**Actions:**

* Check database connectivity
* Review error message in span details
* Look for related errors in Logs
* Check if database is overloaded (see Metrics)

**Screenshot needed:** Trace with error span

#### Sequential Operations That Could Be Parallel

**Characteristics:**

* Multiple operations happen one after another
* Each waits for the previous to complete
* Total duration is the sum of all operations

**Example:**

* Fetch user data: 100ms
* Fetch order history: 100ms
* Fetch payment methods: 100ms
* **Total: 300ms** (could be \~100ms if done in parallel)

**What this means:** Optimisation opportunity

**Actions:**

* Refactor code to fetch data concurrently
* Potential 3x speedup in this example

### Linking Traces to Other Data

#### 1. Trace → Logs

**When:** You see an error span in a trace\
**Action:** Look for log entries with the same trace\_id

Many trace visualisations have a "View Logs" button that automatically filters logs to that trace ID.

#### 2. Logs → Trace

**When:** You find an error in logs\
**Action:** Copy the trace\_id from the log and search for it in Traces

This gives you the complete context around the error.

#### 3. Metrics → Traces

**When:** Dashboard shows increased latency\
**Action:** Find traces from that time period with high duration

This helps you understand what changed to cause the slowness.

### Tips for Trace Analysis

#### ✅ DO:

* **Start with the longest spans** - They're usually the problem
* **Check error spans first** - Errors often cause cascading slowness
* **Compare to successful traces** - See what's different
* **Look for patterns** - One slow request might be random; many indicate a real issue
* **Use trace IDs from logs** - They provide the most relevant context

#### ❌ DON'T:

* **Assume one trace tells the whole story** - Look at multiple traces
* **Ignore fast operations** - Sometimes the problem is something that should happen but doesn't
* **Forget about sampling** - Not every request generates a trace (by design, to reduce overhead)
* **Overlook nested spans** - The real problem might be hidden in a sub-operation

### Understanding Trace Sampling

For performance reasons, not every request generates a trace. The system uses **sampling** to capture a representative subset.

**What this means for you:**

* Traces for **errors** are almost always captured (high priority)
* Traces for **slow requests** are usually captured
* Traces for **normal, fast requests** may not all be captured

**If you can't find a trace:**

* The request may not have been sampled
* Try finding a similar request from the same time period
* Or trigger the request again and search for the new trace

### Common Trace Investigation Questions

1.  "_**This trace looks normal, but users say it's slow**"_:\
    &#xNAN;_&#x50;ossible causes:_

    * Network latency between user and server (not captured in trace)
    * Client-side rendering time (trace only shows server-side)
    * Multiple sequential requests (each fast, but total UX is slow)

    _Action:_ Check Client Analytics for client-side performance data
2.  "_**I see the error, but why did it happen?**_"

    _Look at:_

    * **Tags/attributes on the error span** - May include error details
    * **Spans before the error** - What was the application doing just before failure?
    * **Logs with the same trace\_id** - Often have more detailed error messages
3.  "_**The trace has many services - which one is the problem?**_"

    _Strategy:_

    1. Sort spans by duration (if visualisation allows)
    2. Identify the longest span
    3. That service/operation is where to start investigation
    4. Check if that service's Metrics show issues

### Next Steps

* _**Found a slow operation?**_ → Check if Metrics show a pattern
* _**See an error?**_ → Search Logs for detailed error messages
* **Need to be notified of trace errors?** → Set up Alerts _(coming soon)_

## Technical Details

The tracing system uses:

* **Jaeger** for trace visualisation
* **OpenTelemetry** for trace collection and instrumentation
* **Tempo** for trace storage
* **B3 Propagation** for trace context across services
