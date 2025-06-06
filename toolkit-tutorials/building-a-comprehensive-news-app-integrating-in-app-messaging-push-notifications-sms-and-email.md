# Building a Comprehensive News App: Integrating In-App Messaging, Push Notifications, SMS, and Email

In this tutorial, we focus to building a robust communication framework within news application on the ComUnity Platform, leveraging pre-built modules and functionalities available in the Toolkit. Starting with templates modules as our foundation, you’ll gain insights into efficiently integrating and customising these components to suit your application needs. As we progress, the tutorial will guide you through the setup of various communication channels—such as in-app messaging, push notifications, SMS, and email—offered by the Toolkit.

This structured approach not only simplifies the development process by using existing, well-tested modules but also lays a solid foundation for understanding how to establish effective communication mechanisms. By exploring these foundational setups, you will acquire the skills necessary to further enhance and scale any application on the dynamic ComUnity platform. By the end of this guide, you’ll not only have a bespoke blog application equipped with sophisticated communication tools but also the expertise to expand and adapt these functionalities to create more comprehensive applications.

{% hint style="info" %}
For a deeper understanding, refer to the [Communication](../toolkit-guides/communications/)s guide as you progress through this tutorial. This comprehensive resource provides additional details and explanations of the concepts covered here.
{% endhint %}

## **Overview**

In this comprehensive guide, you will:

* **Integrate Pre-built Modules**: Learn how to seamlessly integrate pre-built modules when creating your project, utilising existing functionalities to speed up development.
* **Extend the Data Model**: Expand the data model to include new entities that facilitate the integration of various communication channels, ensuring a robust foundation for your application’s communication needs.
* **Set Up Communication Process:** Define communication events and create templates for channels like in-app messaging, push notifications, SMS, and email. Implement change interceptors to dynamically manage messages, then activate these communication channels to start operations.
* **Test Communication Functionality**: Verify that the communication setup works as expected, ensuring reliable and effective communication throughout your application.

This tutorial is perfect for developers familiar with [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) , [WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022), [ Entity Framework](https://learn.microsoft.com/en-us/ef/), and [OData](https://www.odata.org/documentation/) who want to explore building applications on ComUnity.

## **Prerequisites:**

* Internet connection
* ComUnity user account with appropriate access (contact ComUnity support)
* [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) programming skills
* Understanding of [WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022),[ Entity Framework](https://learn.microsoft.com/en-us/ef/), and [OData](https://www.odata.org/documentation/)
* [Visual Studio 2022](https://visualstudio.microsoft.com/) (Community, Professional, or Enterprise)

## **Walkthrough**

1. [**Module Integration and Initial Setup**](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#module-integration-and-initial-setup)**:**
   * Start with the integration of necessary pre-built modules into your project, setting up the core functionalities of your blog application.
   * Configure initial project settings to incorporate these modules, ensuring they fit well within the overall application architecture.
2. [**Data Model Extension and Configuration**](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#data-model-extension-and-configuration)**:**
   * Extend your existing data model to include new entities necessary for supporting the planned communication functions, such as entities for communication preferences, logs, and user interactions.
   * Define and configure relationships between these new and existing entities to ensure smooth data flows and functionality integration.
3.  #### [Configuration of Communication Events and Sequential Template Setup](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#configuration-of-communication-events-and-sequential-template-setup-1)

    1\. Configuration of the Communication Template

    * Start with a Single Channel: Begin by configuring one communication channel, such as In-App Messaging. This channel should be set up to manage messaging operations triggered by user interactions or other specified events.
    * Configure Additional Channels Sequentially: Continue by setting up additional channels such as Push Notifications, SMS, and Email. Configure each channel one at a time to ensure detailed attention and comprehensive setup.

    2\. Adapting Change Interceptors for Event Handling

    * Implement Change Interceptors: For each configured channel, implement change interceptors. These interceptors are crucial for handling specific events that trigger communications, such as new post alerts, comment notifications, or urgent updates.
    * Ensure Effective Data Manipulation: Verify that interceptors are effectively accessing and manipulating the required data. They should integrate seamlessly with the communication functionalities to provide a smooth operational flow.
4. [**Activating Communication Channels and Setting Priorities:**](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#activating-communication-channels-and-setting-channel-priorities)  Initially, all communication channels are deactivated by default. Channel priorities determine the order in which communications are processed and sent.&#x20;
5. [**Testing and Validation for Each Channel:**](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#testing-and-validation-for-each-channel)
   * After configuring and setting up interceptors for a channel, conduct rigorous testing to ensure that communications are triggered appropriately and data handling is correct.
   * Validate the integration of each channel’s setup within the application, checking for performance issues or data inconsistencies.
   * Regularly publish these configurations to the ComUnity platform to test in a live-like environment, gathering feedback for iterative improvements.

## Module **Integration and Initial Setup**

In this section, we'll walk you through the process of creating a project by utilizing pre-defined  templates within the ComUnity Developer Toolkit. This approach allows you to leverage existing templates to quickly establish the foundation of your news application. Here are the steps to get started:

1. &#x20;Login into the ComUnity Developer Toolkit.
2.  Create a project using the **Custom Project** template with a unique title,  add search to add the **News,  Feedback** and **Notification**  templates in the **Select one or more templates to the project** field an illustration is shown in the following diagram:\


    <figure><img src="../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>
3.  **Build your project to verify the integrity of your Data Model and ensure that it is free from any errors.**\


    <figure><img src="../.gitbook/assets/image (401).png" alt=""><figcaption><p>Build and Launch</p></figcaption></figure>

## **Data Model Extension and Configuration**

In this section, we will focus on extending the Data Model. This involves creating additional entities that are crucial for configuring various communication channels within your application. We will also establish the necessary associations between these entities to ensure seamless data integration and functionality, in addition to that we will also configure table security settings for these entities to specify entity-level permissions, ensuring data integrity and access control.

1.  Define the following entities in your project's Data Model view [Customising the Data Model](../toolkit-guides/data/customising-the-data-model.md) to learn more if you are not sure how to proceed:\


    <table><thead><tr><th width="156">Entity</th><th width="108">Properties</th><th width="123">Data Types</th><th width="180">Rules</th><th width="117">Required</th><th>Default Value</th></tr></thead><tbody><tr><td>ShareWithFriend</td><td>FriendCell</td><td>string</td><td>          -</td><td>Checked</td><td>     -</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

    &#x20;
2.  In this step, we'll establish **Table Security** rules for the entities we've previously created. These rules are crucial as they determine who has the permissions to view, edit, and delete data within the table linked to each entity. the images that follow show the desired permission for the entities we added in the previous steps. Adjust the permissions by checking (to grant) or unchecking (to revoke) the relevant boxes for each role:\


    <figure><img src="../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure>
3.  In this step we will create associations of the entities we created in the step above, using the relationships specified in the table below, view [Creating Entity Associations: Configuring Table Links](../toolkit-guides/data/creating-entity-associations-configuring-table-links.md) to learn more if you are not sure how to proceed:\


    <table><thead><tr><th width="155">From Entity</th><th width="124">To Entity</th><th width="172">Relationship Type</th><th width="167">From Entity Navigation Name</th><th width="178">From Relationship</th><th width="165">To Entity Navigation Name</th><th width="150">To Relationship</th></tr></thead><tbody><tr><td>UserProfile</td><td>ShareWithFriend</td><td>One is to Many</td><td>Shares</td><td>0..*</td><td>Sender</td><td>0..1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>


4. **Build your project to verify the integrity of your Data Model and ensure that it is free from any errors.**&#x20;

We have successfully extended the Data Model, created necessary entity associations, and configured table security to enhance your application's communication functionalities. These steps ensure robust data integration and controlled access, preparing your system for advanced features.

Next, we will focus on configuring communication events and event triggers, which are essential for activating the application’s communication channels under specific conditions.

## Configuration of Communication Events and Sequential Template Setup

In this section, we will focus on the configuration and setup of interceptors for key communication channels within your application. These channels include:

* [**SMS**: Sharing the app with friends via SMS](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#sms-sharing-the-app-with-friends-via-sms)
* [**EMAIL**: Obtaining user feedback via email](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#email-obtaining-user-feedback-via-email)
* [**INAPP**: Sending in-app notifications to all users when new news articles are published](building-a-comprehensive-news-app-integrating-in-app-messaging-push-notifications-sms-and-email.md#inapp-sending-in-app-notifications-to-all-users-when-new-news-articles-are-published)

This setup involves detailed configuration of each specified templates, along with the implementation of interceptors that activate these communications under appropriate conditions. This framework not only supports these initial communication functionalities but is also designed to be scalable, allowing for the integration of additional channels as your application develops.

### SMS: Sharing the app with friends via SMS

To enable the feature that allows users to share your application with friends via SMS, follow these detailed steps:

1. **Access the Communication Settings:**
   * In the Toolkit, navigate to the sidebar and click on the "**Communication**" menu item. This will display any existing events in your project on the Communication screen.
   *   Click the "**+Add an event**" button. In the pop-up modal, select "**ShareWithFriend**" under the **Entity** field and "**OnAdd**" under the **Event** field. Leave the **Name** field at its default value "**Default**" and click "**Create**" to create the event.\


       <figure><img src="../.gitbook/assets/image (404).png" alt=""><figcaption></figcaption></figure>
2. **Configure the Event:**
   *   Select the event you just created, click its corresponding **pen icon** this will open the **Action Templates** modal of the current event.\


       <figure><img src="../.gitbook/assets/image (405).png" alt=""><figcaption></figcaption></figure>
   *   Under the **Details** tab, ensure the **Template Name** reads "**OnAddSharewithFriendDefault**".\


       <figure><img src="../.gitbook/assets/image (406).png" alt=""><figcaption></figcaption></figure>
   *   Switch to the **SMS** tab and click **"Add SMS Template"** and fill in the fields as instructed below (details for these fields should be provided here).\


       <table><thead><tr><th width="249">Field</th><th>Value</th></tr></thead><tbody><tr><td>Cell Number</td><td><p></p><pre class="language-csharp"><code class="lang-csharp">@Model.Data.FriendCell
       </code></pre></td></tr><tr><td>Message</td><td><p></p><pre class="language-csharp"><code class="lang-csharp"><strong>@{ var pre = ""; var post = ""; 
       </strong>if (Model.Data.UserName != "") 
       { pre = Model.Data.UserName + " has shared the"; post = "app with you,"; 
       } else { pre = @"The"; post = "app has been shared with you,"; 
       } } 
       @pre '@Model.Data.AppName @post please click: @Model.Data.Url
       </code></pre><p></p></td></tr></tbody></table>


   * Click "**Save**" to finalise the event configuration.
3. **Integrate Custom Code:**
   * Go to **Data** > **List** and select the "**ShareWithFriend**" entity, then click **More Settings** > **Custom Code**. A text editor will open showing the custom code associated with the current entity.
   *   Find the "**OnAdd**" change interceptor and add the specified code below the relevant comment.



       ```csharp
       // START auto-generated - OnAdd
       public override void OnAdd(newsappContext context)
       {
           base.OnAdd(context);
           // END auto-generated, add custom code below this line
           var un = "";
           if (!string.IsNullOrEmpty(Sender.Name))
               un += Sender.Name;
           if (!string.IsNullOrEmpty(Sender.Surname))
               un += un.Length == 0 ? "" : " " + Sender.Surname;
           if (un == "")
               un += Sender.Cell;
           var nameRec = Config.PublishedAppName();
           var urlRec = Config.BaseUrl();
           var appName = Config.AppName();
           var cs = Config.ComsService();
           if (nameRec != null && urlRec != null && appName != null && cs != null)
           {
               var data = new
               {
                   UserName = un,
                   FriendCell = FriendCell,
                   AppName = nameRec,
                   Url = urlRec,
               };
               var payload = ComsServices.JsonSerialize(data);
               ComsServices.TriggerEvent(appName, "OnAddShareWithFriend", payload, cs, Config.ComsServiceUsername(), Config.ComsServicePassword());
           }

       }

       ```


   * Close the text editor and click "**Save**" in the Properties Editor to apply the changes.
4. **Create the Share Screen:**
   * Click on the "**Screens**" menu item in the sidebar.
   * Find the **Feedback** screen, click the three-dot button next to it, and select "**Add screen below**".
   * In the modal that appears, set the **Title** to "**Share**", keep the default setting of "**Form page**" for the **Screen type**, and click the "**Add screen**" button.
   *   **Configure Screen Properties:** Select the **Share** screen and open the **Properties Editor** to adjust its settings as detailed in the following table. Focus only on the properties mentioned; leave all other properties at their default values unless specified otherwise.\


       <table><thead><tr><th width="125" align="center">Properties </th><th align="center">Property Value</th></tr></thead><tbody><tr><td align="center">Title</td><td align="center"><p></p><pre><code>Share App
       </code></pre></td></tr><tr><td align="center">Target URL</td><td align="center"><p></p><pre><code>/UserProfile(guid'{{=userguid}}')/Shares
       </code></pre><p></p></td></tr><tr><td align="center">Icon</td><td align="center"><p></p><pre data-title="// This icon is optional you can add any icon of your choice" data-full-width="true"><code>nn_share
       </code></pre></td></tr><tr><td align="center">Entity Name</td><td align="center">ShareWithFriend</td></tr></tbody></table>


   *   **Build Screen Content:** After setting the screen properties, build the content of the Share screen as outlined in the table below. Adjust screen controls and their properties as necessary to achieve the desired layout and functionality. Be sure to click the "**Save**" button in the Properties Editor to apply and preserve your changes.\


       <table><thead><tr><th width="191">Screen Control</th><th width="176" align="center">Properties </th><th align="center">Property Value</th></tr></thead><tbody><tr><td>Paragraph</td><td align="center">Markdown</td><td align="center"><p></p><pre><code>To share Our App with a friend, please insert their mobile number below:
       </code></pre></td></tr><tr><td>Input</td><td align="center">Property Name</td><td align="center"><p></p><pre><code>FriendCell
       </code></pre><p></p></td></tr><tr><td>Button</td><td align="center">Success Content</td><td align="center"><p></p><p></p><pre data-full-width="true"><code>Thank you for sharing our application.
       </code></pre><p></p></td></tr><tr><td></td><td align="center">Button Text (Long)</td><td align="center"><pre><code>Share
       </code></pre></td></tr><tr><td>Paragraph</td><td align="center">Markdown</td><td align="center"><p></p><pre data-full-width="true"><code>Our experience works on every type of mobile phone. Both Smart and Non-Smart devices. Please share it with your friends.
       </code></pre><p></p></td></tr></tbody></table>


5. **Build and Launch** your project that it is error-free. This step is crucial to confirm that all new configurations and code integrations have been correctly implemented. Launching your project also allows you to view changes in real-time, providing an immediate visual confirmation that your application behaves as expected.

### EMAIL: Obtaining user feedback via email

To enable the feature that allows users to share feedback about your application with friends via Email, follow these detailed steps:

{% hint style="info" %}
Dynamic email communications are exclusively restricted to email addresses issued by our organisation during testing. This means that both the 'from' and 'to' email addresses used in your communications must be officially provided by ComUnity Platform organisation. This policy ensures security and compliance with our internal email communication standards.

If you need to set up a 'to' email address for receiving test emails or require any assistance with email configuration, please contact the ComUnity Platform Team. They are available to provide you with the necessary support and guidance to ensure your email communications are set up correctly and efficiently.
{% endhint %}

1. **Access the Communication Settings:**
   * In the Toolkit, navigate to the sidebar and click on the "**Communication**" menu item. This will display any existing events in your project on the Communication screen.
   *   Click the "**+Add an event**" button. In the pop-up modal, select "**Feedback**" under the **Entity** field and "**OnAdd**" under the **Event** field. Leave the **Name** field at its default value "**Default**" and click "**Create**" to create the event.\


       <figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>
2. **Configure the Event:**
   *   Select the event you just created, click its corresponding **pen icon** this will open the **Action Templates** modal of the current event.\


       <figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>
   *   Under the **Details** tab, ensure the **Template Name** reads "**OnAddFeedbackDefault**".\


       <figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
   *   Switch to the **Email** tab and click **"Add Email Template"** and fill in the fields as instructed below (details for these fields should be provided here).\


       <table><thead><tr><th width="249">Field</th><th>Value</th></tr></thead><tbody><tr><td>To Address</td><td><p></p><pre class="language-csharp"><code class="lang-csharp">@Model.App.CustomerSupportEmailAddress
       </code></pre></td></tr><tr><td>FromAddress</td><td><p></p><pre><code>@Model.App.FromAddress
       </code></pre></td></tr><tr><td>Subject</td><td><pre><code>Attention: Feedback Submitted
       </code></pre></td></tr><tr><td>Text Body</td><td><pre><code>Feedback submitted from app
       </code></pre></td></tr></tbody></table>


   * Click "**Save**" to finalise the event configuration.
3. **Configure Communication Environment Variables** - CustomerSupportEmailAddress
   * Locate  and click Environment Settings' **cog** icon in the Toolkits top-navigation bar
   * Go to **Communication** > **Custom Values tab**, all custom environmental communication variables associated with your project will be displayed
   * Click Add a configuration setting a Add configuration modal will appear set the Name to CustomerSupportEmailAddress and the Value to a ComUnity Platform issued email address.
   * Click "**Add"** button.
4. **Integrate Custom Code:**
   * Go to **Data** > **List** and select the **"Feedback"** entity, then click **More Settings** > **Custom Code**. A text editor will open showing the custom code associated with the current entity.
   *   Find the "**OnAdd**" change interceptor and add the specified code below the relevant comment.



       ```csharp
       // START auto-generated - OnAdd
       public override void OnAdd(newsappContext context)
       {
           base.OnAdd(context);
           Serviced = false;

       // END auto-generated, add custom code below this line
           var an = Config.AppName();
           var cs = Config.ComsService();
           if (an != null && cs != null)
           {
               var payload = ComsServices.JsonSerialize(this);
               ComsServices.TriggerEvent(an, "OnAddFeedbackDefault", payload, cs, Config.ComsServiceUsername(), Config.ComsServicePassword());
           }

       }
       ```


   * Close the text editor and click "**Save**" in the Properties Editor to apply the changes.
5. **Build and Launch** your project that it is error-free. This step is crucial to confirm that all new configurations and code integrations have been correctly implemented. Launching your project also allows you to view changes in real-time, providing an immediate visual confirmation that your application behaves as expected.

## **INAPP**: Sending in-app notifications to all users when new news articles are published

To enable the feature that allows users to receive in-app notifications about new news articles published in your application, follow these detailed steps:

1. **Access the Communication Settings:**
   * In the Toolkit, navigate to the sidebar and click on the "**Communication**" menu item. This will display any existing events in your project on the Communication screen.
   *   Click the "**+Add an event**" button. In the pop-up modal, select "**News**" under the **Entity** field and "**OnAdd**" under the **Event** field. Leave the **Name** field at its default value "**Default**" and click "**Create**" to create the event.\


       <figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>
2.  **Configure the Event:**

    *   Select the event you just created, click its corresponding **pen icon** this will open the **Action Templates** modal of the current event.\


        <figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>
    *   Under the **Details** tab, ensure the **Template Name** reads "**OnAddNewsDefault**" and fill in the fields as instructed below (details for these fields should be provided in the table below)\


        <figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

    &#x20;\


    <table><thead><tr><th width="249">Field</th><th>Value</th></tr></thead><tbody><tr><td>Member OData List URL</td><td><p></p><pre class="language-csharp"><code class="lang-csharp">@Model.App.DataServiceUrl/UserProfile
    </code></pre></td></tr><tr><td>Member ID OData Field</td><td><p></p><pre><code>Id
    </code></pre></td></tr></tbody></table>



    * Click "**Save**" to finalise the event details configuration.
    *   Select **In App** tab, fill in the fields **User Id**,  **Action**, **Title** and **Message**, as instructed below (details for these field values should be provided in the table below):\


        <figure><img src="../.gitbook/assets/image (415).png" alt=""><figcaption></figcaption></figure>



        <table><thead><tr><th width="249">Field</th><th>Value</th></tr></thead><tbody><tr><td>User ID</td><td><pre><code>@Model.Profile.Id
        </code></pre></td></tr><tr><td>Action</td><td><p></p><pre><code>LINK:NewsItem?id=@Model.EventData.NewsId
        </code></pre></td></tr><tr><td>Title</td><td><pre><code>@Model.EventData.Title
        </code></pre></td></tr><tr><td>Message</td><td><pre><code>@Model.EventData.Description
        </code></pre></td></tr></tbody></table>


    * Click "**Save**" to finalise the in-app notification template configuration.
3. **Integrate Custom Code:**
   * Go to **Data** > **List** and select the **"News"** entity, then click **More Settings** > **Custom Code**. A text editor will open showing the custom code associated with the current entity.
   *   Find the "**OnAdd**" change interceptor and add the specified code below the relevant comment.



       ```csharp
       // START auto-generated - OnAdd
       public override void OnAdd(newsappContext context)
       {
          base.OnAdd(context);
          var dt = Created == null ? DateTime.UtcNow : Created;
          CreatedDateStr = dt.ToString("dd MMM yyyy - HH:mm");	

       // END auto-generated, add custom code below this line
           var an = Config.AppName();
           var cs = Config.ComsService();
           if (an != null && cs != null)
           {
               var payload = ComsServices.JsonSerialize(this);
               ComsServices.TriggerEvent(an, "OnAddNewsDefault", payload, cs, Config.ComsServiceUsername(), Config.ComsServicePassword());   
           }

       }
       ```


   * Close the text editor and click "**Save**" in the Properties Editor to apply the changes.
4. **Build and Launch** your project that it is error-free. This step is crucial to confirm that all new configurations and code integrations have been correctly implemented. Launching your project also allows you to view changes in real-time, providing an immediate visual confirmation that your application behaves as expected.

## **Activating Communication Channels and Setting Channel Priorities**

To enable communications, specify channel priorities within the channel settings. This activation is essential for starting the communication process.&#x20;

To initialise communication channels, follow these steps:

1.  In the Toolkit, navigate to the Project name in the bottom left of the navigation bar click the Project Settings **cog** icons, the Project settings modal will appear:\


    <figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption><p>Project Settings</p></figcaption></figure>
2.  Select the **Communications** tab to view **Channel Priorities** in your project if any exist:\


    <figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption><p>Channel Priorities</p></figcaption></figure>
3.  Click **+Add a channel priority** button in the **Add a channel priority** modal that appears select **EMAIL** and click the **Add** button.\


    <figure><img src="../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>
4. Repeat the step above to select on channels **INAPP** and **SMS**.
5. **Launch** your project and proceed to test the Communication we have set up in the previous steps.

## **Testing and Validation for Each Channel**

To ensure that the communication events and event handlers set up in your project function as intended, we recommend conducting thorough testing by following typical user actions within the application. Below are step-by-step instructions to test each communication channel, using the example of sharing the app with friends via SMS:

1. **Launch the Web App:**
   * Start by launching the project web application to access its features.
2. **Create and Use a User Account:**
   * Sign up to create a new user account.
   * Or else, sign in with your new account credentials.
3. **Create Another User Account with Staff Role:**
   * **Sign Up for a Second Account**:
   * Repeat the sign-up process to create a second user account.
   * **Assign Staff Role**:
     * Assign it the "Staff" role within the Toolkit view[ Users and Roles ](../getting-started/manage-your-project/users-and-roles.md)for more details about user management

**Test SMS Communication:**

1. Navigate to the **Share** page within the web app.
2. Enter a valid cell phone number into the "**Friend Cell**" field.
3. Click the "**Share**" button.
4. Verify that the cell number entered receives the intended SMS message, confirming that the SMS functionality is working correctly.

<figure><img src="../.gitbook/assets/image (407).png" alt=""><figcaption></figcaption></figure>

**Test Email Communication:**

1. Navigate to the Feedback page within the web app.
2. Enter  feedback in the "**PLEASE ENTER FEEDBACK**" field.
3. Click the "**SEND**" button.
4. Verify that the email address you configured to receive feedback email  receives the intended email message, confirming that the Email functionality is working correctly.

**Test In-App Communication:**

1. **Sign In as Admin**:
   * Use your admin account credentials to sign in.
2. **Navigate to News Article Section**:
   * Go to the "Admin" tab in the main menu.
   * Select "News Article".
3. **Add and Publish a News Article**:
   * Click on "Add New Article".
   * Fill in the article details (e.g., title, description, detail and photo).
   * Publish the article.
4. **Check Notifications**:
   * Navigate to the "Notification" tab.
   * You should see a  personal notification alerting you that a news article has been published.
   * This confirms that the in-app notification functionality is working correctly.

This process simulates a real user's experience, allowing you to confirm the operational effectiveness of communication features and to identify any areas needing adjustment.
