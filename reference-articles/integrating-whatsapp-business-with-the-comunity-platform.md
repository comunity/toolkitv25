---
description: A technical guide for businesses and developers
---

# Integrating WhatsApp Business with the ComUnity Platform

To integrate WhatsApp Business with the ComUnity Platform, users will need to create accounts on third-party providers that offer APIs for sending and receiving WhatsApp messages programmatically. This integration enables businesses to streamline customer communication and take advantage of WhatsApp's features, such as automation and quick response times. \
\
Several cloud communications platforms offer this service, including [Twilio](https://www.twilio.com/en-us), which provides APIs for sending SMS, voice, and WhatsApp messages programmatically. [Twilio](https://www.twilio.com/en-us)'s WhatsApp API supports sending text, images, and audio files, as well as message templates and message tracking.

To create a [Twilio](https://www.twilio.com/en-us) WhatsApp Sender account from scratch and integrate it with the ComUnity Platform, you'll need to follow these high-level steps:

{% hint style="info" %}
You need a Facebook Business Manager account as part of the verification process for applying for a Twilio Phone Number with WhatsApp capabilities. Facebook owns WhatsApp, and as such, they require businesses to go through a verification process to ensure that they are legitimate and authorized to use WhatsApp for business purposes. The verification process involves connecting your Facebook Business Manager account to your WhatsApp Business account, so you need to have a Facebook Business Manager account to create a WhatsApp Business account on [Twilio](https://www.twilio.com/en-us).
{% endhint %}

1. Sign up for a [Twilio](https://www.twilio.com/en-us) account: Visit [https://www.twilio.com/](https://www.twilio.com/) and click on **Sign up** to create a new [Twilio](https://www.twilio.com/en-us) account. Provide your name, email address, and a password. After signing up, verify your email and phone number as prompted.
2. Access the [Twilio](https://www.twilio.com/en-us) Console: Once your account is created and verified, log in to your [Twilio](https://www.twilio.com/en-us) account and access the [Twilio](https://www.twilio.com/en-us) Console.
3. Enable the WhatsApp Sandbox: Enable the WhatsApp Sandbox in your account by going to the Programmable Messaging section in the [Twilio](https://www.twilio.com/en-us) Console, and then clicking on **Try the Sandbox today** or visiting the WhatsApp Sandbox page directly at [https://www.twilio.com/console/sms/whatsapp/sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox).
4. Configure the WhatsApp Sandbox: Follow the instructions to connect your personal WhatsApp account to the Sandbox by sending a message with a specific code to a [Twilio](https://www.twilio.com/en-us)-provided WhatsApp number. Once connected, you can use the Sandbox to test your WhatsApp integration.
5. Develop your application: With the Sandbox set up, develop your application using the [Twilio](https://www.twilio.com/en-us)  API for WhatsApp, using a supported programming language and following the API documentation: [https://www.twilio.com/docs/quickstart/whatsapp](https://www.twilio.com/docs/quickstart/whatsapp).
6. Create a Facebook Business Manager account: If you haven't already, create a Facebook Business Manager account by following the instructions here: [https://www.facebook.com/business/help/1710077379203657](https://www.facebook.com/business/help/1710077379203657). This account is necessary for the verification process during the application for a [Twilio](https://www.twilio.com/en-us) Phone Number with WhatsApp capabilities.
7. Apply for a [Twilio](https://www.twilio.com/en-us) Phone Number with WhatsApp capabilities: After testing your application in the Sandbox, apply for a [Twilio](https://www.twilio.com/en-us) Phone Number with WhatsApp capabilities. Go to the [Twilio](https://www.twilio.com/en-us) Console, navigate to the Programmable Messaging section, and then click on **WhatsApp** in the left sidebar. Follow the instructions to submit your application for a WhatsApp-enabled [Twilio](https://www.twilio.com/en-us) number. Note that this process requires approval from WhatsApp and may take a few weeks.
8. Configure your [Twilio](https://www.twilio.com/en-us) Phone Number: Once your application is approved, and you have a [Twilio](https://www.twilio.com/en-us) Phone Number with WhatsApp capabilities, configure the number in the [Twilio](https://www.twilio.com/en-us) Console. Set the webhook URLs for incoming messages and status updates, which will point to your application's endpoints.
9. Deploy your application: With your [Twilio](https://www.twilio.com/en-us) WhatsApp Sender account set up and your application developed, deploy your application to a live environment.\


<figure><img src="../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>
