---
hidden: true
---

# Bulk SMS Campaigns

This guide details the process for creating an administrative screen to broadcast bulk SMS messages. The system will target all **UserProfile** records that meet three conditions: they are assigned the Recipient role, have opted-in to mobile communications **(ContactByMobile** is true), and have a valid South African phone number (the **Cell** field starts with `+27`).

#### Prerequisites

Before proceeding, confirm the project environment is configured as follows:

* Project Template: The project was created using the News Feed template and includes the Notifications and the UserRoles templates
* Entities:
  * UserProfile (platform): Contains the fields `Id` (Guid), `Cell` (string), `ContactByMobile` (bool), `Name`, `Surname` and `Email`.
  * Campaign (custom): Contains the fields `CampaignId` (int) and `Message` (string).
  *
* Roles: Two user roles, Staff and Recipient, must exist in the project, Staff is provided by default create the Recipient role.
* SMS Provider: By default a South African SMS provider has been configured under Project Settings → Communications → SMS, update this to meet your specific needs.&#x20;
*   User Data Model: The UserProfile entity is a standard part of the platform's data model that holds a user's personal details. A user's assigned roles are stored in a related collection. The OData query used later in this tutorial (`$expand=Roles`) is the key to linking a user's profile to their roles for filtering. For context, a typical user data object from the system looks like this:

    JSON

    ```
    {
        "Id": "6F8D39F7-BDCB-4D0C-B737-DB6B9BE5BEDC",
        "userguid": "6F8D39F7-BDCB-4D0C-B737-DB6B9BE5BEDC",
        "Identifier": "jacquelineb@comunityplatform.com",
        "profile": {
            "Id": "6F8D39F7-BDCB-4D0C-B737-DB6B9BE5BEDC",
            "Email": "user@example.com",
            "Photo": null,
            "Name": "Jack",
            "Surname": "Sparrow",
            "Created": "2025-09-01T03:44:19.667",
            "Modified": "2025-09-01T03:44:20.823",
            "Deleted": null,
            "Cell": null,
            "ContactByMobile": true,
            "ContactByEmail": true,
            "ContactByPush": true,
            "StreetAddress": null
        },
        "roles": [
            "Staff"
        ]
    }
    ```



#### Step 1: Configure User Roles and Permissions

The first step is to configure the necessary platform user roles. The **Staff** role grants permission to create and send campaigns, while the **Recipient** role identifies the target audience for these campaigns.

1. Navigate to Project Settings → App users & roles → Roles.
2. Verify that both Admin and Recipient roles are present.
3. Assign the Admin role to your administrative user account.
4. Assign the Recipient role to all user profiles that should be eligible to receive SMS broadcasts.

#### Step 2: Build the Admin Campaign Screen

This step involves creating the user interface for composing and sending campaign messages.

1. Navigate to Screens → Add screen and select the Form page template.
2. Set the form's Entity to Campaign and its Title to **Campaign**.
3. Add an Input control and bind it to the Message field. It is recommended to set the control's Type to Text Area.
4. In the screen's Properties → Permissions, restrict screen visibility to the Admin role.
5. Save the screen.

Saving a record from this form creates a new row in the **Campaign** entity, which triggers the **OnAdd** event configured in the subsequent steps.

#### Step 3: Create the SMS Broadcast Event

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

#### Step 4: Trigger the Event with a Custom Interceptor

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
4. Save the custom code.

#### Step 5: Configure the SMS Provider

Ensure the project is correctly linked to the configured SMS service.

1. Navigate to Project Settings → Communications → SMS.
2. Select the configured South African provider (or Mock Service for development).
3. Enter the required API credentials and sender ID.
4. Save the configuration and build the project.

#### Step 6: Implement Data Validation

To ensure data integrity and prevent delivery errors, add a client-side validation rule to the `Cell` input on the `UserProfile` form.

1. Open the `UserProfile` form for editing.
2. Select the input control bound to the Cell field.
3. Add a Regex validation rule with the following settings:
   * Label: `Mobile`
   * Regex Rule: `^\+27\d{9}$`
   * Error Message: `Enter a valid South African mobile number, e.g. +27821234567.`

Optional Enhancement: To improve user experience, consider adding server-side code (to the `OnUpdate`/`OnAdd` events of `UserProfile`) to automatically sanitize the input by stripping characters like spaces or dashes before validation.

#### Step 7: Perform End-to-End Testing

The final step is to test the system to ensure it functions as expected.

1. Prepare a test user profile that meets all the targeting criteria:
   * The user must be assigned the Recipient role.
   * The `ContactByMobile` boolean field must be set to `true`.
   * The `Cell` field must contain a valid South African number (e.g., `+27821234567`).
2. Log in to the application with an Admin user account.
3. Navigate to the Campaign screen.
4. Enter a test message and Save the form.

An SMS should be delivered to the test device. If using the Mock Service, verify the request was sent by checking the provider's logs or developer console.

