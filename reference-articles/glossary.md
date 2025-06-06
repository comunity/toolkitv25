# Glossary

[A](glossary.md#as-a-service) [B](glossary.md#background-processes) [C](glossary.md#cascading-actions) [D](glossary.md#data) [E](glossary.md#entity) [F](glossary.md#field-types) [G](glossary.md#group-samples) [H](glossary.md#hierarchical-relationship) [I](glossary.md#icons) [J](glossary.md#journey-as-a-service) [K](glossary.md#key-vault-integration) [L](glossary.md#launch) [M](glossary.md#major-version) [N](glossary.md#navigation-page) [O](glossary.md#odata) [P](glossary.md#page-link) [Q](glossary.md#qa-testing-environment) [R](glossary.md#razor) [S](glossary.md#sample) [T](glossary.md#table-security) [U](glossary.md#unknown-events) [V](glossary.md#validation) [W](glossary.md#weather-icons) X Y Z

### …as a Service

> A delivery model where specific functionalities, platforms, or business solutions are provided to users on-demand, typically via the cloud. This approach abstracts complexity by offering modular, reusable, and scalable components that can be integrated into broader systems. Examples include Journey as a Service, Platform-as-a-Service (PaaS), and Software-as-a-Service (SaaS).
>
> In the context of the ComUnity Platform, as a Service reflects its capability to provide modular, business-ready digital solutions that cater to both internal and external use cases. The platform supports reusable code and configurations, enabling organisations to build customer journey platforms, business solutions, and enterprise services efficiently. This modularity allows organisations to adopt the platform as a foundation for delivering their services, ensuring scalability, flexibility, and reduced development overhead.

### Accumulative Users

> &#x20;A performance indicator that measures the cumulative number of unique users interacting with the project over a specific period. This metric helps track user engagement and growth trends.

### App Versioning

> App versioning is the systematic practice of assigning unique version identifiers to distinct releases of an application. It ensures clear differentiation between updates, improvements, and feature changes over time. This process allows developers to maintain compatibility across different app versions, manage upgrades efficiently, and provide a stable user experience. The ComUnity Toolkit includes a versioning feature that simplifies this process, supporting the efficient deployment of app updates across supported platforms.

### Apple Store URL

> The URL of an application’s listing on the Apple App Store, used for iOS apps.

### Application Name

> The Application the immutable, system-defined identifier of an application, set during project initialisation by the project owner. It is used as the core identifier for the application across development and deployment contexts. The Application Name appears in technical contexts such as browser tabs, internal identifiers, and URLs, ensuring consistency and reliability for system-level interactions. It cannot be changed once defined, maintaining a stable reference throughout the application’s lifecycle.

### Application Namespace

> The namespace associated with the application, which is used for referencing within the project.

### Application Title

> The Application Title is a customisable, user-defined label displayed prominently in the application interface, such as in app headers or other user-facing contexts. By default, the Application Title inherits the Application Name but can be modified to suit branding or contextual requirements. Unlike the immutable Application Name, the Application Title offers flexibility and can be updated at any time without affecting the underlying application identifier or system references.

### Architecture Documentation

> This provides a high-level view of the software's structure and interaction between its components. It often includes diagrams, such as UML diagrams, to illustrate system architecture, data flows, and other structural aspects of the system.

### Authentication

> Authentication is the process of verifying the identity of a user or entity attempting to access a system, network, or application. It ensures that the claimed identity is legitimate and authorised to access the requested resources.

### Authorisation

> Authorisation refers to the process of defining and enforcing access rights and permissions for users, applications, or entities. It determines what actions or resources an authorised entity can access, modify, or perform within the platform, based on roles and organisational policies. This ensures secure and role-based access control across projects and applications.

### Azure Function Apps Integration

> A feature in the ComUnity Developer Toolkit that allows teams to integrate event-driven, server-less functions into their projects. It enables **custom logic**, **workflow automation**, and **external service connections** without requiring complex infrastructure management.

### Azure Logic Apps

> A cloud-based service that allows you to **automate workflows**, **integrate applications**, and **connect data across systems**. Logic Apps support event-driven automation, scheduled tasks, and seamless integration with over 400 [Azure](https://learn.microsoft.com/en-us/azure/logic-apps/) and third-party services.

### Azure Logic App Name

> The name provided during the creation of an Azure Logic App to uniquely identify it within the ComUnity Developer Toolkit and [Azure](https://learn.microsoft.com/en-us/azure/logic-apps/).

### Azure Specification

> The set of guidelines provided by Azure for preparing and packaging function apps to ensure compatibility during deployment.

### Azure Blob Storage Integration

> A storage solution integrated into the Media Services component that supports uploading, downloading, and managing large unstructured data files (up to 270 GB).

### Background Processes

> Internal operations managed by the Communications Service that occur behind the scenes, abstracting complexity from developers.

### BaseEntity

> The default foundational entity from which all other entities in the Toolkit inherit. BaseEntity provides essential fields and properties, such as creation and modification timestamps, which streamline consistent data management across inherited entities.

### Bindings

> Domains associated with a custom website in the ComUnity Developer Toolkit. By default, an initial binding (e.g., <\<tenantname>>.webdev.comunity.me) is created when a custom website is published. Developers can add multiple bindings to a single custom website, enabling diverse domain configurations. Bindings require DNS registration, which can be managed independently or through the ComUnity Platform’s domain registrar services.

### Blank Project

> A template option that allows users to create a new project from scratch without any predefined configurations.

### Build

> The process initiated to compile and provision resources for your application on [Microsoft Azure](https://learn.microsoft.com/en-us/azure/), based on your Data model and project configurations. It may also trigger data migrations and publish the project to [Internet Information Services](https://learn.microsoft.com/en-us/iis/) (IIS).

### Build and Launch

> A combined action that builds your project and automatically launches the web version in a new browser tab.

### Build Status Indicator

> A visual representation of your project’s build status, showing yellow for pending, green for success, and red for a failed build.

### Build Version

> The build version is the third component in the versioning convention (e.g., _x.y.z_). It is primarily used for internal tracking of minor incremental changes, such as bug fixes, patches, or optimisations that do not introduce new features. This identifier helps developers and teams manage continuous updates while ensuring stability and consistency throughout the application’s lifecycle.

### Change Interceptor

> A mechanism that monitors changes to specific entities or data and triggers events that initiate messaging workflows.

### Channel Priorities

> Settings that determine the importance and order of communication channels to ensure messages are delivered efficiently through preferred pathways.

### Client Analytics

> &#x20;A component of the Observability suite that tracks user interactions, engagement, and feature usage within an application. It helps developers gain actionable insights to guide improvements and future development.

### CommsService.TriggerEvent()

> A helper function in the ComUnity Developer Toolkit that simplifies the process of triggering events programmatically. It abstracts complexities by activating messaging workflows with a single call.

### Communications Data

> Refers to the data exchanged and transmitted through a communication service. It encompasses the information, messages, or signals sent and received between users, devices, or applications using a communication service.

### Communication Flow

> The end-to-end process of triggering an event, configuring templates, and delivering messages through defined communication channels.

### Communications

> An event-driven API within the ComUnity Developer Toolkit that enables developers to integrate centralised messaging workflows triggered by specific application events. These workflows involve the series of actions that occur between triggering an event and successfully delivering a message to target users across multiple channels, including email, SMS, in-app messaging, push notifications, HTTP, and WhatsApp. Communications are centralised, automated, and event-driven to streamline the delivery of messages and enhance user engagement.

### Communication Settings

> Configuration options in the Toolkit that allow developers to define messaging workflows, set channel priorities, and incorporate pre-defined or custom values for dynamic communication.

### Communications Service

> A service that manages the delivery of messages across diverse communication channels. It operates independently and processes events without referencing other services, such as the Data Service.

### Communication Channels

> The pathways through which communication is delivered, including:
>
> * Email
> * SMS
> * WhatApp
> * In-App Messaging
> * Push Notifications
> * HTTP

### Concurrent Responses

> A metric that tracks the number of simultaneous responses handled by the server. Monitoring concurrent responses provides insight into system load and its ability to handle high-traffic conditions.

### Configuration of Application Settings

> Refers to the process of specifying and adjusting parameters, options, and preferences that control the behaviour and functionality of an application. This includes setting values for configurable aspects such as database connections, API keys, user interface preferences, feature toggles, and other customisable settings.

### Copy Entities

> Refers to the process of duplicating or replicating entities, such as data objects, files, or database records. It involves creating an exact or partial copy of the original entity for preservation or manipulation separately.

### Controller Class

> A class responsible for managing the interaction between virtual entities and external services. The controller class handles logic and REST operations, enabling data fetching, updating, and CRUD operations from the external service within the Toolkit.

### Create a Project

> The process of starting a new project in the ComUnity Developer Toolkit by selecting a template or using a blank template, and entering the necessary project details.

### CRUD

> CRUD refers to the four major functions implemented in database applications: create, retrieve, update, and delete. These functions serve as user interfaces to databases, allowing users to perform operations such as creating new records, retrieving existing data, updating records, and deleting records. CRUD operations manipulate entities in databases and enforce constraints on database tables.

### Cross-Environment Visibility

> A feature that allows users to view how configuration settings are applied across Development, QA, and Production environments, making it easier to spot discrepancies.

### Custom Binding

> A unique domain name added to a custom website in the ComUnity Developer Toolkit. Custom bindings allow developers to configure specific domain addresses for their applications and may require assistance from the Toolkit’s technical team for activation.

### Custom Classes

> System-generated classes within the `<<Project name>>.Custom` namespace, designed to encapsulate custom logic, functionality, or data structures. They allow developers to introduce specialised behaviours, define unique properties, and implement custom functionalities that align with specific project requirements, while promoting modularity and separation of business logic.

### Custom Icon Library

> A feature that allows developers to upload their own custom icons in the form of SVG files, enabling unique branding and personalised designs.

### Custom Website

> A feature in the ComUnity Developer Toolkit used to build standalone websites or web applications when the default functionality of the Integrated Navigation and UI Builder cannot meet specific UI requirements. It enables developers to create solutions with customised designs, layouts, and functionalities beyond the capabilities of the Toolkit’s standard screen-building tools.

### Customising the Data Model

> Customising the data model refers to the process of modifying or extending the structure and schema of a database or data storage system to meet specific requirements or business needs. It involves making changes to entities, attributes, relationships, constraints, and other elements of the data model to align with the unique data structures and functionalities required by the software application.

### Custom Workflows

> Sequences of automated tasks or processes that can be created and managed within the Toolkit to handle routine operations or complex data flows using Azure Function Apps.

### Data

> In the ComUnity Developer Toolkit, _data_ refers to the structured information organised into entities, attributes, and relationships that form an application’s data model. The Toolkit supports defining this model as either a Diagram (Entity Relationship Diagram, ERD) or a List, which is then translated into a Visual Studio project via Entity Framework Code First. This enables an efficient and direct transition from data model design to database structure, optimising data management and customisation.

### Data Model

> The structured framework that outlines the organisation of data within a project, including entities, attributes, relationships, and constraints, serving as the foundation for database schema design.

### Data Privacy

> Data privacy refers to the protection of individuals' personal information and ensuring that their sensitive data is handled securely, used appropriately, and not accessed or disclosed without their consent. It involves implementing measures and practices to safeguard data against unauthorized access, misuse, or disclosure.

### Data Types

> A data type is an attribute that specifies the type of data that the object can hold: integer data, character data, monetary data, date and time data, binary strings, and so on. The properties of a field describe the characteristics of data added to that field. A field's data type is the most important property because it determines what kind of data the field can store.

### Debugging

> Debugging requires the developer to examine the flow of control and the values of variables that caused a bad result, an exception to be thrown, or some other problem, in the process to resolve issues in the build.

### Deleting Entities

> In the ComUnity Developer Toolkit, efficient data management includes the ability to delete entities and entity fields when they are no longer needed in your data model. This section focuses on the functionality provided by the toolkit to remove entities and their associated fields.

### Deployment

> The process of making a software application or system available and operational in a particular environment. It involves the installation, configuration, and setup of the software or system so that it can be used by end-users or integrated into a larger infrastructure.

### Deployment History

> A detailed record of past deployments within an environment (e.g., Development, QA). This history includes deployment names, dates, and status, providing insights into deployment patterns and aiding troubleshooting.

### Development Environment

> The default environment where developers write, test, and refine code. This environment is isolated to ensure code integrity and allows free experimentation before moving the code further down the pipeline.

### Diagram View

> A graphical representation of the data model within the ComUnity Developer Toolkit. The Diagram view allows developers to visualise entities and their relationships, select entities to view or edit properties, and design data structure visually.

### Digital Platform

> A Digital Platform is a bespoke Platform as a Service (PaaS) product composed of people, processes, and tools that enable teams to rapidly develop, iterate, and operate Digital Services at scale.

### Domain Mappings

> A feature in Project Settings that enables the setup and management of domain names associated with a project, ensuring accurate URL mappings across deployment environments. _This feature is applicable to versions of the Toolkit prior to 24.x._

### Dynamic Action Templates

> Configurable templates that define the behaviour, content, and delivery of messages for specific events. These templates can be customised across supported communication channels, such as email, SMS, in-app messaging, push notifications, HTTP, and WhatsApp.

### Dynamic List Rendering in Form Pages

> Refers to the process of generating and displaying lists or collections of data dynamically within a form-based web page or application. It involves populating a list or dropdown menu with data retrieved from a data source, such as a database, API, or user input, allowing users to select or interact with the list items.

### Entity

> A distinct data object or concept within a data model, representing a real-world item (such as a customer or product) that includes attributes to define its characteristics and relationships to connect with other entities.

### Entity Associations

> Associations refer to the relationships between different entities in a data model, such as one-to-one, one-to-many, or many-to-many. These associations define how entities are logically connected or related within the model.

### Entity-Level Access Control

> A security measure that manages permissions at the entity level, determining which roles have access to specific entities. Entity-Level Access Control allows developers to configure entity access based on the roles defined in the project, ensuring data privacy and security.

### Entity Framework Code First

> A development approach within the .NET framework where a data model is defined in code (typically using C#), and the underlying database structure is generated based on this code, allowing for flexibility and control in data modelling for additional details view [Tutorial: Get Started with Entity Framework 6 Code First using MVC 5](https://learn.microsoft.com/en-us/aspnet/mvc/overview/getting-started/getting-started-with-ef-using-mvc/creating-an-entity-framework-data-model-for-an-asp-net-mvc-application).

### Entity Hierarchy and Inheritance

> The organisational structure where entities share common attributes and behaviors through inheritance. This feature allows developers to set up parent-child relationships, enabling entities to inherit properties and reduce redundancy in the data model.

### Entity Navigations

> In the ComUnity Developer Toolkit, _Entity Navigations_ are properties within an entity class that provide access to related entities in the data model. Leveraging Entity Framework Code First, these navigations are automatically generated based on defined associations, allowing developers to traverse relationships, such as one-to-many or many-to-many, and enabling easy access to associated data directly within the code. Defined as reference or collection properties, entity navigations streamline the retrieval and management of related entities, supporting efficient interaction across connected data structures.

### Entity Property

> The set of attributes and configurations that define an entity’s characteristics within the data model. These properties include name, data type, constraints, and relationships, offering control over the structure and behaviour of each entity.

### Entity Relationship Diagram (ERD)

> A graphical representation of an application’s data model showing data entities, their attributes, and the relationships between them. ERDs aid developers in understanding, designing, and optimising complex data structures within a database schema.

### Entity Hierarchy

> The structured arrangement of entities within the data model where entities inherit properties and behaviours from parent entities. This hierarchical setup promotes data consistency, reuse, and logical organisation, especially in complex models.

### Environments

> The distinct stages in the deployment process, each designed to handle specific aspects of development, testing, and live production. These include Development, QA/Testing, and Production environments, with visual cues to differentiate them.

### Environment-Specific Observability

> A configuration requirement where observability features must be activated for each deployment environment individually. This ensures precise monitoring and analysis of application performance in different environments.

### Error Identification

> The process of detecting errors and exceptions within an application using trace data. Tracing enables developers to trace errors back to their source for faster resolution.

### Event (Communications)

> A specific occurrence or action within an application that serves as a trigger for messaging workflows. Events are associated with entities and initiated programmatically using helper functions like CommsService.TriggerEvent().

### Event (Notifications)

> A significant system-level occurrence or change that is logged and monitored for system integrity, performance, and user awareness. Events are categorised into Platform, Organisation, Project, Toolkit, or Unknown and are associated with severity levels to prioritise responses.

### Event Action

> A mechanism that executes predefined automated workflows or responses in reaction to events or notifications triggered by the communication service. Event Actions monitor specific events or signals and perform actions based on those triggers, enabling efficient and automated responses within the system.

### Event-Driven Architecture

> A software design pattern where messaging workflows are initiated in response to events. The ComUnity Platform leverages this architecture to facilitate communication through events exposed via REST APIs.

### Event Details

> The configuration settings for event templates. This includes specifying data sources and key information required for building dynamic templates.

### Event Templates

> Templates that govern the behaviour and delivery of messages for an event. Developers can configure these templates by customising their content, format, and channel-specific settings.

### Field Types

> Refers to the different categories or classifications of data that can be stored within a field or column of a database or data structure. It defines the type of data that can be assigned to a particular field and determines how the data is stored, validated, and processed.

### Form Controls

> Refers to interactive elements or components used in user interfaces to gather input from users within a form. They provide a way for users to enter data, make selections, and interact with a software application or website.

### Friendly File Name

> A human-readable name mapped to the SHA file name in the Filenames Data Service for ease of identification and retrieval.

### Form pages

> A _Form page_ is a screen type used for embedding forms to perform Create, Read, Update, and Delete (CRUD) operations. It can also display static elements (e.g., text, images) and dynamic lists. Form Pages can be integrated as top-level navigation screens or as sub-screens linked through Page Links and other controls. They are configurable with properties like title, icons, role-based access, entity names, and Target URLs for data operations.

### Foreign Key Property

> An attribute in an entity that links it to another entity, enforcing a relationship through a reference key. In the ComUnity Developer Toolkit, foreign key properties are automatically generated in entity associations, ensuring data integrity between related entities.

### Full Deployment

> A complete deployment of all components of an application, including the Data Service, Authorisation Service, Client, Communication Service, Configuration, and Screens. Full deployment is used for major updates or when structural changes require all components to be redeployed.

### Function App Package

> A compressed **.zip** file containing the core code and configuration files for an Azure Function App. This package must meet Azure specifications and include only essential files to ensure successful deployment.

### Graphics Magick Modifiers

> A set of operations applied to images fetched from the Media Server for manipulation. Examples include resizing, cropping, rotating, blurring, and applying effects such as sepia or oil painting.

### Group Templates

> Complex templates designed to create fully-fledged applications with multiple features. These can be selected during project initialisation or applied to extend the functionality of existing projects.

### Hierarchical Relationship

> A parent-child relationship between entities within the data model established through inheritance. Hierarchical relationships allow child entities to inherit attributes from parent entities, supporting efficient data modelling and minimising redundant configurations.

### Hierarchical Structure - Screens

> The _Hierarchical Structure_ within the ComUnity Developer Toolkit refers to the organisational layout of screens using a tree-like format, where top-level screens act as primary nodes that define the application’s main navigation. These screens can have nested child nodes (Navigation and Form pages), creating a structured navigation flow for managing content and user interactions.

### Icon Management

> A feature in the ComUnity Developer Toolkit that allows developers to browse, manage, and implement icons from various libraries such as Bootstrap Icons, [Font Awesome 6](https://fontawesome.com/), [Devicon](https://devicon.dev/), and [Material Design](https://m3.material.io/styles/icons/overview), as well as upload custom icons for projects.

### Image Transformation Pipeline

> A declarative system in the Media Services that dynamically processes images to adapt them to device capabilities, optimising bandwidth and processing resources.

### Image Modifiers

> Parameters appended to image URLs to manipulate images dynamically. Examples include `$resize`, `$crop`, `$rotate`, `$blur`, `$sepia`, and more.

### Inheritance

> A feature in the ComUnity Developer Toolkit that enables entities to inherit properties and behaviours from a designated parent entity. Inheritance allows for the creation of hierarchical relationships within the data model, reducing redundancy and facilitating efficient data structure design.

### Inherits from Entity

> A property in each entity’s configuration that specifies its parent entity, defining the inheritance relationship. By setting the _Inherits from Entity_ value, developers can establish hierarchical links between entities, creating a layered structure within the data model.

### Integrated Navigation and UI Builder

> Refers to the feature in the ComUnity Developer Toolkit that enables developers to create and manage navigation structures and user interfaces for screens.

### Integrations

> Refers to the process of connecting different software systems, services, or components to work together and exchange data seamlessly. It involves creating bridges between disparate systems to enable interoperability and streamline workflows.

### Images Text Content

> Refers to the textual information embedded within an image or associated with an image. It involves the practice of including descriptive or explanatory text within the image itself or providing text content that is related to the image.

### [Jaeger](https://www.jaegertracing.io/docs/1.18/)

> An open-source tracing tool integrated into the ComUnity Platform for monitoring and troubleshooting distributed systems. Jaeger supports the collection, visualization, and analysis of trace data to enhance system observability.

### Key Vault Integration

> A security feature that allows sensitive configuration settings, such as passwords and API keys, to be stored securely using Azure’s Key Vault, providing encryption and protection for these values.

### Launch

> An action that opens the web version of your project in a browser without rebuilding, used when no modifications have been made since the last build.

### Legacy Icons

> Icon sets from older versions of the ComUnity Developer Toolkit that are still supported for backward compatibility.

### List (Data Model Representation)

> A non-visual, structured representation of the data model where entities, attributes, and relationships are organised as a list, offering a simpler alternative to [ERD](glossary.md#entity-relationship-diagram-erd) for defining data models without a graphical diagram.

### List Dynamic List Rendering

> Refers to the process of dynamically generating and rendering a list of items in the navigation pane or sidebar of a user interface. This list is populated with data retrieved from a data source or generated programmatically.

### List View

> A non-graphical, structured representation of the data model within the ComUnity Developer Toolkit. The List view organises entities and their properties in a list format, allowing developers to manage data structure through a straightforward, text-based interface.

### Major Version

> The first number in the versioning convention (e.g., _X_.0.0), representing significant changes or breaking updates to the application. These updates may introduce new functionality, alter existing features, or require user intervention to upgrade due to potential compatibility impacts.

### Managed Media Server

> A secure media server configuration that enforces permission-based and time-bound access to storage resources, increasing application security.

### Manual Role Assignment

> The current process by which the Toolkit Administrator assigns users to organisations manually, after which the Organisational Administrator assigns their specific roles.

### Material Design Icons

> An icon library integrated into the Toolkit, offering icons based on Google’s Material Design principles.

### Media

> Content types supported by the ComUnity Platform’s Media Services, including structured data (API-driven) and unstructured data (e.g., files, images, videos). Media enriches digital solutions by enabling efficient content processing and management.

### Media Services

> A robust component of the ComUnity Platform responsible for processing and managing structured and unstructured data, supporting operations such as uploads, downloads, and media transformations.

### Metrics

> Quantitative data points that monitor the real-time performance, resource utilisation, and operational health of an application. Metrics help identify system behaviour trends, optimise resource usage, and resolve issues proactively.

### Metrics Dashboard

> &#x20;A visual interface in the ComUnity Toolkit that presents detailed metrics data, including graphs and trends, to monitor project performance. It includes key indicators such as server response times, concurrent responses, accumulative users, and daily request volumes.

### Microsoft URL

> The URL of an application’s listing on the Microsoft Store, used for Windows apps.

### Minor Version

> The second number in the versioning convention (e.g., 1._X_.0), indicating incremental updates that add new features or improvements without introducing breaking changes. Minor versions enhance functionality while maintaining compatibility with existing systems.

### Media Server

> Refers to a computer or network device that stores, manages, and distributes multimedia content such as audio, video, images, and other media files.

### Meta Data (Integrations)

> Information required to define an integration, typically including the [OpenAPI/Swagger ](https://swagger.io/specification/)specification. MetaData enables the Toolkit to auto-generate proxy classes and streamline communication with external services.

### Moustache Templating

> Refers to a logic-less template syntax that allows developers to generate dynamic content by filling in placeholders within a template. It separates presentation and logic, making web applications easier to maintain and reuse.

### Navigation page

> _Navigation pages_ are specialised screens in the ComUnity Developer Toolkit that enable the creation of complex navigation structures within an application. They are versatile, capable of displaying both static content (like text, images, and lists) and dynamic content retrieved from entities, lists, or custom objects. These pages are based on the _List_ node type, allowing them to contain other Forms, Lists, and Screen Controls, making them highly adaptable to various navigation requirements. Navigation Pages can be directly integrated into the navigation hierarchy, enhancing the flexibility and depth of your app’s structure.

### Observability

> &#x20;A feature in the ComUnity Developer Toolkit that provides tools to monitor and analyse an application’s performance, usage, and behavior across deployment environments. It includes capabilities such as client analytics, metrics, and traces to offer comprehensive insights.

### Observability Integration

> &#x20;A prerequisite for accessing the Metrics Dashboard. Observability must be enabled in the project’s deployment environment to collect and display performance metrics.

### OData

> [OData ](https://www.odata.org/documentation/odata-version-3-0/?msclkid=237b40adce7311ecae5bf187856e481c)helps developers focus on business logic while creating RESTful APIs, providing a standardised way of building and consuming data APIs, which enables interoperability between systems.

### One-to-Many Relationship

> A type of entity association in which a single entity instance is related to multiple instances of another entity. In the Toolkit, a one-to-many relationship is established using Table Links, allowing efficient structuring of hierarchical data.

### One-to-One Relationship

> A type of entity association where each instance of an entity is linked to a single instance of another entity. This relationship is configured through Table Links, creating exclusive pairs between entities for structured data alignment.

### OpenTelemetry

> &#x20;A unified observability framework integrated into the ComUnity Platform that provides standardised tools and APIs for generating and exporting tracing and metric data.

### OpenTracing Data Model

> &#x20;A conceptual framework used to represent trace data. It defines the structure and relationships of traces, spans, and associated metadata within distributed systems.

### Organisation

> In the context of the Toolkit, an Organisation refers to a structured entity, typically representing a company or group, within which users, teams, and projects are managed. An Organisation is registered on the platform and is overseen by an Organisation Administrator, who has full control over its users, teams, projects, and settings.

### Organisational Administrator

> A user responsible for managing all aspects of an organisation within the Toolkit, including managing teams, users, and projects. They have full control over the organization and can assign roles and responsibilities to team members. The user responsible for the complete management of an organisation within the Toolkit.

### Organisation Events

> Events related to organisational activities, such as user management actions, role assignments, and policy updates, which serve as triggers for workflows within the application.

### Organisational Management

> The feature in the Toolkit that enables Organisation Administrators to manage users, teams, and projects within their organisation. This functionality supports a structured and collaborative environment by offering tools for effective oversight.

### Organisational Settings

> A section in the Toolkit accessible only to admins, where the Organisation Administrator can view and modify key details of their organisation, such as the organisation name and user roles.

### Organisation Name

> The name of the organisation linked to the project, displayed within the General section.

### Organisational Settings

> Settings accessible to organisation admins that allow for the comprehensive management of the organisation. This includes managing user roles, permissions, teams, and general organisational settings.

### Page Link

> A _Page Link_ is a screen control in the ComUnity Developer Toolkit used to extend the navigation hierarchy by linking Navigation pages to Form pages. This control facilitates the creation of system-generated Form pages, configurable with properties such as layout type, icons, and access permissions. By using Page Links, developers can efficiently connect different sections within the application, optimising navigation flow and enhancing the user experience.

### Page Analytics Configuration

> A setup process initiated by clicking "Create Page Analytics Configuration" in the environment settings. This action activates observability features, allowing data collection for analytics, metrics, and traces.

### Partial Deployment

> A deployment method where only specific parts of the application (e.g., Authorisation Service, Communication Service, Configuration) are updated. It is used for minor updates or fixes that do not require redeploying the entire application.

### Platform Events

> Critical system-level occurrences within the platform, such as outages, resource limits (e.g., disk space or memory), or critical errors, that trigger messaging workflows or require immediate attention.

### Permissions

> The specific actions and operations a user is allowed to perform based on their assigned role. Permissions control access to sensitive features and data within the Toolkit.

### Performance Bottleneck

> A specific point in an application workflow where performance is significantly slowed, often identified using trace data. Bottlenecks can include long request durations, resource contention, or inefficient processes.

### Performance Monitoring

> The practice of tracking, analysing, and optimising key performance indicators (KPIs) such as response times, request volumes, and user engagement to maintain system health and reliability.

### Permissions Interface

> An intuitive configuration tool within Table Security that displays a list of available roles and associated permissions. This interface allows developers to easily enable or disable permissions for each role, providing precise control over entity access.

### Production Environment

> The deep purple environment where fully tested and stable applications are deployed for end users. This is the final stage in the deployment process and requires careful planning to maintain service continuity.

### Project

> A project in the ComUnity Developer Toolkit refers to the namespace and all configurations that define an application. Each project belongs to a single tenant.

### Project Events

> Events related to organisational activities, such as user management actions, role assignments, and policy updates, which serve as triggers for workflows within the application.

### Project Name

> A unique identifier entered during the project creation process that distinguishes a project within the ComUnity Developer Toolkit.

### Project Settings

> A section within the ComUnity Development Toolkit that allows users to manage key configurations for a project, such as versioning, application name, namespace, and organisation details.

### Project Owner

> The individual responsible for managing a specific project, including overseeing progress, assigning teams, and controlling access to project details. They operate under the guidance of the Organisational Administrator.

### Project Management

> The responsibility of overseeing all projects within the organisation, including assigning project ownership and ensuring the efficient execution of project tasks.

### Properties Dialogue

> A section in the Toolkit’s interface where users can view and adjust the properties of an entity or field. The Properties Dialog provides access to customisation options and settings, supporting detailed data model configuration.

### Property Type

> The property type specifies the kind of data that can be stored in an entity property. It defines the format and constraints for the data, such as text, number, boolean, date, and relationship.

### QA/Testing Environment

> A vibrant purple environment used for testing code after the development phase. This environment closely mimics the production environment to identify potential issues and ensure the application functions correctly before it reaches end users.

### Razor

> [Razor](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-9.0) is a markup syntax that allows embedding server-based code (such as Visual Basic and C#) into web pages. It combines HTML markup with server-side code to generate dynamic content.

### Razor Syntax

> Razor syntax is used to template communication data into channels. Fields in the template accept both static and dynamic content, and when the system executes an action, expressions are evaluated and fields are resolved.

### Relationship

> Relationship is a property type used to establish connections between entities. It represents associations or dependencies between entities, for example, a "user" entity may have a "orders" relationship property linking it to order entities.

### Required

> Required is a property attribute that specifies whether a property must have a value. If a property is marked as required, it cannot be left empty or null.

### Requests per Day

> &#x20;A metric that displays the daily volume of requests to the system over a 7-day period. It helps identify usage patterns, peak load times, and stress points on the project's infrastructure.

### Role Based Permissions

> Access control settings that define which roles can perform specific actions on entities. In the Toolkit, role-based permissions allow developers to manage user access to data, ensuring only authorised roles can read, update, or delete information within the data model.

### Roles

> Defined positions within the Toolkit that determine a user’s level of responsibility and access to specific tasks, projects, and operations. Roles are assigned to users to structure their contributions and permissions within an organisation.

### Root Cause Analysis

> A troubleshooting process that uses trace data to determine the underlying cause of an issue or anomaly within an application. Tracing provides detailed context to understand _what_ happened and _why_.

### Runtime Stack

> The specific runtime environment selected for an Azure Function App, such as .NET, Node.js, or Python. This defines the programming environment in which the function executes.

### Template

> Preconfigured application components, including entities, associations, navigation, screens, and application objects, that can be added to a project to quickly implement specific features. Templates can also be used to bootstrap new projects, providing ready-made functionality to accelerate development.

### Scheduled Tasks

> Workflows that run automatically on predefined schedules (e.g., daily, weekly, or periodic operations like data syncing).

### Screen Controls

> Screen Controls refer to the interactive widgets and components used within the Screen Structure section of the Integrated Navigation and UI Builder in the ComUnity Developer Toolkit. These controls enable developers to build and customize the layout and functionality of screens, supporting dynamic user interactions and flexible content presentation. Screen Controls can be used to adjust the appearance, behavior, and content of screens, enhancing the application’s overall user experience.

### Screen Structure

> _Screen Structure_ is a section within the Integrated Navigation and UI Builder in the ComUnity Developer Toolkit. It allows developers to build and visualise the layout of application screens using various screen controls.

### Screen View

> A component within the ComUnity Developer Toolkit where developers can build, organise, and manage application screens.

### Screens

> In the ComUnity Developer Toolkit, _**Screens**_ refers to both a core concept for building an application’s user interface and the section within the _**Integrated Navigation and UI Builder**_ used to view and manage all screens in an app.
>
> _Screens_ are organised into three main categories:
>
> • **Hierarchical Screens**:
>
> Structured within a hierarchical tree and include:
>
> \- **Navigation page**: Defines the flow and navigation structure of the application.
>
> \- **Form page**: Handles user input and data entry.
>
> • **Additional Screens**:
>
> Exist outside the main hierarchy but can be integrated into forms or lists to extend functionality.
>
> • **System Screens**:
>
> Pre-built screens, such as Login, Registration, and OTP screens, included by default in every project. These can be customised but not deleted, ensuring core functionalities remain intact.
>
> \
> Within the _**Integrated Navigation and UI Builder**_, the _Screens_ section provides a centralised view for organising, managing, and customising all screens within the application, allowing developers to efficiently manage the app’s navigation, structure, and user interactions.

### SHA File Naming

> A file naming convention that uses the SHA (Secure Hash Algorithm) of a file to prevent duplicate uploads and ensure consistency in file identification.

### Serve Response Time

> &#x20;A performance metric displayed on the Metrics Dashboard that measures how long it takes for a server to respond to incoming requests. It helps identify latency issues and optimize server performance.

### Severity Levels (Notifications)

> The classification of events and notifications based on urgency, ensuring prioritized action:
>
> • Low: Informational, no immediate action required.
>
> • Medium: Monitoring recommended.
>
> • High: Requires prompt attention.
>
> • Critical: Urgent action needed to prevent significant issues or failures.

### Structured Data

> Data that follows a predefined format and is managed via the OData protocol. It includes APIs for data manipulation and URL-based queries for information retrieval.

### SQL Table Mapping

> The process of creating an entity in the data model that corresponds to an existing SQL table. This feature allows developers to integrate legacy or pre-existing database structures directly into the ComUnity Developer Toolkit, automatically generating entity fields to match the table columns. SQL Table Mapping saves time and ensures data consistency by leveraging existing data schemas within the Toolkit.

### System Screens

> Pre-built screens, such as Login, Registration, Reset Password, and OTP screens, that are part of every project by default and can be customised but not deleted.

### System Reliability

> The ability of a project or system to maintain stable performance and prevent failures. Metrics help enhance system reliability by identifying performance trends and potential issues early.

### Table Security

> A feature within the ComUnity Developer Toolkit that enables the configuration of role-based permissions for entities. Through Table Security, developers can grant or restrict access to specific actions (e.g., read, update, delete) for different roles within a project, enhancing data security and access control.

### Table Links

> A feature in the ComUnity Developer Toolkit that allows users to establish and configure associations between entities, such as one-to-one or one-to-many relationships. Table Links create connections between entities, supporting data integrity and enabling foreign key relationships and cascading actions.

### Table Link Properties

> Configurable settings associated with a Table Link that define the behaviour and characteristics of an entity association. These properties allow developers to customise how entities relate to each other, including setting cascading actions and defining foreign key constraints.

### Team

> Groups of users within an organisation who collaborate on specific tasks or projects. Each team is composed of members with defined roles, such as Developers, Testers, or Designers, and is created and managed by the Organisation Administrator and Project Owners.

### Team Management

> The Organisation Administrator’s task of creating, assigning, and managing teams within the organisation. This includes determining the team composition and modifying roles to optimise project collaboration.

### Tenant

> An instance of the ComUnity Platform, provisioned to an organisation during account registration. Each tenant is distinct and unique, identified by a system-generated name, and can manage multiple projects.

### Template - Communication Service

> A communication service template is a preconfigured, reusable framework that provides a foundation for building communication functionalities within the ComUnity Platform. It serves as a starting point for developing services that support messaging, notifications, real-time data exchange, collaboration, and other forms of interaction between users or system components.

### Temporal Table

> Temporal Tables, also known as System-Versioned or Time Travel Tables, are designed to track changes over time, maintaining a full history of data changes, and allowing easy point-in-time analysis.
>
> **Key Points:**
>
> * **Time-Based Versioning:** Maintains a history of changes made to data over time.
> * **Tracking Changes:** New versions of rows are created when modifications are made.
> * **Querying Historical Data:** Simple queries retrieve data as it existed at any specific point in time.
> * **Automatic Data Maintenance:** Temporal Tables automatically manage versioning and retention.
> * **Database Support:** Supported in DBMS like Microsoft SQL Server, PostgreSQL, and Oracle.

### Themes

> Themes allow developers and designers to create visually appealing and user-friendly interfaces by providing a consistent visual design. They offer a flexible way to customise the appearance of an application without affecting functionality.

### Toolkit Administrator

> A user with the highest level of access within the Toolkit, responsible for the overall management of all organisations, projects, and users. This role includes system-wide control and configuration abilities, such as user approvals and organisation management.

### Traces

> &#x20;A feature that captures detailed execution paths of application requests, providing a step-by-step breakdown of processes. Traces help identify bottlenecks, latency issues, and areas for optimization in request flows.

### Trace Span

> A unit of work within a trace that represents a single operation or step in the execution of a request. Spans include metadata such as timestamps, durations, and tags to provide granular insights.

### Unknown Events

> Events that do not fit predefined categories but are captured for further classification or processing.

### Uniform Resource Identifier (URI)

> A URI is a string of characters used to identify and locate resources on the Internet. It consists of components like scheme, authority, path, query, and fragment, with scheme and path being mandatory.

### Unique

> Unique is a property attribute that ensures the uniqueness of values within that property across all entities. No two entities can have the same value for a unique property.

### URL

> A URL is a subspecies of URI. It is often used to address web pages but can also localize files in the local file system. Every Internet address is a URL, but not every URL is an Internet address.

### User Management

> The process of managing user accounts within an organisation, including granting access, assigning roles, and maintaining user information. Organisation Administrators handle user management through the Organisational Settings.

### Validation

> Validation ensures that data meets certain criteria or constraints, ensuring that the data entered is valid and consistent with specified rules.

### Virtual Entities

> In the ComUnity Developer Toolkit, a _Virtual Entity_ is a type of entity used to represent and integrate data from external services within a project. Virtual entities allow developers to seamlessly connect with external data sources, performing CRUD operations and enabling their data to appear alongside local entities in the project.

### Weather Icons

> A specialised icon set integrated into the Toolkit, containing weather-related symbols for use in applications that require weather visualisation.

### Web Config Class

> A configuration class in the Toolkit’s Web API setup that manages HTTP interactions with external services. It ensures that virtual entities can process OData requests and responses, which allows standardised querying and data manipulation.

### Web Deployment Package

> A compressed archive containing all necessary files, including configuration settings, needed to deploy an application to an IIS server. This package is prepared using tools like Visual Studio and is uploaded during the deployment process.

### WhatsApp Business Integration

> Refers to connecting and integrating the WhatsApp Business API with other systems or applications. It enables businesses to communicate with customers on WhatsApp, send automated messages, provide support, and facilitate transactions.
