# INAPP

In this section, you will learn how to enhance user engagement by leveraging in-app notifications. These notifications provide a convenient way to deliver important updates, alerts, or personalised messages directly within your application. By customising the content and behavior of these notifications, you can create seamless and interactive user experiences. Let's explore the dynamic fields available for customisation within in-app notifications:

1. User ID: The User ID field enables you to specify the recipient of the in-app notification. It corresponds to the user ID property in the @Model.EventData namespace. By dynamically populating this field with the appropriate user ID value, you can ensure that the notification is delivered to the intended recipient.
2. Title: The Title field enables you to provide a concise a title for your in-app notification. This field supports dynamic content, allowing you to personalise the title based on user-specific information or contextual data.
3. Action: This field specifies the URL of the page which the recipient of the in-app notification is redirected to when clicking a notification.
4. Message: The Message field allows you to compose the main body of the in-app notification. It provides an opportunity to deliver detailed information, instructions, or any other relevant content to the user. By utilising dynamic content, you can personalise the message based on user-specific data or contextual information.
5. Request Template: This setting allows you to define a custom request template in-app notification. A default request template for in-app notifications is specified in [Communications Settings/Pre-Defined Values](../communication-settings.md#predefined-values).

```json
// Defautl InAppRequestTemplate
{"Subject":"[Subject]","Message":"[Message]","UserId":"[User_Id]","Created":"[Created]","Modified":"[Modified]","odata.type":"[Namespace].PersonalNotification"}


```

## &#x20;:bulb:Try it out

* [How to Configure In-App Notifications for User Profile Updates Using Communications](../../../toolkit-tutorials/how-to-configure-in-app-notifications-for-user-profile-updates-using-communications.md)

