# Organisational Management

> Organisational Management within the Toolkit is a comprehensive feature designed to empower the Organisation Administrator with the tools and capabilities necessary for effective management and oversight of their organisation. This functionality is pivotal in maintaining a structured, efficient, and collaborative environment within the platform.

## **Responsibility and Prerequisites**

The **Organisation Administrator** is the **key individual** responsible for managing their organisation within the Toolkit. They are the first point of contact and register the organisation on the platform.

## **Key Responsibilities**

* **Managing Users:** Granting access, assigning roles, and maintaining user accounts within the organisation.
* **Creating and Managing Teams:** Establishing teams, assigning members, and managing their composition.
* **Project Management:** Overseeing projects, assigning project owners (leaders), and ensuring efficient project execution.
* **Organisational Control:** Having full visibility into all projects, reassigning project ownership as needed, and modifying team structures to optimise collaboration.

**In essence, the Organisation Administrator holds the highest level of authority within the Toolkit, granting them comprehensive control over their organisation's functionality.**

## **Manage Your Organisation**

### **View and Edit Organisation Details**

To access and modify your organisation's details, follow these steps:

{% hint style="info" %}
Organisational Settings can only be accessed by admins due to the role-based access control enforced in the Toolkit. For any other role, these settings are hidden.
{% endhint %}

1. **Log In**: Sign into the Toolkit with your credentials.
2.  **Access Organisation Settings**: From the main menu, navigate to **"Organisation Settings"**.\\

    <figure><img src="../../.gitbook/assets/image (385).png" alt=""><figcaption><p>Organisation Settings</p></figcaption></figure>
3.  **View and Edit Details**: Here, you can view your organisation's information and edit details such as the organisation's name.

    <figure><img src="../../.gitbook/assets/image (386).png" alt=""><figcaption><p>Organisation Details</p></figcaption></figure>

## **Manage Users and Roles**

To manage users and their roles within the organisation, proceed as follows:

1.  **Access Organisational Settings**: Go to the **"Organisation users and roles"** tab within the Organisational Settings.

    <figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>
2.  **View Users:** This section displays all users associated with your organisation. Use the search functionality to find specific users and the view functionality to find users by role.

    <figure><img src="../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>
3.  **Modify User Access**: To remove a user from the organisation, click the three-dot button next to the user's name and confirm the action in the **"Delete Member"** modal.

    <figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>
4.  **Manage User Roles**: To adjust user roles, click the "View Roles" button next to the respective user. Use the (+) button to assign or remove roles. For more information about the supported roles and their permissions, please refer to the [Supported Roles and Permissions](organisational-management.md#supported-user-roles-and-permissions) section.

    <figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>
5.  **Assign/Remove Roles**: Click the plus icon in the Roles assigned to the user, an "**Assign or remove team member roles**" modal will appear\*\*.\*\* In the **"Assign or remove team member roles"** modal, check or uncheck roles to assign or remove them, respectively.\


    <figure><img src="../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>
6. **Apply Changes**: Click **"Apply"** to save your modifications.

## **Supported User Roles and Permissions**

This section outlines the default user roles supported in the Toolkit. The roles manage access to various components and functionalities within the system. Permissions are environment-specific, and access rights range from 1 to 3.

**Default Roles**

* **Lead Developer**
* **Developer**
* **Operations**
* **Viewer**

Each role has specific permissions across the development (DEV), quality assurance (QA), and production (PROD) environments.

#### Access Rights Legend

* **1**: View only
* **3**: Full access (view and edit)

To learn more about environments, please refer to the[ Environments](../manage-your-project/deploy/environments.md) section.

### **Lead Developer**

| Component Name       | Environment | Access Rights |
| -------------------- | ----------- | ------------- |
| Build & Launch       | DEV         | Full (3)      |
| Deploy               | DEV         | Full (3)      |
| Deploy               | QA          | Full (3)      |
| Develop              | DEV         | Full (3)      |
| Download Backup      | DEV         | Full (3)      |
| Environment Settings | DEV         | Full (3)      |
| Environment Settings | PROD        | Full (3)      |
| Environment Settings | QA          | Full (3)      |
| Operate              | PROD        | Full (3)      |
| Operate              | QA          | Full (3)      |
| Project Settings     | DEV         | Full (3)      |
| Project Settings     | PROD        | Full (3)      |
| Project Settings     | QA          | Full (3)      |
| Communications       | DEV         | Full (3)      |
| Custom Classes       | DEV         | Full (3)      |
| Custom Website       | DEV         | Full (3)      |
| Data                 | DEV         | Full (3)      |
| Integrations         | DEV         | Full (3)      |
| Observability        | DEV         | Full (3)      |
| Observability        | PROD        | Full (3)      |
| Observability        | QA          | Full (3)      |
| Screens              | DEV         | Full (3)      |
| Deploy to QA         | DEV         | Full (3)      |
| Deployment history   | DEV         | Full (3)      |
| Deploy to Production | QA          | Full (3)      |
| Deployment history   | QA          | Full (3)      |

### **Developer**

<table><thead><tr><th width="258">Component Name</th><th>Environment</th><th>Access Rights</th></tr></thead><tbody><tr><td>Build &#x26; Launch</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Deploy</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Deploy</td><td>QA</td><td>Full (3)</td></tr><tr><td>Develop</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Download Backup</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Environment Settings</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Environment Settings</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Environment Settings</td><td>QA</td><td>Full (3)</td></tr><tr><td>Operate</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Operate</td><td>QA</td><td>Full (3)</td></tr><tr><td>Project Settings</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Project Settings</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Project Settings</td><td>QA</td><td>Full (3)</td></tr><tr><td>Communications</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Custom Classes</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Custom Website</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Data</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Integrations</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Observability</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Observability</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Observability</td><td>QA</td><td>Full (3)</td></tr><tr><td>Screens</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Deploy to QA</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Deployment history</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Deploy to Production</td><td>QA</td><td>Full (3)</td></tr><tr><td>Deployment history</td><td>QA</td><td>Full (3)</td></tr></tbody></table>

### **Operations**

<table><thead><tr><th width="251">Component Name</th><th>Environment</th><th>Access Rights</th></tr></thead><tbody><tr><td>Environment Settings</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Environment Settings</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Environment Settings</td><td>QA</td><td>Full (3)</td></tr><tr><td>Develop</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Operate</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Operate</td><td>QA</td><td>Full (3)</td></tr><tr><td>Observability</td><td>DEV</td><td>Full (3)</td></tr><tr><td>Observability</td><td>PROD</td><td>Full (3)</td></tr><tr><td>Observability</td><td>QA</td><td>Full (3)</td></tr></tbody></table>

### **Viewer**

| Component Name  | Environment | Access Rights |
| --------------- | ----------- | ------------- |
| Build & Launch  | DEV         | View (1)      |
| Deploy          | DEV         | View (1)      |
| Deploy          | QA          | View (1)      |
| Develop         | DEV         | View (1)      |
| Download Backup | DEV         | View (1)      |
| Operate         | PROD        | View (1)      |
| Operate         | QA          | View (1)      |
| Communications  | DEV         | View (1)      |
| Custom Classes  | DEV         | View (1)      |
| Custom Website  | DEV         | View (1)      |
| Data            | DEV         | View (1)      |
| Integrations    | DEV         | View (1)      |
| Observability   | DEV         | View (1)      |
| Observability   | PROD        | View (1)      |
| Observability   | QA          | View (1)      |
| Screens         | DEV         | View (1)      |

#### Access Rights Legend

* **1**: View only
* **3**: Full access (view and edit)

## Teams

To effectively manage teams in the Organisation refer to[ Teams](teams.md).

## Conclusion

By following these guidelines, the Organisation Administrator can effectively manage the organisation's structure and member roles within the Toolkit, ensuring a streamlined and efficient operational environment.
