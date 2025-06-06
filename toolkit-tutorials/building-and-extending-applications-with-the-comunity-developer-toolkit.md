# Build a Simple Blog App: The Beginner's Guide to ComUnity Development

In this tutorial, we focus on building a blog application from scratch on the ComUnity Platform. You'll start by developing your own data model, giving you full control over its customisation and a clear understanding of its structure. As the tutorial progresses, we'll guide you through extending this data model, enhancing your application with additional features and functionalities. This approach provides a thorough learning experience for developers eager to understand and utilise the full capabilities of the ComUnity platform. By the end of this guide, you’ll not only have a bespoke blog application but also the skills to extend and improve applications within this dynamic platform.

## What you will learn?

Through this hands-on guide, you'll learn to:

* Define your data model with entities like articles and comments.
* Configure metadata for user access, pages, and navigation.
* Extend the data service for notifications and external data integration.
* Publish your data service for use in the ComUnity platform.

This tutorial is perfect for developers familiar with [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) , [WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022), [ Entity Framework](https://learn.microsoft.com/en-us/ef/), and [OData](https://www.odata.org/documentation/) who want to explore building applications on ComUnity.

## **ComUnity Developer Toolkit Environment:**

The ComUnity Developer Toolkit is hosted in Azure and accessible at: [https://toolkit.comunity.me/](https://toolkit.comunity.me/)

## **Prerequisites:**

* Internet connection
* ComUnity user account with appropriate access (contact ComUnity support)
* [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) programming skills
* Understanding of [WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022),[ Entity Framework](https://learn.microsoft.com/en-us/ef/), and [OData](https://www.odata.org/documentation/)
* [Visual Studio 2022](https://visualstudio.microsoft.com/) (Community, Professional, or Enterprise)

{% hint style="info" %}
Changes made to the Data Service require you to **Build** your app to publish these changes. Subsequently, when modifications are made to screens, you must **Launch** your app to update the application metadata. For further details, see [**Build** and **Launch**](../getting-started/manage-your-project/build-and-launch-your-project.md).
{% endhint %}

## **Assets:**

This section contains various assets which are used in the tutorial.

{% file src="../.gitbook/assets/divider.png" %}

## **Blog Application Features:**

This tutorial builds a simple blog app with the following features:

* Users can create, edit, and publish articles.
* All users can view articles and add comments.
* Authors can tag blog articles and readers can view, and comment on tagged articles.

## **Walkthrough**

1. [**Data Model Configuration**](building-and-extending-applications-with-the-comunity-developer-toolkit.md#data-model-configuration)**:** Define the entities and relationships for your blog application.
2. [**Data Service Publishing**](building-and-extending-applications-with-the-comunity-developer-toolkit.md#data-service-publishing)**:** Publish your defined data model and make it accessible on ComUnity.
3. [**Metadata Configuration**](building-and-extending-applications-with-the-comunity-developer-toolkit.md#metadata-configuration)**:** Set up access rights, pages, and navigation for your blog app.

## **Data Model**

The following diagram shows the data model that will be created for the example application.

<figure><img src="../.gitbook/assets/image (338).png" alt=""><figcaption></figcaption></figure>

## **Data Service Project Development**&#x20;

The ComUnity platform leverages the Entity Framework Code First approach for the Data Service project, which forms the backbone of your application's data model. The Platform Toolkit Application streamlines the process of creating your data services project. It allows for the data model to be outlined through configuration data, simplifying the development process. Once your data model is defined, the Platform Toolkit Application will take charge, automatically generating, building, and publishing the data service project to IIS. This section will guide you through these steps, ensuring a smooth transition from concept to a functioning component of your application.

### Data Model Configuration

To configure your Data Model, follow these steps:

1. &#x20;Login into the ComUnity Developer Toolkit.
2.  Create a project using the Blank Project template with a unique title, an illustration is shown in the following diagram:\


    <figure><img src="../.gitbook/assets/Screenshot 2023-12-18 at 06.01.26.png" alt=""><figcaption><p>Create a new Blank Project in the ComUnity Developer Toolkit</p></figcaption></figure>
3.  After successfully creating your project the Toolkit will successfully redirect you to your project structure. The diagrams below show a the structure of the created Data Model of your project:\


    <figure><img src="../.gitbook/assets/image (336).png" alt=""><figcaption><p>The Data Model of a newly created BlogApp shown as a List</p></figcaption></figure>

    <figure><img src="../.gitbook/assets/image (337).png" alt=""><figcaption><p>The Data Model of a newly created BlogApp shown as a Diagram</p></figcaption></figure>
4. In this step we will create the custom entities shown in the Entity Relationship Diagram (ERD) of the application above and populate them with field properties, to get started:
   1. Navigate to the "**Data**" section within the Toolkit. Once there, locate and click on the "**List view**" tab. This area allows you to view and manage the entities within your data model.
   2. Locate and click the **"Add new entity"** icon to initiate the creation of a new entity.
   3. In the **"Entity Name"** field, enter `Post` as the name of your new entity.
   4.  Confirm the creation by clicking the **"Add Entity"** button. This action will successfully create the "**Post**" entity within your Data Model.\


       <figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Adding the Post entity to the Data Model</p></figcaption></figure>

       <figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Default attributes or properties of a newly created Post entity</p></figcaption></figure>
   5.  To add custom properties to the "Post" entity, right-click on any existing property, follow these steps:

       1. Expand the "**Post**" entity to reveal its properties by clicking the **"+"** sign next to the entity's name.
       2.  To add a new property, click on any existing property within the "Post" entity. A modal will appear, offering you the options to **"Add a property above"** or **"Add a property below"** the selected property. Select a single option from these choices. Refer to the screenshot provided for guidance:\


           <figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption><p>Add properties to an entity</p></figcaption></figure>


       3.  In the **"Add new property"** modal that pops up, enter the desired property name. Finalise this action by clicking the **"Save"** button, as illustrated in the diagram below. Note that the Table in step 5 contains an exhaustive list of all the entities required for the application and their relevant properties.\


           <figure><img src="../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>
       4.  After saving, select the newly added property to customise it further in the Properties Editor. For example, we have adjusted the "**Summary**" property by setting its data type to 'String' (which is the default) and restricting the "**Max Length**" to 256 characters, as shown in the subsequent screenshot.\


           <figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption></figcaption></figure>
       5. Click **"Save"** to apply these specifications and repeat the steps specified above using the data specified in the table below:\


       <table><thead><tr><th width="156">Entity</th><th width="108">Properties</th><th width="123">Data Types</th><th width="180">Rules</th><th width="117">Required</th><th>Default Value</th></tr></thead><tbody><tr><td>Post</td><td>Title</td><td>string</td><td>Max Length = 64</td><td>Checked</td><td>-</td></tr><tr><td></td><td>Summary</td><td>string</td><td>Max Length = 256</td><td>Checked</td><td>-</td></tr><tr><td></td><td>Body</td><td>string</td><td>            -</td><td>Unchecked</td><td>-</td></tr><tr><td></td><td>Publish</td><td>bool</td><td>             -</td><td>Checked</td><td>false</td></tr><tr><td>Tag </td><td>Name</td><td>string</td><td>Max Length = 32</td><td>Checked</td><td>-</td></tr><tr><td></td><td>Icon</td><td>string</td><td>Max Length = 50</td><td>Unchecked</td><td>-</td></tr><tr><td>Comment</td><td>Detail</td><td>string</td><td>            -</td><td>Checked</td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>
5. In this step, we'll establish **Table Security** rules for the entities we've previously created. These rules are crucial as they determine who has the permissions to view, edit, and delete data within the table linked to each entity. Follow the steps below to configure Table Security rules for the "Post" entity:
   1. Navigate to the List view of the entities in your Data Model
   2. Locate and select the "**Post**" entity from the list. This action will activate the Properties Editor specifically for the "Post" entity, allowing you to modify its settings.
   3. With the "**Post**" entity selected, look for and click on the "**Edit Security**" option. This action will open the "Table Security for Post" modal.
   4.  Within the modal, you will see various permissions that can be enabled or disabled for different roles. Refer to the image below for the desired output settings for the "**Post**" Entity. Adjust the permissions by checking (to grant) or unchecking (to revoke) the relevant boxes for each role:\


       <figure><img src="../.gitbook/assets/image (379).png" alt=""><figcaption></figcaption></figure>
   5. After configuring the security settings for the "Post" entity, repeat the same steps for each entity you have added to the Data Model. Select the entity, click on "Edit Security," and adjust the permissions as necessary, ensuring comprehensive security coverage across all entities.
6. In this step we will create associations of the entities we created in the step above, lets link the User Profile to the Post entity, to get started:
   1. Navigate to the List view of the entities in your Data Model
   2. Select the UserProfile entity&#x20;
   3.  Click the icon to add an association, in the Add new entity link you must specify the from and to  entities of your association for which in the case the from entity is the UserProfile and the to entity is Post and then click the Save button\
       \


       <figure><img src="../.gitbook/assets/image (334).png" alt=""><figcaption></figcaption></figure>
   4. &#x20;To view the association between UserProfile and  Post entities created in the previous step, simply expand the collapsible UserProfile in the list. You'll see the Post association listed beneath it, indicating their connection.&#x20;
   5.  Select the association to configure its properties in the Properties Editor, in this case you set the From Relationship to 1(One) and the To Relationship to \*(Many) and click the Save button to persist your settings.\


       <div align="left"><figure><img src="../.gitbook/assets/image (84).png" alt="" width="230"><figcaption></figcaption></figure></div>
   6.  Click Save and repeat the steps specified above using the relationships specified in the table below and ensure that the field "**Add Foreign Key Property"** is checked for all associations you create.\


       <table><thead><tr><th width="155">From Entity</th><th width="124">To Entity</th><th width="172">Relationship Type</th><th width="167">From Entity Navigation Name</th><th width="178">From Relationship</th><th width="165">To Entity Navigation Name</th><th width="150">To Relationship</th></tr></thead><tbody><tr><td>UserProfile</td><td>Post</td><td>One is to Many</td><td>Posts</td><td>Many</td><td>User</td><td>0..1</td></tr><tr><td>UserProfile</td><td>Comment</td><td>One is to Many</td><td>Comments</td><td>Many</td><td>User</td><td>0..1</td></tr><tr><td>Post </td><td>Tag</td><td>Many to  Many</td><td>Tags</td><td>Many</td><td>Posts</td><td>Many</td></tr><tr><td>Post</td><td>Comment</td><td>One is to Many</td><td>Comments</td><td>Many</td><td>Post</td><td>0..1</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

## Data Service Publishing

The ComUnity Developer Toolkit streamlines the development process by automatically provisioning necessary resources on Microsoft Azure and constructing your Data Service project based on the defined data model. This integration includes executing data migrations for existing databases and deploying your project to Internet Information Services (IIS) following a successful build. However, it's crucial to note that any alterations to the data model, custom classes, or virtual entities necessitate a project rebuild to avoid data loss and maintain application consistency, to learn more view [Build and Launch your project](../getting-started/manage-your-project/build-and-launch-your-project.md).

When viewing your application in the browser you will be redirected to the Accept Terms, after clicking the "ACCEPT TERMS" button users are redirected to the authentication screens:

<figure><img src="../.gitbook/assets/image (339).png" alt=""><figcaption><p>Accept Term screen</p></figcaption></figure>

## **Metadata Configuration**&#x20;

In this section of the tutorial, we'll focus on how metadata is utilised to design the application's navigation and its pages. You'll learn how to create various screens for key functionalities, including:

* Viewing all published articles.
* Browsing articles categorised by tags.
* Creating, editing, and tagging posts.
* Editing user profiles.
* Adding comments to articles.
* Admin functions like adding or removing tags, editing all articles, and managing comments (including deletion).

We'll also delve into setting up navigation items. These links are essential for connecting the pages and defining the application's flow. They play a crucial role in forming simple pages containing lists and in structuring the application menus.

Let's create the main screens that exist in the app, the app requires the following screens:

* My Articles - a screen allows users to view all articles they created
* Add Article - a screen that allows users to add blog articles
* Edit Article - a screen that allows users to edit the blog articles they created
* All Articles - a screen that allows users to view all published blog articles
* View Article - a screen that allows users to view a single blog article and  navigate to an Add Comment
* Add Comment -  a screen that allows users to add comments to a blog article

The diagram below shows the hierarchical structure of the aforementioned screens:

<figure><img src="../.gitbook/assets/image (380).png" alt="" width="308"><figcaption><p>Screen hierarchy in the Blog application </p></figcaption></figure>

### My Articles screen

**Data Entry Screens** are a powerful feature of the Toolkit that automate the creation of user interfaces for interacting with database entities. By simply selecting an entity, the Toolkit generates a suite of screens allowing users to view all items associated with that entity, inspect details of individual items, and update information as needed. This functionality is particularly useful for applications requiring dynamic content management, such as managing articles or blog posts. The **"My Articles"** screen will comprise a group of screens enabling users to create blog posts, view their posts, and edit them created from Data Entry Screens. Additionally, these screens will be further customised to incorporate the functionality of adding **Tags**, enhancing the organisation and searchability of content.\
\
To create the **My Articles** screen and its child screens, follow these steps:

1. In the Toolkit, find and click on the **"Screens"** menu item located in the sidebar. All screens which exist in your application will be displayed in the **Screen View**.
2.  Select the any of the top-level screens , such as **"Administration"** and click the three-dot-button adjacent to the selected screen, then click **"Add data screens above"** as shown below:\


    <figure><img src="../.gitbook/assets/image (115).png" alt=""><figcaption><p>Adding Data Entry Screens above Administration screen</p></figcaption></figure>


3.  In the **"Add data entry screens"** modal, use the **Entity** dropdown to choose the **"Post"** entity. This selection informs the Toolkit of the specific entity it should use to generate your screens.\


    <div align="left"><figure><img src="../.gitbook/assets/image (136).png" alt="" width="375"><figcaption><p>Select an entity for your Data Entry Screens<br></p></figcaption></figure> <figure><img src="../.gitbook/assets/image (116).png" alt="" width="275"><figcaption><p>Desired layout after adding Data Entry Screens</p></figcaption></figure></div>


4. With the data screens generated, we will proceed on to customising and configuring each screen to align with the **"My Articles"** concept. This involves setting titles, adjusting properties, and ensuring that the layout and functionality meet your requirements for content management:

#### My Articles > Post  screen

1.  Select the **Post** screen in the **Screen View**, then update the **Title** of the screen in the Properties Editor from "**Post"** to "**My Articles"** as shown in the screenshot below:\


    <figure><img src="../.gitbook/assets/image (134).png" alt=""><figcaption></figcaption></figure>
2. In the Properties Editor set the value of the field Icon to `cog` .
3. Click the **Save** button to persist your changes.
4.  Click and select the **List** screen control in the Screen Structure to activate its Properties Editor, and set the properties outline in the table below:\


    <table><thead><tr><th width="125">Property</th><th width="289">Value</th><th>Description</th></tr></thead><tbody><tr><td>Data Path</td><td>/UserProfile(guid'{{=userguid}}')/Posts</td><td>This property defines the specific endpoint or route for accessing posts associated with a user's profile in the application. The dynamic portion, <code>guid'{{=userguid}}'</code>, is a placeholder that gets replaced with the actual globally unique identifier (GUID) of the user at runtime. This ensures that the data fetched or submitted via this path is precisely linked to the correct user profile, facilitating targeted retrieval or update of posts under a specific user's account. It's essential for operations like displaying a user's articles or submitting new ones under their profile.</td></tr><tr><td>Item Title</td><td>{{= Title}}</td><td><p>The <code>Item Title</code> property specifies the template for dynamically displaying the title of each item, such as a post or article, retrieved from the data source. By using the placeholder <code>{{= Title}}</code>, the system automatically inserts the title of each respective post into the layout or list where this template is applied. This dynamic binding ensures that the displayed title matches exactly what is stored for each post in the database, providing a direct and accurate reflection of the content to the user.</p><p></p></td></tr><tr><td>Item Detail</td><td>{{ = Summary}}</td><td>This property sets the template for presenting a brief description or summary of each item, like an article or blog post. The placeholder <code>{{= Summary}}</code> is used to dynamically insert the summary content of each post into the display interface. This approach allows for a concise overview of each post's content to be presented alongside its title, offering users a snapshot of what the post is about before deciding to read further. It enhances the usability of lists or feeds by giving context to each listed item, making it easier for users to navigate through content.</td></tr></tbody></table>


5. Click the **Save** button to persist your changes.

#### My Articles > Add Post Record  screen

1. **Add Post Record** screen
   1.  Click on the "Add Post Record" screen  in the Screen View to activate its supported  Properties Editor, then set the properties outlines in the table below:\


       <table><thead><tr><th width="100">Property</th><th width="276">Value</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Add Article</td><td>This property defines the heading or title of the screen in the application.</td></tr><tr><td>Target URL</td><td>/UserProfile(guid'{{=userguid}}')/Posts</td><td><p>The <code>Target URL</code> property specifies the endpoint or API route the application will call to perform a specific operation, in this context, to submit or associate new posts with a user's profile. The dynamic part of the URL, <code>guid'{{=userguid}}'</code>, is replaced at runtime with the actual GUID (Globally Unique Identifier) of the user, ensuring that the new posts are correctly linked to the user's profile. This URL pattern facilitates direct access to a subset of data related to the user, specifically their posts, enabling a seamless data submission process.</p><p></p></td></tr></tbody></table>


   2.  Click and select the **Auto Inputs** screen control in the screen screen structure to activate its Properties Editor, and set the properties outline in the table below:\


       <table><thead><tr><th width="275">Property</th><th width="211">Value</th><th>Description</th></tr></thead><tbody><tr><td>Exclude</td><td>Tags,User,Comments</td><td>Comma delimited list of Post entity navigations to exclude from Auto Input control</td></tr></tbody></table>


   3. Click the **Save** button to persist your changes.

#### My Articles > PostEditPage  screen

1. Select the "PostEditPage" screen in the Screen View, then update the Title of the screen in the Properties Editor from **Edit** **Record** to **Edit Article** as we did in the previous step.
2.  Edit the Target URL field from /Post to:\


    ```
    /UserProfile(guid'{{=userguid}}')/Posts({{= postId }})
    ```

    \
    This request is intended to perform a partial update on a specific post within the collection of posts associated with a particular user profile, identified by a GUID.
3. Click **Save** to persist your changes.
4.  Click and select the **Auto Inputs** screen control in the screen screen structure to activate its Properties Editor, and set the properties outline in the table below:\


    <table><thead><tr><th width="275">Property</th><th width="198">Value</th><th>Description</th></tr></thead><tbody><tr><td>Exclude</td><td>Tags,User,Comments</td><td>Comma delimited list of Post entity navigations to exclude from Auto Input control</td></tr></tbody></table>


5. Click **Save** to persist your changes.
6.  Click the "**Edit Article"** screen to activate its supported Properties Editor and carefully observe the **"Name"** property within the Properties Editor. In the example provided below, the name of the screen is identified as **"1PostEditPage"**.\


    <figure><img src="../.gitbook/assets/image (381).png" alt=""><figcaption></figcaption></figure>
7.  Proceed to your **"My Articles"** section and select the **"List"** option to continue. Within the Properties Editor for the **"List"** screen, locate the section for setting the **Target URL**. Update the Target URL field with the following link:



    ```
    LINK:1PostEditPage?postId={{= PostId }}
    ```

    \
    The Target URL you've set, `1PostEditPage?postId={{= PostId }}`, plays a crucial role in linking users from one part of your application to a specific editing page for articles, utilising a dynamic parameter to provide a customised experience.



    <figure><img src="../.gitbook/assets/image (382).png" alt=""><figcaption></figcaption></figure>
8. To view your changes, **either launch your app or, if it's already open, reload the page twice.**

### **All Articles screen**

This screen will allow users to view all published blog articles.

To create the **All Articles** screen, follow these steps:

1.  Select the any of the top-level screens , such as **"My Articles"** and click the three-dot-button adjacent to the selected screen, then click **"Add screen above"** as shown below:\


    <figure><img src="../.gitbook/assets/image (345).png" alt=""><figcaption></figcaption></figure>
2.  When the **Add a new** screen window appears, set **Navigation page** as the **Screen type** and set the **Title** to **"All Articles"** as shown in the screenshot below:\
    \


    <figure><img src="../.gitbook/assets/image (346).png" alt="" width="375"><figcaption></figcaption></figure>
3. Drag and drop the **"List"** form control from the **Screen Controls** onto the **All Articles'** screen.
4.  Position the **List** control in the Screen Structure, refer to the provided image for the desired layout.\


    <figure><img src="../.gitbook/assets/image (347).png" alt=""><figcaption></figcaption></figure>
5. Configure the **List** control
   1.  **Select the List Control:** Click on the List control to activate its Properties Editor.\


       <figure><img src="../.gitbook/assets/image (351).png" alt=""><figcaption><p>Active List Control in the AllArticles screen's structure</p></figcaption></figure>
   2.  **Set the properties:** The table below shows the properties  and values you need to set for the active List. Click More Settings to view settings which are hidden by default\


       | Property    | Value                                                                | Description                                                                                                                                                                                                                                                    |
       | ----------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | Icon        | cogs                                                                 | This property specifies an icon to be used in conjunction with the screen or page title, enhancing the visual appeal and providing a visual cue about the action or content associated with the title.                                                         |
       | Data Path   | /Post                                                                | Defines the endpoint URL (`/Post`) for retrieving data from the backend. This path is used to construct the full oData query URL for fetching data, specifically targeting the "Post" resource in the database.                                                |
       | Query       | Publish eq true and Deleted eq null                                  | This property sets a filter condition for the oData query, instructing the system to retrieve only those records where the `Publish` attribute is `true`. This ensures that only published items are fetched from the database.                                |
       | Item Title  | \{{= Title \}}                                                       | Specifies the template for displaying each list item's title, dynamically inserting the `Title` property of the data item. This allows for a flexible display of titles based on the data retrieved.                                                           |
       | Item Detail | <p>{{= Summary }}<br>Author: {{= User/Name }} {{= User/Surname}}</p> | Sets the template for displaying detailed information about each list item. It combines static text with dynamic data fields, showing the item's `Summary` followed by the author's full name, which is constructed from related user data (Name and Surname). |
       | Target URL  | LINK:AllArticlesList\_PageItem?postId=\{{= PostId \}}                | Defines a template for constructing URLs to link to detailed article views. This property dynamically inserts the `PostId` of the current item into the query parameter of the URL, facilitating navigation to a detailed view page for each article.          |
       | Item Aside  | \{{= Created \}}                                                     | This property defines what is displayed in the aside section of each list item, in this case, the creation date of the article. The template dynamically inserts the `Created` date, formatting it day-month format without the year.                          |


6. To view your changes, **either launch your app or, if it's already open, reload the page twice.**

In the next step, we'll guide you through creating the **"AllArticlesViewPage"** mentioned in the Target URL.



<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

### View Article screen

To create the **View Article** screen, follow these steps:

1. Select the **All Articles** screen created in the previous step.
2.  Select the Screen Structure and then click on the **List** we implemented in the "**All Articles"** to activate its supported Screen Controls.\


    <figure><img src="../.gitbook/assets/image (355).png" alt=""><figcaption></figcaption></figure>
3.  Drag and drop the **"Form"** screen control from the **Screen Controls** onto the activated **List,** the desired output is such that the **Form** control is then nested as **Item 1** in the **All Articles** screen is shown below:\


    <figure><img src="../.gitbook/assets/image (353).png" alt=""><figcaption></figcaption></figure>
4. **Select the Item 1:** Click on the **Item 1** in the Screen View to activate its Screen Structure, Screen Controls and Properties Editor.
5.  Set the properties outlined in the table below, the desired configuration is also shown below:\


    <figure><img src="../.gitbook/assets/image (356).png" alt=""><figcaption><p>Settings for View Articles screen</p></figcaption></figure>



    <table><thead><tr><th width="100">Property</th><th width="276">Value</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>View Article</td><td>This property specifies the title of the screen or page within the application. Setting this value to "View Article" indicates that the screen is dedicated to displaying an article's content, providing users with a clear understanding of the page's purpose. The title is typically displayed at the top of the screen or in the browser tab, serving as a visual indicator of the current view.</td></tr><tr><td>Target URL</td><td>/Post({{= postId }})</td><td>This property defines the specific endpoint or URL to which a user will be directed or from which data will be retrieved. The value <code>/Post({{= postId }})</code> utilises a dynamic parameter <code>postId</code> that is replaced with the actual ID of a post when generating the URL. This enables the application to fetch or display information specific to a particular post. The use of <code>{{= postId }}</code> within the URL structure indicates that this is a templated part of the URL, which will be substituted with a real post ID at runtime, allowing for dynamic navigation or data retrieval based on the user's interaction or selection.</td></tr></tbody></table>
6. Click the **Save** button to persist your changes.
7. Click on the **"View Article"** screen to re-select it. This action will activate the **"Screen Structure"** section for further modifications.
8. Build its Screen Structure Step-by-Step:
   1. Drag and drop three **Paragraph** screen controls into the View Article Screen
   2.  Using Templated Markdown populate each Paragraph screen control **Title**, **Summary** and **Body**.\


       <table><thead><tr><th width="137">Screen Control</th><th width="564">Value</th></tr></thead><tbody><tr><td>Paragraph</td><td> <code>## Title: {{= Title}}</code></td></tr><tr><td>Paragraph</td><td> <code>__Summary: {{= Summary}}__</code></td></tr><tr><td>Paragraph</td><td><code>{{= Body}}</code></td></tr></tbody></table>

       \

   3. To add an optional **"divider.png"** image, drag and drop the **Image** screen control into the screen a. Click the Image control to activate it in the Properties Editor then upload this image[ here](building-and-extending-applications-with-the-comunity-developer-toolkit.md#assets) in the **Image Digest** field.
   4. Note: Add each item individually. This ensures correct placement and order.
   5.  Click **"Save"** after adding each item. This saves your progress and avoids losing changes.\
       \


       <figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption><p>Adding relevant screen controls <br></p></figcaption></figure>

       <figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption><p>Upload image<br></p></figcaption></figure>
9. To view your changes, **either launch your app or, if it's already open, reload the page twice.**

In the next step, we'll guide you through adding functionality to add and view comments.

### **Add Comment screen**

To create the **Add Comment** screen, follow these steps:

1.  Under Additional Screens, select 'User Profiles' and click the three-dot-button adjacent to the selected screen, then click Add screen as shown below:\


    <figure><img src="../.gitbook/assets/image (359).png" alt=""><figcaption></figcaption></figure>
2.  When the Add new window appears, choose Form Page as the page type and set the Title to Add Comment:\


    <figure><img src="../.gitbook/assets/image (362).png" alt="" width="375"><figcaption></figcaption></figure>
3. Select the Add Comments screen created in the previous step, to activate its Screen Structure.
4.  Drag and drop the "Input" and "Button" screen control from the **Screen Controls** onto the Screen Structure:\


    <figure><img src="../.gitbook/assets/image (363).png" alt=""><figcaption></figcaption></figure>
5.  Click on the "Input" control to activate its Properties Editor, then set the properties outlined in the table below:\


    <table><thead><tr><th width="204">Property</th><th width="313">Value</th><th>Description</th></tr></thead><tbody><tr><td>Property Name</td><td>Detail</td><td>Specifies the input label</td></tr></tbody></table>

    \

6.  Click on the "Button" control to activate its Properties Editor, then set the properties outlined in the table below:\


    <table><thead><tr><th width="204">Property</th><th width="313">Value</th><th>Description</th></tr></thead><tbody><tr><td>Button Text</td><td>Add</td><td>Specifies the button label</td></tr><tr><td>Verb Name</td><td>Post</td><td><p>Specifies the HTTP method used for the form action. In this case, "Post" indicates that the form will submit data to the server to create a comment.</p><p></p></td></tr><tr><td>Document Template</td><td><p>{"Detail":"{{= Detail }}", "User@odata.bind":"UserProfile(guid'{{=userguid}}')"}</p><p></p></td><td>Specifies the structure of the data payload for the POST action, including dynamic values to be included in an OData query. The <code>Detail</code> key is populated with the specific detail information, and the <code>User@odata.bind</code> key binds the document to the user profile using the user's GUID.</td></tr><tr><td><p></p><p></p></td><td></td><td></td></tr></tbody></table>

    \

7. To implement functionality to add a comment to a page, click the View Article Page in the Screen View to activate its Screen Structure and Properties Editor.
8. Drag and drop the "List" screen control from the **Screen Controls** and place it below the divider.
9. Click on the List control to activate its supported Screen Controls.
10. Drag and drop the "Single Item"  and the "Entity Items" screen control from the **Screen Controls** onto the activated **List,** the desired output is shown below:\


    <figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>
11. Click on the "Single Item" control to activate its supported  Properties Editor, then set the properties outlines in the table below:\


    <table><thead><tr><th width="93">Property</th><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Add Comment</td><td><p>This property sets the title or heading of the interface screen where users can add a new comment. By naming the screen "Add Comment," it clearly informs users that they are in the section of the application dedicated to submitting their feedback or thoughts on a particular topic or post. This title helps enhance user navigation and usability by providing a clear context for the action they are about to perform.</p><p><br></p></td></tr><tr><td>Icon</td><td>svg/sdk/plus-circle/Bootstrap/regular</td><td>This property specifies an icon to be used in conjunction with the screen or page title, enhancing the visual appeal and providing a visual cue about the action or content associated with the title. The value <code>svg/sdk/plus-circle/Bootstrap/regular</code> points to a specific icon within a structured library or SDK, indicating the use of a "plus-circle" icon from the Bootstrap icon set in its regular style. This icon, often symbolizing the addition of new items or content, is prefixed to the title, offering an intuitive understanding that the user is about to engage in a creation or addition process, such as adding a new comment, post, or item within the application. The use of this icon helps to visually distinguish the action or page, making the user interface more user-friendly and accessible.</td></tr><tr><td>Data Path</td><td>/Comments</td><td>The <code>Data Path</code> property specifies the endpoint or API route used by the application to send or retrieve comments data. The value <code>/Comments</code> indicates that this particular path is dedicated to handling operations related to comments, such as posting new comments or fetching existing ones. It serves as a direct link to the comments resource on the server, ensuring that data can be accurately accessed or submitted by the application.</td></tr><tr><td>Page</td><td>./AddComment</td><td>This property defines the relative path to the page within the application where users can add a new comment. The value <code>./AddComment</code> points to a specific screen or component designed for comment submission, indicating that this page contains the necessary interface elements (such as text input fields and submit buttons) for users to write and post their comments. The "./" prefix suggests that the path is relative, implying that the location of the <code>AddComment</code> page is within the same directory level as the reference point in the application's file structure.</td></tr></tbody></table>
12. Click on the "Entity Items" control to activate its supported  Properties Editor, then set the properties outlines in the table below:\


    <table><thead><tr><th width="212">Property</th><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>EntitySet/Navigation</td><td>/Comments</td><td><p>This property indicates the specific EntitySet or navigation path used within the application's data model, particularly in the context of OData services or similar API structures. The value <code>/Comments</code> designates the targeted dataset or resource for operations, in this case, comments. It functions as a reference to the collection of comment entities, enabling the application to perform actions such as querying, adding, updating, or deleting comment records. By specifying <code>/Comments</code>, the property clearly defines the path for accessing or interacting with comment data stored in the backend. This allows for efficient data manipulation and retrieval, ensuring that the application can dynamically handle user interactions related to comments, such as displaying a list of comments or submitting new ones.</p><p><br></p></td></tr></tbody></table>
13. To view your changes, **either launch your app or, if it's already open, reload the page twice.**

### **Articles By Tag screen**

To create the **Articles By Tag** screen, follow these steps:

1.  Select the any of the top-level screens , such as 'My Articles'. and click the three-dot-button adjacent to the selected screen, then click Add screen as shown below:\


    <figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>
2.  When the **Add a new** screen window appears, choose **Navigation page** as the page type and set the Title to **Articles By Tag** as shown in the screenshot below:\


    <figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>
3.  Click and select the **Articles By Tag** screen  in the screen view to activate its Screen Structure:\


    <figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>
4. In the Properties Editor set the value of Icon to `ticket` .
5. Drag and drop the "List" form control from the **Screen Controls** onto the **Articles By Tag** screen structure and set its layout type to "Grid".
6.  Click on the List control to activate its supported Properties Editor, then set the properties outlines in the table below:\


    <table><thead><tr><th width="147">Property</th><th width="276">Value</th><th>Description</th></tr></thead><tbody><tr><td>Data Path</td><td>/Tag</td><td><p>This property designates the specific endpoint or route within the application's backend from which tag-related data can be accessed or manipulated. The value <code>/Tag</code> signifies that this path is dedicated to operations involving tags, such as retrieving all tags, adding a new tag, or editing existing tags. It serves as a direct link to the tag resource, facilitating seamless interaction with the tag data stored in the database.</p><p><br></p></td></tr><tr><td>Item Title</td><td>{{= Name}}</td><td>This property specifies the name of the Tag by default only the Tag icon is shown</td></tr><tr><td>Target URL</td><td>LINK:TaggedArticles?tagId={{= TagId }}</td><td>This property defines the URL to which a user will be directed or the application will navigate when a particular action is taken, often linked from a UI element like a button or a hyperlink. The value <code>LINK:TaggedArticles?tagId={{= TagId }}</code> constructs a dynamic URL for navigating to a page that displays articles associated with a specific tag. The <code>{{= TagId }}</code> portion is a placeholder that gets replaced with the actual ID of the tag, allowing the application to fetch and display articles tagged with that specific identifier. This dynamic linking method enables a fluid and context-sensitive navigation experience within the application, directly connecting users with the content relevant to the selected tag.</td></tr></tbody></table>

    \

7. Click the **Save** button to persist your changes
8.  Click on the List control to re-select it and activate its supported Screen Controls:\


    <figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>
9.  Drag and drop the "Navigation Page"  screen control from the **Screen Controls** onto the activated **List,** the desired output is shown below:\


    <figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption><p>Item 1 is nested under Articles By Tag screen</p></figcaption></figure>
10. In the next step we will configure **Item 1** to be the **Tagged Articles** screen.

### **Tagged Articles screen**

To configure the  **Tagged Articles** screen created in the previous step, follow these steps:

1.  Click and select the **Item 1** screen in the Screen View, to activate its supported Properties Editor and set the Title to "Tagged Articles":\


    <figure><img src="../.gitbook/assets/image (364).png" alt=""><figcaption><p>Setting the page Title of Item 1<br></p></figcaption></figure>

    <figure><img src="../.gitbook/assets/image (365).png" alt=""><figcaption><p>Item 1 title is updated to Tagged Articles</p></figcaption></figure>
2. Click the **Save** button to persist your changes
3. Click and select the Tagged Articles screen in the Screen View, to activate its Screen Structure:
4.  Drag and drop the "List" form control from the **Screen Controls** onto the **Tagged Articles** screen structure.\


    <figure><img src="../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>
5.  Click on the List control to activate its supported Properties Editor, then set the properties outlines in the table below:\


    <table><thead><tr><th width="192">Property</th><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>Data Path</td><td>/Post</td><td>This property specifies the API endpoint or route for fetching posts from the backend. The <code>/Post</code> value indicates the data path that the application uses to retrieve post-related data, serving as the primary access point for post resources within the system.</td></tr><tr><td>Query</td><td>Publish eq true and Tags/any(id:id/TagId eq {{= tagId }})</td><td><p></p><p>This query filters the posts to be fetched based on specific conditions. It ensures that only posts which are published (<code>Publish eq true</code>) and contain any tags matching a specified tag ID (<code>Tags/any(id:id/TagId eq {{= tagId }})</code>) are retrieved. The <code>{{= tagId }}</code> portion is dynamically replaced with the actual tag ID during the query execution, allowing for flexible and targeted data retrieval based on user interaction or specific criteria.</p></td></tr><tr><td>Item Title</td><td>{{= Title }}</td><td>This property defines the template for displaying each item's title in the list or collection view. The <code>{{= Title }}</code> template dynamically inserts the title of the post from the data retrieved, ensuring that each item accurately represents its corresponding post's title for easy identification by the user.</td></tr><tr><td>Item Detail</td><td>{{= Summary }}<br>Author: {{= User/Name }} {{= User/Surname}}</td><td>Specifies the template for presenting detailed information about each post item. This template combines static text with dynamic placeholders, displaying the post's summary followed by the author's name and surname. The <code>{{= Summary }}</code> inserts the post's summary, while <code>{{= User/Name }}</code> and <code>{{= User/Surname}}</code> are replaced with the author's first and last names, respectively. This detailed format provides a comprehensive overview of each post, enhancing user engagement and understanding of the content available.</td></tr></tbody></table>
6.  Drag and drop the "Form" screen control from the **Screen Controls** onto the activated **List,** this action will nest  a Form Page, **Item 1  as** shown  in the screenshot below:\


    <figure><img src="../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>
7. In the next step we will configure **Item 1** to be the **Tagged Articles View** screen.

### **Tagged Articles  View screen**

To configure the  **Tagged Articles View** screen created in the previous step, follow these steps:

1.  Click and select the **Item 1** screen in the Screen View, to activate its supported Properties Editor and set the  properties outlined in the table below:\


    <table><thead><tr><th width="141">Property</th><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Tagged Article View</td><td>This property sets the title or heading for a specific screen or page within the application, in this case, designated as "Tagged Article View." It indicates that the page is focused on displaying articles that have been tagged with a specific keyword or category. The title helps users understand the context and purpose of the page they are viewing, ensuring a cohesive user experience by clearly identifying the content theme or focus.</td></tr><tr><td>Target URL</td><td>/Post({{= postId }})</td><td><p>The <code>Target URL</code> property specifies the endpoint or resource location that the application should navigate to or fetch data from, based on a dynamic identifier. In this value, <code>/Post({{= postId }})</code>, the URL is constructed to target a specific post within the application, with <code>{{= postId }}</code> serving as a placeholder for the post's unique identifier. This dynamic approach allows for the URL to adapt based on the context in which it is used, enabling direct access to detailed views of posts by substituting the placeholder with an actual post ID. This functionality is crucial for creating a navigable and user-friendly interface where users can easily access detailed information about a specific article or post.</p><p></p></td></tr></tbody></table>
2.  Configure the screen structure for the "Tagged Articles" view to mirror the content, layout, and properties of the "All Articles View." Ensure that the final setup for the "Tagged Articles" view is identical in terms of its presentation and functionality, providing a consistent user experience across both views.

    <figure><img src="../.gitbook/assets/image (367).png" alt=""><figcaption><p>Final screen structure of Tagged Articles View</p></figcaption></figure>
3. For the next step, enhance the "Edit Article" screen by integrating the capability for authors to add Tags to their posts. This addition is crucial as, while we have developed the functionality to display articles based on Tags, we currently lack a mechanism for actually assigning those Tags to articles. This enhancement will bridge that gap, allowing for a more dynamic and organised content management process.

### Implement functionality to Add Tags in the Edit Article screen

To configure functionality and content to add Tags  in the Edit Article screen, follow these steps:

1. Click and select the **Edit Article** screen in the Screen View, to activate its Screen Structure:
2.  Drag and drop the "List" form control from the **Screen Controls** onto the **Edit Article** screen under the  existing content, the desired layout is shown below:\


    <figure><img src="../.gitbook/assets/image (118).png" alt=""><figcaption></figcaption></figure>
3. Click on the **List** control to activate its supported Screen Controls, then drag and drop "Single Item" into the List control.
4.  Click the **Single Item** from within the **List** to activate it so that its supported Properties Editor, then set the properties outlined in the the table below:\


    <table><thead><tr><th width="139">Property</th><th width="227">Value</th><th>Description</th></tr></thead><tbody><tr><td>Title</td><td>Add Tag</td><td>This property sets the heading or name of a specific interface within the application, designated as "Add Tag." It clearly communicates to users that they are interacting with a section or screen dedicated to the creation or addition of new tags. This title is essential for guiding users through the functionality of the app, ensuring they understand they are in the process of tagging items, such as articles or posts.</td></tr><tr><td>Icon</td><td>svg/sdk/plus-circle-dotted/Bootstrap/regular</td><td><p></p><p>This property specifies an icon to be used alongside the user interface, particularly to visually represent the action or feature it accompanies, in this case, adding a tag. The value <code>svg/sdk/plus-circle-dotted/Bootstrap/regular</code> indicates the file path and style for a specific icon within a standardised set or library. The icon, described as a "plus-circle-dotted" from the Bootstrap collection in its regular form, symbolises the addition of new elements or features, such as tags, enhancing the visual appeal and intuitive understanding of the function it represents.</p></td></tr><tr><td>Data Path</td><td>?postId={{= postId }}</td><td><p>The <code>Data Path</code> property defines a query parameter to be appended to a base URL, targeting a specific resource or action within the application. In this context, <code>?postId={{= postId }}</code> is used to specify that the operation or data retrieval should be related to a particular post, identified by its unique ID (<code>postId</code>). The <code>{{= postId }}</code> acts as a dynamic placeholder that is replaced with the actual ID of the post in question, allowing for tailored interactions or data fetches based on the specific post being viewed or edited.</p><p></p></td></tr><tr><td>Page</td><td>./AddTag</td><td>This property indicates the relative path to a specific page or component within the application, named "AddTag." The <code>./AddTag</code> value suggests that this page is dedicated to the functionality of adding new tags, located within the same directory or level as the reference point in the application's structure. This setup facilitates easy navigation and modular development, ensuring that users can access the tag addition features seamlessly as part of their interaction with the app.</td></tr></tbody></table>

    \

5. After adjusting the settings for the Single Item, click outside the screen structure area to deactivate your previous selection.
6.  Drag the "Paragraph" screen control into the Screen Structure. Then, using Markdown, add the text as illustrated in the screenshot provided below.\


    <figure><img src="../.gitbook/assets/image (368).png" alt=""><figcaption></figcaption></figure>
7.  Drag and drop the "List" form control from the **Screen Controls** under the content added in the previous step, the desired layout is shown below:\


    <figure><img src="../.gitbook/assets/image (369).png" alt=""><figcaption></figcaption></figure>
8. Click on the **List** control to activate its supported Screen Controls, then drag and drop "Entity Items" into the List control.
9.  Click the **Entity Items** from within the **List** to activate it so that its supported Properties Editor, then set the properties outlined in the the table below:\


    <table><thead><tr><th width="167">Property</th><th width="191">Value</th><th>Description</th></tr></thead><tbody><tr><td>Entity Set or Navigation Property</td><td>/Tags</td><td>This property specifies the path used to fetch data. In this context, the value "/Tags" indicates that the data for the entity items will be retrieved from the "Tags" endpoint in the OData service.</td></tr></tbody></table>



    <figure><img src="../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>
10. Next, proceed to develop the "Add Tags" screen, as previously mentioned in the TARGET URL section. This step involves creating the actual interface that will facilitate the tagging functionality.

### **Add Tag screen**

To create the **Add By Tag** screen, follow these steps:

1.  Under Additional Screens, select 'User Profiles' and click the three-dot-button adjacent to the selected screen, then click **Add form** as shown below:\


    <figure><img src="../.gitbook/assets/image (372).png" alt=""><figcaption></figcaption></figure>
2.  When the Add new window appears, choose Form Page as the page type and set the Title to Add Tag:\


    <figure><img src="../.gitbook/assets/image (373).png" alt=""><figcaption></figcaption></figure>
3. Click  the **Add Tag** screen created in the previous step, to activate its Screen Structure.
4.  Drag the "Paragraph" screen control into the Screen Structure. Then, using Markdown, add the text as illustrated in the screenshot provided below.\
    \


    <figure><img src="../.gitbook/assets/image (419).png" alt="" width="253"><figcaption></figcaption></figure>
5.  Drag the "Reference Input" screen control into the Screen Structure. The click it to activate its supported Propertied Editor then set the properties outlines in the table below:\


    <table><thead><tr><th width="204">Property</th><th width="313">Value</th><th>Description</th></tr></thead><tbody><tr><td>Property Name</td><td>Tags</td><td>Name assigned to the Reference Input field</td></tr><tr><td>Data Path Template</td><td>/Tag</td><td><p></p><p>The <code>Data Path Template</code> specifies the API endpoint or route for accessing tag-related data. The value <code>/Tag</code> designates the path to the resource where tags are stored or managed in the backend. This path is utilized by the application to perform operations such as retrieving, adding, or updating tags, ensuring a direct link to the tags resource for efficient data handling.</p></td></tr><tr><td>Query</td><td>Posts/all(s:s/PostId ne {{= postId }})</td><td>This query is designed to filter and retrieve data based on certain conditions related to posts. Specifically, it ensures that only posts not matching a specified post ID (<code>PostId ne {{= postId }}</code>) are fetched. The <code>{{= postId }}</code> is a dynamic placeholder that gets replaced with an actual post ID during the query execution, allowing for the exclusion of a specific post from the results. </td></tr><tr><td>List Title Template</td><td>{{= Name}}</td><td>This property defines the template for displaying the title of each item in a list, particularly when dealing with a collection of tags. The <code>{{= Name}}</code> template dynamically inserts the name of the tag from the retrieved data, ensuring that each list item accurately reflects the tag's name. This approach provides a clear and direct representation of tags in the user interface, enhancing navigation and selection within the application.</td></tr></tbody></table>



    <figure><img src="../.gitbook/assets/image (377).png" alt=""><figcaption></figcaption></figure>
6.  Drag the "Button" screen control into the Screen Structure. The click it to activate its supported Propertied Editor then set the properties outlines in the table below:\


    <table><thead><tr><th width="234">Property</th><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>Button Text</td><td>Add</td><td>This property specifies the text to be displayed on a button, guiding users on the action that will be performed upon clicking. The value "Add" indicates that the button is intended for operations that involve adding new items, entries, or data into the application. It's a clear call-to-action for users to initiate an addition process, whether it's adding a new post, tag, or any other entity within the application's context.</td></tr><tr><td>Verb Name</td><td>PATCH</td><td><p>The <code>Verb Name</code> refers to the HTTP method used for a particular operation in web development, especially in API calls. The value "PATCH" specifies that the operation involves partially updating an existing resource. Unlike PUT, which replaces the entire resource, PATCH is used to make changes to specific fields of a resource without altering the entire data set. This method is commonly used for updating records or settings in an application, allowing for more efficient and targeted data modifications.</p><p></p></td></tr><tr><td>Document Template</td><td>{"url":"http://localhost:82/blogapp/ds.svc/Tag({{= Tags/TagId }})"}</td><td>Replace <code>blog-app</code> in the  url  with your application name refer to <a href="../getting-started/manage-your-project/general.md">General</a> for more information on how to access your application name</td></tr></tbody></table>

    \


    <figure><img src="../.gitbook/assets/image (378).png" alt=""><figcaption></figcaption></figure>

## Manage Tags

The responsibility of adding article tags to the application is assigned to the Staff user role. Follow the instructions below to implement this feature:

1. **Access the Administration Screen**:
   * Navigate to the Administration screen.
   *   Locate and select the **Content Management** section within the screen structure.\
       \


       <figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>
2. **Select the List Screen Control**:
   * Under the Content Management section, click the **List screen control** to select it
3. **Add Navigation Page Item Controls**:
   * Drag and drop a **Navigation Page Item** controls into the active list. This action will nest these pages within the Administration page.
4. **Configure the Navigation Page Item**:
   * Select there Navigation Page control from the list by clicking it to activate the Properties Editor.
   *   Populate the necessary fields as outlined below:

       <table><thead><tr><th width="234">Screen Control</th><th>Property</th><th>Value</th></tr></thead><tbody><tr><td>Navigation Page Item </td><td>Title</td><td>Article Tags</td></tr><tr><td></td><td>Icon</td><td>tags</td></tr></tbody></table>
5. Click the **Save** button to persist your changes.
6.  Expand the Administration screen and select the Article Tags screen to activate its relevant Screen Structure and Controls.

    <figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>
7. Drag and drop the Page Link screen control into the Article Tags screen structure&#x20;
8.  Click on the Page Link control then configure its properties outlined in the table below\


    | Property   | Value                                                                                |
    | ---------- | ------------------------------------------------------------------------------------ |
    | Title      | Add Tag                                                                              |
    | Icon       | nn\_more                                                                             |
    | Role Name  | Staff                                                                                |
    | Target URL | /Tag                                                                                 |
    | Page Name  | AdminList2\_ListItem - this page is autogenerated by the system its name might vary. |
    |            |                                                                                      |
9. Click the **Save** button to persist your changes.
10. Drag and drop a **Paragraph** screen control into the Add Tags screen
11. Using Templated Markdown populate the Paragraph with the content:  `##Tags List`
12. Drag and Drop a List into the screen and configure its following properties:\


    | Property   | Value |
    | ---------- | ----- |
    | Target URL | /Tag  |
    |            |       |
13. Click the **Save** button to persist your changes.
14. Expand the Article Tags screen to view the Add Tag screen added in step 8.
15. Click  the Add Tag screen in the Screen View  to activate its Screen controls
16. Drag and Drop two Input controls and Button onto the into the screen and configure their corresponding screen control  properties as specified in the table below:\


    | Screen Control | Property      | Value |
    | -------------- | ------------- | ----- |
    | Input          | Property Name | Name  |
    | Input          | Property Name | Icon  |
    | Button         | Button Text   | Add   |
    |                | Verb Name     | POST  |
17. Click the **Save** button to persist your changes.

Launch your app to publish your changes you will be automatically redirected to a web application, if you have not yet registered in the app proceed to do so. Add a Staff role to your account so as to be able to manage Tags view [Users and Roles](../getting-started/manage-your-project/users-and-roles.md) for information about managing role based user access.

## Conclusion

In conclusion, this tutorial has guided you through the essential steps and techniques to effectively enhance your application. From configuring screen structures to integrating dynamic content management features such as tagging, we've covered a broad spectrum of functionalities that are crucial for a modern, user-friendly application.
