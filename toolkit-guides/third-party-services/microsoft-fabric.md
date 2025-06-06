# Microsoft Fabric

## Overview

[Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/) is integrated into the ComUnity Developer Toolkit (available from version **24.5**) to facilitate data replication and reporting by creating Fabric mirrors of databases. This integration allows developers and analysts to transform and query data in a separate mirrored environment without directly impacting the production database.&#x20;

This functionality is available for single-tenant environments, where organisations manage their own Azure subscription. Users in shared environments do not have access to this feature due to Azure subscription constraints.&#x20;

The integration is currently in development, with the ability to create a Fabric Mirror in the development environment. Future updates will extend this functionality to Quality Assurance (QA) and Production environment.

## Key Features

1. **Fabric Mirror Creation**\
   The Toolkit enables the creation of a Fabric Mirror, which is a replica of the source database. This mirror allows:&#x20;
   1. Replication of all tables or selective tables.
   2. &#x20;Automatic synchronisation when new tables are added in the source database (if full replication is chosen).&#x20;
   3. Manual synchronisation if only selective tables are mirrored.
2.  **Deployment Environment Management**   \
    The Toolkit supports three deployment environments, but currently, Microsoft Fabric is only available in the Development environment:

    1. **Development environment** (currently functional, with Fabric support)
    2. **Quality Assurance (QA) environment** (in progress, Fabric support planned)
    3. **Production environment** (planned, Fabric support pending future updates)

    Each mirrored database follows a naming convention, typically **Env**\_**ProjectName**, to maintain consistency.
3. **Data Transformation and Reporting**\
   Once the Fabric Mirror is created, further transformations can be performed outside the Toolkit within Microsoft Fabric:&#x20;
   1. Combining tables for easier reporting&#x20;
   2. Fetching external data to build enriched datasets
   3. &#x20;Creating new schemas for specific reporting needs. These transformations make the mirrored data more efficient for analysis and visualisation in reporting tools like Power BI.
4.  **Replication Monitoring**\
    The Toolkit provides options to:&#x20;

    1. View replication status&#x20;
    2. Refresh replication status&#x20;
    3. Monitor synchronisation progress&#x20;

    If replication is incomplete or delayed, users can check the Fabric environment for more details

## Microsoft Fabric Configuration Workflow

Creating a Fabric Mirror in the Toolkit allows users to replicate database tables for use in reporting and data transformation without affecting operational databases.&#x20;

The process starts by navigating to **Third Party Services** > **Microsoft Fabric** within the Toolkit, where existing mirrors are listed. Users can initiate a new mirror by selecting **"Create a Fabric mirror"** option, providing an optional description, and choosing the tables to replicate.&#x20;

By default, all existing and future tables are included, but specific selections can be made by unchecking undesired tables. Once the **"Create Fabric mirror"** button is clicked, the mirroring process begins, with completion time varying based on data size.&#x20;

After a successful mirror creation, the entry appears in the UI, where users can access additional options via the ellipsis menu. Users can **delete a mirror**, **view replication status**, and **configure replication settings** from this menu. Selecting View in Fabric Portal redirects users to the Microsoft Fabric portal, where the mirror is identified by its assigned name in the Toolkit.\
\
To create a Fabric Mirror follow these steps:

1.  Navigate to **Third Party Services** > **Microsoft Fabric** in the Toolkit. \


    <figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption><p>Microsoft Fabric in the ComUnity Developer Toolkit</p></figcaption></figure>
2.  Click **"Create a Fabric mirror"** to open the Fabric Mirror creation dialog. \


    <figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption><p>Create a Microsoft Fabric mirror </p></figcaption></figure>
3. Provide an optional description for your mirror in the field provided.&#x20;
4. By default, all tables in your project, including future tables, are selected since the  **"Mirror future tables"** field is checked.&#x20;
5. To select specific tables, uncheck the **"Mirror future tables"** field then uncheck undesired tables from the list shown.&#x20;
6. Click the **"Create Fabric Mirror"** button to initiate the process.&#x20;
7. Processing time depends on the size of the data being mirrored. After successful mirroring, your Fabric Mirror will appear in the UI with its details.&#x20;
8.  Click the ellipsis (⋮) menu next to your mirror entry, then select **“Refresh replication status”** to check if the Fabric Mirror has been fully deployed on the Fabric Portal.\


    <figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Newly created Fabric Mirror with an ongoing deployment—indicated by the absence of a <strong>"Last updated"</strong>  date in the mirror details</p></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption><p>Fully deployed Fabric Mirror—indicated by a <strong>"Last updated"</strong> date in the mirror details. This mirror is now accessible in the Fabric Portal.<br><br></p></figcaption></figure>

    Once replication is complete (indicated by a "**Last updated"** date published in the mirror details), click the ellipsis (⋮) menu and select **“View in Fabric Portal”** to open the Microsoft Fabric portal and view the mirror.

## Microsoft Fabric Documentation

Since Microsoft Fabric handles data transformation and reporting outside the Toolkit, users are encouraged to refer to Microsoft’s official documentation for detailed guidance on:&#x20;

1. [Microsoft Fabric Overview](https://learn.microsoft.com/en-us/fabric/)
2. [Fabric Data Mirroring](https://learn.microsoft.com/en-us/fabric/data-mirroring)
3. [Fabric Workspaces](https://learn.microsoft.com/en-us/fabric/workspaces)
4. [Power BI Integration with Fabric](https://learn.microsoft.com/en-us/fabric/power-bi)
