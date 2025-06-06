# Azure Logic Apps

## Overview

Azure Logic Apps enable you to automate workflows and integrate applications, data, and services across systems. The ComUnity Developer Toolkit simplifies the management of Logic Apps within your projects, providing tools to create, configure, and link Logic Apps seamlessly.

For in-depth details about Azure Logic Apps’ capabilities, visit the [official Microsoft documentation](https://learn.microsoft.com/en-us/azure/logic-apps/).

{% hint style="info" %}
This feature was introduced in the ComUnity Developer Toolkit v**24.3**.
{% endhint %}

## Why Use Azure Logic Apps?

Azure Logic Apps are ideal for:

* Event-Driven Automation: Automatically perform actions (e.g., send an email, trigger a webhook) based on events like database updates or HTTP requests.
* Scheduled Tasks: Set up workflows that run on specific schedules (e.g., daily reports, periodic data syncing).
* &#x20;Seamless Integration: Connect to over 400 Azure and third-party services (e.g., Office 365, Salesforce, APIs).
* Low-Code Workflows: Build workflows visually using a drag-and-drop designer, minimising the need for extensive programming.

For a complete overview of connectors and use cases, refer to the [Logic Apps Overview](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview).

## Integrating Azure Logic Apps into Your Project

Azure Logic Apps allow you to automate workflows and integrate services with minimal effort. This guide walks you through the steps to set up Azure Logic Apps in the ComUnity Developer Toolkit, enabling streamlined automation and integration directly within your project.

To setup Azure logic apps in your project follow the instructions below:

1. **Log In**: Access the Toolkit by entering your credentials.
2. **Open Your Project**: Locate and select your project within the Toolkit.
3.  **Access Azure Logic Apps**: In the sidebar, expand the Third Party Services section and click on the Azure Logic Apps tab to begin the setup process. A list of existing Logic Apps in your project, if any, will be displayed on this screen.\


    <figure><img src="../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>


4.  Click Create an Azure Logic app button, a pop-up window will appear with the heading **Create an Azure Logic App**. You will see a single input field labeled **Azure Logic App Name**, enter a unique name for your Logic App in the field (e.g., MyLogicApp).\


    <figure><img src="../../.gitbook/assets/image (436).png" alt=""><figcaption><p>Create an Azure Logic app</p></figcaption></figure>
5. Once created, the Logic App will appear in the screen with the following details:
   * **Azure Name**: The name of the Logic App.
   * **Endpoint: URL**: Use this URL to test and confirm that your Logic App is correctly configured. Copy and paste it into your browser to access the newly created workflow.
   * **Azure Resource ID**: The unique identifier for the resource in Azure.
   * **Azure Resource Group**: The resource group where the Logic App resides.
   * **Created**: The date the Logic App was created.

## Manage Logic Apps

The ComUnity Developer Toolkit provides several options for managing your Logic Apps efficiently. From accessing detailed configurations in the Azure Portal to refreshing endpoints or removing unused Logic Apps, these tools give you full control over your workflows. Use the features below to ensure your Logic Apps remain up-to-date and optimised for your project’s needs.\
\


<figure><img src="../../.gitbook/assets/image (437).png" alt=""><figcaption><p>Manage Azure logic apps</p></figcaption></figure>

### View Details

1. Select the ellipsis (...) next to the Logic App and click View in Azure Portal.
2. This redirects you to the Azure Portal where you can edit the workflow, add triggers, and configure actions.
3. &#x20;Ensure you have sufficient permissions (e.g., Logic App Contributor) to access and manage resources in Azure. If you encounter a “No Access” error, contact your Azure administrator.

### Refresh Endpoint:

* If your Logic App has a trigger with a URL (e.g., HTTP trigger), click Refresh Endpoint to fetch and display the latest endpoint URL in the toolkit.

### Delete Logic App:

• Use the ellipsis menu to delete an existing Logic App if it’s no longer required.

## Additional Resources

* [Azure Logic Apps Documentation](https://learn.microsoft.com/en-us/azure/logic-apps/)
* [Connectors Overview](https://learn.microsoft.com/en-us/connectors/connector-reference/)
* &#x20;[Error Handling in Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-exception-handling)
