# ComUnity Platform – Azure Marketplace Reference

### Quick Links

* 📘[ **Azure Marketplace Deployment Guide**](toolkit-tutorials/comunity-platform-azure-marketplace-deployment-guide.md) – Step-by-step deployment instructions
* 📄 **Download as Word Document** – For offline use

{% file src=".gitbook/assets/Azure_Marketplace_Deployment_Guide.docx" %}

***

### Overview

This document provides technical reference information for the ComUnity Platform Azure Marketplace offering. Use this alongside the [Deployment Guide ](comunity-platform-azure-marketplace-reference.md)for detailed specifications, credential management, and architecture details.

***

### Deployment Flow Overview

The deployment process follows these stages:

| Stage                         | What You See                                                            | Duration  |
| ----------------------------- | ----------------------------------------------------------------------- | --------- |
| **1. Marketplace Offer**      | Plan selection dropdown (Innovator, Town, etc.)                         | —         |
| **2. Basics Tab**             | Subscription, Resource Group, Region, Password, Application Name fields | —         |
| **3. Review + Create**        | Configuration summary, Co-Admin Access Permission checkbox, validation  | 1-2 min   |
| **4. Deployment Started**     | "Deployment is in progress" with Correlation ID                         | —         |
| **5. Managed App Created**    | Managed Application shows "Created" status                              | \~2 min   |
| **6. Resources Provisioning** | Resources appear in Managed Resource Group (30 total)                   | 10-15 min |
| **7. Custom Script Running**  | VM extension installing platform components                             | 30-45 min |
| **8. Deployment Complete**    | All resources show "Succeeded" status                                   | —         |

***

### Marketplace Offer Details

#### Offer Naming

The marketplace offer appears as **"City as a Platform"** or **"ComUnity Platform"**. The "City as a Platform" naming reflects the target market of municipalities and smart city initiatives, but the toolkit deployed is the full ComUnity Developer Toolkit.

#### Available Plans

Seven pricing plans are available, scaled by municipality size:

| Plan            | Target Use Case              |
| --------------- | ---------------------------- |
| **Innovator**   | Sandbox/testing environments |
| **Town**        | Small municipalities         |
| **Small City**  | Small city deployments       |
| **Medium City** | Medium city deployments      |
| **Large City**  | Large city deployments       |
| **Metropolis**  | Metropolitan areas           |
| **Mega City**   | Major metropolitan regions   |

All plans deploy identical toolkit resources; the difference is in billing structure and support tiers. For testing, select the **Innovator** plan as noted in the marketplace listing.

#### What Gets Deployed

The marketplace deployment creates a **Development environment only**. QA and Production environments must be provisioned separately using the Infrastructure Management feature within the toolkit.

***

### Resource Architecture

#### Resource Group Structure

The deployment creates a nested structure:

| Level                          | Description                                                                |
| ------------------------------ | -------------------------------------------------------------------------- |
| **Marketplace Resource Group** | User-created resource group containing the Managed Application wrapper     |
| **Managed Application**        | Azure marketplace wrapper that manages the lifecycle of deployed resources |
| **Managed Resource Group**     | Auto-created resource group containing all actual platform resources       |

#### Navigating to Resources

**From Marketplace Resource Group → Managed Application → Managed Resource Group:**

1. Open your marketplace resource group (e.g., `JPGTestMarketplaceDec`)
2. You'll see the Managed Application listed (e.g., `JPGTestMarketPlaceApp`)
3. Click on the Managed Application to open its overview
4. In the Essentials section, click the **Managed resource group** link (e.g., `mrg-city-as-a-platform24_4-preview-...`)
5. This opens the resource group containing all 30 platform resources

#### Azure Resources Created

The managed resource group contains approximately 30 resources:

| Resource Type                  | Example Name             | Purpose                                             |
| ------------------------------ | ------------------------ | --------------------------------------------------- |
| **Virtual Machine**            | _(varies)_               | Hosts all platform components and services          |
| **Virtual Network**            | _(varies)_               | Network infrastructure for VM and services          |
| **Network Security Group**     | _(varies)_               | Firewall rules controlling inbound/outbound traffic |
| **Public IP Address**          | _(varies)_               | External access point for toolkit                   |
| **Network Interface**          | _(varies)_               | VM network connectivity                             |
| **SQL Server**                 | _(varies)_               | Database server for platform and project databases  |
| **SQL Databases**              | _(multiple)_             | Platform database, project databases                |
| **Storage Account**            | _(varies)_               | File and media storage                              |
| **Managed Disk**               | _(varies)_               | VM operating system storage                         |
| **Container Apps Environment** | dev                      | Hosts observability container apps                  |
| **Container App**              | grafana                  | Observability dashboards                            |
| **Container App**              | loki                     | Log aggregation                                     |
| **Container App**              | tempo                    | Distributed tracing                                 |
| **Container App**              | prometheus               | Metrics collection                                  |
| **Container App**              | thanos                   | Long-term metrics storage                           |
| **Container App**              | otel-collector           | OpenTelemetry data collection                       |
| **Application Insights**       | appinsights\*\[suffix]\* | Application monitoring and telemetry                |
| **App Configuration**          | appconfig\*\[suffix]\*   | Centralized application settings                    |
| **Key Vault**                  | kvcmty\*\[suffix]\*      | Secure storage for secrets and certificates         |
| **Log Analytics Workspace**    | obs-workspace            | Centralized logging for observability               |

> **Note:** Resource names include auto-generated suffixes (e.g., `eukrhl5h4bmgc`) to ensure uniqueness.

#### Platform Components (on VM)

The following services are installed on the Virtual Machine:

| Component                 | Function                                                               |
| ------------------------- | ---------------------------------------------------------------------- |
| **Config Hub**            | Centralized configuration management for all services                  |
| **Auth Server**           | Authentication and authorization services (OAuth 2.0, Microsoft Entra) |
| **Core Web Services**     | Platform APIs and core business logic                                  |
| **Deployment Agent**      | Automated deployment orchestration, database provisioning              |
| **Communications Server** | Email, SMS, WhatsApp, and InApp messaging                              |
| **Scheduler**             | Background job processing and scheduled tasks                          |
| **Custom Web**            | Application hosting for built projects                                 |
| **Media Server**          | Media file processing and delivery                                     |
| **Data Services**         | Data access layer and ORM services                                     |

***

### Credentials Reference

#### Credential Types

| Credential           | Username                    | Password                                          | Purpose                     |
| -------------------- | --------------------------- | ------------------------------------------------- | --------------------------- |
| **Toolkit Admin**    | admin@communityplatform.com | admin (default)                                   | Web toolkit access          |
| **VM Administrator** | azureuser (auto-set)        | User-specified during deployment (Password field) | Remote Desktop (RDP) access |
| **SQL Server Admin** | Auto-generated              | Auto-generated                                    | Database management         |

> **Note:** The VM username `azureuser` is automatically configured during deployment. The Password you enter in the deployment form is used for this VM account.

#### Credential Retrieval

**Toolkit Admin Credentials**

Default credentials are fixed. Change immediately after first login via the toolkit's user management interface.

**VM Credentials**

The password is set during deployment and cannot be retrieved afterward. If lost:

* Use Azure Portal's VM password reset feature, or
* Redeploy the toolkit with a new password

**SQL Server Credentials**

**Known Limitation:** SQL credentials are auto-generated during deployment but are not currently exposed to users in the deployment outputs. This is being addressed in future versions.

**Workaround:** Contact ComUnity support to retrieve SQL credentials if direct database access is required.

#### When VM Access Is Needed

Most toolkit users never need VM access. VM login is required for:

* Installing additional software on the VM
* Reviewing VM-level logs for troubleshooting
* Configuring Windows-level settings
* Advanced maintenance operations

**Access method:** Remote Desktop Protocol (RDP) to the public IP address

***

### Configuration Parameters

#### Deployment Form Fields (Basics Tab)

| Field                      | Required | Notes                                                                                                        |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| **Subscription**           | Yes      | Must have Contributor or Owner role                                                                          |
| **Resource Group**         | Yes      | Create new recommended. Use clear naming convention.                                                         |
| **Region**                 | Yes      | Select region closest to users. All Azure regions supported.                                                 |
| **Password**               | Yes      | 12+ chars, upper/lower/number/special required                                                               |
| **Confirm password**       | Yes      | Must match Password field                                                                                    |
| **Application Name**       | Yes      | Used in resource naming. Keep concise.                                                                       |
| **Managed Resource Group** | Auto     | Auto-populated with timestamp (e.g., `mrg-city-as-a-platform24_4-preview-20251201140556`). Cannot be edited. |

#### Review + Create Tab

Before deployment, you must accept:

| Requirement                    | Description                                                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Co-Admin Access Permission** | Grants ComUnity (the Provider) administrative access to Azure resources for support and management. Required checkbox. |
| **Validation**                 | Azure runs final validation before enabling the Create button                                                          |

#### Viewing Deployment Parameters

After deployment, you can view configuration values:

1. Navigate to your **Marketplace Resource Group**
2. Click on the **Managed Application**
3. In the left sidebar under Settings, click **Parameters and Outputs**

> **Note:** Passwords are not displayed for security reasons.

***

### Installation Script Behaviour

#### Custom Script Extension

The Custom Script Extension runs a PowerShell script that:

1. Installs Windows components and prerequisites
2. Tests that all prerequisites installed correctly
3. Extracts platform component archive
4. Installs each platform service sequentially
5. Configures database connections
6. Loads platform icons and default data
7. Starts all services
8. Runs verification tests

#### Idempotent Design

The installation script is designed to be **idempotent**—it can be run multiple times safely:

* Checks if services are already installed before installing
* Skips completed steps on re-run
* Always runs verification tests
* Retries failed steps up to 3 times before failing

This means redeploying to the same resource group will pick up from where installation left off if a previous deployment failed.

#### Timing Breakdown

| Phase                                 | Duration          |
| ------------------------------------- | ----------------- |
| Windows components installation       | 5–10 minutes      |
| Prerequisites testing                 | 2–3 minutes       |
| Platform archive extraction           | 5–8 minutes       |
| Service installation (all components) | 10–15 minutes     |
| Platform icons loading                | 5–10 minutes      |
| Final verification                    | 2–3 minutes       |
| **Total**                             | **30–45 minutes** |

***

### Known Limitations

| Limitation                                | Status / Workaround                                                                                                |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **SQL credentials not exposed**           | Auto-generated but not shown. Contact support for retrieval. Enhancement planned.                                  |
| **VM username auto-set**                  | Automatically configured as `azureuser`. Cannot be customized during deployment.                                   |
| **Toolkit admin credentials fixed**       | Default admin/admin. Must change after login. Custom credentials during deploy planned.                            |
| **App Registration required post-deploy** | Manual setup required. Cannot be automated due to permission constraints. See Post-Deployment Setup.               |
| **Limited deployment feedback**           | Script may hang without clear error. Check Deployments view for status. Redeployment may resolve transient issues. |
| **Dev environment only**                  | QA/Production require Infrastructure Management feature. By design.                                                |
| **HTTP only by default**                  | SSL/HTTPS requires post-deployment domain and certificate setup.                                                   |
| **Co-Admin Access required**              | Must accept provider access permission to deploy. Required for support and management.                             |

***

### Region Considerations

The toolkit uses only standard Azure managed services and should deploy successfully in any Azure region. However:

* **Latency:** Deploy to a region close to your users. Cross-region access increases response times.
* **Testing:** Primary testing has been done in South Africa North. Other regions should work identically.
* **Resource availability:** VM sizes may vary by region. The deployment template selects appropriate available SKUs.

***

### Support Procedures

#### Support Contact Information

Support contact details are displayed in the Managed Application overview page after deployment:

| Contact Method    | Details                                            |
| ----------------- | -------------------------------------------------- |
| **Support Name**  | Ann Scott                                          |
| **Support Email** | anns@comunityplatform.com                          |
| **Support Phone** | +27 82 453 9034                                    |
| **Support Link**  | https://www.comunityplatform.com/get\_started.html |

#### When to Contact Support

* Deployment exceeds 90 minutes
* Custom Script Extension fails with errors
* Need SQL Server credentials
* App Registration setup assistance
* Domain and SSL configuration
* Project build failures after deployment

#### Information to Provide

1. Azure subscription ID
2. Resource group name(s)
3. Deployment timestamp
4. Error messages from Deployments view (screenshots helpful)
5. Deployment operation details (tracking ID if available)

***

### Related Documentation

| Document                                                                                               | Description                             |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| [**Azure Marketplace Deployment Guide**](https://claude.ai/chat/Azure_Marketplace_Deployment_Guide.md) | Step-by-step deployment instructions    |
| **Infrastructure Management Guide**                                                                    | Creating QA and Production environments |
| **App Registration Setup Guide**                                                                       | Configuring Azure AD for project builds |
| **Observability Setup Guide**                                                                          | Configuring monitoring and analytics    |
| **Platform Architecture Documentation**                                                                | Technical architecture overview         |

***

### Document History

| Version | Date          | Changes                                                                |
| ------- | ------------- | ---------------------------------------------------------------------- |
| 1.0     | December 2025 | Initial release. Based on deployment walkthrough and technical review. |
