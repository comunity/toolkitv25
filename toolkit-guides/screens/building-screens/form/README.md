# Form

A Form page is primarily used to embed forms, but it can also display static screen components (such as images, text content, [static lists](lists-in-form-pages/static-lists.md)) and [dynamic lists](lists-in-form-pages/rendering-data-from-entity-associations-in-form-pages.md). In some configuration settings, a form page may simply be referred to as a "**Page**". The forms embedded within form pages are essential for implementing Create, Read, Update, and Delete (CRUD) operations.

<figure><img src="../../../../.gitbook/assets/image (168).png" alt=""><figcaption><p>An example of an Add New Fault - Form page which exists in the Fault sample</p></figcaption></figure>

Here are two methods for integrating form pages into your project:

**1. Incorporating Forms as Top-level screens:** One method involves placing a Form page directly within your project's navigation hierarchy. During screen configuration, you can achieve this by specifying the page type as `Form`. Additionally, you can make use of the Copy Form functionality. This approach provides swift access to a form page tailored to your needs.

**2. Adding Forms as Sub-Screens:** Alternatively, as you set up [Page Links](../navigation/page-link.md), [Data Entry Screens](../#data-entry-screens) and [Additional Screens](lists-in-form-pages/static-lists.md#implementing-additional-screens-using-static-lists), the system takes the initiative to generate the required form page. This automated process ensures the creation of a corresponding blank Form page. Furthermore, you can generate new Form page by embedding Form Item within Lists in your Navigation pages, refer to [Adding Sub-Screens to Navigation pages Using List Navigation](../navigation/lists-in-navigation-pages/implementing-sub-screens-in-navigation-pages-using-list-items.md)[ ](../navigation/lists-in-navigation-pages/implementing-sub-screens-in-navigation-pages-using-list-items.md)to explore this method.

Both approaches offer you versatility and simplicity in integrating form pages into your project. When you create a Form page its relevant Screen Controls and Screen Properties are shown in the Screen Controls and Properties panels within the Screen View, respectively:

<div align="center" data-full-width="false"><figure><img src="../../../../.gitbook/assets/image (314).png" alt="" width="146"><figcaption><p>The diagram above shows an in-exhaustive list of Screen Controls of a Form Page, you scroll down to view more controls in the Toolkit</p></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (312).png" alt="" width="280"><figcaption><p>Properties of a newly created Form Page whose system generated name is Faults_Page</p></figcaption></figure></div>

### Properties of a Form page

#### **Title**

This property allows you to specify the title of your navigation page.&#x20;

{% hint style="info" %}
If the title is not set, the system by default uses the name of your link as a title.&#x20;


{% endhint %}

#### **Role Name**&#x20;

This property allows you to specify the user role that has access to the navigation page. &#x20;

{% hint style="info" %}
&#x20;If a Role Name is not specified a navigational component is visible to all authenticated users conversely when a Role Name is specified for a navigational component, that component is then conditionally displayed in the client. Authenticated users on the applications will see only the component which they have permission rights for, otherwise if they do not have the correct access rights the navigational elements will be hidden from their view. \
To learn more about  how to configure user roles and permissions view Authorisation.


{% endhint %}

#### **Icon**&#x20;

This property allows you to select an icon which is used to prefix the[ Title](./#title). &#x20;

{% hint style="warning" %}
For menu item links the Icon field is required otherwise broken icon images will be rendered before your menu items.
{% endhint %}

_The screenshot below shows two menu items displayed as part of the Main Menu on a web application built using the ComUnity Development Toolkit. During navigation configuration the Icon for the Admin link was not selected during development, so it is displayed as a broken image before the link name, whereas for the Notifications menu item, a bell icon was selected._

![](<../../../../.gitbook/assets/image (226).png>)



#### **Selected Icon**&#x20;

This property allows you to specify a selected icon for your IOS applications.

#### **Page**

By default a form page is empty on creation, the Page property allows you to select and copy the content and functionality of an existing form page from a list of all form the pages which exist in your application.

#### **Entity name**

This property allows you to select an entity by name from a list of entities which exist in the Data Model. This value can usually be determined by the system from the Target URL, however when the Target URL is not set then this value may be required in order to set the correct data entity that must be used for the form.

{% hint style="info" %}
The [Entity name](./#entity-name) and the [Target URL](./#target-url) serve the same purpose, to avoid redundancy you define one or the other but not both in the same configuration.


{% endhint %}

#### **Target URL**

The Target URL allows you to specify the OData resource path for the form and must be a collection for an insert and a single record for an update or delete operation.

```
An example an insert (POST) operation
/Fault
Examples for an update (PUT / PATCH) or delete operation
/Fault(23)
/Fault({{= faultId}}) – where faultId will be replaced with a parameter in the Target URL of the parent navigation item.

```

#### **Edit Mode**

A Form page will open in “edit” mode for a new record and “read” mode for and existing record. The Edit Mode will open existing records in “edit” mode when this value is selected.

## What comes next?

Once you have set the properties of your Form Page, you can start building your page content using screen controls. You can find a comprehensive guide on how to do this in the [Screen Controls section](../screen-controls.md). In the next section, we will discuss how to implement features specific to the Form Page, which can all be done using screen controls strategically.

Supported components:

1. [Screen Controls](forms-controls.md)
2. [Lists in Form Pages](lists-in-form-pages/)
