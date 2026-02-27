# Configuring Dynamic Action Templates for Event-Driven Communication Channels

The ComUnity Platform utilises an event-driven architecture to facilitate communication. Events are exposed through a REST API and can be easily triggered with a simple POST request. As part of our low-code platform, we provide a convenient helper function, `CommsService.TriggerEvent()`, to simplify this process.

Communication Events are typically associated with individual entities and are commonly triggered within change interceptors. As a developer, you can create these events and define dynamic action templates for each event. These templates govern the behaviour and delivery of communications across diverse channels, including email, in-app messaging, push notifications, HTTP, WhatsApp, and SMS.

To create an event follow these steps:

1.  Open your project in the Toolkit and navigate to the Communications section to view a list of all the events currently associated with your project, if there are any.<br>

    <figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>
2. Locate the _**(+) Add an event**_ button and click on it to add a new event to your Communications.
3.  A modal window titled _**Add new event**_ will appear on your screen.<br>

    <figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption><p>Add new event modal</p></figcaption></figure>
4. From the dropdown menu, select the entity you want to link the event to.
5. Select the appropriate change interceptor for the event.
6. Optionally, provide a name for your event.
7. Finally, click the _**Create**_ button to add the entity to the _**Communications**_ module.

After setting up the event, you can proceed to configure templates to define the behaviour and delivery of communication for that event. Templates provide you with the flexibility to customise the content and format of communication across different channels.

## Event Templates

When customising an event template, you can access the template settings by clicking the edit  ![](<../../../.gitbook/assets/image (233).png>) icon for the desired event. This action opens a modal window with various tabs representing different aspects of the template configuration.

To customise an event template, follow these steps:

1.  Click the event whose template you want to define to activate it:<br>

    <figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Active Event</p></figcaption></figure>
2.  Click the _**Edit**_  ![](<../../../.gitbook/assets/image (233).png>) icon for the desired event. This action opens a modal window with various tabs representing different aspects of the template configuration:<br>

    <figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>
3. **Event Details:** This tab allows you to specify important details related to the event template. View [Event Details: Understanding Data Sources for Dynamic Template Building](event-details-understanding-data-sources-for-dynamic-template-building.md) to learn more about configuring event details.
4. **Communication Channels :** In the modal window, you will find multiple tabs representing different communication channels supported by the event template. Each tab corresponds to a specific communication channel, such as email, in-app messaging, push notifications, HTTP, WhatsApp, and SMS. Click on each tab to explore the available options and settings for configuring communication channels.

By navigating through these tabs, you can fine-tune the event template according to your requirements, ensuring effective communication across multiple channels.

To learn more about event details and configuring specific communication channels, click the links below:

* [Event Details: Understanding Data Sources for Dynamic Template Building](event-details-understanding-data-sources-for-dynamic-template-building.md)
* [Email](email.md)
* [SMS & Whatsapp ](sms-and-whatsapp.md)
* [INAPP](inapp.md)
* [Push Notifications](push-notifications.md)
* [HTTP](http.md)

{% hint style="warning" %}
**Next Steps**\
Defining Communication Events and templates in the Communications section does not automatically deliver messages. You must manually trigger the corresponding event from the relevant entity change interceptor(s) in your Data model. For full details on the flow and required parameters, see [Triggering the Communication Service](../triggering-the-communication-service.md).
{% endhint %}
