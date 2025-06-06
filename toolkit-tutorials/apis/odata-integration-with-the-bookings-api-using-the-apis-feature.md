# OData Integration with the Bookings API Using the APIs feature

This tutorial demonstrates how to integrate an internal [ **OData 3.0**](https://www.odata.org/documentation/odata-version-3-0/?msclkid=237b40adce7311ecae5bf187856e481c) **API** using the ComUnity Developer Toolkit. The **API,** named **Bookings**, is a sample service prepared internally within the organisation and exposes structured booking data through an [OData](../../reference-articles/odata.md)-compliant interface.

The Toolkit provides native support for OData services, allowing developers to expose data via Virtual Entities, configure access control, and surface external data in the application using standard screen controls.

This tutorial guides you through registering the **Bookings API**, defining a data model, and building a screen to display booking records using a dynamic list.

## Before You Begin

If you are new to the APIs feature in the ComUnity Developer Toolkit, we recommend reviewing the [JSONPlaceholder Todos API](json-placeholder-todos-api-integration-in-a-simple-blog-app.md) tutorial. That tutorial introduces key integration concepts using a REST-based API. This tutorial builds on that foundation but focuses on a direct OData integration, which simplifies request handling by aligning with the Toolkit’s native architecture.

## What You’ll Learn

By the end of this tutorial, you will be able to:

* Register an internal OData 4.0 API in the ComUnity Developer Toolkit
* Define a Virtual Entity that models booking data from the API
* Configure role-based access to surface data to authorised users
* Display booking records using a dynamic list in the UI
* Enable click-to-navigate from list items to a booking detail screen

## About the Bookings OData API

The **Bookings OData API** exposes a single entity type: Booking. It is defined under the namespace ComUnity.Samples.Data.Models, and available via the Bookings entity set.

Each Booking entity includes the following properties:

* BookingId (Int32): The unique identifier for the booking
* Description (String): A short description of the booking
* BookingDate (DateTime): The scheduled date and time
* Created (DateTime): When the booking was created
* Modified (DateTime): When the booking was last modified
* &#x20;IsDeleted (Boolean): Indicates if the booking has been soft-deleted

{% hint style="info" %}
Based on the available metadata, the API supports read operations (GET). Create, update, and delete capabilities are not explicitly defined and should be confirmed before implementing write functionality.
{% endhint %}

## Prerequisites

1. Access Requirements
   1. Access Requirements
      * A ComUnity user account with the necessary permissions (contact ComUnity Support if required).
      * A single-tenant environment is required for API integration (organisations must host their own instance of the Toolkit in Azure).
      * If a single-tenant instance is unavailable, users can request access to the shared ComUnity Platform environment (API management is not supported in this environment).
2. Technical Knowledge
   * C# programming skills
   * CommentFamiliarity with[ WCF Data Services](https://learn.microsoft.com/en-us/visualstudio/data-tools/windows-communication-foundation-services-and-wcf-data-services-in-visual-studio?view=vs-2022\&tabs=csharp), Entity Framework, and [OData](https://app.gitbook.com/o/v0hmafhved1NwFsQQmjL/s/u0RQqzbgKGN4uoL3P89t/reference-articles/odata)
3. Development Tools
   1. Visual Studio 2022
   2. Access to the ComUnity Developer Toolkit
4. Project Setup\
   Before proceeding with the  API integration, ensure that you have:
   1. Created a project using the **Smart City sample** or similar.
   2. Successfully built and launched the project.
   3. &#x20;Registered a user account and signed in to the web app.
5. Read the official Azure API Management(APIM) documentation Import an OData API to understand the fundamentals OData API integration on the Azure platform.\


## Register the Bookings OData API

1. &#x20;In the Toolkit, navigate to **Third Party Services** > **APIs**.
2. Click **Add an Azure API** button.
3. &#x20;Provide a name (e.g., “Bookings API”) and optional description.
4. Select the API definition type as **OData**.
5.  In the **Provide Service** **URL** field, enter:\


    ```
    https://test-bookings-comunity.azurewebsites.net/odata
    ```


6.  &#x20;In the **Definition Link** field, enter the base OData endpoint for the Bookings service:\


    ```
    https://test-bookings-comunity.azurewebsites.net/odata/$metadata
    ```


7. Click **Add Azure API to your project button** to register the **API** on Azure.

Once registered, click the ellipsis (⋮) next to the API and select Fetch operations from Azure to load the available OData entity sets.

## **Verify the API Registration in Azure**:

1. After the API is registered, click the ellipsis (⋮) button next to the API in the Toolkit and select **View in Azure Portal**.
2. You will be redirected to **Azure API Management (APIM)**.
3. Locate your newly created API under **APIs** (use the search function if needed).
4.  Once you select your API, the Entity Sets and Functions tab will open. Click the ellipsis (⋮) next to the Bookings entity set and select Test. You will be redirected to the testing screen. Scroll down and click the Send button to execute the request. This action will fetch all bookings from the Bookings API and display the response data.\
    \


    <figure><img src="../../.gitbook/assets/image (467).png" alt=""><figcaption><p>The Bookings Entity Set as shown on Azure API Management platform</p></figcaption></figure>

## Define the Virtual Entity

1. Go back to the ComUnity Developer Toolkit under **Data**. Create a Virtual Entity named **Booking**. For detailed instructions on creating Virtual Entities in the Toolkit, refer to the  [Virtual Entities](../../toolkit-guides/data/creating-entities-in-the-data-model-step-by-step-guide.md#virtual-entities)  section.
2. Add the following properties to the **Booking entity** using the correct data types:
   1. BookingId → int
   2. Description → string
   3. BookingDate → datetime
   4. Created → datetime
   5. Modified → datetime
   6. IsDeleted → bool
3. Ensure that View permissions are granted to your User role for more details on setting up table permission view the section [Setting Up Role-Based Permissions for Entities: Access Control Configuration](../../toolkit-guides/data/setting-up-role-based-permissions-for-entities-access-control-configuration.md).

## Expose the API via Custom Classes

1.  Go to **Custom Classes** in the Toolkit. Select the **WebApiConfig** class and register your **Booking** Virtual Entity as shown below (line 23):\


    <pre class="language-csharp" data-title="WebApiConfig" data-line-numbers><code class="lang-csharp"><strong>using System;
    </strong>using System.Web.Http;
    using System.Web.Http.OData.Extensions;
    using odataapiintegration.Custom;

    namespace odataapiintegration
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
                builder.EntitySet&#x3C;Custom.Booking>("Booking");

                config.Routes.MapODataServiceRoute("odata", "odata", builder.GetEdmModel());
            }
        }
    }

    </code></pre>


2.  Update the **Booking** entity class as shown below:\


    <pre class="language-csharp" data-title="" data-line-numbers><code class="lang-csharp"><strong>using System;
    </strong>using System.Collections.Generic;
    using System.Linq;
    using System.Web;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace odataapiintegration.Custom
    {
        /*
        The following code should be added to the WebApiConfig class to add this class to the Service Root
        builder.EntitySet&#x3C;Custom.Booking>("Booking");
        */
        public class Booking
        {
            public int BookingId { get; set; }
            public string Description { get; set; }
            public DateTime? BookingDate { get; set; }
            public DateTime? Created { get; set; }
            public DateTime? Modified { get; set; }
            public bool IsDeleted { get; set; }
        }
    }

    </code></pre>


3.  Update your controller class as shown below, ensure that you also update all your packages on your file:\


    {% code title="BookingController" lineNumbers="true" %}
    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Web;
            
    namespace odataapiintegration.Custom
    {
        public class BookingController : System.Web.Http.OData.ODataController
        {
        /**To replace the API’s URL comment below, navigate to Third Party Services > APIs in the Toolkit, locate your API, and copy its URL.**/
              static string _baseUrl =  //***"API_URL"***//;
            // GET: odata/Booking
            [System.Web.Http.OData.EnableQuery]
            public IQueryable<Booking> GetBooking()
            {
                using (var httpClient = new ComUnity.DataServices.ServiceUtility.ComUnityHttpClient(//***"Application Name"***//, //***"Azure API name"***//);
                {
                    var res = httpClient.GetAsync($"{_baseUrl}/Bookings").Result;
                    res.EnsureSuccessStatusCode();
                    var content = res.Content.ReadAsStringAsync().Result;
                    var response = Newtonsoft.Json.JsonConvert.DeserializeAnonymousType(content, new
                    {
                        value = new List<Booking>(),
                    });
                    var bookings = response.value;
                    return bookings.AsQueryable();
                }
            }
           
        }
    }

    ```
    {% endcode %}


4. Build your project after updating your  **Data** model and **Custom Classes** so as to publish your changes and as well as to confirm that there are no errors in your build, if any exist debug and resolve them before proceeding to the next step.

## Build the UI

&#x20;In this section we will outline how to build the **Bookings** screen that shows all bookings as a list.

1. Navigate to Screens in the Toolkit and create a **Bookings** navigation page.
   1. Set an icon of your choice.
   2. Add a **List** control to your screen.
   3. Click the **List** item to activate it.
   4. In the Properties Editor, set the following fields:
      *   Data Path:&#x20;

          ```
          /Booking
          ```
      *   Item Title:&#x20;

          ```
          {{= Description}}
          ```
   5. Click  the **Save** button to persist your changes.
   6. Launch your project to see your list  of the titles of bookings fetched from the JsonPlaceholder API server in the **Bookings** page.

## Conclusion

In this tutorial, we demonstrated how to integrate an internal OData API with the ComUnity Developer Toolkit using a sample service called Bookings. We covered the full workflow: registering the API, defining a Virtual Entity, exposing the data via Custom Classes, and building a user interface that displays booking records and supports navigation to detailed views.

By leveraging the Toolkit’s native support for OData, developers can expose structured external data with minimal overhead, enabling consistent access through the data model and user interface. This approach simplifies integration for well-defined services and provides a strong foundation for building interactive, data-driven applications.

You can further extend this implementation by applying filters, adding sorting and paging, or exploring additional operations if the API supports data modification. Refer to the Toolkit documentation for guidance on building forms, configuring permissions, and implementing more advanced interaction patterns.
