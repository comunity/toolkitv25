# Configuration

> Configuration serves as a centralised configuration management system within the ComUnity Platform, designed to streamline the management of settings across different deployment environments—Development, QA/Testing, and Production. Its primary function is to provide an overview and control mechanism for the settings within each project's environment, enhancing consistency and simplifying the management process.

## **Key Features**

* **Centralised Overview**: Configuration offers a unified view of your project's settings across all environments, enabling easy monitoring and adjustments without the need to access each environment separately.
* **Environment-Specific Configuration**: It allows for the distinction and management of environment-specific settings, ensuring that configurations are appropriate and tailored for each stage of the deployment process.
* **Simplified Management**: By centralising configuration settings this reduces the complexity of managing multiple environments, enabling you to change settings from one central location.
* **Cross-Environment Visibility**: Gain insights into how settings are configured across Development, QA, and Production environments, facilitating a better understanding and quicker identification of configuration discrepancies.
* **Enhanced Security with Key Vault Integration**: Configuration allows for the secure storage of sensitive settings, such as passwords and API keys, by integrating with [Azure's Key Vault](https://azure.microsoft.com/en-us/products/key-vault). This feature provides additional security for stored settings, ensuring they are encrypted and safely managed. Users can easily toggle the storage location of specific settings to the Key Vault, adding an extra layer of protection.

Configuration is an integral tool for maintaining the integrity and consistency of your project's configuration, ensuring that each environment is optimally set up for its intended purpose. Whether you're diagnosing an issue or implementing new features, Configuration provides the necessary infrastructure to manage your configurations efficiently and effectively.

## Manage settings on Configuration

Configuration simplifies the management of your project's settings, offering a user-friendly interface where you can edit, secure, or remove configuration details efficiently. This centralised approach not only enhances the manageability of your configurations but also promotes consistency across different environments.\
\
To manage Configuration settings in your project, follow these steps:

1. **Login to the ComUnity Developer Toolkit**
2. **Select your Project**: From the dashboard, select the project you wish to manage.
3. Open Project Settings: After opening your project in the Toolkit, click the cog icon labelled Project Settings (displayed with a tooltip reading “Project settings”). For additional details on accessing Project Settings, refer to the [General ](../general.md)section.
4. **Access Environment Settings:** In the _Project Settings_ panel, navigate to the top section where environment tabs are displayed. You will see options for Global, Development environment, QA environment, and Production environment. Click on the relevant environment tab to access its specific settings. Selecting an environment allows you to configure its deployment-related settings, ensuring the appropriate configuration for testing, staging, or live production use.
5.  **Manage Configuration Settings**: After selecting an environment, navigate to the Configuration tab to manage environment-specific settings. You will see a list of existing default configuration settings displayed in a table format.\


    * **Toggle Visibility**:
      * **Use the shield icon to toggle the visibility of each setting**, making it public or private according to your project's requirements.
      * Click the shield icon to toggle the visibility of a configuration setting:
        * Private values are securely stored in Azure Key Vault, ensuring they remain encrypted and protected.
        * &#x20;Public values remain visible within the configuration settings panel.\

    * **Use the Same Value for All Environments**: To apply the same value across all environments (Development, QA, and Production), toggle the “Apply globally” capsule-style switch:
      * Enabled: The value is used across all environments.
      * &#x20;Disabled: You can specify different values for each environment.\

    * **Delete a settings**: To remove a configuration setting:
      * Hover over the setting row – a trash can icon will appear on the right.
      * Click the trash can icon associated with that specific setting.
      * Confirm the deletion when prompted.

    <figure><img src="../../../.gitbook/assets/image (442).png" alt=""><figcaption></figcaption></figure>

Once you've created configuration settings, you can refer to them throughout your application. These settings are stored within the Config service and can be accessed and utilised in various parts of your application's code.

```csharp
// To invoke an application setting in your code:
Config.{{Application Setting}}
// A real life example referencing FaultEmail application setting
Config.FaultEmail()
```

Below is a list of common system-generated configuration variables that you'll typically encounter when working with new projects in the ComUnity Platform's Development deployment environment:

1. AppName: The AppName variable represents the name or title of your application. It serves as an identifier within the ComUnity Platform, helping to distinguish your application from others during the development phase.
2. BaseUrl: The BaseUrl variable specifies the base URL or web address of your application. It defines the starting point for all relative URLs within your application and is essential for proper routing and navigation during development.
3. ComsApi: The ComsApi variable refers to the API endpoint or URL of the communication service within the ComUnity Platform. It enables your application to interact with the communication service, facilitating the exchange of messages, notifications, and other communication-related tasks during development.
4. ComsService: The ComsService variable is a URL that represents the specific communication service employed within the application.
5. ComsServicePassword: The ComsServicePassword variable stores the password or secret key associated with the communication service in the Development environment. It is instrumental in authenticating and securely accessing the service.
6. ComsServiceUsername: The ComsServiceUsername variable stores the username or identifier used for authentication and identification within the communication service during development. It allows your application to connect and interact with the service using the designated user or account within the Development environment.
7. MediaServerUploadUrl: The MediaServerUploadUrl variable denotes the URL or endpoint of the media server responsible for uploading and storing media files within the ComUnity Platform's Development environment. It enables your application to seamlessly upload images, videos, or other media content for use within the platform during development.
8. PublishedAppName: The PublishedAppName variable represents the name of your application as it appears to end users or the public within the Development environment. It is commonly utilised for displaying the application name in user interfaces or when referencing the published version of your application during development.
9. WelcomeMessage: The WelcomeMessage variable contains a pre-defined message or greeting displayed to users when they initially interact with your application in the Development environment. It serves as a friendly introduction or provides essential instructions to guide users through their initial experience during development.
