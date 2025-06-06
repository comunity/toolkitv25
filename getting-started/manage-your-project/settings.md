# Project Settings

> The ComUnity Toolkit offers a robust, role-based settings system designed to manage various project specific settings. Understanding these settings is crucial for effective management and configuration. For more detailed information, refer to the relevant sections within Project Settings.

Project configuration in the ComUnity Developer Toolkit is managed through the Project Settings section, which provides a centralised location for defining environment-specific behaviours and data-level controls. Introduced in v24.4, this unified section brings together previously separate Environmental Settings and Project Settings to streamline project setup and governance. While project-level configurations are now centralised, [**Organisation Settings**](../organisations/) remain a distinct area for managing organisation-wide settings.

{% hint style="info" %}
Access to the Project Settings section is permission-based. Only users with the appropriate roles can view or modify these settings. To learn more about managing roles and access within a project, refer to the [Organisations/Roles and Permissions](../organisations/roles-and-permissions.md) section.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (472).png" alt=""><figcaption><p>Access Project Settings</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (473).png" alt=""><figcaption></figcaption></figure>

The new consolidated Project Settings section, with configurations now organised into the following tabs:

1.  Global Tab:

    This tab includes settings applicable across all environments, such as:

    * [General](general.md)
    * [ Versions](app-versioning.md)
    * [Store URLs](store-urls.md)
    * [Themes](themes.md)
    * [Project Teams](../organisations/teams.md#assign-teams-to-a-project)
    * [Communications](../../toolkit-guides/communications/communication-settings.md#project-specific-communication-settings)
    * [Templates](../../toolkit-guides/custom-website/pages/templates.md)
    * [Icons](icon-management.md)
    * [Push Notifications](../../toolkit-guides/communications/configuring-dynamic-action-templates-for-event-driven-communication-channels/push-notifications.md)
2.  &#x20;Environment-Specific Tabs:

    Separate tabs are available for managing configurations specific to each environment:

    * [Development Environment](deploy/environments.md#development-environment-green)
    * [QA Environment](deploy/environments.md#qa-testing-environment-vibrant-purple)
    * [Production Environment](deploy/environments.md#production-environment-deep-purple)

Each environment tab includes the following settings:

* [Configuration](deploy/configuration.md)
* [Communications](../../toolkit-guides/communications/)
* [App users & roles](users-and-roles.md)
* [Observability](../../toolkit-guides/observability/)
* [Function Apps](../../toolkit-guides/third-party-services/azure-function-apps-integration.md)
* Reports

These tabs clearly differentiate between global and environment-specific settings, streamlining navigation and configuration management. Some features, such as Communications, may require management at both the global and environment levels.

### Benefits of the Unified Structure

* Centralised Management: Project-related and environmental configurations are now accessible from a single location.
* Improved Usability: The consolidated structure simplifies the process of configuring and updating settings, reducing the effort required for navigation and management.
