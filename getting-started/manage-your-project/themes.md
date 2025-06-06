# Themes

The ComUnity Developer Toolkit enables developers to customise the appearance of their applications across client platforms, including Android, iOS, Web, and Windows, using themes. A theme is a collection of attributes that define the style and layout of the application, providing flexibility to align the app’s design with branding and user preferences.

Themes offer extensive customisation options, allowing developers to modify components such as tabs, buttons, text size, and label appearance:

* **Tabs:** Developers can customise tab colours, including background and font colours, to align with the app’s design language and branding.
* **Buttons:** Adjust button attributes like background colour, font colour, and visual feedback to seamlessly integrate with the app’s overall aesthetic.
* **Text Size:** Tailor font sizes to enhance readability and support accessibility across devices and screen sizes.

It's important to note that the availability of customisation options may vary depending on the platform. For example, in mobile app development, developers may have the option to modify the accent colour, which is a platform-specific customisation feature.

By leveraging these capabilities, developers can create visually appealing interfaces that enhance usability and cater to diverse user needs. Themes ensure that the app maintains consistency across platforms while accommodating specific design and branding requirements.

Supported clients include:

1. [Android](themes.md#android)
2. [IOS](themes.md#ios)
3. [Web](themes.md#web)
4. [Windows](themes.md#windows)

## **Accessing and Customising Themes in the  ComUnity Developer Toolkit**

To customise the appearance of your app across different client platforms, the Themes feature in the Toolkit provides developers with a convenient interface. Themes allow you to modify attributes and properties of various components, such as tabs, buttons, text size, and label appearance. This guide will walk you through accessing the Themes interface and provide an overview of its layout and functionality.

### **Accessing Themes in the Toolkit**

To access Themes in the Toolkit and begin customising your app's appearance, follow these simple steps:

1. **Login to the ComUnity Developer Toolkit**
2. **Select your Project**: From the dashboard, select the project you wish to manage.
3. Open Project Settings: After opening your project in the Toolkit, click the cog icon labelled Project Settings (displayed with a tooltip reading “Project settings”). For additional details on accessing Project Settings, refer to the [General ](general.md)section.
4.  **Tab View of Supported Clients:** Upon selecting the **Themes** tab, you will be presented with a tab view layout. Each tab represents a supported client platform, such as Android, iOS, Web, and Windows. The tab view allows you to navigate between different clients to customise their specific appearance.\
    \


    <figure><img src="../../.gitbook/assets/image (475).png" alt=""><figcaption></figcaption></figure>

### **Layout and Customisation Options**

Once you've accessed the Themes interface, you will find a user-friendly layout that simplifies the customisation process. Here are some key aspects of the interface:

* **Tab View Menu:** The tab view menu presents each supported client as a separate tab. This enables you to focus on customising the appearance of the app for a specific platform. Simply click on the desired tab to access the corresponding customisation options.
* **Attributes and Properties:** Within each client tab, you will find relevant attributes and properties that can be modified. These options may include colour schemes, font styles, sizes, and other visual settings. All colour attributes are equipped with a built-in colour picker, which supports both selection from a colour palette and manual input of hexadecimal colours.
* **View More Attributes:** In some cases, you may find that the initial view of attributes is condensed to provide a streamlined interface. If you require additional customisation options, you can click on a **More Attributes** option to expand the tab view. This allows you to access and modify a wider range of settings to refine the app's appearance.
* **Save:** Once you have made the desired changes to the attributes and properties, clicking on the Save button will save the modifications. This ensures that your customised settings are applied to the app, reflecting the desired appearance for the selected client platform.

By utilising the intuitive interface of the Themes feature, developers can easily navigate through the supported client tabs, modify the relevant attributes, and create visually appealing and consistent user interfaces for their apps.

In conclusion, accessing and customising Themes in the Toolkit involves navigating to the project settings, selecting the Themes option, and exploring the tab view layout for each supported client platform. With the ability to modify various attributes and properties, including the use of a built-in colour picker, developers can easily customise the appearance of their apps to match branding, enhance usability, and create a personalised user experience.

### **Supported Attributes in Each Client Platform**

In this section, we will provide an overview of the supported settings in the ComUnity Platform that can be customised for each client platform. These settings allow you to modify various aspects of your app's appearance and behaviour to create a unique and engaging user experience that aligns with your brand and audience.&#x20;

During [initial project set up](create-a-project.md), the ComUnity Toolkit provides you with an interface to select primary and accent colours for the colour scheme of your project, which will in turn affect the colours in your theme. However, the document assumes you used the default colour scheme, which consists of primary colour #004080 and accent colour #008000.

### Google Android

**Basic Settings**

When creating a new project, the primary and accent colours can be selected from the dialog. These colours will be used as shown below, with suitable values set for the additional values. These values can be changed as required.

<table><thead><tr><th width="165.33333333333331">Name</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td>Primary</td><td>Set on project creation</td><td>The default colour for the app bar and other primary UI elements</td></tr><tr><td>PrimaryDark</td><td>Primary</td><td>A darker variant of the primary colour, used for the status bar (on Android 5.0+) and contextual app bars</td></tr><tr><td>Accent</td><td>Set on project creation</td><td>A secondary colour for controls like checkboxes and text fields</td></tr><tr><td>Background</td><td>#f6f7f8</td><td>The app background colour</td></tr><tr><td>Text</td><td>#908f9b</td><td>The app text colour</td></tr><tr><td>Deselected</td><td>#d8d9db</td><td>The colour used for disabled controls</td></tr><tr><td>CardBackground</td><td>#ffffff</td><td>The background colour for cards (used in grid lists)</td></tr><tr><td>LinkText</td><td>Primary</td><td>The text colour for links that can be clicked</td></tr><tr><td>ErrorText</td><td>#e96b47</td><td>The text colour for error messages</td></tr><tr><td>InverseText</td><td>#ffffff</td><td>The text colour for dark backgrounds (i.e. text on the App bar)</td></tr></tbody></table>

**More attributes**

The following settings will use the specified default value if not value is set.  The values can be overridden if required.

<table><thead><tr><th width="280">Name</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td>TitleTextSize</td><td>20</td><td>The text size of title text items</td></tr><tr><td>BodyTextSize</td><td>14</td><td>The text size of body text items</td></tr><tr><td>SelectedTextSize</td><td>BodyTextSize</td><td>The text size of selected text items</td></tr><tr><td>DetailedTextSize</td><td>12</td><td>The text size of detailed text items</td></tr><tr><td>LabelTextSize</td><td>10</td><td>The text size of label text items</td></tr><tr><td>TabIndicator</td><td>InverseText</td><td>The colour for the Tab indicator</td></tr><tr><td>TabIndicatorHeight</td><td>4</td><td>The height of the Tab indicator</td></tr><tr><td>TabTextNormal</td><td>InverseText</td><td>The colour for the Tab item text</td></tr><tr><td>TabTextSelected</td><td>InverseText</td><td>The colour for the selected Tab item text</td></tr><tr><td>TabTextNormalAlpha</td><td>180</td><td>The alpha value for Tab item text</td></tr><tr><td>AppBar</td><td>Primary</td><td>The colour for the App Bar</td></tr><tr><td>AppBarText</td><td>InverseText</td><td>The colour for the App Bar text</td></tr><tr><td>UseNavigatorDrawer</td><td>True</td><td>Enables the menu selection (hamburger icon) in the App bar</td></tr><tr><td>UseNavigatorButtons</td><td>True</td><td>Enables the menu bar at the bottom of the screen</td></tr><tr><td>NavigationButtonBackground</td><td>#000000</td><td>Background colour for the bottom menu buttons</td></tr><tr><td>NumNavigationButtons</td><td>5</td><td>The number of menu button to display in the bottom menu bar</td></tr><tr><td>ShowNavigationButtonText</td><td>False</td><td>Show text descriptions on the bottom menu bar buttons</td></tr><tr><td>NavigationButtonNormal</td><td>InverseText</td><td>The colour for the bottom menu bar button icon and text</td></tr><tr><td>NavigationButtonSelect</td><td>Accent</td><td>The colour for the bottom menu bar button icon and text for the selected button</td></tr><tr><td>NavigationButtonTextSize</td><td>DetailedTextSize</td><td>The text size of the descriptions on the bottom menu buttons</td></tr><tr><td>DrawerHeaderBackground</td><td>Primary</td><td>The colour for the drawer header background</td></tr><tr><td>DrawerHeaderText</td><td>InverseText</td><td>The colour for the drawer header text</td></tr><tr><td>DrawerHeaderTextSize</td><td>34</td><td>The size of the drawer header text</td></tr><tr><td>DrawerHeaderHeight</td><td>160</td><td>The height of the drawer header</td></tr><tr><td>DrawerBackground</td><td>Background</td><td>The colour for the drawer background</td></tr><tr><td>DrawerText</td><td>Text</td><td>The colour of the drawer text</td></tr><tr><td>DrawerTextSize</td><td>BodyTextSize</td><td>The text size of the drawer text items</td></tr><tr><td>IconSize</td><td>24</td><td>Sets the app icon size</td></tr><tr><td>CardIconSize</td><td>36</td><td>Sets the icon sizes for lists</td></tr><tr><td>GridIconSize</td><td>48</td><td>Sets the icon sizes for grids</td></tr><tr><td>GridSize</td><td>128</td><td>Sets the size of grid items for a list</td></tr><tr><td>GridElevation</td><td>4</td><td>Sets the elevation of the grid items</td></tr><tr><td>SearchTextSize</td><td>BodyTextSize</td><td>The text size of the search text</td></tr><tr><td>SearchText</td><td>Text</td><td>The colour of the search text</td></tr><tr><td>SearchHintText</td><td>Text</td><td>The colour of the search hint text</td></tr><tr><td>Button</td><td>Primary</td><td>The colour for buttons</td></tr><tr><td>ButtonDisabled</td><td>Text</td><td>The colour for disabled buttons</td></tr><tr><td>ButtonText</td><td>InverseText</td><td>The colour for button text</td></tr><tr><td>ButtonTextSize</td><td>BodyTextSize</td><td>The text size for button text</td></tr><tr><td>LinkButton</td><td>Accent</td><td>The colour for link buttons</td></tr></tbody></table>

#### Additional Resources

* [Android Developer Guide - Themes and Styles](https://developer.android.com/develop/ui/views/theming/themes)\


### iOS

| Name           | Default Value | Description                                                                                           |
| -------------- | ------------- | ----------------------------------------------------------------------------------------------------- |
| Background     | #f6f7f8       | The app background colour                                                                             |
| FormBackground | #ffffff       | The background colour of forms                                                                        |
| Text           | #9008f9b      | The colour of the text                                                                                |
| Accent         | #008000       | The colour of button labels                                                                           |
| Navbar         | #004080       | The background colour of the navigation bar                                                           |
| NavbarAction   | #ffffff       | The colour of the action buttons in the navigation bar                                                |
| TabSelected    | #008000       | The colour of an active tab's text and icons                                                          |
| Tab            | #333333       | The the colour of tab text and icons                                                                  |
| Label          | #004080       | The text colour of form labels                                                                        |
| Error          | #ff0000       | The text colour of error messages                                                                     |
| Link           | #004080       | Colour of links in markdown documents                                                                 |
| SegmentedMenu  | #004080       | Colour of text and icons in segmented menus                                                           |
| StatusbarWhite | checked       | Allows you to toggle the colour of the Status bar at the top of the screen which can be light or dark |
| LabelAllCaps   | checked       | Allows you to capitalise all labels                                                                   |
| LabelFont      | 5             | Allows you to set the font size of labels                                                             |
| ContentFont    | 8             | The font size of content                                                                              |

### WEB

| Name              | Default Value | Description                                                                                |
| ----------------- | ------------- | ------------------------------------------------------------------------------------------ |
| ToolbarBackground | #004080       | Toolbar background                                                                         |
| ToolbarTitle      | #ffffff       | Toolbar text colour                                                                        |
| ToolbarIcon       | #008000       | <mark style="color:orange;">**>>>>>>>Developer Input Requested**</mark>                    |
| InputHighlight    | #004080       | Changes the input (field) lower line to this colour and slightly increases the line width. |
| InputLabel        | #004080       | Label text colour                                                                          |
| TabsBackground    | #efefef       | Background of the colour                                                                   |
| TabsText          | #004080       | Text colour within tabs                                                                    |
| Asside            | #004080       | The text colour of the list items in the list adjacent to the **Asside**                   |
| Avatar            | #004080       | _No longer in use_                                                                         |
| BaseText          | #303030       | Base text colour                                                                           |
| BaseBackground    | #ffffff       | Base page background colour                                                                |

### Windows

| Name             | Default Value | Description                                 |
| ---------------- | ------------- | ------------------------------------------- |
| TitleForeground  | #fffffff      | The colour of the title                     |
| Title Background | #004080       | The background colour of the title          |
| ListForeground   | #494751       | The colour of list items                    |
| ListBackground   | #ffffff       | The background colour of the list           |
| FormLabel        | #008000       | The colour of form labels                   |
| FormError        | #e96b47       | The  colour of form error messages          |
| FormForeground   | #494751       | The colour of the input text of form fields |
| FormBackground   | #ffffff       | The background colour of a form element     |
| MenuForeground   | #495741       | The text colour of the menu items           |
| MenuBackground   | #ffffff       | The background colour of the menu element   |
| PivotSelected    | #ffffff       | The colour of the pivot when selected       |
| PivotUnselected  | #004080       | The colour of the pivot when unselected     |
| PivotBackground  | #004080       | The background colour of the pivot          |
| TileForeground   | #494751       | The text colour of tiles                    |
| TileBackground   | #d8d9db       | The background colour of tiles              |
| TabForeground    | #004080       | The text colour of the tab text             |
| TabBackground    | #ffffff       | The background colour of tab                |
| FormMargin       | 8px           | The margin of the form element              |
| TileMargin       | 4px           | The margin of the tile                      |
| MenuItems        | 5             | Menu items count                            |
| ButtonSize       | 35            | The size of button in width                 |
