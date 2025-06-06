---
description: >-
  Manage app versions for iOS, Android, and Windows with structured updates,
  user notifications for major or minor changes, and clear version control
  throughout your app’s development lifecycle.
---

# Versions

The ComUnity Developer Toolkit enables you to manage app versioning for **iOS**, **Android** and **Windows** applications using the following convection:

```
x.y.z

Whereby:
- x,y and z are dot seperated digits and,
- x denotes the major, y denotes the minor and z denotes the build.
```

When you change the major or the minor, your users will receive an in-app notification prompting them to upgrade to the latest version.

{% hint style="info" %}
Whenever you ship a breaking change update your app version by incrementing either the major or the minor so as to prompt your users to upgrade.
{% endhint %}

### Set application version information

To set up your app version information, follow these steps:

1. **Login to the ComUnity Developer Toolkit**
2. **Select your Project**: From the dashboard, select the project you wish to manage.
3. Open Project Settings: After opening your project in the Toolkit, click the cog icon labelled Project Settings (displayed with a tooltip reading “Project settings”). For additional details on accessing Project Settings, refer to the [General ](general.md)section.
4.  **Navigate to Versions**: In the Project Settings menu, click on the "Versions" option.\


    <figure><img src="../../.gitbook/assets/image (476).png" alt=""><figcaption><p>Manage app version and change details</p></figcaption></figure>
5. Specify the version in the **Android Version(x.y.z)**, **IOS Version(x.y.z)** and the **Windows Version(x.y.z)** boxes where it is applicable.
6. Specify the relevant urls of your app in the **Google Store URL**, **Apple Store URL** and **Microsoft URL** boxes.
7. Describe the relevant change details in the **Android Version**, **IOS Version** and the **Windows Version** boxes.
8. Once completed, click **Save** to apply the updated app version information.
