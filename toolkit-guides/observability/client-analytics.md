# Client Analytics

> The ComUnity Platform offers client analytics functionality through the integration of [Matomo](https://matomo.org/), a leading open-source analytics tool, providing a comprehensive and intuitive interface for analysing user interactions within your projects. This integration furnishes a diverse array of features designed to augment your analytics strategy, enabling effective collection, analysis, and interpretation of user data to drive informed decision-making and optimise user engagement.

## **Key Benefits**

* Track user interactions in real time, providing insights into user behaviour and preferences.
* Access detailed analytics reports, assisting in the identification of trends and informing data-driven decision-making processes.
* Ensure compliance with global data privacy standards, reflecting  [Matomo](https://matomo.org/)'s emphasis on user privacy protection.

To leverage your project's Client Analytics dashboard powered by [Matomo](https://matomo.org/), follow these steps:

1. **Enable Observability**: Activate the observability feature in your project. For detailed instructions on enabling observability within the Toolkit, refer to the [Observability Integration](./#observability-integration) guide.
2.  **Access the Dashboard**: Navigate to the Observability tab. By default, the Client Analytics tab will be displayed, showcasing your analytics dashboard.<br>

    <figure><img src="../../.gitbook/assets/image (387).png" alt=""><figcaption><p>Client Analytics</p></figcaption></figure>

This integration not only enhances the analytical capabilities within the ComUnity Platform but also aligns with the commitment to providing user-centric, secure, and effective digital solutions.

## Understanding Client Analytics

When you navigate to **Observability** → **Client Analytics**, you'll see the Matomo analytics dashboard showing how users interact with your application.

Client Analytics focuses on **user behaviour** (what users do), which complements the other observability tools:

* **Metrics** track system performance (how your infrastructure performs)
* **Traces** track request flows (how data moves through your system)
* **Client Analytics** track user actions (how people use your application)

Together, these three tools give you complete visibility: system health, request-level debugging, and user experience insights.

## Key Metrics Explained

### Visits vs Visitors

Understanding the difference between visits and visitors helps you measure both total engagement and unique user growth.

**Visits (Sessions)**

* A visit is one browsing session by a user
* If a user visits your app in the morning, leaves, and returns in the afternoon, that counts as 2 visits
* Session typically ends after 30 minutes of inactivity
* **Use this to:** Understand total engagement and activity levels

**Visitors (Unique Users)**

* A visitor is a unique person (tracked by device/browser)
* Same person visiting multiple times = 1 visitor, multiple visits
* **Use this to:** Track your actual user base size and growth

**Example:**

* 100 visitors made 250 visits = Each user visited \~2.5 times on average
* This indicates moderate engagement—users return but aren't heavily engaged

### Pages Per Visit (Engagement Depth)

**What it shows:** Average number of pages or screens viewed during each visit

**Interpreting the metric:**

* **Higher is better** - Indicates users exploring and engaging with your app
* **Context matters** - What's "good" depends on your application type

**Typical ranges by application type:**

* E-commerce: 3-5 pages typical
* Content/News apps: 5-10 pages indicates good engagement
* SaaS/Productivity tools: 2-4 pages per session
* Single-purpose apps: 1-2 pages may be normal

**Warning signs:** Very low pages per visit (1-2) in applications that expect exploration might indicate:

* Users not finding what they need
* Poor navigation or confusing interface
* Technical issues preventing page loads
* Wrong audience or unclear value proposition

**Action:** Review which pages users land on and where they immediately exit. Check for navigation issues or missing content.

### Visit Duration

**What it shows:** Average time users spend in your application per visit

**Context-dependent benchmarks:**

* **News/Content app:** 5-15 minutes indicates engaged reading
* **Productivity tool:** Longer sessions show active use (10-30 minutes)
* **E-commerce:** 2-5 minutes for browsing and purchasing
* **Quick-action apps:** 1-2 minutes may be perfectly normal

**Warning signs:** Very short visits (under 30 seconds) consistently might indicate:

* Users arriving with wrong expectations
* Technical problems (slow loading, errors)
* Poor first impression or unclear interface
* Search engine traffic to irrelevant pages

**Improvement strategies:**

* Improve page load times (check Metrics for performance issues)
* Clarify value proposition on landing pages
* Enhance navigation and content discovery
* Review entry pages for relevance

### Bounce Rate

**What it shows:** Percentage of visits where the user viewed only one page and left without any interaction

**Calculation:** Single-page visits ÷ Total visits × 100

**Healthy bounce rates by application type:**

* **Blog/Article sites:** 40-60% is normal (users read one article and leave)
* **E-commerce:** 20-40% is healthy
* **Web applications:** Under 20% is ideal
* **Landing pages:** 70-90% is common (single purpose)

**High bounce rate concerns:** If your bounce rate exceeds 70% for an interactive application, investigate:

* Slow page loading (check Metrics dashboards)
* Users not finding expected content
* Poor mobile experience (compare device types)
* Confusing navigation or broken links

**Action steps:**

1. Identify specific high-bounce pages
2. Review those pages for technical errors (check Logs)
3. Analyse entry source (did users expect something else?)
4. Test the user experience on that page

### Real-Time Visitors

**What it shows:** Number of users actively using your app right now

**Practical uses:**

**1. Monitor launches or campaigns**

* Watch real-time visitors during a product launch
* Verify marketing campaigns are driving traffic
* See immediate impact of announcements

**2. Verify deployment health**

* Real-time visitors dropping to zero = potential problem
* Sudden spike might indicate bot attack or viral content
* Compare to typical patterns for the time of day

**3. Understand peak usage times**

* Identify when most users are active
* Schedule maintenance during low-traffic periods
* Plan capacity for known peak times

### Top Pages and Screens

**What it shows:** Most visited pages in your application, ranked by visit count

**Strategic uses:**

**Identify your most valuable features**

* High-traffic pages represent key user workflows
* These pages deserve the most testing and optimization
* Performance issues here have biggest impact

**Prioritise development efforts**

* Focus improvements on pages users actually visit
* Deprioritise or remove unused features
* Optimise high-traffic page performance first

**Understand user navigation patterns**

* See how users move through your app
* Identify unexpected usage patterns
* Discover shortcuts or workarounds users have found

**Example insights:**

* Settings page has very high traffic → May need simplification
* Help page is most popular → Main UI may need clarification
* Advanced feature page has low traffic → Consider hiding or promoting it

### Geographic Distribution

**What it shows:** Where your users are located, broken down by countries and cities

**Strategic uses:**

**Plan localisation efforts**

* If 30% of users are in Spain, consider Spanish translation
* Identify emerging markets worth targeting
* Understand cultural context for feature development

**Schedule maintenance windows**

* Choose times when your primary markets are asleep
* Minimise impact on your largest user bases
* Coordinate with timezone distribution

**Detect unusual patterns**

* Sudden traffic from unexpected countries may indicate bots
* Geographic concentration helps identify business opportunities
* Compare geographic distribution to your target market

**Security considerations:**

* Unusual geographic spikes may indicate attacks
* Cross-reference with error rates in Logs
* Monitor for distributed login attempts

### Device Types: Mobile vs Desktop vs Tablet

**What it shows:** Breakdown of devices users are using to access your application

**Critical for responsive design:**

* If 80% of users are on mobile but your app isn't mobile-optimized, that's a critical issue
* Tablet users often get poor experiences on responsive designs optimized for mobile/desktop
* Device preferences vary by user demographic and application type

**Prioritization guidance:**

* **Focus optimization on dominant device type first**
* **Test critical workflows on all device types users actually use**
* **Compare bounce rate and engagement across devices**

**Warning signs:**

* Mobile bounce rate much higher than desktop → Responsive design issues
* Very short mobile sessions compared to desktop → UX problems
* High mobile traffic but low conversions → Mobile checkout flow problems

**Action:** Navigate to **Visitors** → **Devices** → **Device Type** and compare:

* Bounce rate across devices (should be similar)
* Pages per visit (mobile slightly lower is acceptable)
* Conversion rates or goal completion

### Browser and Operating System

**What it shows:** Which browsers and OS versions your users are using

**Practical decisions:**

**Testing priorities**

* Test on browsers that represent 90%+ of your traffic
* Focus testing on specific browser versions your users have
* Identify if users are stuck on old browsers (corporate restrictions?)

**Support decisions**

* Safely drop support for browsers with <1% usage
* Plan compatibility testing around actual user distribution
* Identify browser-specific issues in error patterns

**Debug browser-specific issues**

* Cross-reference browser data with error logs
* Identify if certain browsers have higher error rates
* Test features in browsers showing problems

### Traffic Sources and Referrers

**What it shows:** How users found your application

**Source categories:**

* **Direct:** User typed URL or used bookmark (indicates loyalty/awareness)
* **Search Engines:** Google, Bing, etc. (organic discovery)
* **Social Media:** Facebook, Twitter, LinkedIn, etc.
* **Referral Sites:** Links from other websites
* **Campaigns:** Marketing campaigns with tracking parameters

**Strategic uses:**

**Measure marketing effectiveness**

* Track which campaigns drive the most traffic
* Calculate ROI by comparing campaign cost to conversions
* Identify most effective channels

**Understand discovery patterns**

* High search traffic indicates strong SEO or brand awareness
* Social media traffic patterns show viral potential
* Referral traffic identifies partnership opportunities

**Optimize acquisition strategy**

* Double down on high-performing channels
* Investigate why certain channels underperform
* A/B test different acquisition approaches

### Navigating Time Ranges

Matomo allows you to analyse data across different time periods. Selecting the right time range helps you understand patterns versus anomalies.

#### Recommended Time Ranges by Use Case

**Today (Real-time monitoring)**

* Monitor current campaign or launch performance
* Verify deployment didn't break user experience
* Track real-time response to announcements
* **Caution:** Incomplete data - today's metrics will change

**Yesterday (Completed day analysis)**

* Compare to historical data without partial data skewing results
* Verify yesterday's deployment success
* Review complete day patterns
* **Best for:** Day-to-day monitoring and comparisons

**Last 7 Days (Weekly patterns)**

* Identify weekday vs weekend patterns
* Smooth out daily variations
* See weekly trends emerging
* **Best for:** Understanding normal variation

**Last 30 Days (Monthly trends)**

* Monthly trends and patterns
* Compare month-over-month growth
* Seasonal pattern analysis
* **Best for:** Strategic planning and reporting

**Custom Date Range (Specific comparisons)**

* Before/after feature releases
* Campaign period analysis
* Quarter-over-quarter comparisons
* **Best for:** Measuring specific changes or events

## Practical Analytics Workflows

#### Workflow 1: Track Feature Adoption

**Goal:** Determine if users are adopting your new feature

**Steps:**

1. Navigate to **Behaviour** → **Pages** (or **Screens** for mobile apps)
2. Search for the page or screen where your feature is located
3. Review visit count and trend over time
4. Calculate adoption rate: (Feature page visits ÷ Total site visits) × 100

**Metrics indicating success:**

* **Increasing visits over time** - Growing adoption
* **Return visitors to feature page** - Users finding value
* **Reasonable time on page** - Users engaging with feature
* **Low exit rate** - Users continuing to other pages

**Metrics indicating problems:**

* **High bounce rate on feature page** - Users trying but not engaging
* **Short time on page** - Feature not compelling or unclear
* **Declining visits after initial spike** - Initial interest but no retention
* **High exit rate** - Feature is a dead end

**Action based on findings:**

* If low adoption: Improve feature promotion and discoverability
* If high bounce: Review feature UX and clarity
* If short sessions: Add more value or clearer instructions
* If high exit: Connect feature better to other workflows

#### Workflow 2: Identify Drop-Off Points in Workflows

**Goal:** Find where users abandon multi-step processes (checkout, onboarding, forms)

**Steps:**

1. Navigate to **Behaviour** → **Pages**
2. Review exit rates (percentage of sessions ending on each page)
3. Map your expected workflow step-by-step
4. Identify pages with unusually high exit rates

**Example: E-commerce checkout analysis**

1. Product page: 30% exit (normal—users browsing)
2. Cart page: 20% exit (acceptable—users comparing)
3. Shipping info: 15% exit (acceptable)
4. **Payment info page: 60% exit** ← **Problem identified**
5. Confirmation: 2% exit (normal)

**Investigation steps:**

1. **Check for technical errors** - Search Logs for errors during that time period
2. **Review page performance** - Check Metrics for slow loading on that page
3. **Test user experience** - Actually go through the flow yourself
4. **Compare devices** - Is drop-off higher on mobile vs desktop?
5. **Check form validation** - Are validation errors causing frustration?

**Common drop-off causes:**

* Unexpected costs revealed late in process
* Complex or confusing form fields
* Technical errors or slow loading
* Security concerns (lack of trust indicators)
* Required account creation
* Limited payment options

#### Workflow 3: Compare Mobile vs Desktop Experience

**Goal:** Ensure mobile users have an experience comparable to desktop users

**Steps:**

1. Navigate to **Visitors** → **Devices** → **Device Type**
2. Compare key metrics between Mobile and Desktop:
   * Bounce rate
   * Pages per visit
   * Average visit duration
   * Conversion rates (if goals configured)
3. Identify significant discrepancies

**Healthy mobile patterns:**

* Bounce rate within 10-15% of desktop
* Pages per visit 20-30% lower than desktop (normal - mobile users more focused)
* Visit duration 30-40% shorter than desktop (normal - mobile sessions shorter)
* Conversion rates within 20% of desktop

**Problem indicators:**

* Mobile bounce rate 2x higher than desktop → Responsive design issues
* Very short mobile sessions (under 30 seconds) → Major UX problems
* High exit rate on specific pages (mobile only) → Page not mobile-friendly
* Mobile conversions significantly lower → Mobile checkout flow problems

**Action steps:**

1. Test the mobile experience yourself on actual devices
2. Check Metrics for mobile page load times
3. Review Logs for mobile-specific errors
4. Use browser developer tools to test responsive design
5. Consider mobile-first redesign if mobile is dominant traffic source

#### Workflow 4: Measure Campaign Effectiveness

**Goal:** Calculate ROI and effectiveness of marketing campaigns

**Prerequisites:**

* Campaigns must use tracking parameters (UTM codes)
* Example: `?utm_source=facebook&utm_campaign=spring_sale`

**Steps:**

1. Navigate to **Acquisition** → **Campaigns**
2. Select the campaign period in date range
3. Review campaign metrics:
   * Total visits
   * New visitors brought in
   * Bounce rate (quality of traffic)
   * Pages per visit (engagement)
   * Goal conversions (if configured)
4. Calculate cost per acquisition (CPA)

**ROI Calculation:**

```
Campaign cost: $1,000
Visitors brought: 500
Conversions: 50
Average order value: $50

Revenue generated: 50 × $50 = $2,500
ROI: ($2,500 - $1,000) ÷ $1,000 = 150%
```

**Quality indicators:**

* **Low bounce rate** (< 40%) - Relevant traffic
* **High pages per visit** - Engaged visitors
* **Strong conversion rate** - Effective targeting
* **Return visitors from campaign** - Building loyalty

**Poor performance indicators:**

* **High bounce rate** (> 70%) - Wrong audience or misleading ads
* **Very short sessions** - Poor landing page experience
* **Low conversion despite high traffic** - Landing page optimization needed
* **High cost per conversion** - Need better targeting or creative

#### Workflow 5: Identify Your Power Users

**Goal:** Understand what highly engaged users do differently

**Steps:**

1. Navigate to **Visitors** → **Engagement** → **Visits by Duration**
2. Review users with longest sessions (top 10%)
3. Navigate to **Visitors** → **Engagement** → **Pages per Visit**
4. Identify users viewing the most pages
5. Cross-reference to find overlap

**Power user characteristics to identify:**

* Much longer than average session duration
* Significantly more pages per visit
* Frequent return visits
* Complete key workflows or conversions
* Access advanced features

**Strategic uses of power user insights:**

* **Feature prioritisation** - What features do power users love?
* **User personas** - Create profiles of highly engaged users
* **Retention tactics** - What keeps power users coming back?
* **Monetisation** - Power users often willing to pay for premium features
* **Beta testing** - Recruit power users for testing new features

## Understanding User Segments

Segmenting users helps you understand different behaviour patterns and optimise for specific groups.

### New vs Returning Visitors

**New Visitors:**

* First time visiting your application
* Critical for acquisition metrics
* Higher bounce rate is more acceptable (they're exploring)
* Need clear onboarding and value proposition
* May not complete goals on first visit

**Returning Visitors:**

* Came back after initial visit
* Strong indicator of product-market fit
* Should have better engagement metrics
* Already understand your interface
* More likely to convert or complete goals

**Healthy application indicators:**

* Growing mix of both new and returning visitors
* Return visitor rate of 40-60%
* Returning visitors have 2-3x engagement vs new
* New visitor conversion rate reasonable for your industry

**If return visitor rate is low (< 20%):**

* Users trying once and not finding value
* Lack of sticky features or compelling content
* Poor first-time user experience
* No reason to return (check if you have new content or features)

### Segmenting by Geography

Different regions often use features differently:

* **Cultural differences** affect feature preferences
* **Time zones** affect peak usage hours
* **Internet speeds** vary by region (affects performance needs)
* **Language preferences** may indicate localisation needs
* **Regulatory requirements** vary by country

**Action:** Use geographic data to inform localisation, feature development, and support priorities.

### Segmenting by Device

**Mobile users often exhibit different behaviour:**

* Shorter, more focused sessions
* Use different features (location-based, camera)
* Need simpler, faster interfaces
* May require different optimisation priorities

**Desktop users typically:**

* Longer sessions with more exploration
* Complete complex workflows
* Use productivity features more
* Tolerate more complex interfaces

**Action:** Optimise critical workflows for each device type's usage patterns.

## Privacy and Compliance

Matomo is designed with privacy as a core principle and helps you comply with data protection regulations.

#### Privacy Features Built Into Matomo

**IP Address Anonymisation**

* Matomo automatically anonymises IP addresses
* Only partial IP addresses are stored
* Users cannot be individually identified by IP

**Do Not Track (DNT) Respect**

* Matomo honours browser DNT signals
* Users who set DNT are not tracked
* Automatic compliance with user preferences

**Cookie-less Tracking Option**

* Matomo can track without using cookies
* Reduces privacy concerns
* Maintains compliance with strict regulations

**Data Ownership**

* All data stays on your infrastructure
* No sharing with third-party advertising networks
* Complete control over data retention and deletion

#### Compliance with Regulations

**GDPR (Europe)**

* Matomo provides required privacy controls
* Supports user data export and deletion requests
* Built-in consent management features
* No data transferred outside your control

**CCPA (California)**

* Supports opt-out requirements
* Provides data access for users
* Enables data deletion on request

**HIPAA/Healthcare**

* Can be configured for healthcare compliance
* No PII stored if configured correctly
* Full audit trail of data access

#### User Privacy Rights

Users of your application have the right to:

* **Know what data is collected** - Analytics tracking is disclosed
* **Opt out of tracking** - Via DNT or your consent mechanism
* **Access their data** - Request report of tracked activities
* **Delete their data** - Request removal from analytics

**Best practices:**

* Include analytics tracking in your privacy policy
* Provide clear opt-out mechanism
* Respect user privacy preferences
* Only track what you need for legitimate purposes

### Setting Up Goals and Conversions

Goals track specific user actions that indicate success for your business. This is an advanced feature typically configured by administrators.

**Common goal types:**

* User completes registration
* User makes a purchase
* User submits a form
* User watches a video to completion
* User reaches a specific page (thank you page)
* User stays on site for specific duration

**Why goals matter:**

* Convert raw visits into meaningful business metrics
* Calculate conversion rates and ROI
* Identify which traffic sources deliver valuable users
* Optimize user flows toward goal completion

**Note:** Goal configuration requires administrator access. If you need goals set up, contact your platform administrator or see the Technical Documentation.

## Connecting Analytics to Other Observability Data

Client Analytics tells you **what users do**, but sometimes you need to understand **why** by correlating with system data.

#### Analytics → Logs

**When:** Analytics shows users abandoning a specific page\
**Action:** Check Logs for errors on that page during the same time period

**Example:**

```
Analytics: 80% bounce rate on checkout page at 2:00 PM
Logs: Multiple "payment gateway timeout" errors at 2:00 PM
Conclusion: Technical issue causing user abandonment
```

**Steps:**

1. Note exact time when bounce rate increased
2. Navigate to Logs
3. Search for errors: `{service_name="checkout"} |= "ERROR"`
4. Filter to the time period
5. Identify correlation between errors and bounce rate

#### Analytics → Metrics

**When:** Analytics shows traffic spike but poor engagement\
**Action:** Check Metrics to see if performance degraded under load

**Example:**

```
Analytics: 10,000 visits but average session duration dropped to 10 seconds
Metrics: Server response time increased to 5 seconds during traffic spike
Conclusion: Performance issues under load ruined user experience
```

**Steps:**

1. Note when engagement metrics dropped
2. Navigate to Metrics dashboard
3. Check P99 latency, error rate, and resource usage
4. Compare normal load to spike period
5. Identify performance bottleneck

#### Analytics → Traces

**When:** Users report slow page loads on specific features\
**Action:** Use Traces to identify slow operations

**Example:**

```
Analytics: Users spending very little time on reports page
Traces: Report generation taking 30+ seconds (users giving up)
Conclusion: Backend performance issue, not UX issue
```

**Steps:**

1. Identify problematic page from Analytics
2. Navigate to Traces
3. Search for traces to that endpoint
4. Review trace duration and identify bottlenecks
5. Optimise slow operations



### Tips for Effective Analytics Use

#### ✅ DO:

* **Check analytics regularly** - Weekly for production apps minimum
* **Focus on trends, not single days** - Day-to-day fluctuations are normal
* **Segment your data** - Overall metrics hide important patterns
* **Set up goals** - Track what actually matters to your business
* **Compare time periods** - This month vs last month, this quarter vs last quarter
* **Correlate with other data** - Link to Logs, Metrics, Traces when investigating issues
* **Test on real devices** - Don't rely only on data, experience it yourself

#### ❌ DON'T:

* **Obsess over vanity metrics** - Total visits matter less than engagement and conversion
* **Ignore context** - Traffic drop might be expected (weekend, holiday)
* **Make decisions from small samples** - Need enough data for statistical significance
* **Forget about bots** - High traffic with 100% bounce rate might be bot traffic
* **Compare dissimilar time periods** - Holiday week vs normal week isn't meaningful
* **Ignore mobile experience** - If mobile is growing, prioritize mobile optimization
* **Skip the qualitative** - Numbers tell you what, but not why

### Next Steps

* **See unusual user behaviour?** → Check Logs and Metrics for system issues
* **Want to track custom events?** → See Instrumentation _(coming soon)_
* **Need to be notified of traffic anomalies?** → Set up Alerts _(coming soon)_
* **Want detailed analytics setup?** → See Technical Documentation

### Technical Details

Client Analytics is powered by:

* **Matomo** - Open-source analytics platform
* **Privacy-first tracking** - GDPR, CCPA, and HIPAA compliant
* **Self-hosted** - Data stays on your infrastructure
* **No third-party sharing** - Complete data ownership
