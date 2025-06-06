# Communication Settings

When defining communication events within the Toolkit, it is essential to consider the associated metadata to ensure effective and efficient message delivery. This section delves into two main categories of communication settings: Environment-Specific and Project-Specific Communication Settings. Each of these categories encompasses key aspects such as Channel Priorities, Pre-Defined Values, and Custom Values, which are crucial for configuring communication events to meet specific needs and contexts.

## Environment-Specific Communication Settings

Environment-Specific Communication Settings pertain to configurations that vary based on the deployment environment, such as development, testing, staging, or production. These settings ensure that communication events are appropriately configured for the context in which they are executed. To access and manage the metadata associated with these communication events in the Toolkit, navigate to the [Configuration ](../../getting-started/manage-your-project/deploy/configuration.md) section, where you will find detailed instructions on how to set up and adjust these settings. Within this environment-specific context, you can define:

### Pre-Defined Values

The Pre-Defined Values section provides access to the InAppRequest Template. This template serves as a predefined structure for specific types of messages or notifications. Utilising predefined values can save time and effort in setting up communication events, offering standardised options for elements such as sender names, email subjects, SMS templates, or push notification content. By leveraging these predefined values, you can maintain consistency across your messages and streamline the configuration process.

### Custom Values

The Custom Values section is where you define your @Model.App namespace, which contains constants for your application-level data. Examples of such constants include BaseURL, FromAddress, ToAddress, and PushRootName. Custom Values allow you to personalise and customise your communication events based on specific requirements or preferences. By utilising the @Model.App namespace, you can effectively incorporate application-level data into your templates and messages.

## Project-Specific Communication Settings

Project-Specific Communication Settings, on the other hand, are unique to each project within the Toolkit. These settings allow you to define communication parameters that are specific to your project's needs, ensuring that all communication events align with your project's objectives and requirements. To manage these settings, refer to the [General](../../getting-started/manage-your-project/general.md#access-project-settings) section for comprehensive guidelines on accessing and configuring the necessary metadata. Within this project-specific context, you can define:

### Channel Priorities

The Channel Priorities field allows you to specify the importance level of a message, ranging from Critical, High, Medium, to Low. By assigning channel priorities, you can ensure that messages are delivered through the preferred channels based on their importance. The default channel priority is set to Medium, but you can adjust it according to your specific communication requirements.
