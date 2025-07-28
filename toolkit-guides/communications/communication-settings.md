# Communication Settings

When defining communication events within the Toolkit, it is essential to consider the associated metadata to ensure effective and efficient message delivery. Settings can be applied at two levels: Global and Environment-Specific.

## **Global Settings**

Global settings typically contain application-wide constants. These are managed under the

Project Settings > Configuration tab. This section is where you define constants for your application-level data, such as

`AppName` and `BaseUrl`. For each setting, you can use a toggle to specify whether its value should apply globally across all environments or be set individually for a specific environment.

## **Environment-Specific Settings**

Environment-specific settings allow you to use different services and credentials for each deployment environment (e.g., Development, QA, Production) as of v25.2, these are primarily managed under the **Project Settings** > **Communications** tab.

### Provider-Based Configuration (available from v25.2)

The management of communication settings has been significantly enhanced to provide granular, provider-based control for each environment.

Channel-Based Tabs: Settings are organised into tabs for each communication channel, such as **Email**, **SMS**, **Push**, **InApp**, and **WhatsApp**.

#### **Provider Selection**

&#x20;Within each channel, you can now select a specific `ServiceProvider` (e.g., SendGrid, Twilio, Office 365) for each environment. For testing, a `Mocked` or sandbox provider is also available.

#### **Provider Requirements**

To use most third-party providers, such as Twilio and Office 365, you must have your own active subscription with that service.&#x20;

* For some providers, like SendGrid and Bulk SMS, a pre-configured community option is available, but you can also choose to configure your own.&#x20;
* Dynamic Fields & Credentials:  Selecting a provider will reveal the specific settings required for that service.
* You must obtain the necessary credentials (e.g., API keys, tokens, IDs) from the provider's administration portal to enter into these fields. This documentation includes guidance with screenshots on how to locate these values for supported providers.

Based on the provided screenshots, here is a consolidated overview of the settings required for the supported communication providers:

## Supported Communication Provider Settings

**Microsoft Office 365**

To configure Office 365 as a provider, you need to register an application within Microsoft Azure. The configuration requires the following steps:

* App Registration:
  * Navigate to your app registration's overview page in Azure.&#x20;
  * You will need the `Application (client) ID` and the `Directory (tenant) ID`.&#x20;
* API Permissions:
  * From the API permissions tab, you must grant the necessary permissions for your application.
  * Required permissions may include `Mail.Send`, `Mail.ReadWrite`, `User.Read`, and `offline_access` for Microsoft Graph.
* Client Secret:
  * Go to the Certificates & secrets tab.&#x20;
  * Create aNew client secret.&#x20;
  * The `Value` of this secret will be used as the application password.&#x20;

**Twilio**

For Twilio integration, you will need credentials from your Twilio account dashboard.

* Account SID: This is your account identifier.&#x20;
* Auth Token: This is the authentication token for your account.

**SendGrid**

SendGrid configuration requires an API Key.

* Navigate to Settings and then API Keys in your SendGrid account.
* You can create and manage your `API Keys` from this page. The key itself is used for authentication.&#x20;

**BulkSMS**

BulkSMS provides credentials through its advanced settings.

* API Tokens:
  *   You can manage API tokens under

      Settings > Advanced Settings > API Tokens.&#x20;
  * These tokens provide alternative credentials for the JSON API.&#x20;
* EAPI (Legacy):
  *   The legacy EAPI settings are found under

      Settings > Advanced Settings > EAPI.&#x20;
  * The `EAPI URL` for this service is `https://api-legacy.bulksms.com/eapi`.&#x20;
