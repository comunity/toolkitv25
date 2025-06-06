---
description: 'Enhancing Form Interaction: Utilising Lists for Rendering Entity Associations'
---

# Entity Items - List Item

When designing a Form page to manage a specific entity, it’s often beneficial to enhance the user experience by incorporating additional information derived from related entities. This is where **Entity Items - List Item** comes into play. Entity Items are special types of list items almost always used to resolve associations (also known as navigations) between entities or navigate to related screens.

<div align="left"><figure><img src="../../../../../.gitbook/assets/image (35).png" alt="" width="167"><figcaption><p>Entity Items -  screen control as shown in the screen view</p></figcaption></figure> <figure><img src="../../../../../.gitbook/assets/image (37).png" alt="" width="563"><figcaption><p>Entity Items - screen control as shown in the screen structure</p></figcaption></figure></div>

To effectively use Entity Items, you must first define associations to the entity being managed by the Form in your Data Model. These associations, also referred to as navigations, link the main entity to related entities, allowing for dynamic retrieval of associated data. For more information on setting up these associations, refer to the Table Links section in your Data Model documentation.

Once the associations are defined, you can integrate a List control within the Form page. This List control dynamically fetches and displays data from the associated entities, enriching the context and functionality of the Form page.

{% hint style="danger" %}
Associations to the entity managed by the Form must be defined in the Data Model before they can be used in a List control on a Form page.
{% endhint %}

For example, on a User Profile Form page, the List control might be configured to display the user's most recent orders, providing valuable insights into their purchasing history. In another scenario, it could be used to showcase communities or groups that the user is associated with, offering a glimpse into their social interactions and affiliations.

The versatility of the List control makes it an invaluable tool for enhancing the user experience on a Form page. By displaying relevant associated entities, the List control helps users better understand and interact with the main entity. Additionally, the List control can be customised to align with the design principles of your application, offering different layouts, styles, and interaction behaviours to ensure a seamless user experience.

In pages containing a List with Entity Items, the **Target URL** of the page serves as a base. The **Entity Set or Navigation Property** (e.g., `/Comments`) is appended to this Target URL to resolve the association. This means that when a user interacts with the list item, they are navigated to the appropriate related screen or entity, ensuring a cohesive and intuitive navigation experience.

### Implement Dynamic List Rendering using Entity Items

To implement dynamic list rendering using Entity Items, the following properties are essential:

#### **Query Filter**:&#x20;

Specifies the query that must be applied when fetching the records for the list items. Templates can be used to dynamically generate the query based on the current state of the application.

#### **Search Fields**:&#x20;

Specifies the fields that must be used for search operations to filter the list.

#### **Stale After**:&#x20;

This property is no longer supported.

#### **Entity Set or Navigation Property**&#x20;

Specifies the entity set or navigation property from which the list items will be fetched. For example, if the Entity Set or Navigation Property is `/Comments`, it will be appended to the Target URL of the page that contains the List. This effectively resolves the association by directing the user to the relevant associated data.

#### **Target URL Prefix**

Specifies the URL path that should be prepended to the page Data Path when generating the Target URLs for the list items. Templates can be used to dynamically generate the URL path based on the current state of the application.

By carefully configuring these properties, you can create dynamic, context-sensitive lists that enhance the functionality and user experience of your Form pages.
