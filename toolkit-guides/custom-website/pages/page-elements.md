# Page Elements

Page elements are modular code blocks of dynamic page content written in [Razor syntax](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0). A page element by definition belongs to a single page.

The Page Elements feature in the ComUnity Toolkit empowers developers with a customisable utility to create tailored page components that meet specific requirements. These versatile tools facilitate the implementation of CRUD (Create, Read, Update, Delete) functionality within custom website pages. By seamlessly interacting with the Data service, developers can manipulate and dynamically display data within their web pages.

To access the page settings and leverage the Page Elements, follow these steps:

1. Open your project in the ComUnity Toolkit and navigate to the Custom Website section.
2. Select the Pages tab to view a comprehensive list of all existing pages within your Custom Website.
3. Choose the specific page you want to customise, and an array of icons will be displayed.
4. Locate and click the ![](<../../../.gitbook/assets/image (304).png>) icon associated with that page.
5.  A modal window titled **Add a Page Element** will appear on your screen. \


    <div align="left"><figure><img src="../../../.gitbook/assets/image (211).png" alt="" width="375"><figcaption></figcaption></figure></div>
6.  In the modal window, provide a name for the page element and select the desired type. You can choose between two available types: **Element** and **Form Element**

    {% hint style="info" %}
    **Form elements** are designed to facilitate the posting of form-related data to the platform. However, it is worth noting that this feature is currently underutilised, and may require removal. As a best practice, use **Elements** for all form-related tasks.
    {% endhint %}


7. After successfully creating the page element, it will be added to the page hierarchy.
8. Select the created page element to build and configure its settings. This action will reveal a pop-up screen dedicated to customising the page element's specific settings.

## Page Element Settings

Page Element Settings in the ComUnity Developer Toolkit offer developers the ability to fine-tune and customise various aspects of their page elements. These settings play a crucial role in configuring the behaviour and display of dynamic content within web pages.

In order to explore these settings in detail, developers can refer to the comprehensive guide on Dynamic List Rendering in a Navigation Page, which provides in-depth information and examples. This guide covers essential topics related to Page Element Settings, including the properties and their functionalities.\


Let's explore the details of the individual Page Element Settings:

### Name

This property displays the name of your page element.

### Page Tag

This property allows you to define a unique name that serves as a reference when templating your page element into a page. Refer to [Templating Page Elements ](./#templating-page-elements)for further details.

### Data Path

This property is used to define the resource path of an [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/).

### Query

This property is used to define the query options of an [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/).

### Sort Order

The Sort Order determines the ordering of the data as specified on the Data Path. It functions similarly to platform data queries. You can specify a comma-separated list of fields that you want to sort on. For example, "Name, Surname desc, DateOfBirth".

### Max Items

The Max Items property is used to specify a limit on the number of records to display on the client.

{% hint style="danger" %}
Pagination is not yet supported.
{% endhint %}

### Content

The payload that is returned by the oData URL you defined in your  [Data Path](page-elements.md#data-path) and  [Query](page-elements.md#query)  is referenced to as `Model` in your content definition.&#x20;

The code samples shown below show a [Data Path](page-elements.md#data-path) and [Query](page-elements.md#query) used to fetch data from the **BaseNotification** entity in the Data Service and the [Content](page-elements.md#content) definition written using  [Razor syntax](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0) shows logic for iterating over the payload referenced to as `Model` and then displaying the outcome on the web using markup:

**Data Path**&#x20;

```csharp
/BaseNotification
```

**Query**

```csharp
Deleted eq null and isof('TEST12345.BroadcastNotification')
```

**Content definition in** [Razor syntax](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0)

```csharp
@{var cnt = Model == null ? 0 : ((IEnumerable<IDictionary<string,object>>)Model).Count();}
    @if (cnt == 0) {
        <div style="padding:32px">No notifications have been sent.</div>
    } else {
    foreach(var item in Model) {
        <div class="card">
            <div class="card_container">
            <h4><b>@item["Subject"]</b></h4>
            <p>@item["Message"]</p>
            </div>
        </div>
        }
    }}
```

By understanding and configuring these various Page Element settings, you can customise and optimise the behaviour and display of your page elements within the ComUnity Developer Toolkit.
