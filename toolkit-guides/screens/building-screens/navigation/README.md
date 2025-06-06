# Navigation

**Navigation** pages are a powerful feature that enables the creation of complex navigation structures within applications. They can display both static content (such as images, text, and static lists) and dynamic content, and can be directly integrated into the navigation hierarchy.

The underlying node type for a **Navigation** page is a List, allowing it to contain other [Forms](../form/), Lists, and various Screen Controls. This versatility makes **Navigation** pages a flexible tool for building a wide range of navigation structures tailored to your application's needs.

Moreover, **Navigation** pages support the use of dynamic Lists, which are an effective way to present data from various sources, including entities, lists, and custom objects. These Lists can be customised to meet the specific requirements of your application, providing a dynamic and responsive user experience.

**Examples of How to Use Navigation pages:**

* Creating a hierarchical navigation structure with multiple levels of pages.
* Designing a navigation system tailored to the specific needs of an application.
* Displaying dynamic content using Lists to enhance user engagement.

## Properties of a Navigation page

* **Name**\
  This is the name you designated to your page during creation.
* **Title**\
  This property allows you to customise the title of your navigation page.
*   **Icon**\
    This property allows you to select an icon which is used to prefix the[ Title](./#title).

    {% hint style="warning" %}
    For [main menu](https://github.com/comunity/comunity-docs/blob/master/toolkit-guides/screens/building-screens/navigation/broken-reference/README.md) items the Icon field is required otherwise broken icon images will be rendered before your menu items.
    {% endhint %}

## What comes next?

Once you have set the properties of your **Navigation** page, you can start building your page content using screen controls. You can find a comprehensive guide on how to do this in the [Screen Controls section](../screen-controls.md). In the next section, we will discuss how to implement features specific to the **Navigation** page, which can all be done using screen controls strategically.

1. [Lists](lists-in-navigation-pages/)
2. [Page Links](page-link.md)
