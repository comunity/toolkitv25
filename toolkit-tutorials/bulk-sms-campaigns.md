---
hidden: true
---

# Bulk SMS Campaigns

This guide details the process for creating an administrative screen to broadcast bulk SMS messages. The system will target all **UserProfile** records that meet three conditions: they are assigned the Recipient  user role, have opted-in to mobile communications **(ContactByMobile** is true), and have a valid South African phone number (the **Cell** field starts with `+27`).

#### Prerequisites

Before proceeding, confirm the project environment is configured as follows:

* Project Template: The project was created using the **News Feed** template and includes the **Notifications** and the **UserRoles** templates, refer to&#x20;
* Entities:
  * UserProfile (platform): Contains the fields `Id` (Guid), `Cell` (string), `ContactByMobile` (bool), `Name`, `Surname` and `Email`.
  * Campaign (custom): Contains the fields `CampaignId` (int) and `Message` (string).
* SMS Provider: By default a MeSMS provider has been configured under Project Settings → Communications → SMS, update this to meet your specific needs.&#x20;
* Successfully build your project.

### Validate Platform Roles, Application Roles, and Permissions

The first step is to confirm that the correct platform authorisation roles and application roles exist and are configured with the right permissions.

* Platform Roles: These are default authorisation roles available to all projects.
  * The Staff role is particularly important, as it grants permission to create and send campaigns.
* Application Roles: These are project-specific roles introduced via the UserRoles template.
  * Create a role called Recipient to identify the target audience for campaigns.
  * This role is stored in the UserRole entity and allows you to segment users and query them in the Data Model.

{% hint style="info" %}
When you build your project, the platform roles are automatically used to populate application roles, which are then persisted in the UserRole table.
{% endhint %}

### Build Your Project

Build your project to ensure that platform and application roles are correctly generated and available for assignment.

#### Create and Assign User Accounts

1. Create two user accounts with different email addresses.
2. Navigate to App Users & Roles in Project Settings, then open the Development environment tab.
3.  Assign the Staff role to one user — this grants the necessary authorisation to manage and send campaigns. You can confirm this capability by going to **Screens** > **Administration** > **User Admin Options** > **Edit User Role**, this screen helps you manage user roles and its added to the project as part of the UserRole template:\


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
2. Click the ellipsis (⋮) next to Sent Messages, then select “Add screen below”.
3. Choose Form page as the screen type and set the page title to Campaigns.
4. Select the newly created Campaign screen set its Target URL to /Campaign
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

    Code snippet

    ```
    @Model.App.DataServiceUrl/UserProfile?$expand=Roles&$filter=Roles/any(r: r/Name eq 'Recipient') and ContactByMobile eq true and length(Cell) gt 0 and startswith(Cell,'+27')
    ```
*   Member ID OData field:

    ```
    Id
    ```

**SMS Tab (Message Content)**

Define the SMS message template. The communication engine will generate and send one message per user returned by the audience query.

*   Cell Number:

    ```
    @Model.Member.Cell
    ```

    This expression pulls the cell number from each individual user record identified by the audience query.
*   Message:

    ```
    @Model.EventData.Message
    ```

    This expression pulls the message content from the `Campaign` record that triggered the event.

#### Trigger the Event with a Custom Interceptor

An interceptor is custom code that executes when a data event occurs. You will add code to the `OnAdd` event of the `Campaign` entity to trigger the communication event when a new campaign is saved.

1. Navigate to Data → List → Campaign.
2. Select More Settings → Custom Code → OnAdd.
3.  Add the following C# code below the auto-generated line:

    C#

    ```
    // Triggers the Action Template; the audience query handles the fan-out.
    ComsServices.TriggerEvent(
        Config.AppName(),
        "OnAddCampaignDefault", // Must match the event name from Step 3
        ComsServices.JsonSerialize(new { Message = Message }),
        Config.ComsService(),
        Config.ComsServiceUsername(),
        Config.ComsServicePassword()
    );
    ```
4. Save the Custom Code.

#### Configure the SMS Provider

Ensure the project is correctly linked to the configured SMS service.

1. Navigate to Project Settings → Communications → SMS.
2. Select the configured South African provider (or Mock Service for development).
3. Enter the required API credentials and sender ID.
4. Save the configuration and build the project.

#### Implement Data Validation

To ensure data integrity and prevent delivery errors, add a client-side validation rule to the `Cell` input on the `UserProfile` form.

1. Open the `UserProfile` form for editing.
2. Select the input control bound to the Cell field.
3. Add a Regex validation rule with the following settings:
   * Label: `Mobile`
   * Regex Rule: `^\+27\d{9}$`
   * Error Message: `Enter a valid South African mobile number, e.g. +27821234567.`

Optional Enhancement: To improve user experience, consider adding server-side code (to the `OnUpdate`/`OnAdd` events of `UserProfile`) to automatically sanitize the input by stripping characters like spaces or dashes before validation.

### Perform End-to-End Testing

The final step is to test the system to ensure it functions as expected.

1. Prepare a test user profile that meets all the targeting criteria:
   * The user must be assigned the Recipient role.
   * The `ContactByMobile` boolean field must be set to `true`.
   * The `Cell` field must contain a valid South African number (e.g., `+27821234567`).
2. Log in to the application with an Admin user account.
3. Navigate to the Campaign screen.
4. Enter a test message and Save the form.

An SMS should be delivered to the test device. If using the Mock Service, verify the request was sent by checking the provider's logs or developer console.

