# Custom Classes

Custom Classes in the ComUnity Platform serve as a powerful tool for developers to enhance and customise the functionality of their projects, while simultaneously promoting modularity and separation of business logic. They provide a flexible foundation that enables developers to implement specialised behaviours, define unique properties, and introduce custom functionalities that precisely align with their project's requirements.

One notable advantage of Custom Classes is their ability to facilitate the separation of business logic from other components within the project. By encapsulating specific functionalities within these classes, developers can establish a modular code structure, resulting in improved maintainability, readability, and ease of updates. This separation of concerns promotes code reusability and allows for more efficient development and debugging processes.

A custom class within the `<<Project name>>.Custom` namespace is a system-generated class that serves as a framework for developers to incorporate their own custom logic, functionality, or data structures within the ComUnity Platform. This custom class provides developers with the necessary structure and context to seamlessly integrate their project-specific elements into the platform.

Custom Classes are commonly utilised for defining custom helper classes, which offer additional utilities and functionalities that cater to specific tasks within the project. These helper classes extend the capabilities of the ComUnity Platform, enhancing its adaptability to diverse project requirements. Additionally, Custom Classes are also instrumental in implementing [Virtual Entities](broken-reference), allowing developers to create virtual representations of entities within the ComUnity Platform, thereby facilitating efficient data management and manipulation.

By leveraging Custom Classes, developers can take full advantage of the ComUnity Platform's flexibility and customisation capabilities. The modular and separated nature of these classes promotes code organisation, reusability, and maintainability, resulting in more robust and adaptable projects. This empowers developers to tailor the functionality of the ComUnity Platform to their specific project needs, leading to more efficient development processes and ultimately delivering high-quality solutions.

To create a Custom Class, follow these steps:

1.  Open your project in the Toolkit and navigate to the **Custom Classes** section. Here, you will find a list of all existing custom classes in your project.\\

    <figure><img src="../.gitbook/assets/image (281).png" alt=""><figcaption><p>Custom Classes in the Toolkit</p></figcaption></figure>
2. Locate the **(+) Add a class** button and click on it to add a new class.
3.  A modal window titled **Add custom class** will appear on your screen.\\

    <div align="left"><figure><img src="../.gitbook/assets/image (200).png" alt="" width="375"><figcaption></figcaption></figure></div>
4. In the modal window, provide a unique name for your custom class in the designated **Class Name** box. Choose a unique name that accurately reflects the purpose or functionality of your class.
5. Finally, click **Add** to create the custom class.

After creating the custom class, it will be displayed on your screen. When you click on the newly created class, the in-app code editor will appear, presenting you with the boilerplate code for the class definition. This code provides a starting point for you to add your custom class definition and tailor it to your project's requirements.

{% code lineNumbers="true" %}
```csharp
// Boilerplate code for a custom class
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
        
namespace <<<ProjectName>>>.Custom
{
    public class <<<Custom Class>>>
    {
    }
}

```
{% endcode %}

For a more extensive modification workflow, it is recommended to download the project to your local development environment. By doing so, you can leverage your preferred code editor and its features to make changes to the class definition. After making the desired modifications, you can copy and paste the updated class definition back into the in-app code editor, to learn more view Debugging and editing your application code.

To learn more about setting up your local ComUnity Project development environment, you can refer to the relevant documentation or resources available. These resources will provide detailed instructions and guidance on configuring your local environment to effectively work with the ComUnity Project.

Once you have made the necessary modifications to your custom class, ensure to build your project. Building the project incorporates the changes made to the custom class, along with any other modifications, into the project's codebase.

In addition to creating custom classes, you also have the option to delete a class if needed. Simply select the class you wish to delete and click on the trash can icon adjacent to the class name. This action will remove the class from your project, allowing for easy management and organisation of your custom classes.

By following these steps, you can effectively create, modify, and delete custom classes in the ComUnity Toolkit, providing you with the flexibility and control to tailor your project's functionality to your specific needs.
