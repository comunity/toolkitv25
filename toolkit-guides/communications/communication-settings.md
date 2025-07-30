# Communication Settings

This section outlines how to configure communication settings within the ComUnity Toolkit. It includes:

* Global and environment-specific configuration
* Supported communication channels
* Provider setup requirements
* Best practices for secure and reliable messaging workflows

{% hint style="info" %}
**Version Note**

> The features in this section are available from ComUnity Toolkit version 25.2 onwards.
>
> If you’re planning to manage communication credentials independently for QA, Dev, and Production environments, upgrading to v25.2 or later is strongly recommended.
{% endhint %}

## Configuration Overview

The Toolkit supports communication via multiple channels, including [**Email**](configuring-dynamic-action-templates-for-event-driven-communication-channels/email.md), [**SMS**](configuring-dynamic-action-templates-for-event-driven-communication-channels/sms-and-whatsapp.md), [**INAPP**](configuring-dynamic-action-templates-for-event-driven-communication-channels/inapp.md),[ **Push Notifications**](configuring-dynamic-action-templates-for-event-driven-communication-channels/push-notifications.md), and [**WhatsApp**](configuring-dynamic-action-templates-for-event-driven-communication-channels/sms-and-whatsapp.md).

Configurations are managed at two levels:

* [**Global Settings**](communication-settings.md#global-settings): Application-wide constants and default priorities used across all environments.
* [**Environment-Specific Settings**](communication-settings.md#environment-specific-settings-v25.2-update): Channel and provider configurations tailored for each environment (e.g., Development, QA, Production).

{% hint style="warning" %}
In deployed environments, users are fully responsible for setting up third-party providers and securely managing all credentials.
{% endhint %}

## **Global Settings**

Global settings define the baseline behaviour and default data for communications across your project.

1.  **Channel Priorities**

    * Access: **Project Settings** > **Global** > **Communications**
    * Description: These settings establish the default delivery importance for each channel.

    | Channel  | Example Priority |
    | -------- | ---------------- |
    | Email    | Medium           |
    | In-App   | Medium           |
    | SMS      | Medium           |
    | WhatsApp | Medium           |


2.  **Custom Values**

    * Access: **Project Settings** > **Communications** > **Custom Values**
    * Description: Used to define and inject global constants into your application logic. Each value can be toggled to apply globally or be overridden per environment. Sensitive values can be marked with a secrecy shield.

    | Setting Name       | Example Value                  | Description                          |
    | ------------------ | ------------------------------ | ------------------------------------ |
    | Tenant             | `ComUnityTest`                 | Identifier for multi-tenant setup.   |
    | SourceEmailAddress | `noreply@comunityplatform.com` | Default sender address.              |
    | ReplyToAddress     | `noreply@comunityplatform.com` | Email used for replies.              |
    | ReplyToEntity      | `MessageEvent`                 | Binds replies to a messaging entity. |
    | Namespace          | `comcity`                      | Logical grouping for communications. |
    | LogLevel           | `3`                            | Verbosity of system logging.         |
    | FromAddress        | `noreply@comunityplatform.com` | Alias used for outbound messages.    |



## Environment-Specific Settings (v25.2 Update)

From version 25.2, the ComUnity Toolkit provides an enhanced interface for managing communication settings independently for each environment. This allows you to define a specific communication provider and its unique credentials for each supported channel, ensuring a clear separation between your Development, QA, and Production configurations.

**Configuration Steps**

1. Navigate to the **Communications** hub
   * Access the settings via **Project Settings** > **Communications**.
   * Select the tab for the environment you wish to configure: **Dev**, **QA**, or **Prod**.
2. Select a Communication Channel
   * Within the chosen environment, select the tab for the channel you want to set up (e.g., Email, SMS, Push, In-App, WhatsApp).
3. Choose a Service Provider
   * From the Service Provider dropdown, select the provider you wish to use for the chosen channel.
   * Click the Save icon to apply your selection — any dynamic fields required by the selected provider will then appear automatically.
   * For local development and testing, it’s recommended to use the Mock Service option.
4. Enter Provider Credentials
   * Once a provider is selected, the required configuration fields (e.g., API keys, usernames, base URIs) will be displayed.
   * You must obtain these credentials from the provider’s official administration portal and enter them securely into the fields provided.

## **Provider Requirements & Setup Guides**

To integrate external services, you must have an active account with the provider and obtain the necessary credentials.

## Microsoft 365

Follow these steps to register an application in Azure and configure it with the necessary credentials and permissions.

**1. Register the Application**

1. Navigate to the **Azure Portal** → **Azure Active Directory** → **App registrations**.
2. Click + New registration and create a new application (e.g., ComUnityEmailClient).

**2. Record Credentials & Secrets**

1. From the application's Overview page, copy the following IDs:
   * Application (client) ID → Use this for the `O365Client` field.
   * Directory (tenant) ID → Use this for the `O365Tenant` field.
2. Go to the Certificates & secrets tab.
3. Click + New client secret. After creating it, copy the secret's Value.
   * Use this value for the `O365ClientSecret` field.

{% hint style="warning" %}
The client secret value is only displayed once upon creation. Ensure you copy and store it in a secure location immediately.
{% endhint %}

**3. Set API Permissions**

1. Go to the API Permissions tab.
2. Click + Add a permission, select Microsoft Graph, and choose Delegated permissions.
3. Add the following permissions:
   * `Mail.Send`
   * `User.Read`
   * `offline_access`
4. After adding the permissions, ensure you Grant admin consent for your directory.

References: [Learn Microsoft](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365)

### Twilio (SMS & WhatsApp)

1. Login to your [Twilio Console](https://www.twilio.com/console).
2. From the main account dashboard, copy your:
   * `Account SID`
   * `Auth Token`
3. For WhatsApp integration, you must also:
   * Configure approved Senders in your Twilio account.
   * Set the `TwilioWhatsAppUser`, `Password`, `From`, and `Callback` values within the Toolkit.

References: [Twilio SMS Guide](https://www.twilio.com/en-us/guidelines/sms) | [Twilio WhatsApp Guide](https://www.twilio.com/docs/whatsapp/tutorial)

### SendGrid (Email)

1. Login to your [SendGrid Dashboard.](https://login.sendgrid.com/)
2. Navigate to Settings > API Keys.
3. Create an API Key with the necessary permissions and copy the generated key.

Docs: [API Key Setup](https://www.google.com/search?q=%23)

### BulkSMS (SMS)

#### Generating a BulkSMS API Token

1. Log in to the [BulkSMS Portal](https://www.bulksms.com/account/ui/index.html#/login).
2. Navigate to **Settings** > **Advanced Settings** > **API Tokens.**
3. Click **Create Token**.
4. Enter a descriptive name for the token (e.g., ComUnityIntegration).
5. Immediately copy the Token ID and Token Secret.

{% hint style="warning" %}
&#x20;For security reasons, the Token Secret will only be displayed once. Please store these credentials in a secure location, like a password manager
{% endhint %}

<div align="center"><figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure></div>

#### BulkSMS Toolkit Configuration

When configuring the Bulk SMS toolkit, map your credentials as follows:

* **BulkSMSUser**: Use the Token ID.
* **BulkSMSPassword**: Use the Token Secret.

## **CellSys**

The CellSys integration is not self-service. Unlike providers such as BulkSMS or SendGrid, CellSys does not expose full setup documentation publicly. To integrate with engage their support team through their [website](https://cellsys.co.za/). Upon account registration and payment they will provide  API credentials you can use the the platform.

## **Best Practices**

* Secure Storage: Always store sensitive values securely and mark them with the secrecy shield in the Toolkit.
* Limited Permissions: When creating API keys, grant only the minimum permissions necessary for the integration to function.
* Regular Audits: Periodically review provider permissions and credentials to ensure ongoing compliance and security.
* Use Mock Services: Use the built-in mock services for all local development and testing to avoid incurring costs or sending unintended communications.

**For further assistance, please refer to the official provider documentation or contact your system administrator.**
