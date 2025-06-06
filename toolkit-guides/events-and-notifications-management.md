# Events and Notifications Management

In the ComUnity Toolkit, an event represents any significant occurrence or change within the system that warrants attention. Events are integral to maintaining system integrity, monitoring performance, and ensuring a responsive user experience. The scope of events in the ComUnity Toolkit includes, but is not limited to:

* **Platform Events**: These are critical to the overall health and performance of the platform. Examples include system outages, resource limits being reached (e.g., disk space, memory usage), and critical errors.
* **Organisation Events**: Events related to specific organisational activities, such as user management actions, role assignments, and organisational policy updates.
* **Project Events**: These events pertain to project-specific activities, such as creation, updates, and deletions of projects, task assignments, and status changes.
* **Toolkit Events**: These involve actions within the Toolkit itself, such as updates to Toolkit configurations, new feature deployments, and user feedback logs.
* **Unknown Events**: Events that do not fall into the predefined categories, which may need further classification.

## Accessing and Managing Events

**Accessing Events**

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Event and Notifications</p></figcaption></figure>

1. **Notification Panel**:
   * Click on the bell icon located in the top-right corner of the dashboard to access the notification panel.
   * The notification panel displays the latest notifications, categorised by their severity (low, medium, high, critical).
2. **Events Page**:
   *   To view all events, click on the `Show all events` link at the bottom of the notification panel. This will take you to the comprehensive events management page.\\

       <figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Events Management</p></figcaption></figure>

## **Filtering and Managing Events**

1. **Filtering Events**:
   * Use the left sidebar to filter events by `Importance`, `Date Range`, `Status`, and `Categories`.
   * Importance levels include: High, Medium, Low, and Critical.
   * Date ranges can be set to view events from the last day, week, month, or a custom range.
   * Status filters allow you to view events that are `New`, `In Process`, or `Processed`.
   * Categories help in narrowing down events specific to Organisation, Platform, Project, Toolkit, or Unknown.
2. **Managing Events**:
   * Events can be marked as read or unread by clicking on the three dots menu in the top-right corner of each event.
   * Change the status of events to reflect their current processing state (New, In Process, Processed).
   * Use the search bar to find specific events quickly.
   * Expand or collapse event details to view more information about each event.

## Notifications

\\

<figure><img src="../.gitbook/assets/image (420).png" alt=""><figcaption><p>Notification Settings</p></figcaption></figure>

### **Customise Notifications**

There are two ways to access notification settings:

1. **Via Events Page**:
   * On the events management page, click on the **Notification Settings** link at the bottom left.
2. **Via Profile Menu**:
   * Navigate to **Account** > **Profile** > **Notification Settings** from the main dashboard.

* **Notification Settings Interface**:
  * The notification settings interface allows users to control what types of notifications they receive and how they receive them. Users can toggle notifications on or off for different categories of events.
* **Notification Categories**:
  * **Organisation Events**: Includes notifications for user management, security, and access.
  * **Platform Events**: Includes notifications for services and infrastructure.
  * **Project Events**: Includes notifications for version control, storage, security events and alerts, performance and response times, monitoring and logs, integration failures, infrastructure, and error events (compilation and runtime exceptions).

**Severity Levels**

* Notifications are colour-coded based on their severity to help prioritize actions:
  * **Low**: Informational notifications that do not require immediate attention.
  * **Medium**: Notifications indicating actions that should be monitored.
  * **High**: Notifications requiring prompt attention to prevent potential issues.
  * **Critical**: Urgent notifications that need immediate action to prevent system failures or significant problems.

## Technical Implementation Details

### **Event Logging and Notification Dispatch**

* Events are logged in the system and notifications are generated based on user roles and subscriptions.
* The system automatically categorises events and dispatches notifications to relevant users, ensuring that all critical activities are monitored and addressed promptly.

## Conclusion

The ComUnity Toolkit's events and notifications management system provides a robust framework for monitoring and responding to significant occurrences within the platform. By utilising the filtering and management capabilities, developers can maintain a high level of system awareness and ensure timely responses to critical events. For further assistance or to report issues, please contact the support team.
