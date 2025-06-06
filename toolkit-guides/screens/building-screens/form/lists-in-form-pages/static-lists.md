# Static Item - List Item

The **Static List Item** in the ComUnity Toolkit is a component used to add a single, predefined list item to a [Form](../) screen. Unlike [Single List Items](single-item-list-item-properties-and-practical-uses.md) or[ Entity Items](rendering-data-from-entity-associations-in-form-pages.md), static list items do not retrieve data from the [Data Service](../../../../data/) but are configured with static values. Each item can be customised with optional properties such as a title, icon, details, and an Action URL, based on the developer’s specific requirements.

The Action URL is an optional property that enables navigation to a different Form screen. However, it is not mandatory; developers may choose to omit the Action URL if the static list item is intended to display information or perform a non-interactive function.

Static List Items are ideal for displaying fixed options or actions that remain consistent and do not require dynamic data, making them well-suited for use cases such as linking to predefined screens or providing consistent navigation options.

<div align="left"><figure><img src="../../../../../.gitbook/assets/image (38).png" alt="" width="161"><figcaption><p>Static List - screen control as shown in the screen view</p></figcaption></figure> <figure><img src="../../../../../.gitbook/assets/image (39).png" alt="" width="563"><figcaption><p>Static List - screen control as shown in the screen structure and relevant properties</p></figcaption></figure></div>

### Properties of Static List Item

#### **Action URL**

The navigate path to be used when the list item is selected.The Action URL is an optional property of Static List Items in the ComUnity Toolkit. It defines the navigation path for these items, allowing users to be directed to specific screens within the application when a static list item is selected.\
\
**Key Features**

* &#x20;**Navigation to System Screens**: The Action URL can be used to navigate directly to system screens using absolute paths, such as /Register or /ChangePassword
*   **Navigation to Form Screens**: For custom and Additional Form screens **LINKs** are used (e.g., LINK:BusinessOwnerEventsRespondPage?eventId=\{{= eventId \}}). This allows for dynamic navigation by passing context-specific data, such as entity IDs. The same rules that apply when defining Target URLs for lists in Navigation screens are also used when defining Action URLs.\
    The syntax for the Action URL can have 0 to N parameters passed to the LINK,

    ```
    as shown below: 
    LINK:<link id>
    LINK:<link id>?<key=value>
    LINK:<link id>?<key=value>&<key=value>

    // An  example of a Target URL
    LINK:FaultAddPage?faultType={{= FaultTypeId }}
    ```



* Optional Property: The Action URL is not mandatory. If the static list item is intended to serve an informational purpose without any navigational function, the Action URL can be omitted.

#### **Title**

This property allows you to specify the title of a list list item. This property is required.

#### **Icon**

This property allows you to select an icon for a list list item.

#### **Detail**

This property allows you to specify the detail of a list list item. This property is required.

#### Aside This property is used to specify static content that is placed in the top right corner of the list box.

#### **Count**

{% hint style="warning" %}
This property is no longer supported.
{% endhint %}

#### **Image URL**

The image URL property allows you to upload an image to your list item, view Images to learn more.

#### **Icon Image URL**

The name of the icon to be displayed. If set, this will be used instead of the icon value.
