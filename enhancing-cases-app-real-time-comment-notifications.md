# Enhancing Cases App: Real-time Comment Notifications

This tutorial demonstrates how to extend the functionality of an existing "Cases" application built with the ComUnity Developer Toolkit. We will implement a feature where users who have commented on a case are notified when a new comment is added to that same case. This enhancement significantly improves user engagement and provides timely updates in a collaborative case resolution process.

We will focus on modifying the data model, adding custom server-side logic, configuring communication channels, and building the necessary user interface screens to support this notification feature.

### What You’ll Learn

In this tutorial, you will:

* Extend an existing data model by creating a new **Comment** entity.
* Establish relationships (Table Links) between the **Comment** entity and existing entities (**Cases**, UserProfile).
* Configure role-based security (Table Security) for the new **Comment** entity.
* Implement custom C# code within the **Comment** entity's **onAdd** function to trigger an event when a new comment is created.
* Set up an in-app communication channel.
* Define a communication event and action template to send notifications to relevant users.
* Build and configure UI screens to display cases, view existing comments, and add new comments.
* Test the end-to-end notification functionality.

### Prerequisites

Before you begin, ensure you have the following:

* **Access Requirements:**
  * A ComUnity user account with the necessary permissions to create projects, modify data models, and configure communications.
  * An environment where the ComUnity Developer Toolkit is accessible.
* **Technical Knowledge:**
  * Basic understanding of C# programming.
  * Familiarity with data modelling concepts (entities, properties, relationships).
  * Experience navigating and using the ComUnity Developer Toolkit.
* **Existing Application:**
  * A pre-existing "Cases" application. If you don't have one, you'll need to create it first, typically using a relevant project template provided by the Toolkit. The steps below assume this base application is in place.

### Application Features (Enhanced)

This tutorial will add the following key feature to your Cases application:

* **Comment Notifications:** When a user adds a comment to a case, all other users who have previously commented on that specific fault will receive an in-app notification about the new comment.

### Walkthrough

Follow these steps to implement the comment notification feature.

#### 1. Project Setup and Initial Build

* When creating the project, ensure you include the **Cases** and **Notifications** templates, as these are required for a basic issue logging and response system. The **Cases** template (formerly known as **Fault Log**) allows users to log cases or issues, while admins manage, track, and resolve them. The Notifications template is used to wire in-app notifications into your project. Refer to the ComUnity Developer Toolkit documentation for detailed instructions on creating a project.
* Or else add the Cases and Notifications templates to a already existing project if they don't exist.

2. **Initial Build:**

* Build your project to ensure the base **Cases** application is functioning correctly before we begin adding new features.

#### 2. Extend the Data Model

We need to define a new entity to store comments and link it to case and users.

1. **Define the Comment Entity:**
   * Navigate to the **Data** section in the Toolkit.
   * Create a new Entity named **Comment**.
   * Add the following properties to the **Comment** entity:
     * `Content` (Type: `string`)
     * `CommentId` (Type: `Guid`, ensure this is set as the Primary Key, or if a default `Id` is created, you can rename/repurpose it or add `CommentId` specifically as a unique identifier).
2. **Create Table Links:** Establish relationships between the `Comment` entity and the `Case` and `UserProfile` entities. You will need to create two table links for the `Comment` table:
   * **Table Link: Comment to Case**
     * **From Entity:** `Case`
     * **From Relationship:** `*(Many)`
     * **From Navigation Name:** `Comments` (This will be the property name on the `Case` entity to access its comments)
     * **To Entity:** `Comment`
     * **To Relationship:** `1(One)`
     * **To Entity Navigation Name:** `Case` (This will be the property name on the `Comment` entity to access its parent case)
     * Ensure the `Add Foreign Key Property` link is **Checked** (enabled).
   * **Table Link: Comment to UserProfile (Commentator)**
     * **From Entity:** `UserProfile`
     * **From Relationship:** `*(Many)`
     * **From Navigation Name:** `Comments` (This will be the property name on the `UserProfile` entity to access comments made by the user)
     * **To Entity:** `Comment`
     * **To Relationship:** `1(One)`
     * **To Entity Navigation Name:** `Commentator` (This will be the property name on the `Comment` entity to access the user who made the comment)
     * Ensure the `Add Foreign Key Property` link is **Checked** (enabled).
3. **Configure Table Security for `Comment` Entity:** Set the permissions for different user roles on the `Comment` entity.
   * Select the `Comment` entity.
   * In the Properties Editor, locate the **Edit Table Security** setting.
   * Configure the permissions as follows:
     * **Administrator Role:** `All` permissions (Checked)
     * **Staff Role:** `All` permissions (Checked)
     *   **User Role:** `Insert` permission (Checked) and  `View` permission if users need to see comments. Adjust as per your own preferences.\
         \
         \


         <figure><img src=".gitbook/assets/image (483).png" alt=""><figcaption><p>Table Security for the Comment Entity</p></figcaption></figure>

#### 3. Implement Custom Code for Event Triggering

We'll add custom C# code to the **Comment** entity. This code will execute when a new comment is added, triggering an event that will be used for notifications.

1. **Access Custom Code for Comment Entity:**
   * With the **Comment** entity selected in the Data model, find the **Custom Code** setting in the Properties Editor and open it.
2. **Update Code to the class constructor:**
   1.  Locate the constructor function as shown below so as to inject a guid id whenever a comment in injected in the database:\


       <pre><code> public Comment() : base()
         {
           // END auto-generated, add custom code below this line
           // Check if id is a guid, if not inserted
           if(CommentId == Guid.Empty) {CommentId = Guid.NewGuid();}
       <strong> }
       </strong>		
       </code></pre>


3.  **Add Code to `onAdd` Function:**

    * Locate or add the `onAdd` function (this function is typically part of the entity's lifecycle hooks).
    * Insert the following C# snippet inside the `onAdd` function:

    ```
    public partial class Comment
    {
        partial void onAdd()
        {
            // Your existing onAdd logic, if any, can go here.

            var appName = Config.AppName();
            var comsService = Config.ComsService();

            if (appName != null && comsService != null)
            {
       
                var payload = ComsServices.JsonSerialize(this); 

                ComsServices.TriggerEvent(
                    appName,
                    "OnAddCommentDefault", // This is a unique name for your event
                    payload,
                    comsService,
                    Config.ComsServiceUsername(),
                    Config.ComsServicePassword()
                );
            }

            // Your existing onAdd logic, if any, can go here.
        }
        // Other custom code for your entity might be here
    }

    ```

    * **Note on `CaseCaseId`**: The audience query for notifications later uses `@Model.EventData.CaseCaseId`. Ensure that the CaseCase`Id` (or the correct navigation property representing the Case's ID) is part of the `Comment` entity data being serialized in `payload`. If `Comment` has a navigation property like `Case` which in turn has `CaseId`, the serialized payload should reflect this structure, or you might need to adjust the payload to include `CaseCaseId` directly if the `ComsServices.JsonSerialize(this)` doesn't automatically include it in a way that `EventData.CaseCaseId` can access. Often, this means ensuring the foreign key to `Case` is correctly named and populated on the `Comment` object before serialization.
4. **Save and Build:**
   * Click **Save** to persist your custom code changes.
   * Build your project to ensure there are no compilation errors.

#### 4. Setting Up Communication for Notifications

Configure the Toolkit's communication features to send notifications when the `OnAddCommentDefault` event is triggered.

1. **Configure Communication Channel:**
   * Click the **Project Settings** cog icon.
   * Navigate to the **Communication** tab.
   * Click **Add** to create a new communication channel.
   * Select **INAPP** as the channel type.
   * Set the **Channel Priority** to `Medium` (or as appropriate for your needs).
   * Click **Save** and close Project Settings.
2. **Create a Communication Event:**
   * In your Project navigation pane, go to **Communications**.
   * Click **Add an Event**. An "Add new event" modal will appear.
   * **Entity:** Select **Comment** (the entity that triggers the event).
   * **Event:** Enter `OnAddCommentDefault` (this must exactly match the event name used in your custom code).
   * **Name**: Leave Default selected so that the automatic event name created by the Toolkit  is `OnAddCommentDefault` (as this exactly match the event name used in your custom code).
   * Click **Create**.
3. **Define the Action Template (Audience and Content):**
   * Hover over your newly created `OnAddCommentDefault` event in the Communications list.
   * Click the **pencil (edit) icon** to open the Action Template modal.
   * **Configure the Audience Section:** This determines who receives the notification.
     *   **Member OData List URL:**

         <pre><code><strong>@Model.App.DataServiceUrl/UserProfile?$filter=Comments/any(com:com/Case/CaseId eq @Model.EventData.CaseCaseId)
         </strong></code></pre>

         * **Explanation:** This OData query aims to find `UserProfile` records.
           * `Comments/any(com:com/Case/CaseId eq @Model.EventData.CaseCaseId)`: Selects users who have made any comment (`com`) where that comment is linked to the same case (`Case/CaseId`) as the new comment (`@Model.EventData.CaseCaseId`). `@Model.EventData` refers to the payload you sent with `TriggerEvent`. Ensure your `Comment` payload correctly exposes `CaseCaseId` (e.g., via a navigation property or direct field).
           * `and Id ne @Model.EventData.Commentator.Id`: This part ensures the user who _just posted_ the comment does not receive a notification about their own comment. Assumes `Commentator.Id` is available in the event data.
     *   **ExpandPath Additional Data OData URL:**&#x20;

         ```
         @Model.App.DataServiceUrl/UserProfile(guid'@Model.EventData.CommentatorId')
         ```

         * **Explanation:** We will use the ExpandPath to populate the @Model.Data namespace with the commentator's user profile details.
   * **Member ID OData Field:** `Id` (This is typically the primary key field of the `UserProfile` entity).
   * Click **Save** to persist audience changes.
4. **Set Up INAPP Message Template:**
   * Within the same Action Template modal (or by re-opening it for the `OnAddCommentDefault` event), select the **INAPP** tab (for  the INAPP channel you configured).
   * Define the template for the in-app notification:
     * **USER ID:** `@Model.Profile.Id` (This tells the system which field on the audience member's profile contains their user ID).
       * **Title:** `New comment on an issues you are following`
       *   **Message:**&#x20;

           ```cshtml
           @Model.Data.Name commented: @Model.EventData.Content

           ```
5. **Save Changes:**
   * Click **Save** to persist your INAPP template settings.

#### 5. Build Application Screens

Now, let’s update the existing screens in the Cases app to let users view all cases, add and view comments, and also receive in-app notifications when other users comment on issues they’ve previously commented on.

1. **All Cases Screen:** This screen will list all cases logged in the app. Users can select a case to view its details and comments.
   * **Create Screen:**
     * Navigate to **Screens** in the Toolkit.
     * In your main app navigation structure, add a new **Navigation page**.
     * Set the following properties in the Properties Editor:
       * **Title:** `All Cases`
       * **Screen type:** `Navigation page`
       * **Icon:** Choose an appropriate icon (e.g., `svg/sdk/file-ruled-fill/Bootstrap/regular` or similar).
   * **Screen Structure (List of Cases):**
     * On the newly created `All  Cases` screen structure, add a **List** control.
     * Select the List control to open its properties in the Properties Editor.
     * Define the following:
       * **Data Path:** `/Case` (Case is the entity set name for cases).
       * **Target URL:** `LINK:AllCasesList_PageItem?id={{= CaseId}}`
         * **Important Note:** `DetailedCase_PageItem` is a placeholder for the system-generated name of the "Detailed Case"  screen you will create next. After creating the Detailed Case screen, verify its actual system name (often found in its **Name** setting in your Properties Editor) and update this `Target URL` accordingly. `{{= CaseId}}` assumes `CaseId` is the primary key of your `Case` entity.
     * Click **Save**.
2. **Detailed Case Screen:** This screen will show the details of a selected case and its associated comments.
   * **Create Screen (as a sub-screen):**
     * Go back to the `All Cases` screen in the screen structure.
     * Select the **List** control you added.
     * Drag a `Form` control from the **Screen Controls**  panel _into_ the **List** control. This action creates a sub-screen for each list item.
   * **Configure Sub-Screen:**
     * In the screen hierarchy (usually on the left pane), you should see a new sub-screen appear under "All Cases". It might have a default name. Click the **plus icon (+)** adjacent to `All Cases` if the sub-screen is not immediately visible.
     * Select this newly created sub-screen to configure it.
     * In the Properties Editor, set the following:
       * **Title:** `Detailed Case` (or `Case Details`)
       * **Target URL:** `/Case({{= id}})` (This sets the data context for the screen to a specific fault, using the `id` parameter passed from the `All Cases` list. Ensure `id` matches the parameter name in the `Target URL` of the All Cases list).
     * Click **Save**.
   * **Screen Structure for Detailed Case:**
     * **Display Case Properties:**
       * Drag an **Auto Inputs** (or "Auto Form" / "Detail View" depending on Toolkit version) control onto the `Detailed Case` screen structure. This control will display the properties of the `Case` entity.
       * Select the Auto Inputs control. In the Properties Editor:
         * **Exclude:** `Created,Modified,Comments,Name,Surname,Photo,StreetAddress,Status,Longitude,Latitude` (Adjust this list to exclude fields you don't want to display or that are handled differently).
         * **Field order:** `Description` (Optionally, specify the order of fields, e.g., place `Description` first).
       * Click **Save**.
     * **"Add Comment" Section:**
       * Drag a **List** control onto the `Detailed Case` screen canvas, placing it below the case details. This list will contain a single item to navigate to the "Add Comment" screen.
       * Select this newly created **List**.
       * Drag a **Single Item** control _into_ this **List**.
       * Select the Single Item control. In the Properties Editor:
         * **Icon:** Choose an icon (e.g., `svg/sdk/chat-dots/Bootstrap/regular`).
         * **Title/Label:** `Add a comment`
         * **DataPath**: `/Comments`
         * **Page:** `./AddComment`
           * **Note:** `AddComment` is a placeholder for the name of the "Add Comment" screen you will create under "Additional Screens". Update this once that screen is created and you know its actual navigation name or path.
       * Click **Save**.
     * **Display Comments Section:**
       * **Header:** Drag a **Paragraph** control onto the `Detailed Case` screen structure, below the "Add Comment" link section.
         * Select the Paragraph control. In the Properties Editor, under Markdown/Content, add: `### Comments`
         * Click **Save**.
       * **List of Comments:** Drag a **List** control onto the screen structure, below the "Comments" header.
         * Select this List control.
         * Drag an **Entity Item** _into_ this List.
         * Select the Entity Item control. In the Properties Editor:
           * **Entity Set or Navigation Property:** `/Comments` (This should be the navigation property from `Case` to `Comment` that you defined in the data model, e.g., `/Case({{=id}})/Comments` or simply `/Comments` given the context is already the specific fault).
           * **Target URL Prefix:** `/CaseCaseId({{ =Id}})`&#x20;
         * Click **Save**.
3. **Add Comment Screen:** This screen will be a form for users to type and submit a new comment.
   * **Create Screen:**
     * Navigate to the **Additional Screens** section of your project in the Toolkit (or the equivalent area for forms/modals not in the main navigation).
     * Select an existing screen or a folder, select an existing screen like UseProfile a modal will pop-up  choose the option like **Add Form**.
     * An "Add new Screen" modal will appear. Define the properties:
       * **Title:** `Add Comment`
       * **Entity:** `Comment`&#x20;
       * Click **Save**\
         (Note the system-generated **Name** value it must be consistent with **Page** value we specified in the Add Comment section of the "Detailed Case" screen).
   * **Screen Structure:**
     * **Comment Input Form:**
       * Drag an **Auto Inputs**  the `Add Comment` screen structure. This will create a form based on the **Comment** entity.
       * Select the **Auto Inputs** control. In the Properties Editor:
         * **Exclude:** `Commentator,Case,CommentId`
       * Click **Save**.
     * **Submit Button:**
       * Drag a **Button** control onto the structure, below the **Auto Inputs** form.
       * Select the **Button**, in the Properties Editor:
         * **Action:** `Save` (to save the new `Comment` record).
         *   **Document Template (for saving related data):**

             {% code overflow="wrap" %}
             ```
             {
             "Content":"{{= Content }}", "Commentator@odata.bind":"UserProfile(guid'{{=userguid}}')"
             }
             ```
             {% endcode %}

             * **Explanation & Important Notes:**
               * `{{= Content }}`: Binds to the content input by the user.
               * `{{=userguid}}`: This is a placeholder. The current logged-in user's GUID is already available in the page's context as `userguid`.&#x20;
         * **On Success Navigation:** On default you navigate back to the "Detailed Case" screen after successful submission.
       * Click **Save**.

#### 6. Final Build and Test Your Application

1. **Build Your App:**
   * Perform a full build of your project from the ComUnity Developer Toolkit.
2. **Launch and Login:**
   * The application should open automatically in a new browser tab after a successful build.
   * Create a new user account (e.g., UserA) if you haven't already, and log in.
   * Optionally, create a second user account (UserB) in a different browser or incognito window to test notifications between users.
   * For all testing user accounts ensure you complete your profile in app and include your name.
3. **Create a Test Case:**
   * Navigate to the section of your app where cases are created (this functionality should be part of your base Cases app).
   * Create a new general Case for testing.
4. **First User Adds a Comment:**
   * Log in as UserA.
   * Navigate to the **All Cases** screen.
   * Select the test case you created to go to its **Detailed Case** screen.
   * You should see the case details and the "Add New Comment" link.
   * Click "Add New Comment". You should be taken to the **Add Comment** screen.
   * Enter a comment in the `Content` field and click "Save".
   * You should be redirected back (if configured) or manually navigate back to the Detailed Case screen. Your new comment should be visible under the "Comments" section.
5. **Second User Adds a Comment (and First User gets Notified):**
   * Log in as UserB (in a separate browser session).
   * Navigate to the **All Cases** screen, find the same test case, and go to its **Detailed Case** screen. UserA's comment should be visible.
   * UserB clicks "Add New Comment", adds their own comment, and submits.
6. **Check Notifications for First User:**
   * Switch back to UserA's session.
   * Navigate to the **Notifications** tab/section in your main app navigation (this is a standard Toolkit feature).
   *   UserA should see an in-app notification stating that UserB commented on the case, along with the message content you defined in the INAPP template.\
       \


       <figure><img src=".gitbook/assets/image (482).png" alt=""><figcaption></figcaption></figure>
7. **Verify Custom Code and Event Triggering:**
   * If notifications are not working, check the Toolkit's logs or debugging tools for any errors related to the `onAdd` custom code in the `Comment` entity or the `ComsServices.TriggerEvent` call.
   * Verify that the event `OnAddCommentDefault` is being correctly triggered and that the payload contains the necessary data (`CaseCaseId`, `Commentator` details, `Content`).
   * Double-check the **Audience** OData query in the Communication Action Template for correctness and ensure it can resolve users based on the event payload.

### Conclusion

Congratulations! You have successfully extended your Cases application to include real-time comment notifications. Users are now informed when new comments are added to cases they are involved with, fostering better communication and quicker resolutions.

This tutorial covered extending the data model, implementing custom server-side logic for event triggering, configuring the Toolkit's communication system, and building the necessary UI screens.

**Further Enhancements to Explore:**

* **Email Notifications:** Extend the communication setup to also send email notifications in addition to in-app messages.
* **Notification Preferences:** Allow users to configure their notification preferences (e.g., opt-out of certain notifications).
* **Different Event Triggers:** Implement notifications for other events, such as when a case status changes.
* **UI Polish:** Further refine the UI for displaying comments and notifications for a better user experience.

By applying these concepts, you can continue to build more dynamic and interactive applications using the ComUnity Developer Toolkit.
