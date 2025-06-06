# Event Details: Understanding Data Sources for Dynamic Template Building

Before examining the specific fields of event details, it is important to understand the available data sources and their role in building dynamic templates. Templates rely on data stored across multiple databases and are exposed to the templates through different namespaces. The templates are written in[ Razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0). In the ComUnity Platform, there are up to four namespaces from which communication data can be accessed:

{% hint style="info" %}
It is important to familiarise yourself with two essential technologies: [oData Version 3.0](https://www.odata.org/documentation/odata-version-3-0/) and[ Razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0) syntax. These technologies are crucial for querying data from the namespaces and creating dynamic content in your templates.\
\
In [Razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0) views, data sources are represented with a prefix of @ symbol. For example, you'll find data sources named as `@ModelApp`, `@Model.Data`, and so on in the subsequent sections. The @ symbol indicates that these sources are accessed using[ Razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0) syntax to incorporate dynamic data into the templates.

All the data referenced here can be accessed under [Communication Settings](../communication-settings.md); please refer to the Communication Settings section for access.
{% endhint %}

## @Model.App

The @Model.App namespace contains application-level data which by default includes constants [BaseUrl ](event-details-understanding-data-sources-for-dynamic-template-building.md#baseurl)and the [DataServiceUrl](event-details-understanding-data-sources-for-dynamic-template-building.md#dataserviceurl). This is typically where a developer will define global variables. If it is desired the[ @Model.App ](event-details-understanding-data-sources-for-dynamic-template-building.md#model.app)namespace can be extended to include other communication variables, to learn more view [Extend @Model.App](event-details-understanding-data-sources-for-dynamic-template-building.md#extend-model.app).

### **BaseUrl**

The BaseUrl is the endpoint of your web client.

{% hint style="info" %}
If you include the BaseUrl in your template, when users click on it, they will be redirected to your web application.
{% endhint %}

To render the BaseUrl in your templates, use the[ Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

`@Model.App.BaseUrl`

### DataServiceUrl

The value of DataServiceUrl is an endpoint that is used to access the Data Service. This is the [OData](https://www.odata.org/documentation/odata-version-3-0/) RESTful API exposing your custom entities. This is how you access your data.

To refer to the DataServiceUrl in your template configurations, use the [Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

`@Model.App.DataServiceUrl`

### Extend @Model.App

In your project you might have to create more than one template, in that situation you might find yourself referring to the same data repeatedly. For example, for a given organisation the feedback email address you use will likely not change for the different templates used in your communications with your clients, in that scenario you would have to repeat your feedback email whenever it is required in a template.

Common data can be configured as custom variables which can then be accessed in the [@Model.App](event-details-understanding-data-sources-for-dynamic-template-building.md#model.app) namespace in your templates.

{% hint style="info" %}
When you use the Fault Starter Template to create your project, the variables FeedbackEmail, FromAddress, LogLevel, ReplyToEntity and SourceEmailAddress are already pre-defined in[ Communication Settings/Custom Value](../communication-settings.md)s as part of the application-level data.
{% endhint %}

To extend the[ @Model.App](event-details-understanding-data-sources-for-dynamic-template-building.md#model.app) namespace view Configuration.

To render the custom values contained[ @Model.App](event-details-understanding-data-sources-for-dynamic-template-building.md#model.app) namespace in your templates, use the [Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

`@Model.App.{Variable Name}`

## @Model.EventData

This namespace contains the event payload. The event payload is data in json format which is passed to an event when it is triggered. In most cases the payload is simply a json representation of the affected record. You can also build up your own custom json body, to be used as a payload.

A sample event payload, when an event is triggered in one of the Faults table’s change interceptors, the payload will consist of raw data in json format that makes up a single record in the Faults table as shown in the code snippet below.

```aspnet
// Case Record 
{
"CaseId": 2,
"Name: "Bonolo",
"Surname": "Hanisi",
"StreetAddress": "7 De Wet Terrraces, Goodwood, Capetown",
"Photo": "",
"Description": "Blocked stoem drains!!!!!!",
"ReferenceNumber": 234,
"Latitude": "-33.909990",
"Longitude": "18.5491670"
"FaultSubTypeFaultSubTyppeId": 580,
"FaultIdFaultId": 32,
"UserId": "abcfg123e",
"Created": "2022-03-07T07:112:40.763Z",
"Modified": "2022-03-07T07:12:40.763Z"
}
```

## @Model.Data

When configuring content for your templates you have the liberty to create custom oData queries to access data in your Data Service, to learn more view the [Event Action/Expand Path](event-details-understanding-data-sources-for-dynamic-template-building.md#expand-path). The response payloads from your queries are used to populate the @Model.Data namespace.

## @Model.Profile

To render @Model.Profile data in your templates, use the [Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

`@Model.Profile. {Property name}`

While the @Model.App and @Model.EventData namespaces provide some pre-populated data upon triggering the Communication Service, it's important to configure additional data sources through the Event Action. This ensures the availability of more extensive data for building robust and dynamic templates. The Event Action allows you to specify additional data sources accessible through the @Model.Profile and @Model.Data namespaces. This flexibility enables you to incorporate specific data for general communication settings and further enhance template customisation.

By understanding and utilising these data sources, you can leverage the power of dynamic template building and create effective communication experiences within your ComUnity project.

## Common Helper Methods used in Templating

The following C# methods are commonly used in [explicit Razor expressions](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-7.0#explicit-razor-expressions) during templating:

1. [`Uri.EscapeDataString(String)`](https://learn.microsoft.com/en-us/dotnet/api/system.uri.escapedatastring?view=net-7.0)`:`Transforms a string to its escaped form, an example is shown below:

```csharp
//If 'item.DocumentName' contains characters that is not valid in a url, it needs to be escaped...
<a href="@(Model.App.BaseUrl)/u/f/@Uri.EscapeDataString(item.DocumentName)">@(item.DocumentName)</a>

```

2. [`Raw(Object|String)`](https://learn.microsoft.com/en-us/dotnet/api/system.web.webpages.html.htmlhelper.raw?view=aspnet-webpages-3.2): Transforms html into an html body, as shown in the example below:

```csharp
(@Raw(Model.EventData.EmailBody)

```

3. [`DateTime.AddHours(Double)`](https://learn.microsoft.com/en-us/dotnet/api/system.datetime.addhours?view=net-7.0): This method returns a new DateTime object with the number of hours specified added to its value as shown in the example below:

```csharp
(@Model.Data.StartDateTime.AddHours(2).ToString("dd/MM/yyyy HH:mm")

```

4. Conditionals: The code snippet below demonstrates how you can use conditional statements when templating messages:

```csharp
// Using Razor to test vales: 
@if (Model.Data.Items.Count == 0) {...}
@if (Model.Data.Summary == null) {...}
 
```

## URL Shortening

URL shortening is often used for two reasons: to track when a URL is accessed and to save space in messages where the length is limited, such as in SMS where HTML cannot be used to display friendly names.\
\
By default all the urls contained in messages are shortened, config can be altered to exclude certain URL's from being shortened by extending the @Model.App namespace with the following variable **`ShortUrlExclusions`** whose value is a comma delimited list of all URLs to be excluded an example is shown in the screenshot below:

<figure><img src="../../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

## Event Details

In the Event Details section, you'll find a breakdown of the supported fields that allow you to customise your event template. These fields provide essential information and parameters for defining the behaviour and delivery of your communication. By familiarising yourself with these fields and their configuration options, you can optimise your event template to effectively meet your communication requirements. Let's explore each field in detail to understand how you can enhance your event template for seamless and impactful communication.

### Template Name

This property is used to specify the name of the template associated with the event action. An empty template is a valid value of this field.

{% hint style="info" %}
An empty template is a template which only has a name configured, its channels and content are yet to be set up.
{% endhint %}

### Expand Path

This property is used to define an [oData ](../../../reference-articles/odata.md)query that will populate the @Model.Data namespace.

{% hint style="warning" %}
The ComUnity Development Toolkit only supports the [oData](../../../reference-articles/odata.md) 3.0 specification.
{% endhint %}

#### Syntax of the Expand Path

`@Model.App.DataServiceUrl/{oData Query}`

```cshtml
// An example of an oData Query 

@Model.App.DataServiceUrl/Fault(@Model.EventData.Fault)?$expand=Status
```

To parse @Model.Data and display a single item in your templates, use the [Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

```cshtml
@Model.Data.{Property name}
```

If the response payload from the 'Expand Path' query, contains more that one value, these values will be added to the `Items` collection as part of the @Model.Data namespace. Within the template one can parse over these `@Model.Data.Items` to create, for instance a list or table using the [Razor expression](https://docs.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0):

```cshtml
foreach (var item in @Model.Data.Items) {...}
```

### Member List Path

This property is used to define an [oData ](../../../reference-articles/odata.md)query which typically fetches a member list. A member list is an array of records which contain the user IDs of the intended recipients of your communications. The response payload from the Member List Path can then accessed for templating through the @Model.Profile namespace.

{% hint style="warning" %}
After configuring the Member List Path it is required that you specify the [Member ID Field](event-details-understanding-data-sources-for-dynamic-template-building.md#member-id-field).
{% endhint %}

Templates are called for each item returned by the **Member List Path**. For example, if the response payload contains 5 members, the templates will be called 5 times, with the respective member's information being populated from the @Model.Profile namespace each time. However, if the response payload from the **Member List Path** query is empty, the @Model.Profile namespace will not contain any information for templating. In this scenario, the templates will be called only once, and the information available from the @Model.EventData and @Model.Data namespaces will be used.

### Member ID Field

This property is used to specify the property whose value is a user id  or user identifier in each member list item as defined by the [Member List Path](event-details-understanding-data-sources-for-dynamic-template-building.md#member-list-path).

### Context Field

A unique identifier (GUID) used to bind together all messages (email, SMS, push, in-app, etc.) related to a particular process, event, or conversation.

#### How It Works:

* Inserted manually into the payload when triggering communication.
* Saved in the database against each communication record.
* Later enables grouped querying and full traceability of related messages.

{% hint style="warning" %}
Context field should be of data type [GUID](https://docs.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/guid/guid-data-type).
{% endhint %}

* manually into the payload when triggering communication.

Practical Usage of the Context Field

| Scenerio                           | Context Field Source   | Communication Structure                                                                                          | Why Context is Useful                                                      |
| ---------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Fault Management                   | Fault ID (GUID)        | **Hierarchical**: Initial fault report  → Status update → Closure message                                        | Links all updates and communications about one fault lifecycle             |
| Support Ticketing                  | Ticket ID (GUID)       | **Hierarchical**: Ticket created →  Agent assigned →  Customer updated âž” Ticket closed                         | Full customer journey is traceable under one context ID.                   |
| Vacancy Posting                    | Vacancy ID (GUID)      | **Flat/Bulk**: Single event triggers many outbound communications                                                | Context groups all job notifications related to that one vacancy posting.  |
| Bulk Campaign (Event Announcement) | Event ID (GUID)        | **Flat/Bulk**: One campaign broadcast across channels (email, SMS)                                               | Easy to audit who was notified and when, even across different channels.   |
| Chat System                        | Conversation ID (GUID) | **Hierarchical (Conversational Flow)**: User message →  Agent reply →  System auto-response → Follow-up messages | Rebuild full conversation history across multiple messages and directions. |

### Attachment Path

This property allows you to specify a physical path (URL) to an internet discoverable file you want to attach to your email.

{% hint style="warning" %}
When setting up email attachments use the[ Attachment Path](event-details-understanding-data-sources-for-dynamic-template-building.md#attachment-path) or [Attachment oData List Path](event-details-understanding-data-sources-for-dynamic-template-building.md#attachment-odata-list-path) field configurations, but not both fields at the same time.
{% endhint %}

### Attachment oData List Path

The Attachment oData List Path property allows you to specify and [oData ](../../../reference-articles/odata.md)query that is used to fetch an attachment list. An attachment list is an array of records which contain the files you intend to attach to your emails.

{% hint style="warning" %}
After configuring the Attachment oData List Path it is required that you specify the [Attachment oData Field](event-details-understanding-data-sources-for-dynamic-template-building.md#member-id-field).
{% endhint %}

### Attachment oData Field

This field is used to specify the property whose value is an attachment file in each attachment list item as defined by the[ Attachment oData List Path](event-details-understanding-data-sources-for-dynamic-template-building.md#attachment-odata-list-path).

### Attachment Name

This property allows you to specify is a custom user facing name for your attachment.

### Priority

The priority field allows you to specify the level of importance of a message as a digit in the range from 1 up to 4.

<table><thead><tr><th>Priority Level</th><th>Meaning</th><th data-hidden></th></tr></thead><tbody><tr><td>1</td><td>Critical</td><td></td></tr><tr><td>2</td><td>High</td><td></td></tr><tr><td>3</td><td>Normal</td><td></td></tr><tr><td>4</td><td>Low</td><td></td></tr></tbody></table>

{% hint style="info" %}
The priority a user assigns to a channel is compared to the priority of a message. If the importance of a message is higher or equal to what the user allows for a channel, the channel will be utilised.\
Priority level 1(Critical) messages will never be blocked on any channels. Only use in extreme cases. **User** **preferences should always be considered**.
{% endhint %}
