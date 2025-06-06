# Manage Entities in the Data Model: Step-by-Step Guide

Entities are the **building blocks of your data model**, representing the objects or concepts that you want to structure and manipulate in your application. This guide provides a step-by-step approach to creating, configuring, and managing entities within your project, ensuring data integrity and efficient data handling.

In the **ComUnity Developer Toolkit**, you can create entities within your data model in two ways:

* **Entities** – Define entities from scratch to model your application’s specific data structures. This also includes the option to create entities **from an existing SQL table**, allowing you to incorporate structured data directly into your model.
* **Virtual Entities** – Define entities that enable your data model to interact with **third-party APIs**, allowing queries to these services within the Toolkit as part of the data model.

This guide covers:

* &#x20;Creating and managing custom Entities
* Using **Virtual Entities** to integrate third-party services
* &#x20;Configuring **WebApiConfig** to expose **Virtual Entities** via  [OData](../../reference-articles/odata.md)&#x20;
* Copying, modifying, and deleting entities efficiently

By following this guide, you will be able to define, configure, and manage both internal and external data models while maintaining a structured approach to data querying, integration, and API management.

{% hint style="success" %}
📖 Learn More: [**OData**](../../reference-articles/odata.md) **in the ComUnity Developer Toolkit**

The ComUnity Developer Toolkit follows the OData specification to enable structured data querying across the platform. Once an entity is created, it is automatically exposed via OData, allowing Pages to query and interact with entity data efficiently.

For further details on how  [OData](../../reference-articles/odata.md)  is utilised within the Toolkit, refer to  [Reference Articles/OData](../../reference-articles/odata.md).
{% endhint %}

## Entities

Entities define the **core data structures** in the **ComUnity Developer Toolkit**. They allow you to model data within your application by creating structured representations of objects or concepts.

This section covers the process of **creating entities**, including defining them from scratch and using the option to create entities from an **existing SQL table**.

### Creating custom Entities

To create a custom entity, follow these steps:

1. In your project settings in the Toolkit navigate to Data then select Diagram or List to view your Data Model.
2.  Locate the ![](../../.gitbook/assets/ComUnity-Icon-v4-AddEntity-16px.png) icon on the Diagram or List (shown below) view. This icon allows you to add a new entity to your data model.\


    <figure><img src="../../.gitbook/assets/image (453).png" alt=""><figcaption><p>Diagram view of the Data model<br></p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (455).png" alt=""><figcaption><p>List view of the Data model<br></p></figcaption></figure>
3.  Click ![](../../.gitbook/assets/ComUnity-Icon-v4-AddEntity-16px.png) icon, and an **Add a new entity** modal window will appear on your screen.\


    <div align="left"><figure><img src="../../.gitbook/assets/image (456).png" alt="" width="375"><figcaption><p>Add new entity modal</p></figcaption></figure></div>


4. In the **Entity Name** box, provide a descriptive name for your entity. Choose a name that represents the object or concept it represents in your application. Note that a valid entity name is unique and cannot contain special characters or spaces.
5. Finally, click on the **Add an entity** button to create your custom entity.

### Adding Entity Fields and Configuring Field Settings

When you create a new entity in the ComUnity Developer Toolkit, it automatically inherits from a **BaseEntity**, which provides several default fields (attributes). These attributes include:

1. `Created`: Represents the timestamp when the entity was initially created. This property is set to the exact date and time when the entity was added to the system and is immutable.
2. `Modified`: Indicates the timestamp when the entity was last modified. This property is updated every time the entity undergoes any changes, reflecting the most recent date and time of modification. Like the `Created` property, the `Modified` property is also immutable.
3. `Deleted`: Marks the entity as deleted, typically by setting a flag or status to indicate its removal from the system. Similar to the previous properties, the `Deleted` property is immutable.
4. `<EntityName>Id:` An integer (int) type property that serves as the unique identifier for all records created from the entity.

The method of viewing entities fields depends on whether they are represented in an entity diagram or as a list:

1. **Diagram**: For entities presented in an entity diagram, the entity fields are visually represented within the diagram itself. Each entity will have its attributes displayed directly in the diagram, providing a comprehensive overview of its structure and relationships.
2. **List**: If the entities are presented as a list, you can expand and view their attributes by clicking the (+) icon that precedes the entity name. This will expand the entity and display its attributes in a detailed view. Conversely, to hide the properties, you can click the (-) icon.

To add properties an entity, follow these steps:

{% hint style="info" %}
According to Microsoft’s .NET naming guidelines, public members such as properties should use Pascal casing, where each word begins with an uppercase letter. As a result, all properties in the data model have to be capitalised to ensure compatibility with C# standards and to avoid conflicts or unexpected behaviour at runtime.

For more details, see [Microsoft’s .NET Naming Guidelines](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).
{% endhint %}

1. Right-click on an existing property in the entity structure.
2. In the context menu, choose one of the following:
   1. "Add a property above” – Inserts a new property above the selected one.
   2. “Add a property below” – Inserts a new property below the selected one.
3. The Add Property modal appears.
4. In the **Name** field, provide a descriptive name for your field. Note that a valid field name  is unique and cannot contain special characters or spaces.
5. Click “**Add property**” to insert the new property in the specified position.
6.  Select the newly added property to activate it. Configure its settings in the Properties Editor, including:\


    <table><thead><tr><th width="128.62778578362656">  Property  name</th><th width="235.6155899626268">Function</th><th>Value selection</th></tr></thead><tbody><tr><td><strong>Property Type</strong></td><td>Select the type of data to be stored in this field. See <a href="../../reference-articles/data-types.md">Datatypes</a>.</td><td>Select one from the list of 14 options.</td></tr><tr><td><strong>Entity Key</strong></td><td>Sets the primary key.</td><td>Select the checkbox if the field is the primary key.</td></tr><tr><td><strong>Maximum Length</strong></td><td>Defines the maximum number of characters this field can accommodate.</td><td>Enter the maximum number.</td></tr><tr><td><strong>Column Name</strong></td><td>Defines the name for this field.</td><td>Enter a name for this field as it will appear in the database.</td></tr><tr><td><strong>Column Order</strong></td><td>To use composite keys the Entity Framework (EF) requires you to define an order for the key properties. <br>You can do this by using the Column annotation to specify an order. <br>If you have entities with composite foreign keys, then you must specify the same column ordering that you used for the corresponding primary key properties.<br><em>For more information: Go to Entity framework annotations URL</em> <br><a href="https://docs.microsoft.com/en-us/ef/ef6/modeling/code-first/data-annotations"><em>https://docs.microsoft.com/en-us/ef/ef6/modeling/code-first/data-annotation</em>s</a></td><td>The order value is relative (rather than index-based) so any values can be used. For example, 100 and 200 would be acceptable in place of 1 and 2.</td></tr><tr><td><strong>Database Generated</strong></td><td>An important database features is the ability to have computed properties. <br>If you're mapping your Code First classes to tables that contain computed columns, you don't want Entity Framework to try to update those columns. <br>But you do want the EF to return those values from the database after you've inserted or updated data. <br><em>For more information: Go to Entity framework DatabaseGenerated URL</em><br><a href="https://docs.microsoft.com/en-us/ef/ef6/modeling/code-first/data-annotations#databasegenerated"><em>https://docs.microsoft.com/en-us/ef/ef6/modeling/code-first/data-annotations#databasegenerated</em></a></td><td>Select one of:<br><em>Computed, Identity, None.</em></td></tr><tr><td><strong>Minimum Length</strong></td><td>Enter a minimum number of characters this field can accommodate</td><td>Enter the minimum number.</td></tr><tr><td><strong>Indexed</strong></td><td>You can create an index on one or more columns using the IndexAttribute. Adding the attribute to one or more properties will cause EF to create the corresponding index in the database when it creates the database..</td><td>Select the checkbox to activate the creation of an Index.</td></tr><tr><td><strong>Field Type</strong></td><td>Select the behaviour type for this field. See <a href="../../reference-articles/field-types.md">Field Types</a>. </td><td>Select the required field type from the dropdown list.</td></tr><tr><td><strong>Title</strong></td><td>You can enter a Title name to define a custom label for the field when it is added to a form in the UI.</td><td></td></tr><tr><td><strong>Default Value</strong></td><td>Enter a default value for this field when a new record is created.</td><td></td></tr></tbody></table>


7. Click **Save** to apply the changes.

Once added, the property will be available in the entity structure and can be referenced in queries or used in data models.

### Creating Entities from Existing SQL Tables

Integrate your existing data seamlessly into your data model using the ComUnity Developer Toolkit. By automatically generating entity fields from your existing tables, you save time and effort. Simply migrate your database to the ComUnity platform with the assistance of the ComUnity Team, and during entity creation, these existing tables will be readily available in your Data model. Simplify the process and ensure data consistency by leveraging this automation feature.

To create an entity from existing SQL Tables, follow these steps:

1. Follow the steps outlined in [Create a Custom Entity](creating-entities-in-the-data-model-step-by-step-guide.md#create-custom-entities) to access the **Add a new entity modal** window.
2.  In the modal window, under **Create from existing SQL Tables**, you will find a greyed-out select field.



    <div align="left"><figure><img src="../../.gitbook/assets/image (457).png" alt="" width="375"><figcaption><p>Create from existing SQL table option<br></p></figcaption></figure></div>
3. Click on **Create from existing SQL Table** to activate the select field.
4. Choose an option from the select field that corresponds to the existing SQL table you want to create an entity from.
5. In the **Entity Name** box, provide a descriptive name for your entity. Choose a name that represents the object or concept it represents in your application. Note that a valid entity name is unique and cannot contain special characters or spaces.
6. Finally, click **Add an Entity** to create the entity based on the selected SQL table.

By following these steps, you can effortlessly incorporate your existing SQL tables into your data model, leveraging the power of the ComUnity Developer Toolkit.

### Entity Properties

To view the entity properties in a Diagram view, simply click on the entity's header section with a grey background colour. An active entity can be identified by its blue border, and none of its entity fields will be active (active entity fields have a blue background colour). This action will open a properties dialog that displays the global properties specific to the entity.

Conversely, if you are in a List view, clicking on an entity will activate it, and an active entity will have a distinctive blue background colour. Clicking on the entity in this view will also open the properties dialog, allowing you to explore and modify the entity's global settings.

For a detailed description and explanation of each entity property, please refer to the table below.

<table><thead><tr><th width="171.33333333333331">Property Name</th><th>Description</th></tr></thead><tbody><tr><td>Inherits from Entity</td><td>View <a href="managing-inheritance-in-the-data-model-configuring-entity-hierarchy-and-inheritance.md">Managing Inheritance in the Data Model: Configuring Entity Hierarchy and Inheritance</a></td></tr><tr><td>Entity Set Name</td><td>The name of the EntitySet in <a href="../../reference-articles/odata.md">OData</a> URLs. By default the Entity Set and SQL table name are the same.</td></tr><tr><td>Edit Table Security</td><td>View <a href="setting-up-role-based-permissions-for-entities-access-control-configuration.md">Setting Up Role-Bases Permissions for Entities: Access Control Configuration</a></td></tr><tr><td>Custom Property Definitions</td><td><mark style="color:orange;"><strong>Unsupported in V4</strong></mark></td></tr><tr><td>Table Name</td><td>SQL table name</td></tr><tr><td>Temporal (History) Table</td><td>Choose whether to add or remove support for storing change history</td></tr><tr><td>Reset Custom Code</td><td>Check to replace custom code with default template</td></tr><tr><td>Custom Code</td><td>Logic that executes when intercepting change operations</td></tr><tr><td>List Title Template</td><td>Default template used for rendering titles of lists containing items of the entity set</td></tr><tr><td>List Detail Template</td><td>Default template used for rendering detail line of lists containing items of the entity set.</td></tr><tr><td>Sort Order</td><td>Default sort order when fetching entity set</td></tr><tr><td>Data Service Url</td><td>Override the default <a href="../../reference-articles/odata.md">OData</a> URL for the EntitySet endpoint with a custom Web API URL handling reading, inserting, updating and deleting records.</td></tr><tr><td>Max Age</td><td>The valid life time for data used in automatically refreshing lists.</td></tr></tbody></table>

### Copy Entities

In the ComUnity Developer Toolkit, we understand the importance of efficiency and productivity when it comes to creating entities in your data model. To help streamline the entity creation process, we provide a handy feature called **Copy Entities**. This function allows you to quickly duplicate existing entities, saving you time and effort by leveraging pre-existing configurations.

The Copy Entities function is designed to simplify the task of creating similar entities or replicating entities with similar properties, fields, or settings. Instead of starting from scratch and manually recreating each entity, you can utilise the Copy Entities function to duplicate an existing entity as a starting point. This not only accelerates the entity creation process but also ensures consistency and reduces the chance of errors or omissions.

To utilise the **Copy Entities** function in the ComUnity Developer Toolkit, follow these steps:

1. Right-click on the entity you want to copy. This action will open a context menu.
2. In the context menu, select "Copy this entity." This will trigger the opening of a modal titled **Copy Entity**.
3. In the **Copy Entity** modal, specify the name for the new entity by entering it in the **New entity name** box. Choose a unique and descriptive name for the copied entity.
4. Finally, click the **OK** button to initiate the copying process. The selected entity will be duplicated, and the newly created entity will be added to your data model.

By following these steps, you can efficiently create copies of entities within the ComUnity Developer Toolkit. This functionality allows you to speed up the entity creation process and streamline your data model management.

In the ComUnity Developer Toolkit, we understand the importance of efficiency and productivity when it comes to creating entities in your data model. To help streamline the entity creation process, we provide a handy feature called **Copy Entities**. This function allows you to quickly duplicate existing entities, saving you time and effort by leveraging pre-existing configurations.

The Copy Entities function is designed to simplify the task of creating similar entities or replicating entities with similar properties, fields, or settings. Instead of starting from scratch and manually recreating each entity, you can utilise the Copy Entities function to duplicate an existing entity as a starting point. This not only accelerates the entity creation process but also ensures consistency and reduces the chance of errors or omissions.

To utilise the **Copy Entities** function in the ComUnity Developer Toolkit, follow these steps:

1. Right-click on the entity you want to copy. This action will open a context menu.
2. In the context menu, select "Copy this entity." This will trigger the opening of a modal titled **Copy Entity**.
3. In the **Copy Entity** modal, specify the name for the new entity by entering it in the **New entity name** box. Choose a unique and descriptive name for the copied entity.
4. Finally, click the **OK** button to initiate the copying process. The selected entity will be duplicated, and the newly created entity will be added to your data model.

By following these steps, you can efficiently create copies of entities within the ComUnity Developer Toolkit. This functionality allows you to speed up the entity creation process and streamline your data model management.

### Delete an entity

To delete an entity, follow these steps:

1. Select the entity you want to delete by clicking on its header section with a grey background colour. An active entity can be identified by its blue border, and none of its entity fields will be active (active entity fields have a blue background colour). This action will open a properties dialog that displays the global properties specific to the entity.
2. Alternatively, if you are in a List view, simply click on the entity you wish to delete. An active entity will be distinguished by a distinctive blue background colour.
3. Once the entity is selected, you will notice a trash can icon located in the header section. Clicking on this icon will trigger a modal window titled **Delete an Entity**.
4. Finally, click the "Delete Entity" button to permanently remove the selected entity from your data model.

{% hint style="danger" %}
It's important to note that deleting an entity will also remove all associated fields and any data stored within them. Exercise caution when performing entity deletions and ensure that you have appropriate backups or data migration strategies in place.
{% endhint %}

### Delete an entity property

To delete an entity field, follow these steps:

1. Select the entity field you wish to delete. If you are working in a Diagram view, click on the field directly. Alternatively, if you are viewing the entities in a List view, right-click on the entity field to reveal a context menu.
2. In the context menu, select the **Delete this field** option. This action will initiate a confirmation modal titled **Delete Field Entity**.
3. Review the details presented in the modal, ensuring that you have selected the correct field for deletion.
4. Finally, click the **Delete Field** button to permanently remove the selected entity field from your data model.

{% hint style="danger" %}
Please note that deleting an entity field will result in the loss of any data associated with that field. Therefore, exercise caution when deleting fields and ensure that you have appropriate data backup or migration strategies in place.
{% endhint %}

## Virtual Entities

In the **ComUnity Developer Toolkit**, **Virtual Entities** provide a way to **model external data sources** within the **data model**, enabling seamless integration with third-party APIs.

Unlike **regular Entities**, which define data structures that map to SQL tables, **Virtual Entities are not linked to a database**. Instead, they act as an **abstraction layer**, allowing data from **external APIs** to be **retrieved and processed dynamically** while still supporting **OData-based queries**.

Virtual Entities allow applications to interact with API-driven data **just like regular entities**, making it easier to integrate third-party services while maintaining a **consistent query experience** within the Toolkit.

### Why use Virtual Entities ?

Virtual Entities allow applications to **model and interact with external APIs as structured entities**, ensuring:

* **Consistent Data Interaction** – API data is accessed through **OData-based queries**, just like internal data models.
* **No Database Mapping Required** – Since Virtual Entities retrieve data dynamically, they do not map to an SQL table.
* &#x20;**Seamless Integration with External APIs** – API responses are handled like structured entity data within the Toolkit.
* &#x20;**Unified Querying Mechanism** – Developers can interact with API-driven data using **the same syntax and tools** as regular entities.

### Creating Virtual Entities

To create a virtual entity follow these steps:

1. Open your project settings and navigate to the **Data** section.
2. Locate the ![](https://comunity.gitbook.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fu0RQqzbgKGN4uoL3P89t%2Fblobs%2FnHcxyiXXdB38PLbM5ekH%2Fimage.png\&width=300\&dpr=4\&quality=100\&sign=e80ec206\&sv=2) icon, this icon allows you to add a new virtual entity to your data model.
3.  Click the ![](https://comunity.gitbook.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2Fu0RQqzbgKGN4uoL3P89t%2Fblobs%2FnHcxyiXXdB38PLbM5ekH%2Fimage.png\&width=300\&dpr=4\&quality=100\&sign=e80ec206\&sv=2) icon, an **Add a virtual entity** modal window will appear on your screen. \


    <div align="left"><figure><img src="../../.gitbook/assets/image (452).png" alt="" width="375"><figcaption><p>Add virtual entity modal<br></p></figcaption></figure></div>
4. In the modal window, provide a unique name for your virtual entity in the designated **Name** box.
5. By default, the checkboxes for **Add entity class**, **Add controller class**, and **Add controller sample code** will be selected. These options generate boilerplate code for the entity and controller classes that are associated with your virtual entity. This code is placed in your project's [Custom Classes](https://comunity.gitbook.io/learning.comunityplatform/toolkit-guides/custom-classes). If you wish to include the generated code, you can leave these checkboxes selected. This will automatically generate the code for you. However, if you prefer to define your own custom entity and controller classes, you can unselect these checkboxes. This allows you to create and specify your own custom classes in the [Custom Classes](https://comunity.gitbook.io/learning.comunityplatform/toolkit-guides/custom-classes) section of your project, tailored to your specific requirements.
6. Finally, click **OK** to create the virtual entity.

After creating a virtual entity, it will be visible in the Data section, either in the Diagram or List view. In the Diagram view, you can see the newly created virtual entity displayed with a single field, which is typically the entity ID.\


<figure><img src="../../.gitbook/assets/image (459).png" alt="" width="280"><figcaption><p>An active newly created virtual entity with a single field called OrderId</p></figcaption></figure>

When you need to add additional fields to a virtual entity, the process is similar to adding fields to a regular entity. However, it's important to declare these fields within the entity class definition located in the Custom Classes section of your project.

Furthermore, when you select a virtual entity in the Diagram/List view, it will be visually highlighted with a blue border to indicate its active status. On the right-hand side of the Toolkit, the Properties Editor will appear. This editor provides convenient access to various properties of the virtual entity, including its name, entity class, and controller class.

<div align="center"><figure><img src="../../.gitbook/assets/image (27).png" alt="" width="284"><figcaption><p>A Properties Editor of a Order - virtual entity</p></figcaption></figure></div>

To modify the entity and controller classes, you can expand the text editor by clicking on the ![](<../../.gitbook/assets/image (238).png>) icon. This action allows you to access and edit the underlying codebase of your virtual entity. Utilising this feature, you can declare additional fields within your virtual class. Additionally, you can modify the controller class directly in the Data settings, eliminating the need to navigate to the Custom Classes section.

By utilising the text editor and modifying the controller class in the Data settings, you can conveniently make changes to your virtual entity, including adding fields and adjusting the behaviour of the controller, streamlining the customisation process.

{% hint style="info" %}
The properties you define at this stage will be added to the application metadata and only these properties will be rendered in the client wherever your current virtual entity is referenced to.
{% endhint %}

### Configuring WebApiConfig for Virtual Entities

After creating a Virtual Entity, it must be registered in WebApiConfig to be accessible via OData. This ensures that OData requests are correctly routed and that external services can be queried through the Web API.

To do this, navigate to Custom Classes > WebApiConfig, locate the CustomRegister method, and add an entry for the newly created Virtual Entity. Once modified, rebuild the project to apply the changes.

The WebApiConfig class ensures that:

1. Virtual Entities are registered as part of the OData model.
2. OData requests are properly routed to Virtual Entities.
3. External services can be accessed and queried through the Web API.

#### Modifying WebApiConfig

By default, WebApiConfig includes only system-generated entities:

{% code title="" lineNumbers="true" fullWidth="false" %}
```csharp
using System;
using System.Web.Http;
using System.Web.Http.OData.Extensions;

namespace todo1602251024
{
	/*
	For additional details on using OData in ASP.NET Web API, visit the following link.
	https://docs.microsoft.com/en-za/aspnet/web-api/overview/odata-support-in-aspnet-web-api/
	*/
	public static partial class WebApiConfig
	{
		static partial void CustomRegister(System.Web.Http.HttpConfiguration config)
		{
			// Web API configuration and services

			// Web API routes
			config.MapHttpAttributeRoutes();

			System.Web.Http.OData.Builder.ODataConventionModelBuilder builder = new System.Web.Http.OData.Builder.ODataConventionModelBuilder();
			//builder.EntitySet<ClassName>("ClassName");

			builder.EntitySet<Custom.NotificationView>("NotificationView");
            config.Routes.MapODataServiceRoute("odata", "odata", builder.GetEdmModel());
		}
	}
}
```
{% endcode %}

#### **Registering a Virtual Entity**

To expose a newly created Virtual Entity (e.g., Custom.Order), update WebApiConfig as follows:

{% code title="" lineNumbers="true" fullWidth="false" %}
```csharp
using System;
using System.Web.Http;
using System.Web.Http.OData.Extensions;

namespace blog1602251024
{
	/*
	For additional details on using OData in ASP.NET Web API, visit the following link.
	https://docs.microsoft.com/en-za/aspnet/web-api/overview/odata-support-in-aspnet-web-api/
	*/
	public static partial class WebApiConfig
	{
		static partial void CustomRegister(System.Web.Http.HttpConfiguration config)
		{
			// Web API configuration and services

			// Web API routes
			config.MapHttpAttributeRoutes();

			System.Web.Http.OData.Builder.ODataConventionModelBuilder builder = new System.Web.Http.OData.Builder.ODataConventionModelBuilder();
			//builder.EntitySet<ClassName>("ClassName");
                       builder.EntitySet<Custom.Order>("Order");

			builder.EntitySet<Custom.NotificationView>("NotificationView");
            config.Routes.MapODataServiceRoute("odata", "odata", builder.GetEdmModel());
		}
	}
}

```
{% endcode %}

After making these changes, rebuild the project to apply the modifications.

**Key Considerations When Modifying WebApiConfig**

* Explicit registration is required for each Virtual Entity.
* Ensure correct namespaces when adding entities (Custom.Todo).
* Rebuild the project after modifying WebApiConfig.
* Verify **OData** routes to confirm Virtual Entities are correctly exposed.

