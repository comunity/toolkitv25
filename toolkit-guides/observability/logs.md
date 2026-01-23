# Logs

The ComUnity Developer Toolkit provides comprehensive logging capabilities through integration with [Grafana Loki](https://grafana.com/docs/loki/latest/), enabling developers and DevOps personnel to monitor system events, debug issues, and track communications across platform components. This feature offers a streamlined interface for viewing logs without requiring direct access to Grafana, bringing observability directly into the Toolkit experience.

Logging is a foundational component of the ComUnity Platform’s Observability framework, working alongside [Metrics](metrics.md) (system performance data) and [Traces ](traces.md)(request flow visibility). While Metrics provide aggregated performance indicators and Traces capture the journey of individual requests, Logs offer detailed event-level information about what is happening within your application at any given moment.

### Key Benefits

1. **Real-Time Visibility**: Monitor system events as they occur across all platform components. Logs capture detailed information about operations, errors, and warnings, providing immediate insight into system behaviour.
2. **Communication Debugging**: Troubleshoot email and messaging issues directly within the Toolkit. The Communication Service logs reveal why messages may not be sending, including invalid email addresses, missing channel configurations, and delivery failures.
3. **Error Identification**: Quickly identify and diagnose issues using colour-coded severity levels. Error logs (red) highlight critical issues requiring immediate attention, while warning logs (orange) indicate potential problems that may need investigation.
4. **Flexible Filtering**: Search and filter logs by time range, component, severity, and custom search terms. Advanced search options include attribute searching, case sensitivity, and regular expression pattern matching.
5. **Custom Instrumentation**: Add logging to your own project code using provided code snippets, enabling you to track application-specific events and debug custom functionality.

### Understanding Log Levels

Logs are categorised by severity to help you quickly assess the nature and urgency of each entry:

| Level           | Colour | Description                                                                  | Action Required                                            |
| --------------- | ------ | ---------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Information** | Green  | Standard operational messages documenting normal system activity             | No action required; useful for understanding system flow   |
| **Warning**     | Orange | Potential issues that may require attention but are not immediately critical | Review when convenient; may indicate developing problems   |
| **Error**       | Red    | Critical issues that have occurred and require investigation                 | Immediate attention recommended; indicates system failures |

{% hint style="success" %}
💡 When viewing logs, start by filtering for errors to identify critical issues, then expand to warnings and information logs for context.
{% endhint %}

### Types of Logs

The Toolkit provides two distinct log views, each designed for different audiences and purposes. Understanding the difference is essential for effective troubleshooting.

#### Comparison Overview

| Aspect                 | Platform Logs                                      | Project Logs                                       |
| ---------------------- | -------------------------------------------------- | -------------------------------------------------- |
| **Location**           | Platform → Observability → Logs                    | \[Your Project] → Observability → Logs             |
| **Intended Audience**  | DevOps personnel, System Administrators            | Developers, Project Teams                          |
| **Access Requirement** | Toolkit Administrator role                         | Project access (any role with project permissions) |
| **Scope**              | All platform infrastructure components             | Single project only                                |
| **Default Content**    | Platform services automatically logged             | Empty — requires custom instrumentation            |
| **Primary Use Case**   | Infrastructure monitoring, communication debugging | Application-specific debugging                     |

### Platform Logs

#### What They Are

Platform Logs provide visibility into the entire platform infrastructure. These logs are generated automatically by platform components and capture system-level events across all services.

#### Who Can Access

**Required Role**: Toolkit Administrator

To access Platform Logs, you must be logged in as a Toolkit Administrator. This role grants access to platform-wide observability data but does not automatically grant access to individual project data.

{% hint style="info" %}
If you are a Toolkit Administrator and see a white screen when clicking on a specific project, this is expected behaviour. Toolkit Administrators have platform-level access but may not have permissions to view project-specific data. The system does not differentiate between view and edit permissions at the project level — if you lack project access, the menu options simply won’t be available.
{% endhint %}

#### How to Access

1. Log in to the Toolkit with **Toolkit Administrator** credentials.
2. Click **Platform** in the top navigation bar.
3. Navigate to **Observability** in the left menu.
4. Select **Logs**.
5.  Choose your time range and component, then click **Refresh**.\
    <br>

    <figure><img src="../../.gitbook/assets/image (534).png" alt=""><figcaption></figcaption></figure>

#### What You’ll See

Platform Logs display activity from all platform components. Common components include:

<table><thead><tr><th>Component</th><th width="114">Description</th><th>Typical Log Content</th></tr></thead><tbody><tr><td><strong>Core Web Service</strong></td><td>Main application server</td><td>Metadata retrieval, project access events, table name operations</td></tr><tr><td><strong>Communication Data Service</strong></td><td>Event triggers for messaging</td><td>Communication event initiations, trigger data</td></tr><tr><td><strong>Communication Service</strong></td><td>Email/message delivery logic</td><td>Delivery attempts, channel configurations, error details</td></tr><tr><td><strong>Communications API</strong></td><td>API-level operations</td><td>API requests, authentication, response data</td></tr><tr><td><strong>Database Services</strong></td><td>Data layer operations</td><td>Connection events, query operations</td></tr></tbody></table>

#### Key Capabilities

* View logs from **any component** across the platform
* Debug **communication issues** (why emails aren’t sending)
* Monitor **infrastructure health** across all services
* Identify **cross-component issues** affecting multiple services
* Access **historical data** up to 30 days

#### Primary Use Cases

1. **Communication Troubleshooting**: When emails or messages aren’t being delivered, Platform Logs reveal the complete flow from event trigger (Communication Data Service) through delivery attempt (Communication Service), including specific error messages like “no channels defined” or “invalid email”.
2. **Infrastructure Monitoring**: DevOps teams can monitor all platform components for errors and warnings, identifying issues before they impact end users.
3. **Cross-Service Debugging**: When issues span multiple components, Platform Logs allow you to trace events across the entire infrastructure.

### Project Logs

#### What They Are

Project Logs are scoped to a single project and display logging specific to that project’s operations. Unlike Platform Logs, Project Logs do not contain automatic system logging by default.

#### Who Can Access

**Required Access**: Any user with project permissions

If you can access and work within a project, you can view that project’s logs. There is no separate role requirement beyond standard project access.

#### How to Access

1. Log in to the Toolkit.
2. Open your project from the project list.
3. Navigate to **Observability** in the main menu.
4. Select **Logs**.
5. Choose your time range and click **Refresh**.

#### What You’ll See

**By default, Project Logs are empty.**

Project Logs only display:

* Custom logs you have added to your project code using the provided code snippets
* (Future) Platform logs tagged with your project identifier

#### Current Limitations

| Limitation                | Explanation                                                                    | Workaround                                                                       |
| ------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **No automatic logging**  | Unlike Platform Logs, no system events are logged by default                   | Add custom logging to your entity code using code snippets                       |
| **No communication logs** | Emails/messages sent from your project don’t appear in Project Logs            | View Communication Service logs in Platform Logs (requires Toolkit Admin access) |
| **Project tag not set**   | Platform components don’t currently write the project identifier to their logs | Planned for future release                                                       |

{% hint style="info" %}
**Future Enhancement**: The platform team plans to include project-related communication logs in the Project Logs view. This requires platform components to tag their logs with the project identifier, which is not yet implemented. Once available, you’ll see communication logs (like email delivery results) directly in your Project Logs without needing Platform-level access.
{% endhint %}

#### Key Capabilities

* View **custom application logs** added to your project code
* Filter by **time range** up to 30 days
* **Search** log content including attributes
* Track **application-specific events** you’ve instrumented
* Debug **custom functionality** you’ve built

#### Primary Use Cases

1. **Application Debugging**: Track specific events in your custom code, such as when records are created, updated, or deleted.
2. **Custom Workflow Monitoring**: Log key points in your business logic to understand application behaviour.
3. **Error Tracking**: Capture and review errors specific to your application’s custom functionality.

### Access Rules Summary

| User Role                 | Platform Logs | Project Logs               | Notes                                                                 |
| ------------------------- | ------------- | -------------------------- | --------------------------------------------------------------------- |
| **Toolkit Administrator** | ✅ Full Access | ⚠️ Requires Project Access | May see white screen on projects without explicit project permissions |
| **Project Developer**     | ❌ No Access   | ✅ Full Access              | Limited to projects they have permissions for                         |
| **Project Viewer**        | ❌ No Access   | ✅ View Access              | Can view but may not modify logging configuration                     |

#### Understanding the White Screen

If you’re a Toolkit Administrator and encounter a white screen when clicking on a project:

**Cause**: You have platform-level administrative access but haven’t been granted access to that specific project.

**Why It Happens**: The Toolkit doesn’t differentiate between view-only and edit permissions at the project level. Without explicit project access, the system hides all menu options rather than showing a limited view.

**Resolution Options**:

1. Have a project administrator add you to the project with appropriate permissions
2. Access the project using an account that has project-level permissions
3. Use Platform Logs to view infrastructure-level data (if that meets your needs)

### Choosing the Right Log View

| If You Need To…                   | Use           | Why                                                  |
| --------------------------------- | ------------- | ---------------------------------------------------- |
| Debug why an email isn’t sending  | Platform Logs | Communication Service logs are only in Platform Logs |
| Monitor overall platform health   | Platform Logs | Shows all infrastructure components                  |
| Debug custom code you’ve written  | Project Logs  | Shows your custom instrumentation                    |
| Track application-specific events | Project Logs  | Scoped to your project only                          |
| Investigate cross-service issues  | Platform Logs | Shows interactions between components                |
| Understand a specific user action | Project Logs  | Add custom logging to capture the flow               |

### Using the Logs Interface

Both Platform Logs and Project Logs share the same interface controls. This section describes how to use the filtering, search, and display features.

#### Time Range Selection

The time range filter determines the period for which logs are retrieved:

* **Predefined Ranges**: Select from options such as “Last 30 days” for quick filtering.
* **Custom Range**: Choose specific start and end dates for precise time periods.
* **Maximum Range**: Custom ranges are limited to approximately 30 days to ensure performance.

{% hint style="danger" %}
When you change the time range, the Available Components dropdown automatically updates to show only components that have logged data within that period. The dropdown displays the count of components found (e.g., “3 components found”).
{% endhint %}

#### Component Selection

The **Available Components** dropdown allows you to filter logs by specific services:

| Option                 | Description                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------- |
| **All Components**     | Displays logs from all services mixed together; useful for getting a complete picture |
| **Specific Component** | Filters to logs from a single service; useful for focused troubleshooting             |

**Common platform components you may encounter:**

* `core-web-service` — Application server logs
* `communication-data-service` — Communication event triggers
* `communication-service` — Message delivery logic
* `communications-api` — Communication API operations

#### Log Line Limit

The **Log Line Limit** setting controls how many log entries are returned per query:

* **Default**: 100 log entries
* **Adjustable**: Increase this value to retrieve more logs
* **Indicator**: If “Records Found” equals your limit, there may be additional logs available

**To retrieve more logs:**

1. Increase the Log Line Limit value in the top toolbar.
2. Click **Refresh** to reload with the new limit.

#### Search Functionality

The search box filters the displayed logs based on your search terms. Three toggle buttons next to the search box control search behaviour:

| Toggle             | Function                                                                                                                                                        | Use Case                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Attributes**     | When enabled, searches within expanded log attributes (detailed information visible when you click a log entry). When disabled, only searches visible log text. | Enable when searching for specific values in log details                             |
| **Case Sensitive** | When enabled, matches exact case (e.g., “ERROR” won’t match “error”).                                                                                           | Enable when searching for specific log levels written in capitals                    |
| **Regex**          | Enables regular expression pattern matching for advanced searches.                                                                                              | Enable for complex pattern matching (e.g., `E.*` matches anything starting with “E”) |

**Search Examples:**

```
error                    → Finds logs containing "error" (case-insensitive with toggle off)
ERROR                    → Finds logs with uppercase "ERROR" (case-sensitive toggle on)
no channels defined      → Finds specific communication error messages
invalid.*email           → Regex pattern for invalid email variations
```

#### Expanding Log Details

Each log entry can be expanded to reveal additional attributes:

1. Click on any log entry in the list.
2. The entry expands to show detailed attributes including:

* **Service Name**: The component that generated the log
* **Scope Name**: Additional context about the log source
* **Timestamp**: Precise time of the event
* **Custom Attributes**: Any additional data logged with the entry

{% hint style="info" %}
When the Attributes search toggle is enabled, your search will include these expanded details, allowing you to find logs based on information not visible in the collapsed view.&#x20;
{% endhint %}

### Adding Custom Logs to Your Project

You can instrument your project code with custom logging to track specific events and aid debugging. The Toolkit provides code snippets to simplify this process.

#### Prerequisites

Before adding custom logging, ensure your project is configured to send logs to the correct observability endpoint:

1. Open your project in the Toolkit.
2. Navigate to **Settings** → **Environment** → **Configuration**.
3. Locate the **Observability Log URL** setting.
4. Verify the URL points to the production observability stack (not a test environment).
5. Save any changes and rebuild your project if necessary.

#### Step-by-Step Instructions

1. **Open your project** in the Toolkit.
2. **Navigate to the entity** where you want to add logging.
3. **Select the entity** (not a property) to access the code editor.
4. Click on **Custom Code** property to open the Code Editor for that entity.
5. **Click the green Code Snippets button** in the top right corner(Code Snippets in image below)
6. **Select the appropriate log snippet**:

* Info Log
* Warning Log
* Error Log
* Log with Attributes

1. **Copy the snippet code**.
2. **Paste into the desired method** (e.g., `OnAdd`, `OnUpdate`, `OnDelete`).
3. **Customise the log message** to describe what is being logged.
4. **Add the required import** if not already present (see Troubleshooting below).
5. **Save and publish** your project.
6. **Trigger the event** (e.g., add a record) to generate the log entry.

<figure><img src="../../.gitbook/assets/image (535).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (536).png" alt=""><figcaption></figcaption></figure>

#### Available Log Snippets

Four code snippets are available for logging:

| Snippet                 | Severity     | Use Case                                                |
| ----------------------- | ------------ | ------------------------------------------------------- |
| **Info Log**            | Information  | Standard operational messages; normal activity tracking |
| **Warning Log**         | Warning      | Potential issues; situations that may need attention    |
| **Error Log**           | Error        | Critical errors; failures requiring investigation       |
| **Log with Attributes** | Configurable | Logs with additional custom data attached               |

#### Code Snippet: Basic Info Log

Use this snippet to log a simple informational message:

```csharp
/* The following line must be moved to the includes at the top of the file
using ComUnity.DataServices.Observability;
*/
var tracer = HttpContext.Current.Items["ComUnityTracer"];
if (tracer != null)
{
    (tracer as Tracer)?.Log("log details", new List<KeyValuePair<string, string>>(), EventSeverity.eventlog_information_type);
}
```

#### Code Snippet: Warning Log

Use this snippet to log potential issues that may need attention:

```csharp
/* The following line must be moved to the includes at the top of the file
using ComUnity.DataServices.Observability;
*/
var tracer = HttpContext.Current.Items["ComUnityTracer"];
if (tracer != null)
{
    (tracer as Tracer)?.Log("log details", new List<KeyValuePair<string, string>>(), EventSeverity.eventlog_warning_type);
}
```

#### Code Snippet: Error Log

Use this snippet to log critical errors requiring investigation:

```csharp
/* The following line must be moved to the includes at the top of the file
using ComUnity.DataServices.Observability;
*/
var tracer = HttpContext.Current.Items["ComUnityTracer"];
if (tracer != null)
{
    (tracer as Tracer)?.Log("log details", new List<KeyValuePair<string, string>>(), EventSeverity.eventlog_error_type);
}
```

#### Code Snippet: Log with Additional Attributes

Use this snippet when you need to include structured data with your log entry:

```csharp
/* The following line must be moved to the includes at the top of the file
using ComUnity.DataServices.Observability;
*/
var tracer = HttpContext.Current.Items["ComUnityTracer"];
if (tracer != null)
{
    var atts = new List<KeyValuePair<string, string>>
    {
        new KeyValuePair<string,string>("key", "value")
    };
    (tracer as Tracer)?.Log("user profile updated", atts, EventSeverity.eventlog_information_type);
}
```

**To customise:**

1. Move the `using ComUnity.DataServices.Observability;` statement to the top of your file.
2. Replace `"user profile updated"` with your descriptive log message.
3. Add or modify key-value pairs in the `atts` list to include relevant data:

```csharp
var atts = new List<KeyValuePair<string, string>>
{
    new KeyValuePair<string,string>("EntityId", entity.Id.ToString()),
    new KeyValuePair<string,string>("UserEmail", currentUser.Email),
    new KeyValuePair<string,string>("Action", "Created")
};
```

4. Change the `EventSeverity` value as needed for warnings or errors.

#### EventSeverity Reference

| Severity Level | Constant                                  | Colour in UI |
| -------------- | ----------------------------------------- | ------------ |
| Information    | `EventSeverity.eventlog_information_type` | Green        |
| Warning        | `EventSeverity.eventlog_warning_type`     | Orange       |
| Error          | `EventSeverity.eventlog_error_type`       | Red          |

#### Customising the Snippets

All four snippets follow the same pattern. To customise:

1. **Move the import statement**: Copy `using ComUnity.DataServices.Observability;` to the top of your file with the other `using` statements.
2. **Replace the log message**: Change `"log details"` to a descriptive message (e.g., `"Tag added successfully"` or `"Payment processing failed"`).
3. **Add attributes if needed**: Replace the empty `new List<KeyValuePair<string, string>>()` with your attribute list:

```csharp
var atts = new List<KeyValuePair<string, string>>
{
    new KeyValuePair<string,string>("EntityId", entity.Id.ToString()),
    new KeyValuePair<string,string>("UserEmail", currentUser.Email),
    new KeyValuePair<string,string>("Action", "Created")
};
(tracer as Tracer)?.Log("Record created", atts, EventSeverity.eventlog_information_type);
```

4. **Choose the appropriate severity**: Use `eventlog_information_type` for normal operations, `eventlog_warning_type` for concerning situations, and `eventlog_error_type` for failures.

#### Troubleshooting Custom Logging

**"Tracer could not be found" Error**

If you encounter this error when publishing:

1. Open the Code Editor for your entity.
2. Locate the `using` statements at the top of the file.
3. Add the following import:

```csharp
   using ComUnity.DataServices.Observability;
```

4. Save and publish again.

{% hint style="info" %}
The code snippets include a comment reminding you to move this import statement. Ensure it's placed with the other `using` statements at the top of your file, not inline with your method code.
{% endhint %}

**Logs Not Appearing**

If your custom logs don't appear in the interface:

1. **Wait 5 minutes**: Logs may take up to 5 minutes to propagate through the system.
2. **Verify the Observability URL**: Check that your project configuration points to the correct observability stack.
3. **Rebuild and relaunch**: After configuration changes, rebuild and relaunch your project to ensure the data service restarts with the new settings.
4. **Check the time range**: Ensure your selected time range includes the time when the event occurred.

## Common Use Cases

#### Debugging Communication Issues

The Communication Data Service and Communication Service logs are particularly valuable for troubleshooting email and messaging problems.

**Scenario**: Emails are not being sent from your application.

**Investigation Steps:**

1. Navigate to **Platform** → **Logs** (as Toolkit Administrator).
2. Set the time range to cover when the communication should have occurred.
3. Select **Communication Data Service** from Available Components and refresh.
4. Look for the event trigger that initiated the communication.
5. Switch to **Communication Service** (or **Communications API** if available) and refresh.
6. Search for error messages such as:

* `no channels defined` — Channel configuration is missing
* `invalid email` — Email address format is incorrect
* Delivery failure messages — External email service issues

**Common Causes:**

* Missing or misconfigured communication channels
* Invalid email addresses in recipient fields
* Authentication issues with email providers

{% hint style="info" %}
Previously, debugging communication issues required contacting support to investigate database logs. With Platform Logs, you can now self-serve this investigation.
{% endhint %}

Platform administrators can use logs to monitor overall system health.

**Daily Health Check:**

1. Navigate to Platform Logs.
2. Set time range to “Last 24 hours”.
3. Select “All Components” and refresh.
4. Filter for errors by typing `error` in the search box with Attributes enabled.
5. Review any red (error) entries for critical issues.
6. Review orange (warning) entries for potential developing problems.

**Key Indicators to Watch:**

* Repeated errors from the same component
* Warnings increasing in frequency
* Database connection issues
* Authentication failures

#### Debugging Custom Project Code

When troubleshooting custom functionality you’ve built:

1. **Add strategic logging** at key points in your code:

* Method entry points
* Before and after external calls
* In error handling blocks
* When processing important data

1. **Use appropriate severity levels**:

* Info for tracking normal flow
* Warning for unexpected but recoverable situations
* Error for failures

1. **Include context in log messages**:

* Entity IDs
* User information
* Input values
* State information

1. **Use attributes for structured data** when you need to log multiple related values.

### Technical Reference

#### Underlying Technology

The Logs feature integrates with the Grafana observability stack:

| Component         | Purpose                     | Documentation    |
| ----------------- | --------------------------- | ---------------- |
| **Grafana Loki**  | Log aggregation and storage | Used for Logs    |
| **Grafana Tempo** | Distributed tracing         | Used for Traces  |
| **Prometheus**    | Metrics collection          | Used for Metrics |

The Toolkit interface provides a streamlined view of Loki logs without requiring separate Grafana credentials or navigation. If you have direct access to Grafana, you can also view logs there with additional query capabilities.

#### Log Retention

Logs are retained according to the platform’s data retention policy. Contact your administrator for specific retention periods.

#### Performance Considerations

* Custom ranges are limited to approximately 30 days for performance reasons.
* Large log volumes may take longer to load; use component filtering to improve response times.
* The Log Line Limit prevents excessive data transfer; increase only when necessary.

### Best Practices

1. **Start with errors**: When troubleshooting, filter for errors first to identify critical issues.
2. **Use component filtering**: Rather than viewing all components, focus on the specific service you’re investigating.
3. **Add meaningful log messages**: When adding custom logs, include enough context to understand the situation without needing to look at code.
4. **Log at appropriate levels**: Reserve errors for actual failures; use warnings for concerning situations; use info for tracking normal operations.
5. **Include identifiers**: Always log entity IDs, user IDs, or transaction IDs to correlate logs with specific operations.
6. **Review logs regularly**: Don’t wait for problems—periodic log review can identify issues before they become critical.

### Future Roadmap

The following enhancements are planned for the Logs feature:

1. **Project-Tagged Communication Logs**: Communication service logs related to a specific project will appear in that project’s logs (requires platform components to tag logs with project identifiers).
2. **Automatic Platform Event Inclusion**: Select platform events affecting your project may be included automatically in Project Logs.

{% hint style="info" %}
These enhancements are dependent on platform component updates and are subject to change.
{% endhint %}

### Related Topics

* Metrics — Monitor application performance and resource utilisation
* Traces — Track request flows and identify performance bottlenecks
* Client Analytics — Understand user engagement and application usage patterns

{% hint style="info" %}
The Logs interface design may be updated based on UX team feedback. Future releases may include improved layout options for component selection and additional filtering capabilities.
{% endhint %}
