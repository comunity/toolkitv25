---
description: Introducing screens and providing instructions for effective screen management
---

# Building Screens

## Overview

Screens are a fundamental feature within the ComUnity Toolkit, enabling developers to design and manage navigation and content structure efficiently. This feature uses a hierarchical structure, offering an intuitive approach to organising, navigating, and presenting information to users.

In this hierarchy, the top-level screens act as the primary elements that define your application’s main menu. These screens form the foundation of your app’s navigation. In the Screen View, you can expand these top-level screens if they contain nested child screens. When the project is built during development, the underlying Toolkit processes will render a web app where these top-level screens appear in a sidebar as part of the main menu. Depending on the environment (such as production or QA), the same application can be built for mobile or desktop platforms, with the navigation structure adapted accordingly. The visibility and accessibility of these screens in the menu depend on the Role-Based Access (RBA) configurations set for different user roles. This ensures that users only see the screens they have permission to access, based on their role within the application.

## Hierarchical Structure and Node Types

The ComUnity Toolkit utilises a recursive hierarchical structure, where each screen is represented as a node within the hierarchy. The root node represents the top-level screen, and it can have child nodes, which are either **Lists** or **Pages**. These nodes form the building blocks of your app’s navigation and content structure:

• **List**: A List serves as a container node that can hold Pages, other Lists, and relevant Screen Controls. It is versatile and can be used to implement complex navigation structures. Lists can also present data in various formats, such as grids and tabs, and link to sub-screens, providing flexibility in how information is displayed.

**• Page:** Pages are also container nodes that can include child nodes like other Pages or Lists. They are essential for implementing CRUD operations, form handling, and dynamic lists. Pages form the interactive components of your application, allowing users to engage with the app’s functionality.

When you select a node within your screen hierarchy, the associated Screen Controls and relevant properties become visible and accessible. This feature enables you to manage and customise the selected item’s behaviour, appearance, and functionality according to your specific requirements.

## System Screens and Additional Screens

In addition to the hierarchical structure, there are two types of screens that fall outside the hierarchy:

1\. **System Screens**: These screens are predefined within the system and serve specific, often administrative or functional roles. Commonly used to manage authentication within the solution, these screens are critical and should not be deleted. They are not part of the hierarchical structure but are essential for managing the core functionality of the application.

2\. **Additional Screens**: These screens are custom screens that do not conform to the hierarchical structure of the app. They can either be built by users or shipped as part of a starter sample. Additional Screens are typically Form Pages that handle tasks like data entry or processing user input. These screens can only be linked to Form Pages and act as leaf nodes in the hierarchy, terminating a branch since they do not support child nodes. However, developers can link one Form Page to another using Additional Screens, ensuring the flow between Form Pages without disrupting the main hierarchy.

## Managing Screens

When building your application's navigation in the ComUnity Toolkit, it’s essential to approach it as a hierarchical structure. This approach enables effective organisation and structuring of your navigation system.

1. **Top-Level Screens as the Main Menu**: The top-level screens form the main menu of your application, serving as the primary interface for users to access different sections or functionalities. Designing a clear and logically organised main menu is key to providing an intuitive user navigation experience.
2. **Creating Parent and Child Screens**: The ComUnity Toolkit allows you to create parent and child screens, establishing a hierarchical relationship between them. By leveraging these relationships and the drag-and-drop functionality, you can create a well-organised and intuitive navigation system for your users.
3. **Creating Additional Screens:**  Additional Screens in the ComUnity Toolkit provide a way to extend your application's functionality without adhering to the hierarchical structure of parent and child screens. These screens are exclusively[ Form ](form/)pages and can be linked directly to other screens via a relative path. By creating Additional Screens, you can handle specific tasks or input forms that are not part of the main navigation hierarchy but are crucial for specific user interactions. This method allows for greater flexibility in integrating essential forms into your app's workflow, ensuring that user interactions are seamless and efficient. For detailed instructions, refer to the dedicated section on [Creating Functional Links to Additional Screens with Single Item - List Item](form/lists-in-form-pages/single-item-list-item-properties-and-practical-uses.md#creating-functional-links-to-additional-screens-with-single-item-list-item).

### Configuring Top-Level Screens in Your Application

Building a well-organised and user-friendly navigation system is fundamental to delivering an exceptional user experience in your application. One crucial aspect of navigation design is creating top-level pages that serve as primary entry points to different sections or functionalities. In this section, we will guide you through the process of creating a top-level page in your application using the ComUnity Toolkit.

To create a top-level page, follow these steps:

1. Open your project in the ComUnity Toolkit and select the **Screens** tab on the sidebar.
2. In the **Screen View** under the **Screens** tab, click on the **Screen** you wish to set as a top-level page.
3. Next, click on the ellipsis icon next to the selected **Screen**.
4. A modal will appear, providing options for configuring the **Screen** as a top-level page (screenshot shown below).\
   ![](<../../../.gitbook/assets/image (171).png>)![](<../../../.gitbook/assets/image (172).png>)\

5. In the modal window, click the **Add screen above** tab to insert a new navigation directly above the active page. Alternatively, click the **Add screen below** tab to insert a new navigation directly below the active screen.
6.  An **Add a new screen** modal window (see screenshot below) will appear. In the **Title** box, enter a unique title for the screen.\


    <div align="left"><figure><img src="../../../.gitbook/assets/image (182).png" alt="" width="375"><figcaption></figcaption></figure></div>
7. Select a  type from the options available. The supported Screen types in the ComUnity Toolkit are [Navigation](navigation/) and [Form](form/) pages.
8. Click **Add a screen** to create the new Screen with the specified title and type.

Congratulations on successfully creating your new top-level screen and establishing it as a fundamental component of your project's navigation!

To further enhance your Screens and tailor them to your project's specific needs, we encourage you to explore the detailed content available on [Navigation](navigation/) and [Form](form/) pages. These resources offer valuable insights, technical guidance, and best practices for building screens based on their respective types.

### Building Links Between Screens

In the ComUnity Toolkit, screens are linked by either adding sub-screens to existing pages or pointing to pages outside the hierarchy. This creates the navigation paths users follow to move between screens in the app.

Using screen controls, you can configure links to both hierarchical and non-hierarchical pages, enabling structured and efficient navigation.

**Key Points to Consider:**

1. [**Page Links:**](navigation/page-link.md)\
   Page Links provide a mechanism that allows users to navigate from Navigation pages to Form pages within the your project. A Page Link should be configured to point to a new or existing Form page for it to work. Properties such as Layout Type, Icon, Role Name, and Target URL can be adjusted to define how the linked page is displayed and accessed.
2. &#x20;**Lists for Adding Sub-Screens:**\
   Lists can add sub-screens to both Navigation pages and Form pages, whether dynamic or static. This allows additional screens to be linked within the app, improving navigation. Refer to the sections on [Adding Sub-Screens to Navigation pages Using Lists](navigation/lists-in-navigation-pages/implementing-sub-screens-in-navigation-pages-using-list-items.md) and [Lists in Form pages](form/lists-in-form-pages/).

### Data Entry Screens

The central focus when utilising **Data Entry Screens** within the ComUnity Toolkit is to significantly expedite the process of generating multiple screens, eliminating the need for individual construction. This feature introduces a time-saving mechanism by automating the creation of screens that showcase data linked to specific entities. These screens also incorporate dedicated screens for the inclusion and modification of records.

The **Data Entry Screens** encompass three distinct screens, each serving a pivotal role within the data management workflow:

**Top-Level Screen (View Records in List View):** The Top-Level Screen provides a comprehensive list view of records, enabling users to navigate through the records effortlessly. Each list item functions as a clickable link, directing users to detailed information about individual records. Additionally, this screen offers a link to conveniently access the Add Record Screen.

**Edit Record Screen:** Users can seamlessly transition to the Edit Record Screen by selecting a specific record from the list view. This specialised interface facilitates precise modification and updating of selected record data. The detailed form within this interface mirrors the attributes of the record, equipping users with interactive elements such as input fields, dropdown menus, and checkboxes. These elements enable thorough editing based on specific requirements.

**Add Record Screen:** Accessible exclusively from the Top-Level Screen, the Add Record Screen provides an intuitive form for creating new records. This user-friendly form guides users through the process of inputting necessary data for the creation of new records.

The ComUnity Toolkit seamlessly integrates **Data Entry Screens** with a straightforward click, while allowing room for further customisation. Developers possess the ability to align these screens precisely with the unique requirements of their applications. This level of customisation empowers developers to seamlessly integrate and refine Data Entry Screens, fostering a unified and responsive application interface.

The utilisation of **Data Entry Screens** is not only a means of accelerating development, but also a pathway to optimising the user experience and functionality of the application.

To create **Data Entry Screens**, follow these steps:

1. Open your project in the ComUnity Toolkit, select the Screens tab on the sidebar.
2. In the Screen View, you will find a list of all Screens available in your application navigation.
3. In the **Screen View** under the **Screens** tab, click to select the target **Screen** where you intend to position the top-level screen for your **Data Entry Screens** – this can be either above or below the selected Screen.
4. Next, click on the ellipsis icon next to the selected **Screen**.
5. A modal will appear, providing options for configuring the **Screen** as a top-level page (screenshot shown below).\
   ![](<../../../.gitbook/assets/image (178).png>)![](<../../../.gitbook/assets/image (179).png>)
6.  Select one of the following relevant options: **Add data entry screens above** or **Add data entry screens below**. This will prompt the **Add data entry screens** modal to appear (screenshot below).\


    <div align="left"><figure><img src="../../../.gitbook/assets/image (170).png" alt="" width="375"><figcaption></figcaption></figure></div>
7. Inside the **Add data entry screens** modal, you'll find an Entity dropdown. Carefully select the desired entity for which you wish to establish Data Entry Screens.
8. Finally, click the **Add Screens** button. This action will seamlessly integrate your **Data Entry Screens** for the chosen entity.

In conclusion, upon the successful generating of your Data Entry Screens, a top-level screen named in accordance with the specified entity will seamlessly integrate into the designated position, accompanied by the remaining screens nested within. This strategic arrangement allows for effortless access and management. Moving forward, feel free to tailor these screens to align precisely with your preferences, following the familiar process of customising standard screens view  [Form pages](form/) and [Navigation pages](navigation/), for more details.

<figure><img src="../../../.gitbook/assets/image (169).png" alt=""><figcaption><p>The diagram shows an expanded view of three Data Entry Screens automatically generated in the Toolkit from the Fault entity</p></figcaption></figure>

### View Screens

The navigation of your application is organised as a hierarchical tree structure of pages. To navigate through the tree and explore the different levels of your navigation system, follow these steps:

1. Expand a Screen: If a Screen has children, you will see a (+) icon next to it. Click the (+) icon to expand the navigation, revealing its child screens and sub-levels.
2. Collapse a Screen: To simplify the view and collapse a Screen and its child screens, click the (-) icon next to the expanded navigation.

By utilising these expand and collapse icons, you can easily navigate through the hierarchical structure of your application's navigation, allowing for a clear understanding of the relationships and organisation of the different navigation nodes.

### Delete a Screen

In the ComUnity Toolkit, the Delete a Page feature provides a straightforward method to efficiently remove unnecessary or outdated pages from your application. This powerful tool streamlines the page management process, allowing you to maintain a clean and organised project.

To delete a **Screen** and its children, follow these steps:

1. Open your project in the ComUnity Toolkit and select the Screens tab on the sidebar.
2. In the **Screen View** under the **Screens** tab, locate and click on the **Screen** you wish to delete.
3. Click on the ellipsis icon next to the selected **Screen**.
4.  A modal will appear, providing an option to delete a screen and its children (screenshot shown below):\


    <div align="left"><figure><img src="../../../.gitbook/assets/image (183).png" alt="" width="232"><figcaption></figcaption></figure></div>
5.  Within the modal window, click **Delete screen and children**. This action will trigger a "Delete screen" modal (screenshot shown below):\


    <div align="left"><figure><img src="../../../.gitbook/assets/image (184).png" alt="" width="375"><figcaption><p>Delete screen modal</p></figcaption></figure></div>
6. Finally, click the **Delete** button in the modal to confirm the deletion of the child screen and its descendants.

This straightforward process allows you to efficiently remove both the child screen and any associated sub-screens, ensuring your application's hierarchy remains well-organised.

### Copy form page

The **Copy form page** function serves as a convenient utility, enabling the swift generation of Form pages by duplicating existing ones. This feature proves particularly valuable when expediting the process of crafting form-based interfaces. By leveraging this functionality, developers can efficiently replicate the structure and design of pre-existing pages, expediting the creation of new form pages with consistent styling and elements.\
\
![](<../../../.gitbook/assets/image (311).png>)
