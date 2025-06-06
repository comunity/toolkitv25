# Lists in Form pages

Upon selecting a List within a **Form** page, you will be presented with its supported screen controls in the Screen Controls panel, along with its Properties. Notably, a List in a **Form** page does not possess configurable properties; it is equipped solely with a single property—**Name**—which displays its system-generated identification.

<figure><img src="../../../../../.gitbook/assets/image (42).png" alt="" width="237"><figcaption><p>Properties of List</p></figcaption></figure>

When adding a List to a **Form** page, you will be presented with the **List Type's** options. By default, **List** is selected, but you can choose from several other layout types:

<figure><img src="../../../../../.gitbook/assets/image (40).png" alt="" width="375"><figcaption><p>List Types</p></figcaption></figure>

* **List**: Displays items as a standard list.
* **Grid**: Shows items in a grid format.
* **Map**: Displays items as markers in a map view (each item must have a Latitude and Longitude value).
* **Tab**: Presents the items as tabs at the top of the Form.
* **Pie**: Visualises items as a pie chart (requires item value to be a JSON document).
* **Bar**: Visualises items as a bar chart (requires item value to be a JSON document).

In addition to **List Types**, you can define **List Items**, which determine the content displayed within the List:

<figure><img src="../../../../../.gitbook/assets/image (41).png" alt="" width="375"><figcaption><p>List Types</p></figcaption></figure>

* **Entity Items**: Adds multiple list items created from the records contained in a database entity.
* **Single Item**: Adds a single list item that can be templated with data values from the parent page's context.
* **Static Item**: Adds a single static list item.

These supported screen controls and their corresponding properties are instrumental in implementing  [Static Lists](static-lists.md) and [Rendering Data from Entity Associations](rendering-data-from-entity-associations-in-form-pages.md), providing flexibility in how data is presented within your Form page.
