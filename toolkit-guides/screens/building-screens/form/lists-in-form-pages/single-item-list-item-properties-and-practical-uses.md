# Single Item - List Item

The **Single Item - List Item** is a core component of the ComUnity Toolkit, designed to render individual list items within your application’s user interface. It provides flexibility in how data is displayed by allowing properties such as the title, icon, and page to be either dynamically retrieved from a data source or configured with static values.

The **Single Item** can be dynamically configured by defining its **Data Path**. This means that properties like the title, detail, and other attributes can be populated from the Data Service, ensuring real-time, context-specific information is displayed. Alternatively, these properties can be statically set for fixed content, depending on the requirements of your application.

A key feature of the **Single Item** is its ability to create direct, functional links between form screens by configuring the **Page** property, which specifies a relative path to the destination screen.

In this section, we will explore the key properties of a **Single Item**, focusing on its dynamic configuration using the **Data Path**, and provide a step-by-step guide on implementing it within a [Form ](../)page to establish functional links.

<figure><img src="../../../../../.gitbook/assets/image (430).png" alt="" width="155"><figcaption><p>Single Item - screen control as shown in the screen view</p></figcaption></figure>

### Properties of Single List Item

#### **Title**

The title of the list item.

#### **Icon**

The name of the icon to be displayed.

#### **Detail**

The detail of the list item.

#### **Aside**

The aside content that must be displayed in the list item

#### **Count**

{% hint style="warning" %}
This property is no longer supported.
{% endhint %}

#### **Image URL**

{% hint style="warning" %}
This property is no longer supported.
{% endhint %}

#### **Icon Image URL**

The name of the icon to be displayed. If set, this will be used instead of the icon value.

#### **Page**

The page to navigate to when selecting a list item, should be in the following format:

_`./<page_name>`_

#### **Data Path**

Sets the Data Path for the Form. The value specified will be appended to the page name and page Data Path to form the Target URL for the list item. The value can contain templates.

## Creating Functional Links to Additional Screens with Single Item - List Item

To create a functional link between a Form Page and an Additional Screen within your project, follow these steps:

**1. Add a List Component to Your Form page:**\
Begin by incorporating a List component within the Form page where you wish to create the navigation link.

**2. Integrate a Static Item screen control:**\
Within the List, introduce a Static Item screen control. This element will serve as the link between the existing Screen and the Form page.

**3. Access the Static Item Properties:**\
Click on the Static Item screen control  to select it. As you do so, the associated Properties will be revealed for configuration.

**4. Define the Page path:**\
In the displayed Properties, locate the **Page** property. Here, you can specify a relative path that corresponds to the **Additional Screen** you intend to navigate to. For instance, entering `./UserProfile` in the **Page** property would facilitate user movement from the current screen to the UserProfile screen.
