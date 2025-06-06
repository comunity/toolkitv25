# Manual Project Deployment Across Environments

> The deployment process within the ComUnity Platform is a critical pathway that ensures your application is thoroughly tested and stable before it reaches the end-user. Adhering to a structured and sequential progression through the Development, QA/Testing, and Production environments, each stage serves as a gatekeeper, ensuring only the highest quality code is promoted.

## Deployment Types: Partial vs. Full Deployment

When deploying your project within the ComUnity Platform, it is essential to determine whether a partial or full deployment is necessary. Each type of deployment serves different purposes and is used under specific conditions.

### **Full Deployment**

A full deployment involves deploying all components of your application. This includes the Data Service, Authorisation Service, Client, Communication service, Configuration, Screens, and any other modules or services within the application. Full deployments ensure that all parts of the application are updated and synchronised.

**Use cases for Full Deployment:**

* Initial release of the application.
* Major updates or changes that impact multiple modules or components.
* Structural changes to the application that require all components to be redeployed.

**Components in a Full Deployment:**

* Data Service
* Authorisation Service
* Client
* Communication Service
* Configuration
* Screens
* All other application modules and services

### **Partial Deployment**

A partial deployment involves deploying only specific parts of the application. This type of deployment is useful when minor updates or bug fixes need to be applied without redeploying the entire application. Partial deployments save time and resources by targeting only the affected components.

**Use cases for Partial Deployment:**

* Minor bug fixes or updates that affect only a specific module.
* Incremental updates that do not require a full application redeployment.
* Changes to configuration files or settings that do not impact the overall application structure.

**Examples of Partial Deployments:**

* **Authorisation Service**: Deploy updates or fixes to the authorisation without affecting other parts of the application.
* Client: Coming soon..
* **Communication Service**: Update communication configurations or client modules independently.
* **Configuration:** Modify and deploy changes to specific configuration
* **Screens**: Modify and deploy changes to specific screens or UI components.

### **Determining the Deployment Type**

During the deployment process, the ComUnity Platform allows you to select the deployment type based on your needs. For a full deployment, activate the Full Deployment toggle and ensure all components are selected. For a partial deployment, deactivate the Full Deployment toggle and select only the necessary components.

The decision between partial and full deployment should be based on the scope and impact of the changes being made. By selecting the appropriate deployment type, you can ensure a smooth and efficient deployment process, minimizing downtime and maximizing application stability.

## **Prerequisites for Deployment**

1. **Successful Build**: Before initiating deployment, confirm that your project has successfully built without any errors or critical warnings.
2. [**Prepare the Project Archive for Deployment**](manual-project-deployment-across-environments.md#preparing-the-project-archive-for-deployment)

## Prepare the Project Archive for Deployment

To prepare your project archive for deployment, follow these carefully outlined steps to ensure your application is packaged correctly and ready for the deployment process.

1. **Download the Project Archive**:
   *   Obtain the latest version of your project archive. This will include all the necessary files for deployment.\\

       <figure><img src="../../../.gitbook/assets/image (397).png" alt=""><figcaption></figcaption></figure>
2.  **Open the Web.config File**:

    * Use [Visual Studio](https://visualstudio.microsoft.com/downloads/) to access your project's `Web.config` file, which contains critical configurations for deployment which need to be adjusted for the deployment.

    <pre class="language-csharp" data-title="Web.config" data-line-numbers data-full-width="true"><code class="lang-csharp"><strong>// Web.config file example download from the Toolkit
    </strong>&#x3C;?xml version="1.0" encoding="utf-8"?>
    &#x3C;!--
      For more information on how to configure your ASP.NET application, please visit
      http://go.microsoft.com/fwlink/?LinkId=169433
      -->
    &#x3C;configuration>
      &#x3C;configSections>
        &#x3C;!-- For more information on Entity Framework configuration, visit http://go.microsoft.com/fwlink/?LinkID=237468 -->
        &#x3C;section name="entityFramework" type="System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=6.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" requirePermission="false" />
      &#x3C;/configSections>
      &#x3C;appSettings>
        &#x3C;add key="AppName" value="testblog" />
        &#x3C;add key="BaseUrl" value="https://testblog.comunity.me" />
        &#x3C;add key="MediaServerUploadUrl" value="http://localhost/u/" />
        &#x3C;add key="ObservabilityTraceHttpUrl" value="https://otelcollector.obs.comunity.me/v1/traces" />
        &#x3C;add key="PublishedAppName" value="testblog" />
        &#x3C;add key="PushRootName" value="push_r" />
        &#x3C;add key="WelcomeMessage" value="Welcome to your personal 'testblog' App experience. Please go to the My Profile section and provide us with some information about yourself. The more information you provide, the more we can personalise your experience and ensure you receive communications from us that make a difference to you. We wish you a pleasant experience and we look forward to your feedback so that we can add more of the things you want and need." />
        &#x3C;add key="ConfigDeployment" value="Web.config" />
        &#x3C;add key="ConfigComponent" value="ds" />
        &#x3C;add key="Context" value="MultipleActiveResultSets=true;Data Source=(Local);Initial Catalog=testblog;Integrated Security=True;" />
      &#x3C;/appSettings>
      &#x3C;system.web>
        &#x3C;compilation debug="true" targetFramework="4.8">
          &#x3C;assemblies>
            &#x3C;add assembly="Microsoft.CSharp, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.Linq" />
            &#x3C;add assembly="System.Net.Http, Version=4.2.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.Runtime.InteropServices" />
            &#x3C;add assembly="System.Runtime.InteropServices.RuntimeInformation" />
            &#x3C;add assembly="System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.ServiceModel.Activation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
            &#x3C;add assembly="System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
            &#x3C;add assembly="System.Threading.Thread" />
            &#x3C;add assembly="System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
            &#x3C;add assembly="System.Web.Entity" />
            &#x3C;add assembly="System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
            &#x3C;add assembly="System.ComponentModel.DataAnnotations, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
            &#x3C;add assembly="System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
            &#x3C;add assembly="System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
            &#x3C;add assembly="System.EnterpriseServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
          &#x3C;/assemblies>
        &#x3C;/compilation>
        &#x3C;httpRuntime targetFramework="4.6.2" />
      &#x3C;/system.web>
      &#x3C;system.serviceModel>
        &#x3C;serviceHostingEnvironment aspNetCompatibilityEnabled="true" multipleSiteBindingsEnabled="true" />
      &#x3C;/system.serviceModel>
      &#x3C;entityFramework>
        &#x3C;contexts>
          &#x3C;context type="testblog.testblogContext, testblog">
            &#x3C;databaseInitializer type="testblog.testblogInit, testblog" />
          &#x3C;/context>
        &#x3C;/contexts>
        &#x3C;defaultConnectionFactory type="System.Data.Entity.Infrastructure.LocalDbConnectionFactory, EntityFramework">
          &#x3C;parameters>
            &#x3C;parameter value="mssqllocaldb" />
          &#x3C;/parameters>
        &#x3C;/defaultConnectionFactory>
        &#x3C;providers>
          &#x3C;provider invariantName="System.Data.SqlClient" type="System.Data.Entity.SqlServer.SqlProviderServices, EntityFramework.SqlServer" />
        &#x3C;/providers>
      &#x3C;/entityFramework>
      &#x3C;runtime>
        &#x3C;assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="Microsoft.Data.Services" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="Microsoft.Data.Services.Client" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="Microsoft.Data.Edm" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="System.Spatial" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="Microsoft.Data.OData" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30ad4fe6b2a6aeed" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-12.0.0.0" newVersion="12.0.0.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="System.Web.Http" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.2.7.0" newVersion="5.2.7.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="System.Net.Http.Formatting" publicKeyToken="31bf3856ad364e35" culture="neutral" />
            &#x3C;bindingRedirect oldVersion="0.0.0.0-5.2.7.0" newVersion="5.2.7.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="System.Web.Helpers" publicKeyToken="31bf3856ad364e35" />
            &#x3C;bindingRedirect oldVersion="1.0.0.0-3.0.0.0" newVersion="3.0.0.0" />
          &#x3C;/dependentAssembly>
          &#x3C;dependentAssembly>
            &#x3C;assemblyIdentity name="System.Web.WebPages" publicKeyToken="31bf3856ad364e35" />
            &#x3C;bindingRedirect oldVersion="1.0.0.0-3.0.0.0" newVersion="3.0.0.0" />
          &#x3C;/dependentAssembly>
        &#x3C;/assemblyBinding>
      &#x3C;/runtime>
    &#x3C;/configuration>

    </code></pre>
3. **Update Configuration Settings**:
   * Within the `Web.config` file, remove keys 13-19 under `<appSettings>` that are pertinent only to local development.
   *   Modify the `ConfigDeployment` key to reflect the deployment environment, for example: `value="<app_name>_qa"` for QA deployments and `value="<app_name>_prod"` for Production deployments. The updated section should resemble the following:\


       {% hint style="info" %}
       Go to **Project Settings** > **General** and then locate **Application Name** to view your `<app_name>`. Refer to the **General** section for more details.

       It is crucial to adhere to the naming convention for the ConfigDeployment key to accurately reflect the deployment environment (e.g., `<app_name>_qa` for QA and `<app_name>_prod` for Production) to otherwise failure to do so will result in deployment errors
       {% endhint %}

{% code title="Updated Web.config" %}
````csharp
   <?xml version="1.0" encoding="utf-8"?>
   <!--
     For more information on how to configure your ASP.NET application, please visit
     http://go.microsoft.com/fwlink/?LinkId=169433
     -->
   <configuration>
     <configSections>
       <!-- For more information on Entity Framework configuration, visit http://go.microsoft.com/fwlink/?LinkID=237468 -->
       <section name="entityFramework" type="System.Data.Entity.Internal.ConfigFile.EntityFrameworkSection, EntityFramework, Version=6.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" requirePermission="false" />
     </configSections>
     <appSettings>
       <add key="ConfigDeployment" value="testblog_qa" />
       <add key="ConfigComponent" value="ds" />
     </appSettings>
     <system.web>
       <compilation debug="true" targetFramework="4.8">
         <assemblies>
           <add assembly="Microsoft.CSharp, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.ComponentModel.Composition, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.Linq" />
           <add assembly="System.Net.Http, Version=4.2.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.Runtime.InteropServices" />
           <add assembly="System.Runtime.InteropServices.RuntimeInformation" />
           <add assembly="System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.ServiceModel.Activation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
           <add assembly="System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
           <add assembly="System.Threading.Thread" />
           <add assembly="System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
           <add assembly="System.Web.Entity" />
           <add assembly="System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
           <add assembly="System.ComponentModel.DataAnnotations, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />
           <add assembly="System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
           <add assembly="System.Configuration, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
           <add assembly="System.EnterpriseServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
         </assemblies>
       </compilation>
       <httpRuntime targetFramework="4.6.2" />
     </system.web>
     <system.serviceModel>
       <serviceHostingEnvironment aspNetCompatibilityEnabled="true" multipleSiteBindingsEnabled="true" />
     </system.serviceModel>
     <entityFramework>
       <contexts>
         <context type="testblog.testblogContext, testblog">
           <databaseInitializer type="testblog.testblogInit, testblog" />
         </context>
       </contexts>
       <defaultConnectionFactory type="System.Data.Entity.Infrastructure.LocalDbConnectionFactory, EntityFramework">
         <parameters>
           <parameter value="mssqllocaldb" />
         </parameters>
       </defaultConnectionFactory>
       <providers>
         <provider invariantName="System.Data.SqlClient" type="System.Data.Entity.SqlServer.SqlProviderServices, EntityFramework.SqlServer" />
       </providers>
     </entityFramework>
     <runtime>
       <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
         <dependentAssembly>
           <assemblyIdentity name="Microsoft.Data.Services" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="Microsoft.Data.Services.Client" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="Microsoft.Data.Edm" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="System.Spatial" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="Microsoft.Data.OData" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.8.4.0" newVersion="5.8.4.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="Newtonsoft.Json" publicKeyToken="30ad4fe6b2a6aeed" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-12.0.0.0" newVersion="12.0.0.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="System.Web.Http" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.2.7.0" newVersion="5.2.7.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="System.Net.Http.Formatting" publicKeyToken="31bf3856ad364e35" culture="neutral" />
           <bindingRedirect oldVersion="0.0.0.0-5.2.7.0" newVersion="5.2.7.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="System.Web.Helpers" publicKeyToken="31bf3856ad364e35" />
           <bindingRedirect oldVersion="1.0.0.0-3.0.0.0" newVersion="3.0.0.0" />
         </dependentAssembly>
         <dependentAssembly>
           <assemblyIdentity name="System.Web.WebPages" publicKeyToken="31bf3856ad364e35" />
           <bindingRedirect oldVersion="1.0.0.0-3.0.0.0" newVersion="3.0.0.0" />
         </dependentAssembly>
       </assemblyBinding>
     </runtime>
   </configuration>

   ```
   
````
{% endcode %}

4\. **Save and Build**:&#x20;

* Save the changes made in the \`Web.config\` file. \*&#x20;
* Build your project within Visual Studio to confirm that there are no compilation errors or issues with your code.&#x20;

5. Create a Web Deployment Package: Construct a Web Deployment Package using the Publish Web Wizard in Visual Studio. Refer to the guide [**Create a Web Deployment Package in Visual Studio** ](https://learn.microsoft.com/en-us/previous-versions/aspnet/dd465323\(v=vs.110\))for detailed steps.&#x20;

6\. Compress the Package:  Compress the deployment package into a **.zip** file format, readying it for the deployment process.

By the end of these steps, you should have a properly configured and compressed project archive that is ready to be deployed to the designated environment.

## **Deploy Your Web Deployment Package: A Step-by-Step Guide**

To initiate the deployment of a project within the Toolkit, a structured and guided step-by-step process is employed. This methodical approach encompasses the uploading of necessary assets and the precise configuration of deployment scripts. The focal point of this process is the deployment of a web deploy package to an [Internet Information Services (IIS)](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/iis-web-server-overview) server, which ensures that the application is correctly installed and configured for use in the specified environment.

To successfully deploy a project, follow these steps:

**Note:** To progress through each step, ensure all required fields and assets are properly set, then click the "**Next**" button to proceed.

1.  **Set Deployment Name and Release Notes**: Begin by naming your deployment and providing detailed release notes that outline the changes and features included in this deployment.\
    \\

    <figure><img src="../../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>
2. Click the "Create assets" button to proceed with a full deployment
3. To perform a Partial Deployment:
   1. Deactivate the Full Deployment Switch: Ensure the Full Deployment toggle is deactivated.
   2. Select Relevant Components: Choose only the necessary components (e.g., Authorization, Communication, Configuration) to deploy.
   3. Create Assets: Click the "Create assets" button to proceed.
4.  **Upload and Configure the Prepared Web Deploy Package**: Upload the web deploy package prepared according to the [prerequisites](manual-project-deployment-across-environments.md#prerequisites-for-deployment). To upload the package, click the three-dot button to open a modal and select "**Upload replacement**". After uploading, click the "**Accept**" button and the Toolkit will automatically generate deployment scripts for you. Use the chevron button to expand and collapse your scripts.\\

    <figure><img src="../../../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (423).png" alt=""><figcaption></figcaption></figure>
5.  **Review Your Configuration Scripts**: Thoroughly review the configuration scripts to ensure they are correct and will execute as expected without errors. Make any necessary adjustments. \\

    <figure><img src="../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>
6.  **Deploy**: With all configurations and reviews complete, proceed to deploy your project. This final step may take some time, so please be patient.\\

    <figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

In conclusion, following this structured and detailed guide ensures that your project is deployed smoothly and effectively. By methodically setting up, reviewing, and executing each step, you minimise the risk of deployment errors and ensure your application performs optimally in its intended environment. This careful attention to the deployment process not only smooths the transition between environments but also supports the ongoing development and scalability of your application.
