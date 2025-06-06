# Communications

Communications is an event driven API that allows ComUnity Developers to integrate centralised communication into their projects.&#x20;

Central to Communications is the concept of [events](configuring-dynamic-action-templates-for-event-driven-communication-channels/) and [triggers](triggering-the-communication-service.md). With the Toolkit, you can define specific events within your application that act as triggers for communication processes. These events can encompass user actions, or any other event that warrants communication. By capturing these events, you lay the foundation for delivering targeted messages to your users.

The ComUnity Developer Toolkit offers the [ComsService.TriggerEvent() ](triggering-the-communication-service.md)function for efficient communication execution. When an event occurs, invoking this function triggers the Communication Service to manage the delivery of messages across various channels. It abstracts the complexities of background processes, enabling you to focus on creating meaningful interactions with your users.\
\
To configure your messaging flows, the  [Communication Settings ](communication-settings.md) offered by the Toolkit are essential. You can define [Channel Priorities](communication-settings.md#channel-priorities) to assign different levels of importance to messages, ensuring efficient delivery through preferred channels. The Toolkit also provides [Pre-Defined Values](communication-settings.md#pre-defined-values), offering standardised templates for common communication elements such as sender names, subject lines, or notification content. Additionally, [Custom Values](communication-settings.md#custom-values)  allow you to incorporate application-level data and variables, enabling dynamic and personalised messaging experiences.

Communications enable you to integrate messaging capabilities into your projects effortlessly. Whether it's sending notifications, alerts, or updates via email, SMS, or in-app messages, Communications ensures effective information dissemination and enhances user engagement.

{% hint style="info" %}
The Communication Service operates independently, without awareness of other services, such as the Data Service. Therefore, all necessary data must be injected into the Communication Service, either through communication settings or through a communication event, as it cannot reference other contexts outside of itself.
{% endhint %}

Key aspects of Communication in the ComUnity Developer Toolkit:

1. [Configuring Dynamic Action Templates for Event-Driven Communication Channels](configuring-dynamic-action-templates-for-event-driven-communication-channels/)
2. [Triggering the Communication Service](triggering-the-communication-service.md)
3. [Communication Settings](communication-settings.md)

