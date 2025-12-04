# ComUnity Platform - Azure Marketplace Deployment Guide

### Overview

The ComUnity Developer Toolkit is available as a managed application on Azure Marketplace under the name **"City-as-a-Platform: Digital Service Platform for Cities (preview)"**. This guide walks you through deploying the toolkit from marketplace purchase to accessing your fully functional development environment.

#### What Gets Deployed

Your deployment creates a complete ComUnity Platform Toolkit **Development environment** including:

* Virtual Machine hosting all platform components
* SQL Server and databases for platform and project data
* Container Apps Environment with observability stack (Grafana, Loki, Tempo, Prometheus)
* Application Insights, App Configuration, and Key Vault
* Networking components (Virtual Network, NSG, Public IP)
* Approximately 30 Azure resources in total

#### Deployment Timeline

| Phase                        | Duration          |
| ---------------------------- | ----------------- |
| Infrastructure provisioning  | 10–15 minutes     |
| Toolkit installation scripts | 30–45 minutes     |
| **Total deployment time**    | **45–60 minutes** |

#### Available Plans

Seven plans are available, scaled by target municipality size:

| Plan            | Target Use Case                                              |
| --------------- | ------------------------------------------------------------ |
| **Innovator**   | Sandbox/testing environments (recommended for initial setup) |
| **Town**        | Small municipalities                                         |
| **Small City**  | Small city deployments                                       |
| **Medium City** | Medium city deployments                                      |
| **Large City**  | Large city deployments                                       |
| **Metropolis**  | Metropolitan areas                                           |
| **Mega City**   | Major metropolitan regions                                   |

> **Note:** All plans deploy identical toolkit resources. The difference is in billing structure.

***

### Prerequisites

#### Required Access & Permissions

* ✓ **Azure Subscription** – Active subscription with Contributor or Owner role
* ✓ **Azure Portal Access** – Logged in with the correct account
* ✓ **Correct Directory** – Ensure you're in the correct Azure directory/tenant (the offer won't appear in wrong directory)

#### Planning Information

* ✓ Chosen Azure region for deployment (select closest to your users)
* ✓ Resource group naming convention decided
* ✓ Password ready (12+ characters with upper, lower, numbers, special characters)
* ✓ 90 minutes available for deployment and initial setup

***

### Deployment Process

#### Step 1: Access the Marketplace Offer

1. Log into Azure Portal at [portal.azure.com](https://portal.azure.com/)
2. **Verify your directory:** Check the directory indicator in the top right. Switch directories if needed.
3. Click **Create a resource** or navigate to Marketplace
4. Search for **"City-as-a-Platform"** or **"ComUnity"**
5. Select **"City-as-a-Platform: Digital Service Platform for Cities (preview)"**

#### Step 2: Select Your Plan

On the offer page, you'll see the plan selection dropdown with all seven options available:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 140541.png" alt=""><figcaption></figcaption></figure>

1. Select your **Subscription**
2. Click the **Plan** dropdown to see all seven options
3. Select **Innovator** for testing (as recommended in the listing)
4. Click **Create** to proceed to the configuration form

#### Step 3: Configure Basics

Complete the **Basics** tab with the following settings:

**Project Details**

| Field              | Action                                       |
| ------------------ | -------------------------------------------- |
| **Subscription**   | Select the Azure subscription for deployment |
| **Resource group** | Click **Create new** and enter a name        |

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 140648.png" alt=""><figcaption></figcaption></figure>

**Instance Details**

| Field                | Action                                                                   |
| -------------------- | ------------------------------------------------------------------------ |
| **Region**           | Select the Azure region closest to your users (e.g., South Africa North) |
| **Password**         | Enter a strong password (this is used for VM administrator access)       |
| **Confirm password** | Re-enter the password                                                    |

> ⚠️ **Password Requirements:** Minimum 12 characters, must include uppercase, lowercase, numbers, and special characters. **Save this password securely!**

**Managed Application Details**

| Field                      | Action                                                                                        |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| **Application Name**       | Enter a unique name for your deployment                                                       |
| **Managed Resource Group** | Auto-populated (e.g., `mrg-city-as-a-platform24_4-preview-20251201140556`). Cannot be edited. |

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141356.png" alt=""><figcaption></figcaption></figure>

Click **Review + create** to proceed.

#### Step 4: Review and Create

1. Wait for Azure to complete _"Running final validation..."_
2. Review the configuration summary under **Basics**
3. Read the **Co-Admin Access Permission** section
4. Check the box: **"I agree to the terms and conditions above"**
5. Click **Create** to begin deployment

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141534.png" alt=""><figcaption></figcaption></figure>

> **Note:** The Co-Admin Access Permission grants ComUnity administrative access to your Azure resources for support and management purposes.

***

### Monitoring Deployment

#### Deployment Started

After clicking Create, you'll see the deployment in progress notification:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141653.png" alt=""><figcaption></figcaption></figure>

#### Understanding the Resource Structure

The deployment creates a nested structure:

```
Your Resource Group (e.g., JPGTestMarketplaceDec)
└── Managed Application (e.g., JPGTestMarketPlaceApp)
    └── Managed Resource Group (e.g., mrg-city-as-a-platform24_4-preview-...)
        └── ~30 Platform Resources (VM, SQL, Container Apps, etc.)
```

#### Viewing Deployment Progress

1. Navigate to **Resource Groups** in the left menu
2. Click on your resource group

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141917.png" alt=""><figcaption></figcaption></figure>

3. Click on the **Managed Application**

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 142003.png" alt=""><figcaption></figcaption></figure>

4. Click the **Managed resource group** link in the Essentials section
5. Under Settings in the left sidebar, click **Deployments** to see detailed progress

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141816.png" alt=""><figcaption></figcaption></figure>

#### Viewing Operation Details

Click on any resource to see operation details including duration and status:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 141837.png" alt=""><figcaption></figcaption></figure>

#### Deployment Phases

**Phase 1: Infrastructure Resources (10–15 minutes)**

Resources being created include:

* Storage accounts, Virtual Network, Network Security Groups
* Public IP, Virtual Machine, SQL Server and databases
* Container Apps (grafana, loki, tempo, prometheus, thanos, otel-collector)
* Key Vault, App Configuration, Application Insights

**Phase 2: Custom Script Extension (30–45 minutes)**

This is the longest step. The script installs all platform components on the VM including:

* Config Hub
* Auth Server
* Core Web Services
* Deployment Agent
* Communications Server
* And more...

> **Note:** You can safely close your browser – deployment continues in the background. Use the Refresh button to check status.

#### Viewing Created Resources

Once deployment progresses, you can see all resources in the Managed Resource Group:

<figure><img src="../.gitbook/assets/Screenshot 2025-12-01 142103.png" alt=""><figcaption></figcaption></figure>

#### Confirming Successful Deployment

Deployment is complete when the Deployments view shows all items as **"Succeeded"** with green checkmarks, especially the Custom Script Extension.

***

### Accessing Your Toolkit

#### Step 1: Get the Public IP Address

1. Navigate to the Managed Resource Group
2. Click the **Type** column header to sort resources by type
3. Click on the **Virtual Machine** resource
4. In the VM Overview, locate and copy the **Public IP address**



#### Step 2: Access the Toolkit

1. Open a new browser tab
2. Enter the IP address (e.g., `http://42.212.32.44`)
3. The ComUnity Platform Toolkit login page should load

> **Note:** If the page doesn't load, wait 2–3 minutes for services to fully start.

#### Step 3: Log In

Use the default credentials:

| Field        | Value                       |
| ------------ | --------------------------- |
| **Username** | admin@communityplatform.com |
| **Password** | admin                       |

> ⚠️ **SECURITY:** Change these default credentials immediately after first login.

***

### Post-Deployment Setup

#### Immediate Actions

* \[ ] Change the default admin password
* \[ ] Update the admin email address
* \[ ] Create additional user accounts as needed

#### App Registration Setup (Required for Project Building)

> ⚠️ **IMPORTANT:** You cannot build projects until App Registration is configured.

The Deployment Agent needs Azure permissions to create databases. Without App Registration, project builds will fail. Contact ComUnity support for assistance with this setup.

#### Additional Configuration (Optional)

| Configuration               | Description                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| **Custom Domain & SSL**     | Configure a domain name and SSL certificate for HTTPS access           |
| **Observability URLs**      | Connect observability dashboard endpoints                              |
| **Additional Environments** | Use Infrastructure Management to create QA and Production environments |

***

### Troubleshooting

#### Deployment Fails with Password Error

**Cause:** Password doesn't meet complexity requirements.

**Solution:** Delete the failed deployment and create a new one with a password meeting all requirements (12+ characters, uppercase, lowercase, numbers, special characters).

#### Deployment Takes Too Long

| Situation              | Action                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------- |
| **Normal**             | 45–60 minutes total. Custom Script Extension alone takes 30–45 minutes.               |
| **Exceeds 90 minutes** | Contact support. Redeploying to the same resource group may resolve transient issues. |

#### Toolkit Login Page Doesn't Load

* Verify Custom Script Extension shows "Succeeded"
* Wait 2–3 minutes for services to start
* Use HTTP (not HTTPS) – SSL is not configured by default
* Check your network allows access to the VM's public IP

#### Project Build Fails

**Most likely cause:** App Registration not configured.

**Solution:** Contact support to complete App Registration setup.

***

### Deleting Your Deployment

> ⚠️ **WARNING:** Deletion permanently removes all data and cannot be undone.

#### When to Delete

* Completing a test deployment
* Starting fresh after a failed deployment
* Decommissioning the platform

#### How to Delete

1. Navigate to **Resource Groups**
2. Find your marketplace resource group
3. Click **Delete resource group**
4. Type the resource group name to confirm
5. Click **Delete**

This should delete both the marketplace resource group and the managed resource group with all platform resources.

***

### Related Documentation

| Document                                                                                                   | Description                                            |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [**Azure Marketplace Reference**](../comunity-platform-azure-marketplace-reference.md)                     | Technical specifications and credentials               |
| [**Infrastructure Management Guide**](../getting-started/manage-your-project/infrastructure-management.md) | Creating QA and Production environments                |
| **App Registration Setup Guide**                                                                           | Configuring Azure AD for project builds(Coming soon..) |
| [**Observability Setup Guide**](../toolkit-guides/observability/)                                          | Configuring monitoring and analytics                   |

***

***
