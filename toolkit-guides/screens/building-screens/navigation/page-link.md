# Page Link

**Page Links** extend the navigation hierarchy by enabling navigation between **Navigation** and newly created [**Form**](../form/) pages. Once a **Page Link** is created, you have the flexibility to customise it and establish a link to an existing Form page, if desired.

To create a Page Link, follow these steps:

1. **Create or Select a Navigation page:**\
   Begin by creating a new navigation page or selecting an existing one that you wish to use.
2. **Integrate a Page Link:**\
   Drag and position a Page Link screen control within the Screen Structure at an appropriate location.
3. **Access Page Link Properties:**\
   Click on the Page Link element to select it. This action will create a system generated Page and reveal the corresponding properties within the Properties panel.
4. **Configure and Save Properties:**\
   Use the Properties panel to tailor the [Page Link Properties](page-link.md#page-link-properties) as per your preferences. Once the configuration is refined, remember to save your adjustments."

### Properties of a Page Link

The Page Link properties are used to configure the destination [Form](../form/) page that is linked to the Page Link.

**Name**\
This property displays a system-generated name for the destination page. You can change this name to something more meaningful.

**Title**\
This property shows the title of the automatically generated Form page linked to the Page Link. You can change this title to something more descriptive.

**Layout Type**\
Choose a suitable layout type for your Page Link. The available layout types are:

* **Bar:** This layout type displays the destination page contents as a horizontal list item.
* **Card:** This layout type displays the destination page contents as a card.
* **Image:** This layout type displays the destination page contents as an image.
* **Pie:** This layout type displays the destination page contents as a pie chart.
* **PieList:** This layout type displays the destination page contents as a list of pie charts.
* **Tab:** This layout type displays the destination page contents as a tab.
* **Table:** This layout type displays the destination page contents as a table.

#### **Icon**

Customise the icon associated with the destination page contents, selecting an appropriate visual representation.

#### **Role Name**

Define a role name, if necessary, to control access or permissions related to the destination page contents.

#### **Target URL** &#x20;

The Target URL allows you to specify the [OData](../../../../reference-articles/odata.md) resource path for the form and must be a collection for an insert and a single record for an update or delete operation.

```
An example an insert (POST) operation
/Fault
Examples for an update (PUT / PATCH) or delete operation
/Fault(23)
/Fault({{= faultId}}) – where faultId will be replaced with a parameter in the Target URL of the parent navigation item.

```
