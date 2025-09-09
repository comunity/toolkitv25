# Bulk SMS Campaign

This guide details the process for creating an administrative screen to broadcast bulk SMS messages. The system will target all **UserProfile** records that meet three conditions: they are assigned the Recipient  user role, have opted-in to mobile communications **(ContactByMobile** is true), and have a valid South African phone number (the **Cell** field starts with `+27`).

#### Prerequisites

Before proceeding, confirm the project environment is configured as follows:

* Project Template: The project was created using the **News Feed** template and includes the **Notifications** and the **UserRoles** templates, refer to&#x20;
* Entities:
  * **UserProfile** (platform): Contains the fields `Id` (Guid), `Cell` (string), `ContactByMobile` (bool), `Name`, `Surname` and `Email`.
  * **Campaign** (custom): Defines the fields `CampaignId (int)` and `Message (string)`. Insert permission is enabled under **Table Security**. For details on configuring access, see [Setting Up Role-Based Permissions for Entities: Access Control Configuration](../toolkit-guides/data/setting-up-role-based-permissions-for-entities-access-control-configuration.md).
* SMS Provider: By default a MeSMS provider has been configured under **Project Settings** > **Communications** > **SMS**, update this to meet your specific needs.&#x20;
* Successfully build your project.

## Building a Bulk SMS Campaign service

In this section, you will set up the components required to send bulk SMS messages from your application. The process combines platform authorisation roles (to secure who can create and send campaigns) with application roles (to define the recipient audience). You will then build the administrative Campaign screen, configure a communication event for SMS broadcasts, and add a custom interceptor to trigger message delivery when a campaign is created. Finally, you will connect the project to an SMS provider and run end-to-end tests to verify delivery.

### Validate Platform Roles, Application Roles, and Permissions

The first step is to confirm that the correct platform authorisation roles and application roles exist and are configured with the right permissions.

* Platform Roles: These are default authorisation roles available to all projects.
  * The Staff role is particularly important, as it grants permission to create and send campaigns.
* Application Roles: These are project-specific roles introduced via the UserRoles template.
  * Create a role called Recipient to identify the target audience for campaigns.
  * This role is stored in the UserRole entity and allows you to segment users and query them in the Data Model.

{% hint style="info" %}
When you build your project, the platform roles are automatically used to populate application roles, which are then persisted in the **UserRole** table.
{% endhint %}

### Build Your Project

Build your project to ensure that platform and application roles are correctly generated and available for assignment.

### Create and Assign User Accounts

1. Create two user accounts with different email addresses.
2. Navigate to **App Users & Roles** in **Project Settings**, then open the **Development** environment tab.
3.  Assign the **Staff** role to one user — this grants the necessary authorisation to manage and send campaigns. You can confirm this capability by going to **Screens** > **Administration** > **User Admin Options** > **Edit User Role**, this screen helps you manage user roles and its added to the project as part of the UserRole template:\


    <figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Assign Application Roles in the Web App

1. Open the web app you just built and log in with your Staff account.
2. Navigate to: **Administration** > **Users**.
3. Select your second user account and click **Edit User Role**.
4. Assign the **Recipient** role to this user.

This ensures you now have:

* One account with the **Staff** role (authorised to create and send campaigns).
* One account with the **Recipient** role (the target audience for campaigns).

### Build the Admin Campaign Screen

This step involves creating the user interface for composing and sending campaign messages.

1. Navigate to **Screens** > **Administration** > **Sent Messages** .
2. Click the ellipsis (⋮) next to Sent Messages, then select **Add screen below**.
3. Choose Form page as the screen type and set the page title to **Campaigns**.
4. Select the newly created Campaign screen set its Target URL to `/Campaign`.
5. In the Campaigns screen structure, add the following controls:
   * Auto Inputs (to automatically bind to the Campaign entity fields).
   * Button (to allow the user to submit the form).
6. Save the screen.

Saving a record from this form creates a new row in the **Campaign** entity, which triggers the **OnAdd** event configured in the subsequent steps.

### Create the SMS Broadcast Event

This step configures the communication event that defines the target audience and message content.

1. Navigate to Communications → + Add event.
2. Configure the event with the following parameters:
   * Entity: **Campaign**
   * Event: **`OnAdd`**
   * Name: **OnAddCampaignDefault**
3. Open the new event to configure its Action Templates.

**Details Tab (Audience)**

Define the target audience using an OData query that filters the **UserProfile** entity.

*   Member OData List URL:



    ```
    @Model.App.DataServiceUrl/UserRole('Recipient')/UserProfiles
    ```
*   Member ID OData field:

    ```
    Id
    ```

**SMS Tab (Message Content)**

Define the SMS message template. The communication engine will generate and send one message per user returned by the audience query.

*   Cell Number:

    ```
    @Model.Profile.Cell
    ```

    This expression pulls the cell number from each individual user record identified by the audience query.
*   Message:

    ```
    @Model.EventData.Message
    ```

    This expression pulls the message content from the `Campaign` record that triggered the event.

#### Trigger the Event with a Custom Interceptor

An interceptor is custom code that executes when a data event occurs. You will add code to the `OnAdd` event of the `Campaign` entity to trigger the communication event when a new campaign is saved.

1. Navigate to **Data** >  **List** > **Campaign**.
2. Select **More Settings** >  **Custom Code** .
3.  Copy and add the following C# code below the auto-generated line:



    {% code title="Triggers the Action Template" lineNumbers="true" %}
    ```csharp
     // START auto-generated - OnAdd
    public override void OnAdd(campaign010920250515Context context) {
        base.OnAdd(context);
        // END auto-generated, add custom code below this line

        // Resolve app + comms service
        var appName = Config.AppName();
        var cs      = Config.ComsService();
        if (appName == null || cs == null) return;

        // Minimal payload: just the message body for the campaign
        var data = new
        {
            Message = Message
        };
        var payload = ComsServices.JsonSerialize(data);

        // Trigger the bulk-sms event
        ComsServices.TriggerEvent(
            appName,
            "OnAddCampaignDefault",
            payload,
            cs,
            Config.ComsServiceUsername(),
            Config.ComsServicePassword()
        );
    }	 
    	
    ```
    {% endcode %}
4. Save the Custom Code.
5. Build your project to persist these changes.

### Configure the Communications channel &  SMS Provider

Ensure the project is correctly linked to the configured SMS service.

1. Go to Project Setting > Communications > Global
2. Click **Add channe**l property button
3. Under **Channel Priority Name** select **SMS**
4. By default the channel property is then set to **Medium** - this setting is necessary to ensure delivery of SMSs.
5. Navigate to **Project Settings** > **Communications** > **SMS**.
6. To validate or else set SMS provider settings, click the **Development** > **Communications > Sms**
7. Select the SMS provider of your or else select Mock service that sends your SMSes to **MeSMS**.
8. Enter the required API credentials and sender ID.
9. Save the configuration.



### Perform End-to-End Testing

The final step is to verify that the system works as expected from start to finish.

1. Log in with the test user
   * Sign in to the web app using the test user profile created earlier in the _Create and Assign User Accounts_ section.
   * Navigate to My Profile.
   * Click Edit and enter a valid South African mobile number in the Mobile field.
   * Click Save, then Sign Out.
2. Log in with the Staff user
   * Sign in to the web app using the Staff user profile created earlier.
   * Navigate to Administration > Campaigns.
   * Enter a text message in the Message field.
   * Click Save.
3. Verify delivery
   * An SMS should be delivered to the test user’s device.
   * If you are using the Mock Service, confirm that the request was sent by checking MeSMS service.

## Conclusion

You now have a working bulk SMS campaign feature in the ComUnity Toolkit. Staff users can create campaigns, Recipient users can be targeted, and messages are delivered via your configured SMS provider or the Mock service. This setup provides a solid foundation you can extend with additional channels, filters, or scheduling as your project grows.
