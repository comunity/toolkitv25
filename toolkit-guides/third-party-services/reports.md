# Reports

The Reports feature provides a seamless way to embed and display PowerBI reports directly within your Toolkit project interface. By integrating your custom analytics and dashboards into the Toolkit, you create a unified workspace where project management, monitoring, and data analysis coexist, eliminating the need to switch between multiple tools and platforms.

### Key Features

1. **PowerBI Integration**: Embed PowerBI reports directly into your Toolkit interface, providing seamless access to your analytics alongside your project management tools.
2. **Custom Analytics**: Build and display reports tailored to your specific project needs, whether tracking business metrics, operational data, user behavior, or any other domain-specific analytics.
3. **Environment-Specific Reporting**: Configure different reports for each deployment environment (Development, QA, Production), allowing you to monitor environment-specific data and maintain proper data isolation.
4. **Interactive Dashboards**: Leverage PowerBI's full capabilities including interactive visualizations, date filtering, drill-down analytics, and real-time data updates.
5. **Unified Interface**: Access all your analytics within the Toolkit without switching to external tools, streamlining your workflow and improving productivity.

### Understanding Your Data Architecture

Your Toolkit project automatically collects and stores data as your application runs. This data is stored in an MS SQL Database that forms the core of your project's data infrastructure. Key data sources include:

* **User and application data**: Stored in the MS SQL Database
* **Communication logs**: Email, SMS, WhatsApp, and InApp messaging records tracked by the Communications Server
* **Usage analytics**: Web and mobile client interaction data
* **Media and files**: Stored in Azure Blob Storage (referenced in the database)

PowerBI reports connect to your project's MS SQL Database to access this data and transform it into meaningful visualisations and insights.

### Prerequisites

Before configuring Reports in your Toolkit project, ensure you have:

1. **PowerBI Workspace**: An active PowerBI workspace in your Azure environment where you can create and publish reports.
2. **PowerBI License**: PowerBI Pro or Premium licenses for users who will create and publish reports.
3. **Database Connection Details**: Access to your Toolkit project's MS SQL Database connection information, including:
   * SQL Server hostname/address
   * Database name
   * Authentication credentials (username and password, or integrated authentication)
   * Firewall rules configured to allow PowerBI to connect
4. **Report Creation Skills**: Familiarity with PowerBI Desktop or PowerBI Service for creating reports and dashboards.
5. **Data Schema Knowledge**: Understanding of your project's database schema and the tables/views available for reporting.

### Creating PowerBI Reports for Your Project

Before you can display reports in the Toolkit, you must first create them in PowerBI:

#### 1. Connect PowerBI to Your MS SQL Database

**Using PowerBI Desktop:**

* Open PowerBI Desktop
* Click "Get Data" from the Home ribbon
* Select "SQL Server" from the data sources list
* Enter your connection details:
  * **Server**: Your SQL Server hostname or IP address
  * **Database**: Your Toolkit project's database name
  * **Data Connectivity mode**: Choose "Import" or "DirectQuery" based on your needs
* Click "OK" and provide authentication credentials when prompted
* Select the tables and views you want to include in your report

**Connection Tips:**

* Use DirectQuery for real-time data or Import for better performance with historical data
* Ensure your SQL Server firewall allows connections from PowerBI service IP addresses
* If connecting from PowerBI Service (cloud), you may need to configure an On-Premises Data Gateway

#### 2. Explore Available Data

Common tables you might find in your Toolkit database include:

* **Users**: Application user accounts and profiles
* **Communications**: Logs of emails, SMS, WhatsApp, and InApp messages sent through the Communications Server
* **Sessions**: User login and activity sessions
* **Transactions**: Application-specific business transactions
* **Analytics/Events**: Usage tracking and event logs from web and mobile clients
* **Custom Tables**: Any domain-specific tables created for your application

#### 3. Build Your Reports

* Create visualisations relevant to your project's needs
* Design dashboards that provide actionable insights
* Add filters, drill-through capabilities, and interactive elements
* Configure date ranges, slicers, and parameters for dynamic reporting
* Test your report with sample data to ensure accuracy

#### 4. Publish to PowerBI Workspace

* Click "Publish" in PowerBI Desktop
* Select your PowerBI workspace
* Wait for the upload to complete
* Note the **Report ID** and **Dataset ID** (you'll need these for Toolkit configuration)

**To find Report ID and Dataset ID:**

* Open your report in PowerBI Service (app.powerbi.com)
* The Report ID is in the URL: `https://app.powerbi.com/groups/{workspace-id}/reports/{report-id}`
* Navigate to the dataset settings to find the Dataset ID

#### 5. Configure Embedding and Permissions

* In PowerBI Service, navigate to your report settings
* Ensure embedding is enabled for the report
* Configure Row-Level Security (RLS) if needed to restrict data access
* Set up scheduled refresh for your dataset if using Import mode
* Verify that users who will view the report in the Toolkit have appropriate PowerBI permissions

### Reports Integration

The Toolkit's Reports feature is environment-specific, allowing you to configure different reports for each deployment environment of your project. Follow these steps to add and configure reports:

1. **Log In**: Access the Toolkit by entering your credentials.
2. **Open Your Project**: Locate and select your project within the Toolkit.
3. **Navigate to Project Settings**: Click the settings icon to access your project's configuration options.
4. **Access Reports Settings**: From the settings menu, find and click on "Reports". This will display the Report Settings interface.
5. **Select Environment**: Choose the environment (Development, QA, or Production) where you want to configure reports. Note that each environment typically has its own database, so you'll need separate PowerBI reports for each environment.
6. **Add a Report**: Click the "Add a report" button to create a new report configuration.
7. **Configure Report Details**: In the "Edit Report" dialog, provide the following information:
   * **Report name**: Enter a descriptive name for your report (e.g., "Sales Dashboard", "Communications Analytics", "User Engagement Metrics")
   * **Report Id**: Enter the PowerBI Report ID from your PowerBI workspace (found in the report URL in PowerBI Service)
   * **Dataset Id**: Enter the corresponding PowerBI Dataset ID (found in your PowerBI workspace dataset settings)
   * **Embedded URL**: Provide the PowerBI embed URL for the report (optional, depending on your PowerBI configuration)
8. **Save Configuration**: Click "Save changes" to complete the report setup. The Toolkit will validate and store your configuration.
9. **Repeat for Additional Reports**: Add as many reports as needed for your project by repeating steps 6-8.

### Accessing and Using Reports

Once configured, your reports become accessible through the Toolkit's main interface:

1. **Navigate to Reports**: From the main menu sidebar, click on "Reports".
2. **Select Environment**: Ensure you're viewing the correct environment (Development, QA, or Production) using the environment selector at the top of the page.
3. **Choose Report**: Use the report dropdown menu to select which report you want to view.
4. **Interact with Reports**: Once displayed, you can:
   * **Filter by Date**: Use date range selectors to focus on specific time periods
   * **Toggle Views**: Switch between different views or tabs within the report (e.g., Summary vs. Details)
   * **Interact with Visuals**: Click on charts, graphs, and tables to drill down or filter data
   * **Refresh Data**: Reports will display data based on your PowerBI dataset refresh schedule
   * **Export Data**: Use PowerBI's built-in export capabilities if configured in your report

### Example Report Scenarios

While the Reports feature is completely customisable to your project's needs, here are some common report types that projects often implement:

#### Communications Analytics

Monitor messaging activity across all channels supported by the Communications Server:

* **Delivery Metrics**: Track message delivery success rates across Email, SMS, WhatsApp, and InApp channels
* **Volume Trends**: Visualise communication volume over time, identify peak usage periods
* **Failure Analysis**: Identify and analyse delivery failures by channel, error type, and recipient
* **Channel Distribution**: Compare usage across different communication channels
* **Response Times**: Measure time-to-delivery for different message types

**Sample SQL Query for Communications Data:**

```sql
SELECT 
    Type as Channel,
    Created as Timestamp,
    ToAddress as Recipient,
    Subject,
    LastStatus as Status,
    LastError as ErrorMessage
FROM Communications
WHERE Created >= DATEADD(month, -1, GETDATE())
```

#### Usage Analytics

Understand how users interact with your application across web and mobile clients:

* **Active Users**: Track daily, weekly, and monthly active users
* **Feature Adoption**: Monitor which features are most frequently used
* **Session Analytics**: Analyze session duration, frequency, and patterns
* **Geographic Distribution**: Map user locations and regional usage trends
* **Device Breakdown**: Understand the distribution of web vs. mobile client usage, device types, and operating systems
* **User Journey**: Visualize common user paths through your application

**Sample SQL Query for Usage Data:**

```sql
SELECT 
    UserId,
    SessionStart,
    SessionEnd,
    DeviceType,
    Platform,
    Location
FROM UserSessions
WHERE SessionStart >= DATEADD(day, -30, GETDATE())
```

#### Performance and Health Monitoring

Track system performance and operational health:

* **Response Times**: Monitor API response times and identify slow endpoints
* **Error Rates**: Track application errors, exceptions, and their frequency
* **Resource Utilization**: Monitor database query performance, storage usage
* **Uptime**: Track system availability and downtime incidents
* **API Usage**: Analyze API endpoint usage patterns and identify heavy consumers

#### Business Intelligence

Create domain-specific analytics relevant to your application:

* **Transaction Volumes**: Track business transactions, revenue, conversions
* **Customer Metrics**: Monitor user acquisition, retention, churn rates
* **Operational KPIs**: Measure key performance indicators specific to your business
* **Trend Analysis**: Identify patterns and trends in your application data
* **Forecasting**: Use historical data to predict future trends and demands

### Managing Reports

#### Editing Report Configurations

To update an existing report configuration:

1. Navigate to Reports in Project Settings
2. Select the appropriate environment
3. Click the edit icon (pencil) next to the report you want to modify
4. Update the configuration details (name, Report ID, Dataset ID, or Embedded URL)
5. Click "Save changes"

#### Removing Reports

To remove a report from the Toolkit:

1. Navigate to Reports in Project Settings
2. Select the appropriate environment
3. Click the delete icon (trash can) next to the report you want to remove
4. Confirm the deletion when prompted

**Note**: This only removes the report configuration from the Toolkit interface; it does not delete the actual PowerBI report from your workspace or affect your PowerBI dataset.

#### Environment-Specific Configurations

Reports are configured independently for each environment, allowing you to:

* Display different reports in Development vs. Production
* Connect to environment-specific databases (Dev database, QA database, Production database)
* Use test data in Development environments without affecting production analytics
* Maintain separate PowerBI workspaces per environment for better organization
* Control which analytics are visible in each deployment stage
* Test new reports in Development before promoting to Production

**Recommended Approach:**

* Create separate PowerBI workspaces for each environment (e.g., "MyProject-Dev", "MyProject-QA", "MyProject-Prod")
* Configure each workspace to connect to the corresponding environment's database
* This ensures complete data isolation and prevents accidental data mixing

### Best Practices

#### Report Design and Development

* **Start Simple**: Begin with a few essential reports and expand your analytics over time as needs evolve and you become more familiar with your data.
* **Incremental Development**: Build reports iteratively, starting with basic visualizations and adding complexity as requirements become clearer.
* **Data Model Optimization**: Design efficient data models in PowerBI with proper relationships, measures, and calculated columns to ensure good performance.
* **Naming Conventions**: Use clear, descriptive names for reports, measures, and visualizations that indicate their purpose and the data they display.

#### Data and Performance

* **Choose Import vs. DirectQuery Wisely**:
  * Use **Import** for better performance with historical data that doesn't need to be real-time
  * Use **DirectQuery** when you need live data or when dataset size exceeds PowerBI limits
* **Scheduled Refresh**: Configure appropriate refresh schedules for imported datasets (e.g., hourly, daily) based on how current your data needs to be.
* **Aggregations**: For large datasets, use aggregation tables in your SQL database to improve query performance.
* **Date Tables**: Create and use date dimension tables for consistent time-based filtering and analysis.
* **Query Optimization**: Write efficient SQL queries and avoid pulling unnecessary columns or rows into PowerBI.

#### Security and Access Control

* **Row-Level Security**: Implement RLS in PowerBI to ensure users only see data they're authorized to access.
* **Environment Separation**: Use separate databases and PowerBI workspaces for each environment to maintain data isolation.
* **Credential Management**: Securely store and manage database credentials; avoid hardcoding credentials in connection strings.
* **PowerBI Licensing**: Ensure all users who need to view reports have appropriate PowerBI licenses.

#### Maintenance and Documentation

* **Version Control**: Keep track of report changes and maintain versions of your .pbix files.
* **Documentation**: Maintain documentation about:
  * What each report displays and its business purpose
  * Data sources and table schemas
  * Refresh schedules and dependencies
  * How to interpret key metrics and KPIs
  * Known limitations or data quality issues
* **Regular Reviews**: Periodically review your reports to ensure they still meet business needs and retire outdated reports.
* **Monitor Dataset Refresh**: Set up alerts for dataset refresh failures and monitor refresh performance.

### Troubleshooting

#### Report Not Displaying

**Symptoms**: Report area is blank or shows an error message

**Possible Causes and Solutions**:

* **Incorrect Report ID or Dataset ID**: Verify the IDs are correct by checking your PowerBI Service workspace
* **Embedding Not Enabled**: Ensure the report has embedding enabled in PowerBI Service settings
* **Authentication Issues**: Check that PowerBI embedding authentication is properly configured
* **Network Connectivity**: Verify network connectivity between the Toolkit and PowerBI services
* **PowerBI Service Outage**: Check PowerBI service health status

#### Data Not Updating

**Symptoms**: Report displays outdated data

**Possible Causes and Solutions**:

* **Dataset Refresh Schedule**: Check and update the dataset refresh schedule in PowerBI Service
* **Refresh Failures**: Review dataset refresh history for errors
* **Data Source Connection**: Verify the connection to your MS SQL Database is active and credentials are valid
* **Import Mode**: If using Import mode, remember data only updates when the dataset refreshes (not real-time)
* **Gateway Issues**: If using an On-Premises Data Gateway, check its status and configuration

#### Connection Errors

**Symptoms**: Cannot connect PowerBI to SQL Server database

**Possible Causes and Solutions**:

* **Firewall Rules**: Ensure SQL Server firewall allows connections from PowerBI service IP ranges
* **Authentication Failure**: Verify database credentials are correct and account has necessary permissions
* **Server Not Reachable**: Check SQL Server hostname/IP address is correct and server is online
* **Gateway Required**: If SQL Server is not publicly accessible, install and configure an On-Premises Data Gateway
* **SSL/TLS Requirements**: Verify SSL certificate configuration if your SQL Server requires encrypted connections

#### Performance Issues

**Symptoms**: Reports load slowly or timeout

**Possible Causes and Solutions**:

* **Large Datasets**: Consider using aggregations or limiting the date range of data loaded
* **Complex Visuals**: Simplify report visualizations and reduce the number of visuals per page
* **DirectQuery Limitations**: If using DirectQuery, optimize SQL queries and consider switching to Import for better performance
* **Database Performance**: Check SQL Server query performance and add indexes where appropriate
* **Network Latency**: Evaluate network speed between PowerBI and your database

#### Authorisation Errors

**Symptoms**: Users see "Access Denied" or similar messages

**Possible Causes and Solutions**:

* **PowerBI Licenses**: Ensure users have appropriate PowerBI licenses assigned
* **Workspace Permissions**: Verify users have access to the PowerBI workspace containing the report
* **Row-Level Security**: Check RLS rules aren't incorrectly blocking access to data
* **Toolkit Permissions**: Ensure users have the appropriate role in the Toolkit to access the Reports feature

### Advanced Topics

#### Using On-Premises Data Gateway

If your SQL Server database is not publicly accessible (behind a firewall, on-premises, or in a private network), you'll need to install and configure an On-Premises Data Gateway:

1. Download the gateway from the PowerBI Service
2. Install it on a server that can access your SQL Server database
3. Configure the gateway with your database connection details
4. Register the gateway in your PowerBI workspace
5. Configure your dataset to use the gateway for connections

#### Implementing Row-Level Security

To restrict data access based on user roles:

1. Define RLS roles in PowerBI Desktop using DAX filters
2. Assign users to roles in PowerBI Service
3. Test RLS by viewing the report as different users
4. Consider syncing RLS roles with your application's user roles

#### Creating Parameterised Reports

Enable dynamic reports that users can customise:

1. Create parameters in PowerBI Desktop
2. Use parameters in queries and filters
3. Expose parameters in the report interface
4. Users can adjust parameters to view different data slices

By leveraging the Reports feature with your Toolkit's MS SQL Database, you transform the Toolkit into a comprehensive project management and analytics hub, enabling data-driven decision-making and providing visibility into all aspects of your digital project's performance, user engagement, and operational health.
