# Observability

> Observability feature offers a comprehensive suite of tools designed to enhance visibility and insight across your application's performance and usage. With a focus on user-friendliness, the standout aspect of our observability suite is its ease of setup—every feature can be enabled with just a click of a button, streamlining the integration of advanced monitoring capabilities into your workflow.

The ComUnity Platform provides comprehensive observability tools that help you understand your application's health, performance, and user experience. With integrated monitoring, logging, and analytics, you can quickly identify issues, optimise performance, and understand how users interact with your applications.

**What makes our observability different:** Everything is integrated out-of-the-box. Enable observability once, and you immediately get metrics dashboards, log search, distributed tracing, and user analytics—all connected and correlated for faster troubleshooting.

### The Three Pillars of Observability

Observability in the ComUnity Platform is built on three complementary data sources that work together to give you complete visibility:

#### Metrics: System Performance

Monitor your application's health with real-time performance data.

**What you'll track:**

* Request rates, error rates, and latency (P99, P95)
* Resource usage (CPU, memory, database connections)
* Service health and availability
* Custom business metrics

**When to use:** Daily health checks, performance optimization, capacity planning

**Explore Metrics →**

#### Logs: Detailed Event Records

Search and analyse detailed logs to understand what happened and why.

**What you'll track:**

* Error messages and stack traces
* User actions and system events
* API requests and responses
* Application behavior and debugging info

**When to use:** Troubleshooting errors, debugging issues, audit trails

**Explore Logs →**

#### Traces: Request Flow Visualisation

Follow individual requests through your entire system to identify bottlenecks and failures.

**What you'll track:**

* End-to-end request flows across services
* Duration of each operation
* Service dependencies and call chains
* Performance bottlenecks in distributed systems

**When to use:** Debugging slow requests, understanding service interactions, optimizing workflows

**Explore Traces →**

#### Client Analytics: User Behaviour

Understand how users interact with your application through privacy-first analytics.

**What you'll track:**

* User engagement and session duration
* Most visited pages and features
* Geographic distribution and device types
* User flows and drop-off points

**When to use:** Feature adoption analysis, UX optimization, understanding user behavior

**Explore Client Analytics →**

### How These Tools Work Together

The power of the ComUnity Platform's observability comes from how these tools integrate:

**Scenario: Users report slow page loads**

1. **Start with Metrics** → Notice P99 latency spike at 14:30
2. **Check Logs** → Find error messages during that time period
3. **View Traces** → See complete request flow and identify slow database query
4. **Correlate** → All three tools share trace IDs for seamless navigation

**Every log entry includes a trace ID. Every trace links to logs. Metrics dashboards link to both.** This correlation eliminates the need to manually piece together data from different systems.

### Quick Start Guide

#### Step 1: Enable Observability

Observability is enabled per environment. Follow these steps for each deployment environment:

1. **Log into the Toolkit** with your credentials
2. **Open your project** from the project list
3. **Navigate to Observability** in the main menu
4. **Go to Project Settings** → **Observability** tab
5. **Click "Enable Observability"** and wait for the background process to complete
6. **Access your dashboards** from Observability menu

**Screenshot needed:** Project Settings → Observability tab

**Time to enable:** Approximately 2-3 minutes per environment

**Note:** You'll need to enable observability separately for Development, QA, and Production environments.

#### Step 2: Access Your Dashboards

Once enabled, you can access four integrated dashboards:

**Metrics Dashboard**

* View real-time performance data
* Monitor service health
* Track custom metrics
* Create alerts for issues

**Logs Search**

* Search error messages
* Filter by time and service
* Find trace IDs for correlation
* Debug production issues

**Traces Viewer**

* Visualize request flows
* Identify bottlenecks
* Debug slow operations
* Understand service dependencies

**Client Analytics**

* Track user engagement
* Understand feature adoption
* Analyze user flows
* Monitor traffic sources

#### Step 3: Instrument Your Application (Optional)

The platform automatically collects infrastructure metrics, logs, and traces. For deeper insights, you can add custom instrumentation:

**Add custom metrics** for business logic (e.g., payment success rate, user signups) **Add structured logging** for better searchability **Add custom trace spans** for specific operations

**Learn about instrumentation →** _(coming soon)_

### Common Use Cases

#### Use Case 1: Troubleshooting Production Errors

**Problem:** Users reporting "payment failed" errors

**Investigation workflow:**

1. **Logs:** Search for "payment failed" errors
2. **Find trace ID** in the error log entry
3. **Traces:** Open the trace to see full request flow
4. **Identify:** Payment gateway timeout after 30 seconds
5. **Action:** Increase timeout or add retry logic

**Time to resolution:** Minutes instead of hours

#### Use Case 2: Optimising Slow Endpoints

**Problem:** API endpoint taking 5 seconds (should be under 500ms)

**Investigation workflow:**

1. **Metrics:** Notice P99 latency spike in dashboard
2. **Traces:** Filter to slow requests (>4 seconds)
3. **Identify:** Database query taking 4.8 out of 5 seconds
4. **Logs:** Find the actual SQL query in log details
5. **Action:** Add database index or optimise query

**Result:** 10x performance improvement

#### Use Case 3: Understanding Feature Adoption

**Problem:** New feature launched but unsure if users are using it

**Investigation workflow:**

1. **Client Analytics:** Check page visits to feature screen
2. **Compare:** Feature page visits vs total visits = adoption rate
3. **Analyze:** Check bounce rate and time on page
4. **Result:** 15% adoption, high bounce rate = users trying but not engaging
5. **Action:** Improve feature onboarding

**Insight:** Data-driven feature development

#### Use Case 4: Capacity Planning

**Problem:** Need to prepare for traffic surge during campaign

**Investigation workflow:**

1. **Metrics:** Review historical peak traffic patterns
2. **Identify:** Current capacity handles 1,000 req/sec
3. **Calculate:** Expected campaign traffic is 3,000 req/sec
4. **Traces:** Check if any services have bottlenecks under load
5. **Action:** Scale infrastructure proactively

**Result:** Zero downtime during campaign

### Getting Help

#### Documentation

* **Metrics Guide** - Understanding dashboards and creating alerts
* **Logs Guide** - Searching logs and debugging with LogQL
* **Traces Guide** - Reading trace visualizations and finding bottlenecks
* **Client Analytics Guide** - Understanding user behavior and analytics
* **Troubleshooting Guide** - Common issues and solutions _(coming soon)_
* **Quick Reference** - Query cheat sheets and glossary _(coming soon)_

#### Technical Documentation

For platform administrators and advanced configuration:

* **Technical Documentation** - Architecture, configuration, and operations

#### Support

* **Support Channel:** \[link or email]
* **Office Hours:** \[if applicable]

### Best Practices

#### For Daily Monitoring

**Check metrics dashboards daily**

* Review error rates and latency
* Look for unusual patterns
* Verify no alerts are firing

**Use logs for investigation**

* Start with time period when issue occurred
* Search for errors or specific events
* Follow trace IDs to see full context

**Review analytics weekly**

* Track user engagement trends
* Identify popular features
* Monitor mobile vs desktop usage

#### For Troubleshooting

**Follow the investigation pattern:**

1. **Metrics** → Identify when problem started
2. **Logs** → Find specific error messages
3. **Traces** → See complete request flow
4. **Correlate** → Use trace IDs to connect data

**Ask the right questions:**

* **What** happened? (Logs)
* **When** did it happen? (Metrics)
* **Where** in the system? (Traces)
* **Who** was affected? (Analytics)

#### For Performance Optimisation

**Focus on user-facing metrics first:**

* P99 latency (worst-case user experience)
* Error rate (user frustration)
* Page load time (user engagement)

**Use traces to find bottlenecks:**

* Identify longest operations
* Optimize database queries
* Cache expensive operations
* Consider async processing

**Measure the impact:**

* Compare before/after metrics
* Check if user engagement improved
* Verify error rates decreased

### Security and Privacy

#### Data Ownership

All observability data stays on your infrastructure. No data is sent to third-party services.

#### Privacy Compliance

* **GDPR compliant:** IP anonymization, consent management
* **CCPA compliant:** User opt-out and data deletion
* **HIPAA compatible:** Can be configured for healthcare applications

#### Access Control

Observability data access is controlled through ComUnity Platform permissions. Users only see data for projects and environments they have access to.

### Technical Details

#### Technology Stack

* **Metrics:** Prometheus + Grafana + Thanos
* **Logs:** Loki with LogQL query language
* **Traces:** Jaeger + OpenTelemetry + Tempo
* **Analytics:** Matomo (open-source, privacy-first)

#### Data Retention

* **Metrics:** High resolution for 30 days, downsampled for 1 year
* **Logs:** 30 days by default (configurable)
* **Traces:** Sampled storage for 30 days
* **Analytics:** Unlimited retention

#### Performance Impact

* Minimal overhead on applications (< 1% CPU, < 50MB memory)
* Automatic sampling for traces reduces data volume
* Asynchronous logging prevents blocking

### Next Steps

#### Just Enabled Observability?

1. **Understand Metrics →** Start with your service health dashboard
2. **Learn Log Searching →** Find and debug errors quickly
3. **Explore Traces →** Visualise request flows

#### Ready for Advanced Features?

1. **Set Up Alerts →** Get notified when issues occur _(coming soon)_
2. **Add Custom Instrumentation →** Track business metrics _(coming soon)_
3. **Read Technical Docs →** Deep dive into configuration

#### Need Help?

* Review the troubleshooting guides for common issues
* Contact support through \[channel/email]
* Check the quick reference for query syntax
