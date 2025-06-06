# Azure Function Apps

> The Azure Function Apps integration allows teams to extend their Toolkit applications by incorporating event-driven, serverless functions. This integration offers an easy way to introduce custom logic, automate workflows, and connect external services without the need for complex infrastructure management. Designed for flexibility and scalability, this feature empowers teams to enhance their applications with minimal effort.

**Key Features:**

* **Event-Driven Logic:** Implement functions that automatically execute in response to specific triggers, such as data changes, scheduled jobs, or external events. This capability allows you to integrate dynamic functionality without worrying about manual execution or monitoring.
* **Automated Management:** Once integrated, the Toolkit handles the deployment, scaling, and monitoring of your Azure Function Apps. You don’t need to manually manage the Azure infrastructure—focus on your app’s functionality while the platform ensures smooth operations.
* **Custom Workflows:** Create and manage workflows directly within your Toolkit applications. Whether automating routine tasks or processing complex data flows, the platform seamlessly integrates with Azure Function Apps, providing the flexibility to handle diverse requirements.
* **Scalable Architecture:** The platform automatically leverages Azure’s auto-scaling features to maintain optimal performance under varying workloads. Your applications can handle spikes in demand without requiring manual intervention or additional configurations.

For further details on setting up and configuring Azure Function Apps within the Toolkit, refer to the official [Azure Functions documentation](https://learn.microsoft.com/en-us/azure/azure-functions/).

### Azure Function Apps Integration <a href="#observability-integration" id="observability-integration"></a>

Function Apps in the Toolkit are controlled through role-based access (RBA), allowing only authorised roles to create, manage, or deploy functions. Users without the required permissions will be restricted from accessing these features. As with all primary features in the Toolkit, Function Apps require activation in each environment to match the specific deployment contexts of your project.

Before integrating your function app, ensure that it is properly built and prepared for upload. This includes following the appropriate steps to package the function app according to the Azure specification. For more details, refer to the [Preparing Your Function App for Upload](azure-function-apps-integration.md#preparing-your-function-app-for-upload) section.

1. **Log In**: Access the Toolkit by entering your credentials.
2. **Open Your Project**: Locate and select your project within the Toolkit.
3.  **Navigate to Azure function apps**: From the main menu, find and click on " **Azure function apps**". You will be presented with instructions for setting up and managing Function Apps in your project environment. If any function apps already exist, you will see them listed on this screen. For each function app, essential details are displayed, including the function app's name, its URL, and its current status.

    **Viewing Details and Status**

    Each function app listed on this screen displays its name, associated URL, and current status, such as "Active Function App." You can click **View Details** to expand and see more information about the selected function app.\\

    <figure><img src="../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>
4.  Click **"Create a Function App"** to open the **Create an Azure Function App** modal. In the modal, enter the name of your function app in the **Name** field, select the appropriate runtime from the **Runtime Stack** field, and then choose the version from the **Version** field.\\

    <figure><img src="../../.gitbook/assets/image (428).png" alt=""><figcaption><p>Create an Azure Function App</p></figcaption></figure>
5. Click **"Create Function App"** to trigger the background process. Once complete, your newly created function app will appear on the Azure Function Apps screen.
6.  Next, click the **three-dot button (⋮)** next to the function app you created in the previous step, then select **View Details** from the dropdown menu. This will expand the function app to show further details. From here, choose **Edit Function App Details** to upload a `.zip` file containing your Azure Function App application package. Refer to the [Preparing Your Function App for Upload](azure-function-apps-integration.md#preparing-your-function-app-for-upload) section for additional guidance.\\

    <figure><img src="../../.gitbook/assets/image (429).png" alt=""><figcaption></figcaption></figure>
7. Click **"Publish Changes"** to deploy your function app.

{% hint style="info" %}
The **URL** property displayed on the Azure Function Apps screen specifies the server URL for your function app.
{% endhint %}

## Preparing Your Function App for Upload

To ensure your function app is ready for deployment, follow the [Azure specification](https://learn.microsoft.com/en-us/azure/azure-functions/) suitable for your runtime, paying special attention to the following:

1. **Include Only Essential Application Files:** Ensure that your package contains the core function code and necessary configuration files.
2. **Exclude Unnecessary Files and Dependencies:** Avoid packaging large directories like dependency folders or other artifacts, as the deployment process will handle dependencies automatically.
3. **Keep the Package Lightweight:** Focus on including only essential files to reduce upload times and minimise potential deployment issues.

After following these steps, compress the folder into a `.zip` file for upload into the Toolkit.

## Manage Function Apps

To manage your function app, click the three-dot button (**⋮**) next to the function app's name. This will open a menu with the following options:

<figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption><p>Manage function apps menu options</p></figcaption></figure>

* **Edit Function App Details:** Modify the function app's settings, including uploading a new `.zip` file containing your Azure Function App application package. This option is essential for updating the function app or applying changes to its core functionality.
*   **Edit Function App Settings:** Configure environmental variables that will be injected into the function app’s runtime on Azure. This is crucial for setting up the app’s environment-specific configurations, ensuring that it runs correctly within different deployment contexts.For more details on managing your project's settings across all environments, refer to the [Configuration](../../getting-started/manage-your-project/deploy/configuration.md) section. To align your setup with Azure’s best practices, and for additional guidance on configuring environmental variables, refer to the official [Azure Functions documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-dotnet-class-library?tabs=v4%2Ccmd#environment-variables).\\

    <figure><img src="../../.gitbook/assets/image (53).png" alt=""><figcaption><p>The image shows a function app named "MetaFunctionApp" within the QA environment. Here, specific settings, including environmental variables, can be configured for this environment, ensuring that the function app operates correctly within its designated context.</p></figcaption></figure>
* **Delete Function App:** Permanently removes the function app from the platform. Be cautious when using this option, as it cannot be undone.

By utilising these features, you can effectively manage your Azure Function Apps, ensuring they are correctly configured and functioning as intended within your project. The **Edit Function App Settings** option, in particular, allows for precise control over the environmental variables, enabling you to customise how your function app operates across various environments.
