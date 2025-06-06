# Screen Controls

Screen Controls offer a diverse range of UI elements used to build your application's screens. These controls encompass buttons, input fields, drop-down menus, lists, images, multimedia, and more, providing an extensive array of options to create engaging and dynamic user interfaces.

The ComUnity Development Toolkit allows seamless customisation of the behaviour and appearance of these controls, enabling developers to match them precisely to the unique requirements of their applications. When you add a screen control to a screen and correctly configure and save its properties, the Toolkit's underlying engine parses your screen control definition and renders it as a specific user interface (UI) component on the client side.

Supported UI components include lists, images, forms, text, and other interactive elements, allowing for a versatile and tailor-made user experience.

By leveraging the capabilities of Screen Controls, developers can create interactive and user-friendly interfaces that elevate the usability and appeal of their applications. This level of flexibility and functionality empowers development teams to deliver exceptional user experiences and align their applications with specific design objectives.

## Supported Screen Controls

Supported Screen Controls vary depending on the type of screen ([Navigation](navigation/) or [Form](form/) pages) as well as the active screen control. When you select a screen, its supported controls will appear in the Screen Structure. Additionally, as you build the active screen, adding a Screen Control to the screen view and making it active will reveal its relevant controls, allowing you to embed additional Screen Controls where applicable. This dynamic system enables you to create complex and interactive user interfaces by nesting controls within one another. For a comprehensive discussion of the supported controls for each screen type and their specific behaviours, please refer to the relevant sections dedicated to [Navigation](navigation/) and [Form](form/) pages.

## **Adding Screen Controls to a Screen**

The process of adding Screen Controls into your project involves adding them to selected Screens or even to other selected Screen Controls. Some Screen Controls even allow you to embed additional Screen Controls within them, as is the case with [Lists](screen-controls.md#list).

To integrate Screen Controls, follow these simple steps:

1. **Select the Screen or relevant Screen Control:** \
   Begin by choosing the Screen where you intend to add the Screen Control, or select an existing Screen Control that will host the new addition. This selection serves as the foundation for the placement.
2. **Choose the Screen Control:** \
   Access the Screen Control panel and select the desired Screen Control for your project. Depending on your choice, this can be a direct addition or an embedded Screen Control within another.
3. **Drag and Drop Placement:** \
   With your Screen Control selected, use the drag and drop functionality. Hover the control over the chosen area on the screen. As you do so, visual cues like dashed green lines will help identify suitable positions.
4. **Visual Confirmation:** \
   When you hover over a valid placement, a green solid line will appear, indicating that the Screen Control can be dropped in that spot. If satisfied with the placement, release the control to add it to your screen.
5. **Customise and Position:** \
   Once added, the Screen Control will find its place within your page or within the designated Screen Control. You can easily reposition it as needed for optimal layout. Additionally, take advantage of customisation options to tailor the appearance and behaviour to your requirements.

{% embed url="https://toolkitv3.comunity.me/u/d/d63d96facde60b6e98e3dcba8e3e5d668acc0a9da6e35adbff9b7b7a251c2f46.mp4" %}
Add a Screen Control to a Screen
{% endembed %}

After successfully adding the Screen Controls, the screen will load, allowing you to visualise the integration within the layout. To further refine the behaviour and appearance of these added controls, you can delve into their properties configuration.

To configure the properties of a Screen Control, simply follow these steps:

1. **Select the Control:** After the screen loads, you can click on the specific Screen Control that you wish to configure. This selection triggers the display of its properties.
2. **Access the Properties Panel:** Once the control is selected, its relevant properties will appear within the Properties panel. This panel is designed to provide you with a comprehensive overview of the available settings.
3. **Configuration Process:** Proceed to configure the properties according to your project's requirements. You can fine-tune various aspects, such as appearance, behaviour, and interaction functionalities.

By customising these properties, you ensure that each Screen Control aligns precisely with your desired user experience. To apply these customisations, you should click **Save** button positioned at the bottom of the Properties Panel. The Properties panel offers a user-friendly interface to facilitate this customisation, allowing you to create a tailored and cohesive interface for your project.

## Removing a Screen Control

When the need arises to remove a Screen Control from your layout, the process is straightforward and seamless.&#x20;

Follow these steps to achieve the removal:

1. **Select the Control**\
   Begin by selecting the Screen Control that you wish to remove from your layout. Click on it to prepare for the removal action.
2. **Drag to Remove**\
   Once the control is selected, initiate the removal process by dragging it towards the Screen Controls panel. As you do so, keep an eye out for the appearance of a trash can icon within the Screen Controls panel itself.
3. **Delete with a Drop**\
   As you approach the Screen Controls panel with the control, the trash can icon becomes prominent, signifying the deletion capability. Once the control is positioned above the trash can icon, you can confidently release the control to drop it. This action will prompt the immediate removal of the selected Screen Control.

By following these steps, you can efficiently remove unwanted Screen Controls from your layout, ensuring that your interface remains precisely tailored to your project's evolving needs.

{% embed url="https://toolkitv3.comunity.me/u/d/afff5b93e2a7fd1b38f59205a626bedffd5362f6fdba4d083f4f93a1fb694cba.mp4" %}
Drag & Drop to Delete Screen Controls
{% endembed %}

## Standard Screen Controls

Standard screen controls are those that are available in both navigation and form pages. They are the most basic and commonly used screen controls, and include the following:

* [Image](screen-controls.md#images): This control allows you to display an image on a screen.
* [Paragraph](screen-controls.md#paragraph): This control allows you to display text on a screen.
* [List](screen-controls.md#list): This control allows you to display a list of items on a screen and to creating more complex screen layouts and interactions.

In this section, we will discuss these standard screen controls in detail. We will cover their properties, how to use them, how they can be customised to match the specific needs of your application. and some best practices for using them effectively.&#x20;

### Image

Incorporating images into your screen design is a key aspect of creating visually engaging interfaces. When adding an image to a screen, you initially place a system-generated placeholder image, as depicted below. However, through the configuration of your image digest, this placeholder can be effortlessly replaced with your desired image.

#### Properties of an Image&#x20;

* **Name** \
  This property displays the system-generated name of the image.
* **Image Digest**\
  Allows you to seamlessly drop or upload an image from your local computer or preferred source.
* **Digest Preview**\
  Offers a convenient preview feature, allowing you to visualise the added image before finalising its placement.

By leveraging these properties, you can effortlessly introduce and customise images within your screen, enhancing the visual appeal and engagement of your user interface.

### Paragraph

Markdown can be used to add text content to screens.

#### Properties of a Paragraph

* **Name**\
  This property displays the system-generated name of the paragraph.
* **Content**\
  This feature presents a text editor designed specifically for adding content using Markdown formatting. A subset of Markdown it supported when adding text content to screens. The table below gives an overview of the supported elements:

<table><thead><tr><th width="262">Element</th><th>Support</th></tr></thead><tbody><tr><td>Heading Level 1</td><td>#</td></tr><tr><td>Heading Level 2</td><td>##</td></tr><tr><td>Heading Level 3</td><td>###</td></tr><tr><td>Heading Level 4</td><td>####</td></tr><tr><td>Heading Level 5</td><td>#####</td></tr><tr><td>Heading Level 6</td><td>######</td></tr><tr><td>Paragraph</td><td>Blank line to separate one or more lines of text.</td></tr><tr><td>Line Breaks</td><td>End a line with two or more spaces plus newline</td></tr><tr><td>Bold</td><td><pre><code>**bold**
</code></pre></td></tr><tr><td>Italic</td><td><pre><code>_italic_
</code></pre></td></tr><tr><td>Bullet List</td><td><pre><code>- List Item 1
- List Item 2
</code></pre></td></tr><tr><td>Link</td><td><pre><code>[link](https://example.com)
</code></pre></td></tr><tr><td>Image</td><td><pre><code>![Image](http://example.com/image.png)
</code></pre></td></tr></tbody></table>

### List

Lists can play a variety of roles in an application's architecture, depending on their position in the hierarchy and how they are configured. They can be used to display data, navigate between pages, or even create complex layouts. To fully understand the function Lists, refer to the [ Building Screens/Overview ](./#overview)section. For practical implementations and detailed insights, explore the following sections:

* &#x20;[Dynamic List Rendering in a Navigation Page](navigation/lists-in-navigation-pages/dynamic-list-rendering-in-a-navigation-page.md)
* [Page Link](navigation/page-link.md)
* [Implementing Sub-Screens Using Lists](navigation/lists-in-navigation-pages/implementing-sub-screens-in-navigation-pages-using-list-items.md)
* [Static Lists](form/lists-in-form-pages/static-lists.md)
* [Entity Items - List Item](form/lists-in-form-pages/rendering-data-from-entity-associations-in-form-pages.md)

#### Properties of a Paragraph

{% hint style="info" %}
The Properties and Screen controls of a List depend on the screen type of the page in which it is contained, for more details view [Navigation/Lists](navigation/lists-in-navigation-pages/) or [Form/Lists ](form/lists-in-form-pages/)sections.
{% endhint %}
