# Icon Management

Icons are essential UI elements that visually represent functions, features, and commands in applications. In the ComUnity Developer Toolkit, the Icon Management feature allows developers to browse system icons, upload custom icons, and organise them for easy retrieval and implementation.

The Toolkit includes a suite of universally recognised icon libraries,  [Bootstrap Icons](https://icons.getbootstrap.com/), [Font Awesome 6](https://fontawesome.com/), [Devicon](https://devicon.dev/), and [Material Design](https://m3.material.io/), along with a specialised Weather Icons collection. It also maintains backward compatibility with Legacy icons, ensuring a smooth transition for existing projects.

Developers can also upload custom icons, allowing them to integrate unique branding elements and design icons tailored to their application’s needs.

This guide covers how to browse, add, and use icons in your projects.

## **Browse Icons**

To browse system and custom icon libraries in an existing project in the Toolkit, follow these steps:

1. **Login to the ComUnity Developer Toolkit**
2. **Select your Project**: From the dashboard, select the project you wish to manage.
3. Open Project Settings: After opening your project in the Toolkit, click the cog icon labelled Project Settings (displayed with a tooltip reading “Project settings”). For additional details on accessing Project Settings, refer to the [General ](general.md)section.
4.  **Tab View of Supported Icon Libraries:** The Icons tab displays a tile view of supported icon libraries, including [Bootstrap Icons](https://icons.getbootstrap.com/), [Font Awesome 6](https://fontawesome.com/), [Devicon](https://devicon.dev/)  and others.

    You can also access Legacy icons from previous Toolkit versions.



    <figure><img src="../../.gitbook/assets/image (477).png" alt=""><figcaption><p>Icons</p></figcaption></figure>
5. Click **Details** to view system icons in the corresponding library.

## **Adding a Custom Icon Library**

Enrich the visual vocabulary of your applications by adding custom icons to the Toolkit. This section details the process for uploading and managing your custom icons within the Toolkit, ensuring they are optimised for performance and scalability.

To add a icon/icon library to an existing project in the Toolkit, follow these steps:

{% hint style="info" %}
Users are responsible for ensuring that they have the correct licensing to use the icons they intend to upload.
{% endhint %}

1. Go to **Project Settings** > **Icons**.
2. All system icon libraries will appear as tiles, including the **Add Icon** tile view the [Browse Icons](icon-management.md#browse-icons) section above.
3.  Click the **Add Icon** tile to navigate to the **Add a Custom Icon Library** screen:\


    <figure><img src="../../.gitbook/assets/image (320).png" alt=""><figcaption></figcaption></figure>
4.  Click the **Add SVG files** button to upload your icon files from your local machine in the screen showed below:\


    When adding a custom icon library, you can upload individual SVG files or a ZIP file containing SVG files. The upload function will recursively search the ZIP file structure for all SVG files and ignore any files with duplicate names.

    <figure><img src="../../.gitbook/assets/image (330).png" alt=""><figcaption></figcaption></figure>
5. In the screen that appears, specify the following details for your icon or icon library:
   * **Icon library name:** Enter a name for your icon library.
   * **Style:** When incorporating a library, the default Style is set to **regular**. However, you have the flexibility to customise this. To select a different style, simply use the dropdown menu provided. If your needs extend beyond the available options and you wish to define a unique style, you can easily do so by entering a new name in the designated field.
   * **Drag and drop SVG files:** Drag and drop the SVG files for your icon or icon library from your local machine.
6. After adding your icon files, you can preview and categorise your icons.
7. Check the box next to **I have an active license that gives me permission to use these icons**.
8. Finally click the **Add icon library** button.

## Manage Custom Icon Libraries

This section delves into the comprehensive management of custom icon libraries within the Toolkit. Developers can effortlessly add, categorise, and tag their own icon sets, ensuring effortless retrieval and organisation. Moreover, it provides the ability to preview icons to verify their alignment with design goals and enables downloading for seamless integration into applications. By harnessing these functionalities, developers can craft a unified and personalized visual language across their projects, ensuring that each icon not only fulfills a functional purpose but also harmoniously contributes to the overall aesthetic and user experience.

<figure><img src="../../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### **Categorising and Tagging Icons**

<figure><img src="../../.gitbook/assets/image (149).png" alt=""><figcaption><p>Categorising and Tagging Icons</p></figcaption></figure>

Effectively organising and tagging your icon sets is essential for effortless retrieval and seamless integration into your projects. This section provides comprehensive instructions on categorising and tagging your icons within the library, empowering you to enhance icon manageability and streamline your design workflow.

#### Selecting Icon

1. Go to **Project Settings** > **Icons**.
2. All system icon libraries will appear as tiles view the [Browse Icons](icon-management.md#browse-icons) section above for more details.
3. To select a custom icon library, click the **Details** button located within the corresponding tile. This action will display all icons contained within that specific library on your screen.
4. &#x20;Once you've located the desired icon, simply click on it to select it. The selected icon's properties will be displayed on the right-hand side of the screen for further customisation.

#### **Adding a Tag**

1. To tag an icon, click the (+) icon located next to the tag section.
2. Enter the desired tag name in the field that appears.
3. Confirm and save your tag by clicking the checkmark icon.
4. You can click the (x) mark to remove a tag

#### **Adding a Category**

1. For categorisation, click the (+) icon adjacent to the category section.
2. Choose a suitable category from the provided dropdown menu.
3. Finalise your selection by clicking the checkmark icon  to save the category.
4. You can click the (x) mark to remove a category.

By following these straightforward steps, you can efficiently categorise and tag your icons, significantly enhancing the organisation of your library. This process not only streamlines the retrieval of icons but also facilitates their implementation into various aspects of your project, promoting a more efficient and streamlined design workflow.

### **Previewing Icons**

After selecting a Custom Icon Library and clicking the **Details** button, you will be presented with a comprehensive view of all icons contained within that specific library. This allows you to preview each icon in detail, ensuring it aligns with your design vision and project requirements. To preview an icon, simply click on it. The selected icon will be displayed in a larger format, providing a clear view of its details and ensuring it seamlessly integrates with your project's aesthetic and functionality.

### **Downloading Icon Sets**

Once you've identified the target icon for your project, you can effortlessly download it for immediate use. To download an icon, simply click the **Download** button located in the Preview. The selected icon will be downloaded in the appropriate format.

### **Expanding Your Icon Collection: Adding Icons to Custom Icon Sets**

As your design needs evolve, you may find that your existing custom icon sets require additional icons to fully support your project's visual language. The Toolkit's intuitive interface makes it easy to seamlessly add new icons to your existing custom icon sets, ensuring that you have the right icons at your fingertips to bring your design vision to life.

To add icons to a custom icon set, follow these steps:

1. &#x20;Navigate to **Project Settings > Icons** and locate the desired custom icon library.
2. Once you've identified the target library, click the **Details** button located within the corresponding tile. This action will display all icons contained within that specific library on your screen - icon gallery
3. Click the **Manage** tab located this action will display the Add a Custom Icon Library view, for instructions how to add icons view [Adding a Custom Icon Library](icon-management.md#adding-a-custom-icon-library).

## **Implementing Icons in Your Application**

Icons serve as visual cues that empower users to effortlessly navigate and interact with various interface elements. Within the Toolkit, icons seamlessly integrate with a range of list components, elevating both aesthetic appeal and functional effectiveness. This guide delves into the process of implementing icons in diverse [List](../../toolkit-guides/screens/building-screens/screen-controls.md#list) implementations.

Implementing icons into your [List](../../toolkit-guides/screens/building-screens/screen-controls.md#list) is a straightforward process:

1. Locate the list or main menu Item where you wish to implement the icon.&#x20;
2.  Upon selection, an Icon setting option will appear in your Property Settings, granting access to the icon configuration tools.\


    <figure><img src="../../.gitbook/assets/image (325).png" alt=""><figcaption></figcaption></figure>
3.  Click on the (+) icon to reveal the icon editor, a dedicated space for selecting and customising your icons.\


    <figure><img src="../../.gitbook/assets/image (322).png" alt=""><figcaption></figcaption></figure>
4. Choose the desired icon library. The Toolkit selects Bootstrap icons by default, if Bootstrap does not align with your requirements, explore alternative libraries provided within the Toolkit.
5. Browse the selected library and locate the icon that best suits your needs.
6. Once you've selected your icon, click **Use Icon** to apply your changes.
7. Finally click **Save** to persist your changes, the chosen icon will now be integrated into your list, enhancing the user interface.
