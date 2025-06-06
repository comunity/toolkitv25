# Page Development

Page Development in the ComUnity Developer Toolkit allows users to customise and optimise their web pages for a tailored and engaging user experience. By accessing the page settings, users can make adjustments to various elements and configurations. Follow the instructions below to access and modify the page settings for effective page development:\
\
To access the page settings and customise your web page in the ComUnity Toolkit, follow these steps:

1. Select the Pages tab to view a comprehensive list of all existing pages within your Custom Website.
2. Choose the specific page you want to customise, and an array of icons will be displayed.
3. Locate and click the ![](<../../../.gitbook/assets/image (202).png>) icon associated with that page. This action will open a dedicated pop-up screen that exclusively displays the page settings for that particular page.

Within this intuitive pop-up screen, you will find a range of adjustable [page settings](page-development.md#page-settings) at your disposal. These settings include Name, Parent Page Name, Template Name, Role, and Content. Modify these settings according to your specific requirements and preferences, ensuring they align with the desired structure and functionality of your web page.

Once you have made the necessary changes to the page settings, it is essential to click the Save button to apply and save the updated settings. This ensures that your modifications are effectively implemented and preserved, optimising your page development process.

## Page Settings

Page Settings play a pivotal role in configuring and customizing the various aspects of your web pages within the ComUnity Developer Toolkit. By accessing these settings, you can define the essential attributes that shape the behaviour, structure, and content of each page.

Let's explore the details of the individual Page Settings:

### **Name**

This setting displays the name of your page, serving as a unique identifier. Once set, the page name cannot be changed.

### **Parent Page Name**

Use this setting to select a parent page for the current page. The index or home page stands apart from other pages as it does not have a parent page, providing a clear distinction within your Custom Website pages.

### **Template Name**

Choose a template that defines the structure and layout of the current page. Templates ensure consistency across your website and streamline the development process.

### **Role**

Specify the user role that has access to the current page. This allows you to control the visibility and permissions for different users or groups.

### **Content**

The content field allows you to define your page content. Static page content is written using HyperText Markup Language(HTML) and can be linked with external Javascript and Cascading Style Sheet(CSS) whereas [Razor syntax](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-6.0) is used to template dynamic page content.

Any files(**.png**, **.svg**, **.jpeg**, **.js**, **.css**, etc.) that are used in your content should be stored in your **Custom Web** [Resources](resources.md). To reference a resource in your page content use the Relative Uniform Resource Locators(URLs).

```
/Resources/<<Resource name>>
```

\
You can also reference resources which are persisted in the [Media Server ](../../services/media-server.md)in your page content.

<figure><img src="../../../.gitbook/assets/Screenshot 2022-11-16 at 13.20.26.png" alt=""><figcaption></figcaption></figure>

## Creating Hyperlinks within Pages

Relative Uniform Resource Locators(URLs) are used as the value of the **`href`** attribute when creating hyperlinks. By default URL of the index or home page is `/<<Index page name>>` when linking the home page to its child page the value of **`href`** is the relative URL: `/<<Index page name>>/<<Child page name>>` and so on.

## Templating Page Elements

A page may be passed [page elements](page-elements.md#page-tag). To reference a page element in a page use the following syntax:

```
{{= <<Page Tag>>}}
```
