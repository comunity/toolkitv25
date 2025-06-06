# Setting Up Role-Based Permissions for Entities: Access Control Configuration

In the ComUnity Developer Toolkit, managing user-based permissions and access control is made possible through a powerful feature called Table Security. This feature provides a comprehensive interface that allows you to define and configure role-based permissions for your entities.

With Table Security, you have full control over granting or restricting access to specific operations, such as reading, updating, or deleting data, based on different roles within your project. The interface presents a list of available roles, providing you with the flexibility to enable or disable permissions for each role as needed.

<figure><img src="../../.gitbook/assets/image (287).png" alt=""><figcaption><p>The diagram above shows the default Table Security settng for the UserProfile entity</p></figcaption></figure>

To configure role-based permissions for your entities using Table Security, follow these steps:

1. Select the entity for which you want to configure permissions. In a Diagram view, click on the entity's header section with a grey background colour. An active entity is identified by a blue border, and none of its entity fields are active (active entity fields have a blue background colour). This action will open a properties dialog that displays the entity's global properties.
2. Within the properties dialog, locate and click on the **Edit Table Security** option.
3. A modal window titled **Table Security for <\<EntityName>>** will appear, presenting you with an interface to configure role-based permissions.
4. In the interface, you will find a list of roles defined in your project, along with the supported permissions.
5. Use the toggle functionality provided to enable or disable specific permissions for each role. For instance, you can allow the "Read" permission for one role while disabling it for another.
6. Repeat this process for other permissions, such as "Update," "Delete," and any other permissions you need to configure.
7. Finally, click the **Save** button to persist your changes.

<figure><img src="../../.gitbook/assets/image (265).png" alt=""><figcaption><p>An active entity in a Diagram view, showcasing its properties dialogue</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (243).png" alt=""><figcaption><p>An active entity in a List view, showcasing its properties dialogue.</p></figcaption></figure>

By following these steps and utilising the intuitive Table Security interface, you can easily configure role-based permissions for your entities. This allows you to control and manage access to your data based on the specific roles defined in your project. Enhance the security and privacy of your application by granting or restricting permissions to authorised users or roles as required.
