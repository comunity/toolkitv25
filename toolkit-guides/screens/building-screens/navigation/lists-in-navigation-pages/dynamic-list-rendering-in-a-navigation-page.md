# Dynamic List Rendering in Navigation pages

Dynamic list rendering in a **Navigation** page enables you to show lists of data that are fetched from the Data Service dynamically with [OData](../../../../../reference-articles/odata.md), view [Data Path](dynamic-list-rendering-in-a-navigation-page.md#data-path) for implementation details. [Mustache Templating](../../../../../reference-articles/mustache-templating.md) is a valuable tool for creating complex and dynamic [OData](../../../../../reference-articles/odata.md)queries and can also be used to pass data to child pages, such as the unique identifier of a list item, by templating the [Target URL](dynamic-list-rendering-in-a-navigation-page.md#target-url) property. Dynamic Lists can be displayed in a variety of layouts, such as pies, tables, and grids.

**Examples:**

* You could use dynamic list rendering to show a list of products from the Data Service, filtered by category.
* You could use dynamic list rendering to show a list of blog posts from the Data Service, sorted by date.
* You could use dynamic list rendering to show a list of users from the Data Service, grouped by country.

![](<../../../../../.gitbook/assets/Mask group.svg>)

### Implementing Dynamic Lists&#x20;

To implement dynamic list rendering in Navigation screens, the following properties are essential:

#### **Data Path**

This property is used to to define the resource path of an [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/).

{% hint style="warning" %}
When using dynamic list rendering, it is important to make sure that the response payload from the Data Path is a collection. If an individual entity is returned, the application will break.
{% endhint %}



#### **Query**

This property is used to to define the query options of an [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/).

{% hint style="warning" %}
The ComUnity Development Toolkit appends the Data Path and Query values to the system defined service root path  under the hood to form a complete [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/).
{% endhint %}



#### **Item Title**

This property is used to define a dynamic title of the list item. The Item Title is an optional property, if you do not define it by default the system will use the List Title Template.

```
//An example of an item title
{{= Title}}
```

#### **Item Detail**

This property is used to define a dynamic list item details. The Item Detail is an optional property, if you do not define it by default the system will use the List Detail Template.

{% hint style="info" %}
&#x20;The Item Detail field also accepts Markdown content.
{% endhint %}

<pre><code><strong>An example of an item description
</strong>{{= Description}}
</code></pre>

#### **Item Aside**

This property is used to specify content that is placed in the top right corner of the list box. Suitable properties include Created and a derived property called CreatedTimeAgo which is available by default in all entities.

```
// An example of templating of the created at property as an item aside
{{= Created}}

// An example of templating of the created time ago devived property as an item aside
{{= CreatedTimeAgo}}

```

#### **Max Items**&#x20;

This Max Items property is used to specify limit of the records to display on the clients.

#### **Stale After(seconds)**&#x20;

To improve performance the system supports caching for all read operations. The Stale After property allows you to specify the number of seconds the cached data is persisted in cache memory in the current session.

{% hint style="warning" %}
Caching is only supported for [OData URL](https://www.odata.org/documentation/odata-version-3-0/url-conventions/) without the query options parameter.\

{% endhint %}

#### **Search Fields**&#x20;

This property allows you to specify entity properties to be used for filtering the dynamic list. It accepts a comma delimited string of entity properties:\


`Property1,Property2,Navigation_Property`\


```
// An example of a Search Field associated with a list fetched from the Fault Entity
Description,FaultSubType

```

{% hint style="danger" %}
Do not add spaces in your Search Fields values, valid properties are only comma delimited.
{% endhint %}

Navigation properties or entity associations are valid values of the Search Fields list property. They allow application users to filter your dynamic list by navigation property or association type.\
Navigation properties or entity associations are valid values of the Search Fields list property. They allow application users to filter your dynamic list by navigation property or association type.\
\
The Diagram A below show a screenshot of a typical Search Field as it is displayed in the web client during development, when a user clicks the  Navigation Property Dropdown Icon, Navigation Properties appear as shown in Diagram B, application users are able to filter dynamic list by selecting a specific navigation property type from a dropdown of navigation property types.\
\
Diagram A

![](<../../../../../.gitbook/assets/Component 50.svg>)

Diagram B

![Screenshot B](<../../../../../.gitbook/assets/Component 51.svg>)

#### **Icon**

Icon property will show an Icon to the left of the Title / Description.

#### **Image URL**

This property is used to define a dynamic list image. Image URL will show an image to the left of the Title / Description.

```
// An example of the value of Image URL
{{= Photo}}
```

#### **Target URL**&#x20;

When you Create a Navigation Link from a dynamic list to a destination page(navigation or form page), the destination page not reachable unless you specify a Target URL.

The Target URL property allows you to specify a dynamic LINK from each individual list item in the current navigation page to the destination page. The query parameter in the LINK definition is typically an ID of an individual entity.

```aspnet
The syntax for the Target URL can have 0 to N parameters passed to the navigation link,
as shown below: 
LINK:<link id>
LINK:<link id>?<key=value>
LINK:<link id>?<key=value>&<key=value>

// An  example of a Target URL
LINK:FaultAddPage?faultType={{= FaultTypeId }}
```

#### **Additional Notes:**

* The keyword `LINK` is required.
*   `FaultAddPage` is a system generated identifier of your destination page(typically this is a form page), that is listed in the Properties Editor when a page is active. The screenshot below an example of a form page identifier labelled A:

    <img src="../../../../../.gitbook/assets/LINK name.svg" alt="" data-size="original">


* `faultType` is query parameter.
* [Mustache templating](../../../../../reference-articles/mustache-templating.md) is used to reference the dynamic value of the query parameter as shown in the last segment of the Target URL: `{{=FaultTypeId}}`.
