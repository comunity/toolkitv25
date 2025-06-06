# Login

## Overview

The ComUnity Developer Toolkit is a cloud-based solution deployed in [Microsoft Azure](https://azure.microsoft.com/), accessible from any browser. The URL you use to access the Toolkit depends on your organisation’s deployment type:

1\. Shared Multi-Tenancy Environment:

For organisations using the shared ComUnity environment, access the Toolkit via, the [URL](https://toolkitnxt.comunity.me/):

```

https://toolkitnxt.comunity.me/

```

This environment is often used for testing or as part of a multi-tenancy organisational license.

2\. Single-Tenancy Deployment:

For organisations with dedicated Toolkit instances, use the unique URL provided by your administrator. Single-tenancy deployments are hosted in isolated environments for enhanced security and customisation.

{% hint style="success" %}
Use the Toolkit on your desktop for the best possible development experience.
{% endhint %}

The Toolkit supports multiple authentication options to cater to organisational needs. With the release of v24.4, [Microsoft Entra](https://www.microsoft.com/en-za/security/business/microsoft-entra) authentication was introduced for single-tenancy instances hosted in [Microsoft Azure](https://azure.microsoft.com/).

<figure><img src="../../.gitbook/assets/image (31).png" alt="" width="321"><figcaption><p>ComUnity Developer Toolkit - Login options</p></figcaption></figure>

1. [Password-Based Authentication](login.md#password-based-authentication)
2. [Microsoft Entra Login](login.md#microsoft-entra-login) (_Available in  v24.4 and above)_

## Password-based Authentication

Password-Based Authentication is the default login method for users in both shared and single-tenancy deployments. It enables users to securely access the Toolkit using a unique username and password combination provided during registration.

If you are a registered Toolkit user and your registration request has been approved, you can log into the Toolkit using your provided credentials. Upon successful login, you will be directed to the Home Screen, where you can access the Toolkit’s features and functionalities.

### Registration

To create a new user account in the ComUnity Platform, please follow these steps:

1. From the **Home Screen**, click on **Request Access**.
2. You will be directed to the **Request Access** screen.
3. Complete the **Request Access** form by providing your relevant details.
4. Finally, click on the Register button to submit your account request.

Ensure accurate and complete information to expedite the account creation process.

{% hint style="danger" %}
All fields marked with an asterisk \* are required.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (396).png" alt="" width="314"><figcaption><p>ComUnity Developer Toolkit - Register</p></figcaption></figure>

{% hint style="info" %}
After completing your registration, please be aware that your approval may take up to 24 hours to be processed on weekdays. If you registered on a weekend, please note that the waiting period may extend to the first day of the week.
{% endhint %}

### Password Reset

To reset your password, follow these steps:

1. Go to the login screen of the ComUnity Developer Toolkit, as instructed above.
2. Click **Forgotten your password?**
3. Enter your username.
4. For security purposes, the ComUnity platform will need to verify your identity before you can proceed with resetting your password. You will receive a one-time password (OTP) via your preferred channels, if available. Otherwise, it will be sent to the main channel associated with your registered account (e.g., email or SMS).
5. Retrieve the OTP.
6. Enter your new password and OTP in the relevant fields provided.
7. Click **Reset Password**.

## Microsoft Entra Login

As of version 24.4, the ComUnity Developer Toolkit supports [Microsoft Entra](https://www.microsoft.com/en-za/security/business/microsoft-entra) as an authentication mechanism, enabling organisations to facilitate secure sign-ins for their users and partners. This integration offers a seamless, enterprise-grade authentication flow, aligning with modern identity management practices. Microsoft Entra authentication is available exclusively for single-tenancy Toolkit instances deployed in Azure environments.\
\
The introduction of Microsoft Entra authentication enhances the Toolkit’s ability to serve organisations managing complex authentication requirements for their users and partners. By leveraging Microsoft Entra, organisations can provide a unified authentication experience while maintaining high security standards and scalability.\
\
**Advantages**&#x20;

• **Unified Authentication**: Supports both user and partner sign-ins.

• **Enterprise-Grade Security**: Utilises OAuth 2.0 and OpenID Connect protocols.

• **Simplified Management**: Reduces administrative overhead in [Microsoft Azure](https://azure.microsoft.com/)-hosted single-tenancy deployments.

**Limitations**

• [Microsoft Azure](https://azure.microsoft.com/) Deployment Only: Microsoft Entra authentication is exclusive to single-tenancy instances hosted in Azure and is not supported in shared environments or the multi-tenancy ComUnity Platform.

### Steps to Sign In with Microsoft Entra

1\. Ensure you are signed into your organisational-issued Microsoft account. If not, visit [Microsoft Account Login](https://login.microsoftonline.com/) and authenticate.

2\. Open your organisation’s Toolkit instance URL (e.g., https://yourorg.domain).

3\. On the login screen, click Login with Microsoft. You will be authenticated and automatically redirected to the Toolkit’s Home Screen upon successful login.

