# JSON Placeholder Todos API Integration in a Simple Blog App

In this tutorial, we focus on demonstrating API integration using the ComUnity Developer Toolkit, powered by [Azure API Management (APIM)](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts). Rather than starting from scratch, we will accelerate development by leveraging a template, allowing us to focus on key integrations and customisations.

A core aspect of this tutorial is utilising the APIs feature to integrate external data sources. We will connect to the JSONPlaceholder API through Azure APIM, showcasing how the Toolkit enables structured API management and integration while maintaining a well-defined data model. This hands-on guide highlights how Virtual Entities facilitate controlled interaction with third-party services, ensuring secure and efficient API exposure within the Toolkit.

## What You’ll Learn

In this tutorial you will:

* Set up a blog application using a predefined template to accelerate development.
* Register and configure an API in the ComUnity Developer Toolkit to connect to an external data source.
* Define a Virtual Entity to represent the external API within the data model.
* Expose the API via the Virtual Entity by registering it in WebApiConfig.
* &#x20;Create a custom API class (TodosAPI) and update the controller class to handle API interactions.
* Query and display JSONPlaceholder Todos within the blog application.

By the end of this tutorial, you’ll have a functional blog application enhanced with external data integration, as well as the skills to extend and improve applications within the Toolkit.

## Prerequisites

1. Access Requirements
   * A ComUnity user account with the necessary permissions (contact ComUnity Support if required).
   * A single-tenant environment is required for API integration (organisations must host their own instance of the Toolkit in Azure).
   * If a single-tenant instance is unavailable, users can request access to the shared ComUnity Platform environment (API management is not supported in this environment).
2. Technical Knowledge
   * C# programming skills
   * Familiarity with WCF Data Services, Entity Framework, and [OData](../../reference-articles/odata.md)
3. Development Tools
   * Visual Studio 2022 (Community, Professional, or Enterprise)

## **Blog Application Features:**

This tutorial builds a simple blog app with the following features:

* Users can create, edit, and publish articles.
* All users can view articles and add comments.
* Authors can tag blog articles and readers can view, and comment on tagged articles.
* Users can fetch and view todos from JSON Placeholder API

## **Walkthrough**

1. [Build and Launch your Blog from a template](json-placeholder-todos-api-integration-in-a-simple-blog-app.md#build-and-launch-a-blog-from-a-template)
2. [Integrate JSON Placeholder API Todos using **APIs**](json-placeholder-todos-api-integration-in-a-simple-blog-app.md#integrate-json-placeholder-api-todos-using-apis)

## Build and Launch a Blog from a Template

This section walks you through quickly setting up a blog application in just three steps. This forms the foundation for integrating the JSONPlaceholder Todos API in later sections.

To quickly build your blog, follow these steps:

1. &#x20;Login into the ComUnity Developer Toolkit.
2.  Create a project using the Blog Project template with a unique title, an illustration is shown in the following diagram:\


    <figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption><p>Creating a Blog app from a template</p></figcaption></figure>


3. **Build and Launch** your project the after building you will be redirected to your new app, refer to [Build and Launch your project](../../getting-started/manage-your-project/build-and-launch-your-project.md) for further details. Register and log in to access the blog application.

## Integrate JSON Placeholder API Todos using APIs

In this section, we will register, configure, and expose the JSONPlaceholder API within the ComUnity Developer Toolkit using the APIs feature. This process involves:

* Registering the API in the Toolkit and deploying it to Azure API Management (APIM).
* Defining an API operation to retrieve Todos from the JSONPlaceholder API.
* Testing the API in Azure to verify the response.
* Configuring a Virtual Entity to expose the Todos API within the Toolkit.
* Updating Custom Classes and the WebApiConfig class to enable API access.
* Building the UI to display the fetched Todos in the blog application.

By following these steps, you will integrate an external API, expose it within the data model, and render its data on a UI page. This approach demonstrates how to extend applications using the ComUnity Developer Toolkit’s API integration capabilities powered by Azure API Management.

1.  **Register the API in the Toolkit and deploy it to Azure API Management (APIM)**

    1. In the ComUnity Developer Toolkit, open your project and navigate to **Third Party Services** > **APIs**.
    2. Enter a unique name for your API in the **API display name** field.
    3. Select the option **HTTP** as the definition type.
    4. Provide a relevant description.
    5.  In the Provide Web URL field, enter:&#x20;

        ```
        https://jsonplaceholder.typicode.com
        ```
    6. Click **Add Azure API button to your project**  button to deploy the API to Azure API Management (APIM).

    **Note**: The Toolkit will handle API registration and deployment based on your specifications.\


    <figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption><p>Create a new Azure API<br></p></figcaption></figure>
2. **Access and Review the API in  Azure API Management (APIM)**
   1.  Once the API is deployed, click the ellipsis (⋮) button next to **View Details** and select **View in Azure Portal**.\


       <figure><img src="../../.gitbook/assets/image (460).png" alt=""><figcaption><p>View an API in Azure Portal</p></figcaption></figure>


   2. In the **Azure portal**, navigate to **APIs** under **All APIs**.
   3. Use the search function to quickly locate your newly created **API**.
   4. Click on the **API** and open the **Settings** tab to review its details.
3. **Define an API Operation**
   1. Navigate to the **Design** tab and select **Add an operation**.
   2.  Provide a resource name:

       ```
       Todos
       ```
   3. Leave the HTTP Verb to GET which is the default option
   4.  In the URL field, enter the relative path:

       ```
       /todos
       ```
   5.  Click the **Save** button to register the operation.\


       <figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption><p>Defining an operation on Azure (APIM)</p></figcaption></figure>
4. **Test the API Operation in Azure**
   1. Go to the **Test** tab in the Azure API Management Portal.
   2. Select the operation created in the previous step (/todos).
   3.  Click **Send** to execute the request.\


       <figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
   4. Scroll down to verify the response data containing the Todos list fetched from the JSON Placeholder API
5. **Configure Properties and Security of the Todo Virtual Entity in the Data model**
   1. Go back to the ComUnity Developer Toolkit under **Data**.
   2. Create a Virtual Entity named `Todo`. For detailed instructions on creating virtual entities in the Toolkit, refer to the [Virtual Entities](../../toolkit-guides/data/creating-entities-in-the-data-model-step-by-step-guide.md#virtual-entities) section.
      1. Leave the default options selected for **Add Entity class**, **Add Controller class** and **Add controller template code**.
      2.  Click the **Add** button to create the Todo Virtual Entity\


          <figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption><p>Add a virtual entity - Todo<br></p></figcaption></figure>
   3. Add the following entity fields and properties with their respective data types ensure that you delete the default primary key `TodoId` and replace it with `id` , refer to  the section [Adding Entity Fields and Configuring Field Settings for further details on how to configure](../../toolkit-guides/data/creating-entities-in-the-data-model-step-by-step-guide.md#adding-entity-fields-and-configuring-field-settings) fields on an entity:
      1. userId → int
      2. id → int
      3. title → string
      4.  completed → bool\


          <figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption><p>Todo entity with its properties configured<br></p></figcaption></figure>



          <div align="left"><figure><img src="../../.gitbook/assets/image (462).png" alt="" width="283"><figcaption></figcaption></figure></div>
   4. Set the permissions of the Todo Virtual Entity refer the section [Setting Up Role-Based Permissions for Entities: Access Control Configuration](../../toolkit-guides/data/setting-up-role-based-permissions-for-entities-access-control-configuration.md) for more information about configuring Table Security:
      1. Select the **Todo entity** to activate it.
      2. Locate **Table Security**  setting in the Properties Editor.
      3.  Set **View** permission only for the **User** role.\


          <figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption><p>Configuring role based access for the User role<br></p></figcaption></figure>
6. **Expose the Todos JSON Placeholder API via an Virtual Entities and Custom Classes**
   1.  Go to Custom Classes in the Toolkit select the WebConfigApi class and register your Virtual Entity as shown below (line 23):\


       {% code title="WebApiConfig" lineNumbers="true" %}
       ```csharp
       using System;
       using System.Web.Http;
       using System.Web.Http.OData.Extensions;

       namespace jsontodos
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
       			//builder.EntitySet<ClassName>("ClassName");
                               builder.EntitySet<Custom.Todo>("Todo");

       			builder.EntitySet<Custom.NotificationView>("NotificationView");
                   config.Routes.MapODataServiceRoute("odata", "odata", builder.GetEdmModel());
       		}
       	}
       }

       ```
       {% endcode %}


   2.  Create a TodosAPI class add the code below:\


       {% code title="TodosAPI" lineNumbers="true" %}
       ```csharp
       using System;
       using System.Collections.Generic;
       using System.Linq;
       using System.Web;
       using System.Net.Http;
       using System.Net.Http.Headers;
       using Newtonsoft.Json;
               
       namespace jsontodos.Custom
       {
          public class TodosAPI
           {
               private static readonly string _baseUrl = //***"API_URL"***//;
           
               public static List<Todo> GetTodos()
               {
                 var httpClient = new ComUnity.DataServices.ServiceUtility.ComUnityHttpClient("todos120003022025", "todos1200030testing-todosdev");
                   
                   var res = httpClient.GetAsync($"{_baseUrl}/todos").Result;
                   res.EnsureSuccessStatusCode();
                   var content = res.Content.ReadAsStringAsync().Result;
                   var todos = Newtonsoft.Json.JsonConvert.DeserializeObject<List<Todo>>(content);
                   return todos.ToList();
                   
               }

                public static Todo GetTodo(int id) 
               { 
                   var httpClient = new ComUnity.DataServices.ServiceUtility.ComUnityHttpClient("todos120003022025", "todos1200030testing-todosdev");

                   var response = httpClient.GetAsync($"{_baseUrl}/todos/{id}").Result;
                   response.EnsureSuccessStatusCode();
                   var content = response.Content.ReadAsStringAsync().Result;
                   return  Newtonsoft.Json.JsonConvert.DeserializeObject<Todo>(content);
               }

               public static bool AddTodo(string body)
               {
                   var httpClient = new ComUnity.DataServices.ServiceUtility.ComUnityHttpClient("todos120003022025", "todos1200030testing-todosdev");


                   HttpRequestMessage mess = new HttpRequestMessage(HttpMethod.Post, $"{_baseUrl}/todos");
                   mess.Content = new StringContent(body);
                   mess.Content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

                   var response = httpClient.SendAsync(mess).Result;
                   return response.IsSuccessStatusCode;
               }
           }
       }

       ```
       {% endcode %}



       1. To replace the comment on **Line 13** with your API’s URL, navigate to **Third Party Services** > **APIs** in the Toolkit, locate **your API**, and copy its **URL**.
   3.  Update the Todo entity class as shown below:\


       {% code lineNumbers="true" %}
       ```csharp
       using System;
       using System.Collections.Generic;
       using System.Linq;
       using System.Web;
       using System.ComponentModel.DataAnnotations;
       using System.ComponentModel.DataAnnotations.Schema;

       namespace jsontodos.Custom
       {
          
               public class Todo
           {
               public int id { get; set; }
               public string title { get; set; }
               public int userId { get; set; }
               public bool complete { get; set; }
           }
           
       }
       ```
       {% endcode %}


   4.  Update your controller class as shown below:\


       {% code title="TodoController" lineNumbers="true" %}
       ```csharp
       using System.Linq;
       using System.Web.Http.OData;
       using System.Web.Http.OData.Query;
       using System.Web.Http.OData.Routing;
               
       namespace jsontodos.Custom
       {
           public class TodoController : System.Web.Http.OData.ODataController
           {
                // GET: odata/Todos
               [EnableQuery]
               public IQueryable<Todo> GetTodo()
               {
                   return TodosAPI.GetTodos().AsQueryable();
               }

              
               //POST: odata/Todos
               public System.Web.Http.IHttpActionResult Post()
               {
                   var bb = Request.Content.ReadAsStreamAsync().Result;
                   bb.Position = 0;
                   var byteArray = new byte[bb.Length];
                   bb.Read(byteArray, 0, (int)bb.Length);
                   var body = System.Text.Encoding.Default.GetString(byteArray);
                   bool success = TodosAPI.AddTodo(body);
                   if (!success) return BadRequest("Failed to add todo.");
                   return Ok();
               }

           }
       }

       ```
       {% endcode %}


7. **Build the UI -** for more information on how to build lists in Navigation pages refer to the section [Dynamic List Rendering in Navigation pages](../../toolkit-guides/screens/building-screens/navigation/lists-in-navigation-pages/dynamic-list-rendering-in-a-navigation-page.md)
   1. Navigate Screens in the Toolkit and  create a **Todos** Navigational page.
   2. Set an icon of your choice
   3. Add a **List** item to your screen
   4. Click the List item to activate it
   5. In the Properties Editor  set the fields below with the values shown to set up your screen:
      1.  Data Path:

          ```
          /Todo
          ```
      2.  Item Title :

          ```
          {{= title }}
          ```
8.  Build and Launch your project and view your todos in your application.\
    \


    <figure><img src="../../.gitbook/assets/image (461).png" alt="" width="315"><figcaption><p>JSON Placeholder API Todos displayed in a Blog app</p></figcaption></figure>

## Conclusion

This tutorial has demonstrated how to integrate external APIs into an application using the ComUnity Developer Toolkit. By connecting to the JSONPlaceholder API, we successfully retrieved and displayed Todos using a Virtual Entity and the APIs feature.

Beyond this example, you can further enhance your integration skills by:

* Exploring Other API Types – Try integrating APIs using OpenAPI and GraphQL API specifications to understand different API structures and query mechanisms.
* Expanding Functionality – Modify the application to:
  * Post new Todos by extending the API integration with POST requests.
  * View a single Todo by configuring a GET operation with parameters.
  * Update or delete Todos by implementing PUT and DELETE operations.

• Customising the UI – Improve the presentation of Todos \


By applying these additional enhancements, you can deepen your understanding of API integrations and extend the functionality of your application to meet real-world requirements.

**Further Reading**

* [Microsoft Azure Learn - Add an API manually](https://docs.azure.cn/en-us/api-management/add-api-manually)
