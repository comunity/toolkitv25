# Adding Sub-Screens to Navigation pages Using List Navigation

Lists in Navigation pages allow developers to organise and structure sub-screens. This functionality supports both dynamic Lists (configured to pull data from the [Data Service](../../../../data/)) and static Lists (used for displaying predefined sets of links or screens).

This approach is used to add sub-screens to the navigation hierarchy, enabling clear and manageable navigation flows within your application.

**Key Distinctions:**

• Dynamic Lists: These are configured to fetch data from the Data Service, enabling dynamic content to populate sub-screens - to configure a List to make it dynamic define its Data Path property for further details view [Dynamic List Rendering in Navigation pages](dynamic-list-rendering-in-a-navigation-page.md).

• Static Lists: These are used to create fixed sets of links or items without requiring data from the Data service, making them useful for simpler navigation scenarios.

<figure><img src="../../../../../.gitbook/assets/image (33).png" alt=""><figcaption><p>List Navigation</p></figcaption></figure>

## **Steps to Add a Sub-Screen to a Navigation page using Lists:**

1. **Select a List:**\
   Start by selecting a List within the Navigation page. This can be either dynamic (data-driven) or static (predefined).
2. **Access List Screen Controls:** \
   What you see depends on the type of List selected:
   1. **Dynamic List**: Screen controls appear under the title **List Navigation**, displaying the following options:
      1. **Navigation page:** Adds a new Navigation page to the hierarchy.
      2. **Form:** Adds a new Form page to the hierarchy.
   2. Static List: Controls appear under the title **List Items**, displaying:
      1. **Nav Page Item:** Adds a new Navigation page to the hierarchy.
      2. &#x20;**Form Item:** Adds a new Form page to the hierarchy.
3. **Add the Screen Control:**\
   Drop the selected screen control (either Navigation page or Form) into the List to nest a new sub-screen. This action will create a new sub-screen linked to the navigation hierarchy.
4. **Save Changes:** \
   After adding the control and customising any necessary properties (such as titles, layout type, page content or TargetURLs), save the changes to update the navigation structure.

**Additional Tips:**

* If you plan to add multiple links as items to your static list, consider configuring the **Layout Type** property of your list for better organisation and usability.
* Once a sub-screen has been added, the next step is to configure the screen properties of the destination page according to its type. For more information, refer to the documentation on Navigation and Form pages
