# APIs

## Overview

The **Toolkit’s API management feature** enables organisations to **connect to third-party services** by integrating with [**Azure API Management (APIM)**](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts). The Toolkit provides a structured way to **register and configure APIs**, eliminating the need for direct configuration in Azure while ensuring seamless integration with APIM.

Once APIs are registered in the Toolkit, they are **automatically synchronised with Azure API Management**, where developers can configure API operations such as request handling and transformations. The Toolkit serves as the central interface for managing API definitions, while API operations are set up in Azure API Gateway.

After integration, the Toolkit allows organisations to **expose APIs** using **Virtual Entities and** [**Custom Classes**](../custom-classes.md). These features provide a structured approach to defining how APIs are accessed and interacted with, ensuring clear separation of concerns and enabling controlled API consumption.

This API management feature is available for **single-tenant environments**, where organisations manage their own Azure subscription. Shared environment users do not have access to this functionality due to Azure subscription constraints.

For more details on Azure API Management, refer to the [Azure API Management documentation](https://learn.microsoft.com/en-us/azure/api-management/?source=recommendations).

## Key Features

1.  API Creation & Management: Developers can define APIs within the Toolkit, which are then registered in Azure API Management.\
    Supported API types:

    * &#x20;Custom HTTP API – Manually configured endpoints.&#x20;
    * OData API – Supports structured OData queries.&#x20;
    * OpenAPI – Allows importing OpenAPI specifications.
    * GraphQL API – Supports GraphQL-based queries.&#x20;

    APIs can be created using either: A **Service URL** (endpoint-based configuration). A **Definition Link** (importing OpenAPI/OData specifications).
2. Seamless Integration with Azure API Management: APIs registered via the Toolkit are automatically created in Azure API Gateway. The Toolkit UI provides a synchronisation feature to retrieve API operations from Azure. Built-in security policies, such as OAuth2 and JWT authentication, are applied through Azure APIM. API analytics and monitoring are available in Azure API Insights.
3. &#x20;Deployment & Environment Considerations\
   Only available for single-tenant environments, where the organisation manages its own Azure subscription. API deployment and mirroring into QA and Production environments are still under development. Shared environment users cannot access API Management features due to Azure subscription constraints.

## When to Use APIs

APIs management is particularly useful when:

* &#x20;Integrating External Services: If your application needs to communicate with external APIs securely and efficiently.&#x20;
* Centralising API Security & Access Control: By leveraging Azure’s security policies, developers can manage authentication, authorisation, and traffic control without implementing custom security layers.&#x20;
* Enhancing Performance & Scalability: API Management enables caching, request throttling, and rate limiting, ensuring optimal performance under high load.&#x20;
* Monitoring & Logging API Traffic: Developers can track API usage, detect anomalies, and gain insights through Azure APIM’s built-in monitoring tools.&#x20;
* Managing API Versions & Lifecycle: The Toolkit enables versioning and gradual rollouts of API changes, minimising disruptions for consumers. For further insights, explore Azure API Management Use Cases.<br>

## API Configuration Workflow&#x20;

1. Creating an API: Navigate to API Management in the Toolkit. Click "Add New API" and select the API type. Provide either a Service URL (for manual configuration) or a Definition Link (for OpenAPI/OData imports). Define the API name, description, and version. Click Save & Register API – the API is now created in Azure API Management.&#x20;
2. &#x20;Configuring API Operations: API operations must be configured via the Azure API Management Portal: Open Azure API Management Portal. Locate the API created by the Toolkit. Define operations, authentication, and response configurations. Save and publish changes. Return to the Toolkit and click "Synchronise API Operations" to fetch updates from Azure.&#x20;
3. Testing & Deployment: Developers can use mock services in the Toolkit to validate API behaviour. API calls are logged in Azure API Insights for debugging and performance monitoring. Future updates will introduce automated deployment pipelines for QA and Production environments.

## Virtual Entities & Custom Classes for API Exposure

API Management in the Toolkit extends beyond simple configurations—it allows developers to expose APIs using [Virtual Entities](../data/creating-entities-in-the-data-model-step-by-step-guide.md#virtual-entities) and [Custom Classes](../custom-classes.md). These features provide a structured way to interact with API endpoints while maintaining separation of concerns. For detailed instructions, refer to the Virtual Entities & Custom Classes documentation.&#x20;

### Key Workflow

* **Creating a** **Virtual Entity** – Developers can define Virtual Entities to represent external API resources. During setup, the Toolkit automatically generates the **Entity Class**, **Controller Class**, and **Controller Sample Code**, which are stored under **Custom Classes**.
* **Extending APIs with Custom Classes** – The Controller Class can be modified to implement **custom business logic**, allowing APIs to be structured and managed efficiently. Custom Classes provide a flexible way to encapsulate API-related operations.
* **Deploying Extended API Features** – Once custom logic is implemented, the API can be **deployed and made available to consumers**. API updates can be **versioned and synchronised** with **Azure API Management** for ongoing maintenance and improvements.

For more information, refer to the [Virtual Entities](../data/creating-entities-in-the-data-model-step-by-step-guide.md#virtual-entities) & [Custom Classes](../custom-classes.md) documentation.

## &#x20;Code Generation (v25.3)

The Toolkit provides a built-in **code generation feature** that creates ready-to-use C# classes for registered APIs.\
This eliminates the need for manual boilerplate coding and ensures consistent integration across **HTTP**, **OData**, and **OpenAPI** endpoints.

After registering an API under **Azure APIs**, developers can use the **Generate Code** function to automatically create controller and model classes or API wrappers based on the selected API type.\
Generated files are stored under **Custom Classes**, where they can be extended or modified for specific business logic.

**Accessing Code Generation**

1. Navigate to **Third Party Services > Azure APIs**.
2. Select an API from the list to open its configuration screen.
3.  Click the **`</>` Generate code** icon next to the API name.\
    <br>

    <figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

This opens the **Generate Code** dialog for the selected API:

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Generation Options**

Inside the **Generate Code** dialog, select the desired generation mode:

| Option                                            | Description                                                                                                                                                                      | Applies To    |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **API Interface Class**                           | Creates a single wrapper class that exposes available endpoints as callable methods. Use this to integrate external REST or OpenAPI services.                                    | HTTP, OpenAPI |
| **Virtual Entity (Model and Controller Classes)** | Creates a Virtual Entity with a data model and controller automatically derived from OData metadata. Use this to expose structured data from OData endpoints within the Toolkit. | OData         |

**Workflow**

1. **Select API Type** – Choose the API (HTTP, OData, or OpenAPI) from **Azure APIs**.
2. **Fetch Operations or Entities** –
   * For HTTP/OpenAPI: click **Fetch Operations** to retrieve endpoints.
   * For OData: click **Fetch Entities from Azure** to load entity metadata.
3. **Generate Code** – Choose one of the available options:
   * _API Interface Class_
   * _Virtual Entity (Model and Controller)_
4. **Controller Class Name** – Provide or confirm the default name.
5. **Select Methods or Entities** – Tick the operations or entities to include.
6. Click **Generate Code**.
7. Review and click **Save Code** to insert the generated files under **Custom Classes**.
   * A corresponding configuration entry is created in **Config Hub**.
8. The new class or entity can now be used directly in logic, screens, or workflows.

**Behaviour**

* The generator interprets API metadata to build the appropriate class structure.
* For OData APIs, multiple entities are previewed together and saved as separate files.
* HTTP and OpenAPI APIs generate a single API Interface Class that includes all selected endpoints.
* Generated code can be safely modified within **Custom Classes**.
* Re-running the generator does not overwrite existing files unless the same class name is used.

**Example Use**

* **API Interface Class:** Integrate with REST or OpenAPI endpoints using strongly typed method calls.
* **Virtual Entity and Controller:** Represent an OData service as a native Toolkit entity and surface it in screens.
* Combine these generated components with intercept methods or workflow logic to extend API functionality.

**Notes**

* **GraphQL APIs** are not yet supported for code generation.
* Duplicate class names must be resolved before regenerating code.
* Verify **Config Hub** entries before deploying to QA or Production environments.

{% hint style="success" %}
**Try it out** 💡\
Learn how to use Virtual Entities by following this step-by-step tutorial: [JSONPlaceholder Todos API Integration in a Simple Blog App](../../toolkit-tutorials/apis/json-placeholder-todos-api-integration-in-a-simple-blog-app.md)
{% endhint %}
