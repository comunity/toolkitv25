# Countries GraphQL API Integration Using the APIs feature in the Toolkit

In this tutorial, we demonstrate API integration using the ComUnity Developer Toolkit, leveraging its APIs feature to connect with a third-party [GraphQL ](https://graphql.org/)API. The APIs feature is powered by  [Azure API Management (APIM)](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts) and enables structured API registration, management, and controlled data exposure within the Toolkit.

Instead of starting from scratch, we will use a predefined template project to accelerate development, allowing us to focus on integrating external data via GraphQL.

A core aspect of this tutorial is understanding how to integrate and query a GraphQL API in the Toolkit. We will use the [Countries API](https://countries.trevorblades.com/) to fetch and display country data, demonstrating the flexibility of the APIs feature when working with different API types.

{% hint style="info" %}
This tutorial integrates the Countries  API, an open-source project developed by Trevor Blades. The API provides country, continent, and language data and is available under the MIT license.

🔗 GitHub Repository: [Trevor Blades - Countries GraphQL API](https://github.com/trevorblades/countries)

We appreciate the availability of this public API, which allows developers to explore GraphQL queries in a real-world use case.
{% endhint %}

## Before You Begin

If you are new to the APIs feature in the Toolkit, we recommend first reviewing the [JSONPlaceholder Todos API tutorial](json-placeholder-todos-api-integration-in-a-simple-blog-app.md), which covers similar API integration concepts using an HTTP-based REST API. This GraphQL tutorial builds upon the same workflow, with adjustments specific to GraphQL queries and resources.

## What You’ll Learn

By the end of this tutorial, you will:

* Register and configure a GraphQL API in the ComUnity Developer Toolkit.
* &#x20;Define a Virtual Entity to model external country data from the API.
* &#x20;Expose the API via WebApiConfig and Custom Classes for structured data interaction.
* &#x20;Query and display country data using GraphQL queries within the Toolkit.

## Prerequisites

1. Access Requirements
   * A ComUnity user account with the necessary permissions (contact ComUnity Support if required).
   * A single-tenant environment is required for API integration (organisations must host their own instance of the Toolkit in Azure).
   * If a single-tenant instance is unavailable, users can request access to the shared ComUnity Platform environment (API management is not supported in this environment).
2. Technical Knowledge
   * C# programming skills
   * Familiarity with[ WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022\&tabs=csharp), Entity Framework, and [OData](../../reference-articles/odata.md)
3. Development Tools
   * Visual Studio 2022 (Community, Professional, or Enterprise)
4. Project Setup\
   Before proceeding with the GraphQL API integration, ensure that you have:
   1. Created a project from a template – Follow the [Create a Project](../../getting-started/manage-your-project/create-a-project.md) section to set up a new project using the Smart City template.
   2. [Built and launched](../../getting-started/manage-your-project/build-and-launch-your-project.md) the project successfully.
   3. &#x20;Registered a user account in your app – Sign up and log in within your app

Once your project is ready, you can proceed with configuring the GraphQL API.🚀

## Integrate the Countries API using APIs

To configure the GraphQL API in the ComUnity Developer Toolkit, follow these steps:

1. **Obtain the GraphQL Specification Document**
   1. Open the [Apollo GraphQL Playground](https://studio.apollographql.com/public/countries/variant/current/home) for the Countries API.
   2.  Click the Schema icon in the left panel.\


       <figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>
   3.  Select the **SDL** tab.\


       <figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>
   4. Download the **API Schema** as a raw file.
2. &#x20;**Register the GraphQL API in the Toolkit**
   1. In the ComUnity Developer Toolkit, navigate to **Third Party Services** > **APIs**.
   2. Provide a name and an optional description for your API.
   3.  In the Provide Service URL field, enter:\


       ```
       https://countries.trevorblades.com/graphql
       ```


   4.  &#x20;Click the **Select file** button and upload the schema file downloaded in the previous step.\


       <figure><img src="../../.gitbook/assets/image (466).png" alt=""><figcaption><p>Creating a GraphQL Azure API in the Toolkit</p></figcaption></figure>
   5. Click the **Add Azure API to your project** button to register and configure the API in Azure API Management (APIM).\
      This process ensures the API is properly registered and available for further integration within the Toolkit.&#x20;
3. **Verify the API Registration in Azure**
   1. &#x20;After the API is registered, click the ellipsis (⋮) button next to the API in the Toolkit and select View in Azure Portal.
   2. You will be redirected to Azure API Management (APIM).
   3. &#x20;Locate your newly created API under **APIs** (use the search function if needed).
   4. Open the Settings tab and check for any schema validation errors to confirm the API was successfully registered.
4. &#x20;**Test the Countries GraphQL API in Azure**
   1. &#x20;In Azure API Management (APIM), navigate to the **Test** tab.
   2.  Copy and paste the following GraphQL query into the **Query Editor**:\


       ```graphql
       query Countries {
         countries {
           code
           name
           native
           phone
         }
       }
       ```


   3.  &#x20;Click **Send** to execute the query.\


       <figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
   4. &#x20;Verify the response data to confirm that the API is correctly retrieving country details. Once confirmed, you can proceed to define a Virtual Entity for structured interaction with the API within the Toolkit.
5.  **Configure Properties and Security of the Country Virtual Entity in the Data model:** Go back to the ComUnity Developer Toolkit under **Data**. Create a Virtual Entity named Country. For detailed instructions on creating virtual entities in the Toolkit, refer to the [Virtual Entities](../../toolkit-guides/data/creating-entities-in-the-data-model-step-by-step-guide.md#virtual-entities) section, take note to include these properties for the entity.&#x20;

    1. code →  string
    2. name →  string
    3. native →  string
    4. phone →  string

    For guidance on configuring table security and surfacing entity data to user roles, refer to:

    * &#x20;[JSON Placeholder Todos API Integration in a Simple Blog App](json-placeholder-todos-api-integration-in-a-simple-blog-app.md)
    * [Setting Up Role-Based Permissions for Entities: Access Control Configuration](../../toolkit-guides/data/setting-up-role-based-permissions-for-entities-access-control-configuration.md)\

6. **Expose the Countries API via an Virtual Entities and Custom Classes**
   1.  Go to Custom Classes in the Toolkit select the WebConfigApi class and register your Virtual Entity as shown below (line 21):\


       {% code title="WebApiConfig" lineNumbers="true" %}
       ```csharp
       using System;
       using System.Web.Http;
       using System.Web.Http.OData.Extensions;

       namespace countriesgraphqlapitutorial
       {
       	/*
       	For additional details on using OData in ASP.NET Web API, visit the following link.
       	https://docs.microsoft.com/en-za/aspnet/web-api/overview/odata-support-in-aspnet-web-api/
       	*/
       	public static partial class WebApiConfig
       	{
       		static partial void CustomRegister(System.Web.Http.HttpConfiguration config)
       		{
       			// Web API configuration and services

       			// Web API routes
       			config.MapHttpAttributeRoutes();

       			System.Web.Http.OData.Builder.ODataConventionModelBuilder builder = new System.Web.Http.OData.Builder.ODataConventionModelBuilder();
       			builder.EntitySet<Custom.Country>("Country");

       			builder.EntitySet<Custom.NotificationView>("NotificationView");
                   config.Routes.MapODataServiceRoute("odata", "odata", builder.GetEdmModel());
       		}
       	}
       }

       ```
       {% endcode %}


   2.  Update the Country entity class as shown below:\


       {% code title="Country " lineNumbers="true" %}
       ```csharp
       using System;
       using System.Collections.Generic;
       using System.Linq;
       using System.Web;
       using System.ComponentModel.DataAnnotations;
       using System.ComponentModel.DataAnnotations.Schema;

       namespace countriesgraphqlapitutorial.Custom
       {
           /*
           The following code should be added to the WebApiConfig class to add this class to the Service Root
           builder.EntitySet<Custom.Country>("Country");
           */
           public class Country
           {
               public string code { get; set; }
               public string name { get; set; }
               public string native { get; set; }
               public string phone { get; set; }
           }
       }

       ```
       {% endcode %}


   3.  Update your controller class as shown below:\


       {% hint style="info" %}
       &#x20;**GraphQL Integration in the Toolkit**

       The ComUnity Developer Toolkit only supports OData-compliant endpoints. To integrate a GraphQL API, all interactions — including **queries** and **mutations** — must be manually transformed into REST-style HTTP requests within custom controller logic. This involves constructing a POST request with the GraphQL operation embedded as a string payload, sending it to the Azure APIM-hosted endpoint, and parsing the response into a usable format. This approach ensures the Toolkit can treat GraphQL-driven data as if it were native OData, making it compatible with Virtual Entities, UI rendering, and internal query mechanisms.
       {% endhint %}



       {% code title="Country Controller" lineNumbers="true" %}
       ```csharp
       using System;
       using System.Collections.Generic;
       using System.Linq;
       using System.Web;
       using System.Net.Http;
       using System.Net.Http.Headers;
       using Newtonsoft.Json;
               
       namespace countriesgraphqlapitutorial.Custom
       {
           public class CountryController : System.Web.Http.OData.ODataController
           {
           /**To replace the API’s URL comment below, navigate to Third Party Services > APIs in the Toolkit, locate your API, and copy its URL.**/
               
               private static readonly string _baseUrl = //***"API_URL"***//;
           
               // GET: odata/Country
               [System.Web.Http.OData.EnableQuery]

               public IQueryable<Country> GetCountry()
               {
                   var httpClient = new ComUnity.DataServices.ServiceUtility.ComUnityHttpClient(//***"Application Name"***//, //***"Azure API name"***//);
                   var payload = "{\"query\":\"query Query {\\n  countries {\\n    code\\n    name\\n    native\\n    phone\\n  }\\n}\"}";

                   HttpRequestMessage mess = new HttpRequestMessage(HttpMethod.Post, $"{_baseUrl}");
                   mess.Content = new StringContent(payload);
                   mess.Content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

                   var response = httpClient.SendAsync(mess).Result;
                   var content = response.Content.ReadAsStringAsync().Result;
                   
                   var responseObject = Newtonsoft.Json.JsonConvert.DeserializeAnonymousType(content, new
                   {
                       data = new { countries = new List<Country>() },
                   });

                   var countries = responseObject.data.countries;

                   return countries.ToList().AsQueryable();
               }

           }
       }


       ```
       {% endcode %}



7. **Build the UI -** for more information on how to build lists in Navigation pages refer to the section [Dynamic List Rendering in Navigation pages](../../toolkit-guides/screens/building-screens/navigation/lists-in-navigation-pages/dynamic-list-rendering-in-a-navigation-page.md)
   1. Navigate Screens in the Toolkit and  create a **Countries** Navigational page.
   2. Set an icon of your choice
   3. Add a **List** item to your screen
   4. Click the List item to activate it
   5. In the Properties Editor  set the fields below with the values shown to set up your screen:
      1.  Data Path:

          ```
          /Country
          ```

          1.  Item Title :

              ```
              {{= name }}
              ```
8.  Build and Launch your project and view your countries in your application.\


    <figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption><p>Countries served from the Countries GraphQL API in an app</p></figcaption></figure>

## Conclusion

This tutorial demonstrated how to integrate a GraphQL API into a ComUnity Toolkit application using the APIs feature, powered by Azure API Management. By connecting to the open-source Countries GraphQL API, we illustrated how to register and configure APIs, define Virtual Entities, and transform GraphQL queries into OData-compliant operations using custom classes and controllers.

This approach not only enables controlled data access through the Toolkit but also allows developers to model and expose external data using familiar tools and standards. The flexibility to work with GraphQL—despite the Toolkit’s OData-first design—shows how adaptable the platform is for diverse integration scenarios.

To further extend this implementation:

* Try adding GraphQL queries with parameters, such as querying countries by continent or language.
* &#x20;Explore mutation operations and how they can be adapted into REST-style POST requests for OData compatibility.
* Improve the UI to display more detailed country data or filter results.

By applying these techniques, you’ll be able to build dynamic, data-rich applications that consume a variety of third-party APIs while maintaining a well-structured data model and user experience within the ComUnity Platform.
