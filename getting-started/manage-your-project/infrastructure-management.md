# Infrastructure Management

## Overview

The Infrastructure Management feature allows administrators to deploy and manage Azure environments for their Toolkit projects through pre-configured deployment scripts. This integration automates infrastructure provisioning, eliminating the need for manual Azure resource management.

{% hint style="info" %}
**Current documentation is based on implementation as of v25.3.** Interface and functionality subject to change in future releases. The screens shown are not according to final design specifications, as these designs became available after the development cycle had begun. The layout will be significantly different in future releases, but core functionality for managing infrastructure scripts will remain similar.
{% endhint %}

When you purchase and deploy the ComUnity Toolkit from the Azure Marketplace, it is installed into **your own Azure subscription**. The Toolkit operates as a self-contained environment within your Azure infrastructure. The **Development environment is created automatically** during initial deployment from the marketplace.

The Infrastructure Management feature allows you to subsequently provision additional environments (QA and Production) as needed for your development lifecycle.

### Prerequisites

Before using Infrastructure Management features to create QA or Production environments, ensure you have:

#### 1. Active Development Environment

Your initial Toolkit deployment from [Azure Marketplace ](https://marketplace.microsoft.com/en-ie/product/virtual-machines/comunity.comunity-rapid-digitsation-platform?tab=Overview)must be complete and operational. This automatically creates your Development environment with all necessary platform components.

#### 2. Azure Subscription Access

Access to the Azure subscription where your Toolkit is deployed, with permissions to:

* View resource groups and resources
* Monitor deployment status
* Access Azure Portal for verification

#### 3. Administrator Permissions

Role-based access rights within the Toolkit to manage infrastructure scripts. Only users with appropriate administrator permissions can:

* View infrastructure scripts
* Deploy new environments
* Manage existing deployments

#### 4. App Registration Configured&#x20;

An Azure App Registration with appropriate permissions is **required** for the Deployment Agent to:

* Create databases in SQL Server
* Manage Azure resources programmatically
* Configure platform components

**Current Status:** App Registration setup is currently a manual process that must be completed before you can successfully build projects or create new environments. The Deployment Agent requires the following configured values:

* Azure Client ID
* Azure Client Secret

These values are configured in the Toolkit under the Deployment Agent platform component settings.

{% hint style="warning" %}
Detailed documentation for App Registration setup is in development. Contact ComUnity support for step-by-step guidance on creating and configuring the App Registration with the correct permissions. Without this configuration, project builds and new environment deployments will fail when attempting to create databases.
{% endhint %}

#### 5. Understanding of SQL Server Options

Familiarity with the architectural differences between shared and dedicated SQL Server deployments (covered in detail in the [Choosing Between Shared and Dedicated SQL Server](https://claude.ai/chat/04350528-21d1-46ac-927d-f1cb7b27d660#choosing-between-shared-and-dedicated-sql-server) section below).

### Key Features

#### Automated Deployment Scripts

Deploy Azure environments through pre-configured ARM (Azure Resource Manager) templates that handle resource provisioning automatically. The Toolkit manages the deployment process in the background, allowing you to continue working on other tasks whilst infrastructure is being created.

**How it works:**

* You configure and initiate the deployment through the Toolkit interface
* The Toolkit sends the ARM template to Azure
* Azure executes the template, creating all specified resources
* Status updates appear in the Toolkit as deployment progresses
* You receive notification when deployment completes (approximately 30-60 minutes)

#### Environment-Specific Management

Manage separate Development, QA, and Production environments. Each environment operates independently with its own resources:

* **Development Environment**: Cannot be disabled (always available as the primary workspace)
* **QA Environment**: Can be enabled or disabled to control availability
* **Production Environment**: Can be enabled or disabled to control availability

When an environment is disabled, it becomes unavailable in deployment screens but the Azure infrastructure remains intact.

#### Deployment Monitoring

Track deployment progress through status indicators that update as infrastructure scripts execute:

* **New**: Script has been added but not yet deployed
* **Busy**: Deployment is currently in progress
* **Deployed**: Deployment completed successfully
* Status updates automatically without page refresh

You can navigate away from the infrastructure screen during deployment and return later to check progress.

#### Role-Based Access Control

Access to infrastructure management features is controlled through role-based access (RBA). Only users with the required permissions can create, manage, or deploy infrastructure scripts.

{% hint style="info" %}
Infrastructure scripts require activation in each environment to match the specific deployment contexts of your project, similar to other primary features in the Toolkit.
{% endhint %}

### Understanding the Toolkit Architecture

#### Deployment Model

The ComUnity Toolkit operates as a **self-hosted solution** within your Azure subscription:

```
Your Azure Subscription
└── Resource Groups
    ├── Development Environment (auto-created via Marketplace)
    ├── QA Environment (created via Infrastructure Management)
    └── Production Environment (created via Infrastructure Management)
```

**Key Points:**

* The Toolkit is **not** a SaaS service - you own and manage the infrastructure
* All resources exist in **your** Azure subscription
* You have full access to underlying Azure resources through Azure Portal
* The Toolkit provides a management interface on top of your Azure infrastructure

#### What Each Environment Contains

Each complete environment consists of:

**Azure Infrastructure Resources:**

* Virtual Machine (VM) - Hosts all platform components
* Virtual Network - Network infrastructure
* Network Security Group - Firewall rules
* Public IP Address - External access point
* Network Interface - VM connectivity
* SQL Server (if using dedicated option) or databases on shared server
* SQL Databases - Platform and project databases
* Storage Account - File and media storage
* Managed Disk - VM operating system storage

**Platform Components (installed on the VM):**

* **Config Hub** - Centralized configuration management
* **Auth Server** - Authentication and authorization services
* **Core Web Services** - Platform APIs
* **Deployment Agent** - Automated deployment orchestration
* **Communications Server** - Email, SMS, WhatsApp, InApp messaging
* **Scheduler** - Background job processing
* **Custom Web** - Application hosting
* **Media Server** - Media file processing
* **Observability Stack** (if configured) - Monitoring and logging

#### Resource Organization

Azure resources are organized into **Resource Groups**. The structure depends on your SQL Server configuration choice:

**Shared SQL Server Configuration**

```
Dev Resource Group
├── SQL Server (shared)
├── Dev Databases
├── QA Databases (on shared server)
├── Dev VM
├── Dev Networking
└── Dev Storage

QA Resource Group
├── QA VM
├── QA Networking
└── QA Storage
(No SQL Server - uses Dev's server)
```

**Characteristics:**

* Single SQL Server instance in Dev resource group
* All databases (Dev + QA + Prod) on one server
* QA and Prod resource groups contain only VM and supporting infrastructure
* Lower cost, simplified management
* Shared resources between environments

**Dedicated SQL Server Configuration**

```
Dev Resource Group
├── Dev SQL Server
├── Dev Databases
├── Dev VM
├── Dev Networking
└── Dev Storage

QA Resource Group
├── QA SQL Server (dedicated)
├── QA Databases
├── QA VM
├── QA Networking
└── QA Storage
```

**Characteristics:**

* Separate SQL Server for each environment
* Complete isolation between environments
* Each resource group is self-contained
* Higher cost, better performance isolation
* Independent scaling per environment

### Accessing Infrastructure Management

Infrastructure management features are available to users with appropriate administrator permissions.

#### Steps to Access

1. **Log In**: Access the Toolkit by entering your credentials.
2.  After successful login you will be redirected to the **Home** screen:

    <figure><img src="../../.gitbook/assets/image (493).png" alt=""><figcaption></figcaption></figure>
3.  **Navigate to Infrastructure**: From the top main menu bar, find and click on **Infrastructure**. You will be presented with the infrastructure management interface.

    <figure><img src="../../.gitbook/assets/image (494).png" alt=""><figcaption></figcaption></figure>

#### Interface Overview

The Infrastructure Management interface has sections:

1. **All resources** - Where you view all your Azure resources
2. **Resource Groups** - Where you view your Resources Groups
3. **Resource Types** - Where you view the types of the supported resources.
4. **Infrastructure Scripts** - Where you add, deploy, and manage deployment scripts

{% hint style="info" %}
The current infrastructure management interface will change in future releases. The screens are not according to the final design specifications. The layout will be significantly different, but the core functionality for managing infrastructure scripts will remain similar.
{% endhint %}

### Understanding Infrastructure Scripts

Infrastructure scripts are **ARM (Azure Resource Manager) templates** that automate the creation of Azure resources and installation of platform components. When you execute a script, it runs a PowerShell-based installation process that:

1. Creates Azure resources according to the ARM template
2. Installs required Windows features and applications on the VM
3. Installs and configures all platform components
4. Sets up databases and runs initialization scripts
5. Configures networking and firewall rules
6. Verifies installation success at each step

These scripts are available within the **Infrastructure** section when you select the **Infrastructure Scripts** tab.

<figure><img src="../../.gitbook/assets/image (495).png" alt=""><figcaption></figcaption></figure>

#### Available Script Types

Three types of infrastructure scripts are currently available:

**1. Environment with Dedicated SQL Server**

**Purpose:** Creates a complete Azure environment with a dedicated SQL Server instance for complete environment isolation.

**What it creates:**

* New resource group (you specify the name)
* Dedicated SQL Server for this environment only
* All platform databases on the dedicated server
* Virtual Machine for platform components
* Complete networking infrastructure (VNet, NSG, NIC, Public IP)
* Storage account for files and media
* All platform components installed and configured

**When to use:**

* Production environments requiring maximum isolation
* High-traffic applications needing dedicated database resources
* Compliance requirements mandating environment separation
* When budget allows for higher infrastructure costs

**Deployment time:** Approximately 45-60 minutes

**2. Environment with Shared SQL Server**

**Purpose:** Creates a complete Azure environment that reuses the SQL Server from your Development environment, reducing costs while maintaining separate compute resources.

**What it creates:**

* New resource group for environment-specific resources
* Platform databases created on Development's SQL Server (in Dev resource group)
* Virtual Machine for platform components
* Complete networking infrastructure
* Storage account for files and media
* All platform components installed and configured

**What it does NOT create:**

* New SQL Server (uses existing Dev server)

**When to use:**

* Cost-conscious deployments
* QA environments with predictable, lower traffic
* When SQL Server resources are sufficient for multiple environments
* Standard development lifecycle needs

**Deployment time:** Approximately 45-60 minutes

**3. QA Environment BLOB Storage Container**

**Purpose:** Creates a simple resource group with a storage account. This is a **test script** designed to help you understand the infrastructure deployment workflow without the time and resource commitment of a full environment.

**What it creates:**

* Resource group with specified name
* Storage account within the resource group

**When to use:**

* Testing the infrastructure deployment process
* Learning how status updates work
* Verifying your permissions and setup
* Before committing to a full environment deployment

**Deployment time:** A few minutes

### ⚠️ CRITICAL WARNING

**The dedicated and shared SQL Server scripts create and configure complete new environments. These scripts must NOT be run in existing Toolkit environments or production systems.**

Running these scripts in an existing environment will attempt to create new infrastructure and may cause:

* Resource naming conflicts
* Configuration overwrites
* Data loss
* Environment corruption

#### Only Use Full Environment Scripts When:

* &#x20;Creating your first QA environment after initial Toolkit deployment
* Creating your first Production environment
* Setting up isolated testing environments in separate Azure subscriptions
* Provisioning fresh infrastructure under administrator guidance

#### Never Use Full Environment Scripts:

* &#x20;In the current Toolkit Next environment
* &#x20;In existing Production environments
* To "refresh" or "update" an existing environment
* In shared development environments

**If you need to modify an existing environment, contact support for guidance rather than running deployment scripts.**

### Choosing Between Shared and Dedicated SQL Server

One of the most important decisions when deploying QA or Production environments is whether to use a shared or dedicated SQL Server. This choice impacts cost, performance, isolation, and operational complexity.

#### Decision Framework

Consider the following factors:

| Factor              | Shared SQL Server                           | Dedicated SQL Server                         |
| ------------------- | ------------------------------------------- | -------------------------------------------- |
| **Cost**            | Lower - One SQL Server for all environments | Higher - Separate SQL Server per environment |
| **Performance**     | Shared resources may cause contention       | Independent resources, no contention         |
| **Isolation**       | Databases share server resources            | Complete isolation between environments      |
| **Management**      | Simpler - One server to manage              | More complex - Multiple servers              |
| **Scaling**         | Scale affects all environments              | Scale each environment independently         |
| **Backup/Recovery** | Single backup strategy for all databases    | Independent backup strategies                |
| **Security**        | Environments share connection strings       | Separate credentials per environment         |

#### Shared SQL Server - Detailed Analysis

**Architecture:**

```
Dev SQL Server (in Dev Resource Group)
├── Dev Databases
├── QA Databases
└── Prod Databases (if using shared for Prod)
```

**Best for:**

* **Budget-Constrained Projects**: Minimize Azure SQL Server licensing and compute costs
* **Development/Testing Cycles**: QA environments with predictable, moderate traffic
* **Small to Medium Projects**: Applications without intensive database workloads
* **Learning/Evaluation**: Understanding the Toolkit without significant investment

**Advantages:**

* **Cost Effective**: Pay for one SQL Server instead of multiple
* **Simplified Management**: Single server to monitor, patch, and maintain
* **Easier Backup**: One backup policy covers multiple environments
* **Quick Setup**: No need to configure additional SQL Server instances

**Disadvantages:**

* **Resource Contention**: Heavy load in one environment can impact others
* **No Performance Isolation**: Can't independently scale database resources
* **Security Boundaries**: All environments share the same SQL Server access
* **Single Point of Failure**: SQL Server issues affect all environments
* **Harder to Diagnose**: Performance issues harder to trace to specific environment

**Typical Use Cases:**

* Small development teams (5-10 users)
* Applications with < 1000 daily active users per environment
* QA environments running automated tests
* Proof-of-concept or demo environments

#### Dedicated SQL Server - Detailed Analysis

**Architecture:**

```
Dev Resource Group
└── Dev SQL Server
    └── Dev Databases

QA Resource Group
└── QA SQL Server
    └── QA Databases

Prod Resource Group
└── Prod SQL Server
    └── Prod Databases
```

**Best for:**

* **Production Environments**: When reliability and performance are critical
* **High-Traffic Applications**: Significant user loads or transaction volumes
* **Performance-Sensitive**: Applications where database performance is critical
* **Compliance Requirements**: Regulations requiring environment isolation
* **Enterprise Deployments**: Large-scale implementations

**Advantages:**

* **Complete Isolation**: Each environment's database performance is independent
* **Independent Scaling**: Scale SQL resources per environment needs
* **Better Security**: Separate credentials, connection strings per environment
* **Performance Predictability**: No unexpected slowdowns from other environments
* **Isolated Failures**: Issues in one environment don't affect others
* **Easier Troubleshooting**: Performance issues clearly isolated to one environment

**Disadvantages:**

* **Higher Cost**: Multiple SQL Server instances increase Azure spending
* **Complex Management**: Multiple servers to monitor, patch, update
* **More Configuration**: Separate backups, monitoring, alerts per server
* **Additional Overhead**: More resources to manage and maintain

**Typical Use Cases:**

* Production environments for customer-facing applications
* Applications with > 5000 daily active users per environment
* Performance-sensitive business applications
* Environments requiring compliance certification
* Multi-tenant SaaS applications

#### Making the Decision

Use this decision tree:

1. **Is this Production?**
   * Yes → Strongly consider Dedicated
   * No → Continue evaluating
2. **Do you have compliance/security requirements for environment isolation?**
   * Yes → Use Dedicated
   * No → Continue evaluating
3. **Will the environment handle > 5000 daily active users?**
   * Yes → Use Dedicated
   * No → Continue evaluating
4. **Is database performance critical to your application?**
   * Yes → Consider Dedicated
   * No → Continue evaluating
5. **Is budget a primary constraint?**
   * Yes → Use Shared
   * No → Consider Dedicated for better isolation
6. **Is this QA for testing/development purposes?**
   * Yes → Shared is usually sufficient
   * No → Reconsider requirements

#### Cost Considerations

**Approximate Azure SQL Server Costs** (as of 2025, varies by region):

* **Basic Tier**: $5-15/month per database
* **Standard Tier**: $15-200/month per database
* **Premium Tier**: $500-5000+/month per database

**Shared Configuration Example:**

* 1 SQL Server: Standard tier
* 10 databases (Dev + QA + Prod projects)
* **Estimated monthly cost**: $150-400

**Dedicated Configuration Example:**

* 3 SQL Servers: Standard tier each
* 10 databases distributed across environments
* **Estimated monthly cost**: $450-1200

**Note:** These are rough estimates. Actual costs depend on DTU/vCore configuration, storage, backup retention, and region. Use the Azure Pricing Calculator for accurate estimates.

#### Recommendations by Scenario

| Scenario                    | Recommendation | Rationale                              |
| --------------------------- | -------------- | -------------------------------------- |
| **First QA Environment**    | Shared         | Learn the workflow, minimize costs     |
| **Production Environment**  | Dedicated      | Isolation, performance, reliability    |
| **Development/Testing**     | Shared         | Cost-effective, sufficient for testing |
| **High-Traffic Production** | Dedicated      | Performance requirements               |
| **Compliance-Driven**       | Dedicated      | Regulatory requirements                |
| **Budget-Limited**          | Shared         | Minimize infrastructure costs          |
| **Enterprise Scale**        | Dedicated      | Operational maturity needed            |

#### Getting Help with the Decision

If you're uncertain which option is best for your specific situation:

* **Contact Support**: Schedule a consultation with ComUnity support for architectural guidance
* **Start with Shared**: Begin with shared SQL for QA, evaluate performance, then decide for Production
* **Review Azure Costs**: Monitor your Dev environment's Azure costs to estimate additional servers
* **Assess Your Workload**: Analyze your application's database usage patterns in Dev before deciding

{% hint style="info" %}
You can use different approaches for different environments. A common pattern is Shared SQL for QA (lower cost) and Dedicated SQL for Production (better isolation and performance).
{% endhint %}

### What Gets Created: Full Environment Deployment

When you deploy a full environment script (either dedicated or shared SQL), the deployment process takes approximately 45-60 minutes and creates extensive infrastructure and platform components.

#### Phase 1: Azure Resource Creation (5-10 minutes)

The ARM template creates the following Azure resources:

**Networking Components**

* **Virtual Network (VNet)** - Isolated network for the environment
* **Network Security Group (NSG)** - Firewall rules controlling traffic
* **Network Interface Card (NIC)** - Connects VM to network
* **Public IP Address** - External access endpoint

**Compute Resources**

* **Virtual Machine (VM)** - Windows Server hosting platform components
  * Default configuration includes appropriate CPU, RAM, and disk
  * VM size can be specified in script parameters
* **Managed OS Disk** - Storage for Windows operating system and applications

**Data & Storage**

* **SQL Server** (Dedicated option only) - Database server instance
  * If using Shared option, this is skipped
* **SQL Databases** - Multiple databases for platform and projects:
  * Platform system databases
  * Toolkit configuration database
  * Project databases (created as projects are deployed)
* **Storage Account** - Blob storage for:
  * Media files and uploads
  * Platform assets
  * Backup storage

**Supporting Components**

* **Application Insights** (if observability configured) - Telemetry and monitoring
* **Smart Detector Alert Rules** - Automated alerting (limited use currently)

You can monitor this phase in Azure Portal:

1. Navigate to Resource Groups
2. Find your newly created resource group (name you specified)
3. Click "Deployments" in the left sidebar
4. Watch as resources are created one by one

#### Phase 2: Platform Installation (30-50 minutes)

After Azure resources are created, a Custom Script Extension on the VM runs PowerShell scripts that install and configure platform components:

**Installation Steps**

The installation follows this sequence (you can see progress in VM logs):

1. **Download Installation Files**
   * Platform installation package (ZIP file)
   * Required software installers (Node.js, .NET, ImageMagick, Inkscape, etc.)
   * Configuration scripts
2. **Install Windows Features**
   * IIS (Internet Information Services)
   * Web Server components
   * Application Development features
   * Management tools
3. **Install Required Software**
   * Node.js (for certain platform services)
   * .NET Framework/Runtime
   * ImageMagick (image processing)
   * Inkscape (SVG processing)
   * Other dependencies
4. **Install Platform Components** (in order)
   * **Config Hub** - Centralized configuration (installed first)
   * **Auth Server & SDK** - Authentication services
   * **Core Web Services** - Platform APIs
   * **Deployment Agent** - Automated deployment engine
   * **Platform Databases** - Schema creation and initialization
   * **Platform Data Services** - Data access layer
   * **Communications Server** - Messaging infrastructure
   * **Custom Web** - Application hosting environment
   * **Scheduler** - Background job processing
   * **Region API** - Geographic services
   * **Com Service** - Internal communication bus
   * **Media Server** - File and media processing
5. **Configure Services**
   * Set up IIS websites and application pools
   * Configure service ports and bindings
   * Set up firewall rules
   * Configure observability URLs (if available)
   * Initialize configuration settings
6. **Add Platform Icons**
   * Install \~10,000 default icons into the SDK
   * This step alone can take 5-10 minutes
7. **Verification Tests**
   * After each major component installation, the script runs tests
   * Verifies services are running correctly
   * Checks database connections
   * Confirms configuration is valid

**Monitoring Installation Progress**

You can monitor the installation by:

1. **Remote Desktop to the VM:**
   * Get the Public IP address from Azure Portal
   * RDP to the VM using credentials specified during deployment
   * Navigate to `C:\temp\setup\`
   * Open `setup.log` file to see real-time progress
2.  **Watch for these log entries:**

    ```
    Installing Windows Features...
    Installing Required Software...
    Installing Config Hub...
    Installing Auth Server...
    Installing Core Web Services...
    Installing Deployment Agent...
    [etc...]
    Platform installation complete!
    ```
3. **If Installation Fails:**
   * Script attempts to rerun up to 3 times automatically
   * Check `C:\temp\setup\setup_1.log` for second attempt
   * Check `C:\temp\setup\setup_2.log` for third attempt
   * If all retries fail, deployment stops and reports failure

#### What You Get: Complete Working Environment

After successful deployment, you have:

* &#x20;Fully configured Azure infrastructure
* &#x20;All platform components installed and running
* IIS websites configured and accessible
* Databases created and initialised
* &#x20;Default platform icons loaded
* Services running and ready to accept deployments
* Environment accessible via Public IP address (HTTP initially)

#### What Still Needs Configuration

After deployment completes, you'll need to manually configure:

* ❗ **App Registration** - Set Client ID and Secret in Deployment Agent
* ❗ **Observability URLs** - Configure monitoring endpoints (if using observability)
* ❗ **Domain Name** - Point custom domain to Public IP (optional but recommended for Production)
* ❗ **SSL Certificate** - Install certificate and configure HTTPS (optional but recommended for Production)
* ❗ **Enable Environment** - Turn on the environment in Infrastructure settings

#### Default Access Credentials

The newly deployed environment includes default credentials:

**Username:** `admin@comunityplatform.com`\
**Password:** `admin`

{% hint style="info" %}
Change these default credentials immediately after first login, especially for Production environments.
{% endhint %}

#### Accessing Your New Environment

1. Get the Public IP address:
   * Azure Portal → Resource Groups → Your Resource Group → Public IP resource
   * Copy the IP address value
2. Access in browser:
   * Open browser to `http://[PUBLIC-IP-ADDRESS]`
   * You'll see the Toolkit login screen
3. Login with default credentials:
   * Username: `admin@comunityplatform.com`
   * Password: `admin`
4. You're now in the new environment!

#### Verifying Successful Deployment

Check these items to confirm everything deployed correctly:

**In Azure Portal:**

```
[ ] Resource group exists with all expected resources
[ ] VM is running
[ ] SQL Server exists (dedicated) or databases exist on shared server
[ ] Storage account created
[ ] Public IP address assigned
```

**In the Toolkit (new environment):**

```
[ ] Can login with default credentials
[ ] Can navigate through Toolkit interface
[ ] Platform Settings shows all components
[ ] Can create a test project (after configuring App Registration)
```

**Common Issues:**

* Deployment shows "Deployed" but some resources missing → Check Azure deployment logs
* Can't access via IP address → Check NSG firewall rules, verify VM is running
* Can't login → Platform installation may have failed, check VM installation logs



### Deploying QA Environment.

#### Before You Begin

Ensure you have completed the prerequisites:

* ✅ Development environment is operational
* ✅ App Registration configured with Client ID and Secret
* ✅ Decided between Shared vs. Dedicated SQL Server (see decision guide above)
* ✅ Tested deployment workflow with BLOB Storage script
* ✅ Have access to Azure Portal for monitoring

#### Step 1: Choose Your Deployment Script

1. Navigate to **Infrastructure > QA Environment > Infrastructure Scripts**
2.  Click **"Add Script"** button.<br>

    <figure><img src="../../.gitbook/assets/image (499).png" alt=""><figcaption></figcaption></figure>
3. You'll see two main script options:
   * **QA Environment with Dedicated SQL Server**
   *   **QA Environment with Shared SQL Server**<br>

       <figure><img src="../../.gitbook/assets/image (496).png" alt=""><figcaption></figcaption></figure>
4. **Select the appropriate script** based on your decision from the SQL Server architecture section

#### Step 2: Configure Deployment Parameters

The configuration interface will prompt for several parameters. Fill them in carefully:

**Required Parameters**

**Resource Group Name**

* Enter a name for the new QA resource group
* Example: `qa-environment` or `project-qa`
* Use lowercase letters, numbers, and hyphens
* Choose a descriptive name for easy identification

**VM Admin Username** (if prompted)

* Username for Remote Desktop access to the VM
* Example: `adminuser` or `vmadmin`
* Note: Currently the script may auto-fill this or not expose it

**VM Admin Password** (if prompted)

* Password for VM access
* Must meet Azure complexity requirements:
  * At least 12 characters
  * Mix of uppercase, lowercase, numbers, symbols
* **Store this password securely** - you'll need it for VM access

**SQL Username** (if using Dedicated SQL Server)

* Username for SQL Server administrator
* Example: `sqladmin`
* Will be used to connect to SQL Server

**SQL Password** (if using Dedicated SQL Server)

* Password for SQL Server administrator
* Must meet SQL Server complexity requirements:
  * At least 8 characters
  * Mix of uppercase, lowercase, numbers, symbols
* **Store this password securely**

**Region/Location**

* Azure region where resources will be created
* Ideally, use the same region as your Development environment
* Example: `East US`, `West Europe`, `Southeast Asia`
* Note: The interface may not allow changing this currently

**Optional Parameters**

Some parameters may be auto-filled or determined by the script:

* VM size/SKU
* Storage account settings
* Network configuration details

{% hint style="info" %}
The current version of the deployment interface doesn't expose all parameters that will be available in future releases. The script uses reasonable defaults for unexposed parameters.
{% endhint %}

#### Step 3: Review Configuration

Before proceeding:

1. **Double-check all parameters** - especially names and passwords
2. **Verify you're in the QA environment** - not Dev or Prod
3. **Confirm you've chosen the correct SQL Server option** (shared vs. dedicated)
4. **Save passwords securely** - you'll need them later

#### Step 4: Add the Script

1. Click the **Add** button to **add the script** to your environment
2.  The script appears in the infrastructure scripts list:

    * Script name shown
    * Status: **"New"** (not yet deployed)

    <figure><img src="../../.gitbook/assets/image (500).png" alt=""><figcaption></figcaption></figure>

#### Step 5: Deploy the QA Environment

1. Locate your newly added script in the list
2.  Click **"Deploy script"** next to the script<br>

    <figure><img src="../../.gitbook/assets/image (498).png" alt=""><figcaption></figcaption></figure>
3. Deployment begins immediately:
   * Status changes to **"Busy"**
   * ARM template submitted to Azure
   * Background process starts
4. **Estimated deployment time: 45-60 minutes**

#### Step 6: Monitor Deployment Progress

The deployment runs in the background. You can monitor progress in multiple ways:

**In the Toolkit**

* Status indicator updates automatically
* Shows "Busy" while deployment runs
* You can navigate to other Toolkit pages and continue working
* Return anytime to check status

**In Azure Portal (Recommended)**

For detailed progress monitoring:

1. Open **Azure Portal** in another browser tab
2. Navigate to **Resource Groups**
3. Find your QA resource group (name you specified)
4. Click **"Deployments"** in the left sidebar
5. You'll see the deployment in progress:
   * **Deployment name**: Usually contains timestamp
   * **Status**: Running (with spinning indicator)
   * **Duration**: Shows how long it's been running
6. Click on the deployment name to see **detailed progress**:
   * List of all resources being created
   * Status of each resource (Creating, Succeeded, Failed)
   * Any error messages
   * Timeline of operations

**Resources appear in this general order:**

* Virtual Network (VNet)
* Network Security Group (NSG)
* Public IP Address
* Network Interface
* SQL Server (if dedicated option)
* Virtual Machine
* SQL Databases
* Storage Account
* Custom Script Extension (triggers platform installation)

7. **Watch for Custom Script Extension**:
   * This is the last resource created
   * When it starts, the VM is running and platform installation begins
   * This phase takes the longest (30-45 minutes)

**On the VM (Advanced)**

If you want to watch platform installation in real-time:

1. Wait until VM is created (about 10-15 minutes into deployment)
2. Get the VM's Public IP address from Azure Portal
3. **Remote Desktop** to the VM:
   * Use Remote Desktop Connection (Windows) or RDP client
   * Enter the Public IP address
   * Login with VM credentials you specified
4. Navigate to `C:\temp\setup\`
5. Open `setup.log` in Notepad (or Notepad++)
6.  Watch installation progress in real-time:

    ```
    [2025-11-13 10:15:23] Downloading installation files...
    [2025-11-13 10:16:45] Installing Windows Features...
    [2025-11-13 10:18:12] Installing Config Hub...
    [2025-11-13 10:22:33] Installing Auth Server...
    [etc...]
    ```
7. The log shows each component being installed and tested

{% hint style="info" %}
You don't need to watch the installation - it runs completely automated. This is only useful for troubleshooting an or observation.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (501).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (502).png" alt=""><figcaption><p><strong>qa</strong> environment ongoing deployment</p></figcaption></figure>

#### Step 7: Verify Deployment Completion

Deployment is complete when:

**In the Toolkit:**

* Status changes from "Busy" to **"Deployed"** or **"Success"**

**In Azure Portal:**

* Deployment status shows **green checkmark** with "Succeeded"
* All resources show "Succeeded" status
* No error messages or warnings

**Resources Created:**

Navigate to your QA resource group and verify it contains:

**For Dedicated SQL Server:**

* 1 Virtual Machine
* 1 SQL Server
* Multiple SQL Databases (platform databases)
* 1 Storage Account
* 1 Virtual Network
* 1 Network Security Group
* 1 Network Interface
* 1 Public IP Address
* 1 OS Disk (Managed Disk)
* Application Insights (if observability enabled)

**For Shared SQL Server:**

* 1 Virtual Machine
* 0 SQL Servers (uses Dev's server)
* Multiple SQL Databases (in Dev resource group)
* 1 Storage Account
* 1 Virtual Network
* 1 Network Security Group
* 1 Network Interface
* 1 Public IP Address
* 1 OS Disk (Managed Disk)
* Application Insights (if observability enabled)

#### Troubleshooting Deployment Issues

If deployment fails or takes longer than expected:

**Deployment shows "Busy" for over 90 minutes:**

* Check Azure Portal deployment logs for errors
* Look for resource creation failures
* Common cause: Azure quota limits reached

**Deployment shows "Succeeded" but resources missing:**

* Platform installation may have failed
* RDP to VM and check `C:\temp\setup\setup.log`
* Look for error messages in the log
* Platform installation retries up to 3 times automatically

**Deployment shows "Failed":**

* Click deployment name in Azure Portal
* Review error messages
* Common issues:
  * VM size not available in region
  * Quota exceeded
  * Network name conflicts
  * Invalid parameters

**Need Help:**

* Contact ComUnity support with:
  * Screenshot of error
  * Deployment logs from Azure Portal
  * Setup.log from VM (if accessible)
  * Resource group name and subscription ID

### Post-Deployment Setup

After your QA environment deployment completes successfully, several important steps remain before the environment is fully operational and ready for use.

#### Step 1: Enable the QA Environment

New environments are not automatically available within the Toolkit. You must manually enable them:

1. Navigate to **Infrastructure > Azure Infrastructure**
2. The environment management interface displays three environments:
   * **Development Environment**: Enabled (cannot be disabled)
   * **QA Environment**: Disabled
   * **Production Environment**: Disabled
3. Locate the **QA Environment** row
4. Toggle the enable switch to **ON** (or check the enabled checkbox)
5. Click **"Save Changes"** button
6. The QA environment is now enabled within the Toolkit

**What this does:**

* Makes QA environment appear in deployment dropdown menus
* Allows you to deploy projects to QA
* Makes QA visible in environment-related screens

**What this does NOT do (currently):**

* Does not start or stop Azure resources
* Does not affect the actual infrastructure
* Does not back up or restore environment data

{% hint style="info" %}
In upcoming releases, enabling/disabling will control environment state: disabling will shut down and back up the environment, enabling will restore it. This functionality is planned but not yet implemented.
{% endhint %}

#### Step 2: Verify Deployment Success

Before proceeding, confirm the deployment was truly successful:

**Check Toolkit Status**

1. Navigate back to **Infrastructure > QA Environment > Infrastructure Scripts**
2. Find your deployment script
3. Status should show **"Deployed"** or **"Success"**

**Check Azure Resources**

1. Open **Azure Portal**
2. Navigate to **Resource Groups** > Your QA resource group
3. Verify all expected resources exist (see list in previous section)
4. Check that **VM is running**:
   * Find the Virtual Machine resource
   * Status should be "Running"
   * If stopped, start it manually

**Check Platform Access**

1. Get the **Public IP address**:
   * Azure Portal > Resource Groups > QA Resource Group
   * Click on the Public IP resource
   * Copy the IP address value
2. Open browser to `http://[PUBLIC-IP-ADDRESS]`
3. You should see the **Toolkit login screen**
4. Login with default credentials:
   * Username: `admin@comunityplatform.com`
   * Password: `admin`
5. If login succeeds, platform installation was successful!

#### Step 3: Configure Deployment Agent (Critical)

The Deployment Agent requires App Registration credentials to create databases and deploy projects. Without this configuration, you cannot build or deploy projects.

1. In the QA environment (accessed via Public IP), navigate to:
   * **Platform Settings** (or Platform menu)
   * **Deployment Agent**
2. Locate these fields:
   * **Azure Client ID**
   * **Azure Client Secret**
3. Enter the values from your Azure App Registration:
   * Copy Client ID from App Registration in Azure Portal
   * Copy Client Secret from App Registration
4. Save the changes

{% hint style="info" %}
If you haven't created an App Registration yet, this must be done before you can successfully deploy projects. Contact support for step-by-step guidance on creating and configuring the App Registration with correct permissions.
{% endhint %}

#### Step 4: Configure Observability URLs (If Using Observability)

If your project uses observability features, update the monitoring endpoints:

1. Navigate to **Platform Settings** in the QA environment
2. For each platform component that requires observability:
   * Media Server
   * Communications Server
   * Other monitored components
3. Locate the **Observability URL** fields
4. Update with correct monitoring endpoints

{% hint style="info" %}
Observability URL configuration is still being finalised. In some cases, these values should be auto-populated during deployment but currently are not. This will be improved in future releases.
{% endhint %}

#### Step 5: Change Default Credentials (Security)

The environment was deployed with default credentials that should be changed immediately:

1. Login to QA environment as `admin@comunityplatform.com`
2. Navigate to user management section
3. Change the admin password to a strong, unique password
4. Consider creating individual user accounts rather than sharing admin account
5. **For Production environments**, this step is critical and must not be skipped

#### Step 6: Configure Domain Name and SSL (Recommended for Production)

Currently, the QA environment is accessed via IP address over HTTP. For Production environments (and optionally for QA), you should:

1. **Register a domain name** (if not already done)
2. **Configure DNS** to point to the Public IP address:
   * Create an A record pointing to the IP
   * Example: `qa.yourcompany.com` → `20.123.45.67`
3. **Obtain SSL certificate**:
   * Use Let's Encrypt (free, automated)
   * Purchase from certificate authority
   * Use Azure-managed certificates
4. **Install certificate on VM**:
   * RDP to the VM
   * Install certificate in Windows certificate store
   * Configure IIS bindings for HTTPS
5. **Update Toolkit configuration**:
   * Update platform URLs to use HTTPS
   * Update redirect URLs in Auth configuration

{% hint style="info" %}
Domain and SSL configuration is currently a manual process. Documentation for these steps is in development. Contact support for detailed guidance, especially for Production environments where HTTPS is strongly recommended.
{% endhint %}

#### Step 7: Deploy Your First Project to QA

Test the new environment by deploying a project:

1. **In your Development environment** (your main Toolkit instance):
   * Navigate to your project
   * You should now see "QA Environment" in the deployment dropdown
   * If you don't see it, ensure you completed Step 1 (Enable Environment)
2. **Select QA Environment** from the dropdown
3. Click **"Build"** to build the project for QA
4. Monitor the build process:
   * If App Registration is correctly configured, build proceeds
   * Databases are created in QA SQL Server (or on shared server)
   * Project components are deployed
5. Click **"Deploy"** to deploy to QA
6. **Launch** the application in QA
7. Test basic functionality:
   * Can access the application
   * Can login
   * Basic features work
   * Data is separate from Dev environment

#### Step 8: Configure Backups (Production Recommended)

For Production environments, configure backup policies:

1. **SQL Database Backups**:
   * Azure SQL has automatic backups enabled
   * Configure retention period (7-35 days)
   * Consider long-term retention for compliance
2. **VM Backups** (optional):
   * Configure Azure Backup for the VM
   * Set backup schedule (daily/weekly)
   * Configure retention policy
3. **Storage Account Backups**:
   * Enable soft delete for blob storage
   * Consider geo-redundant storage (GRS)

#### Post-Deployment Checklist

Use this checklist to ensure all setup steps are complete:

```
[ ] Environment enabled in Toolkit (Infrastructure > Azure Infrastructure)
[ ] Can access environment via Public IP address
[ ] Can login with default credentials
[ ] Default credentials changed to secure passwords
[ ] App Registration configured (Client ID and Secret)
[ ] Deployment Agent can connect to Azure (test with project build)
[ ] Observability URLs configured (if using observability)
[ ] Environment appears in project deployment dropdowns
[ ] Successfully deployed and tested a project in the environment
[ ] Domain name configured (Production recommended)
[ ] SSL certificate installed (Production recommended)
[ ] Backup policies configured (Production recommended)
[ ] Team members have appropriate access/credentials
```

#### Common Post-Deployment Issues

**Can't build projects in QA:**

* **Cause:** App Registration not configured
* **Solution:** Configure Azure Client ID and Secret in Deployment Agent

**Environment doesn't appear in deployment dropdown:**

* **Cause:** Environment not enabled
* **Solution:** Enable in Infrastructure > Azure Infrastructure

**Can't access via IP address:**

* **Cause:** VM not running or NSG blocking traffic
* **Solution:** Start VM in Azure Portal, check NSG rules

**Projects deploy but don't work:**

* **Cause:** Missing configuration, database connection issues
* **Solution:** Check logs, verify all configuration steps completed

### Managing Deployment Scripts

After adding scripts to your environment, several management options are available through the infrastructure interface.

#### Viewing Infrastructure Scripts

To see all scripts configured for an environment:

1. Navigate to **Infrastructure** from main menu
2. Select the environment (QA or Production)
3. Click on **Infrastructure Scripts** section
4. You'll see a list of all scripts with:
   * Script name
   * Associated URL/identifier
   * Current status (New, Busy, Deployed, Failed)
   * Action buttons (Deploy, View Details, Edit, Delete)

#### Viewing Script Details

To see detailed information about a deployed script:

1. Locate the script in the infrastructure scripts list
2. Click **"View Details"** button
3. The view expands to show additional information:
   * Script parameters used
   * Deployment timestamp
   * Resource group name
   * SQL Server configuration (if applicable)
   * Additional metadata

**Alternative method:**

1. Click the **three-dot menu (⋮)** next to the script
2. Select **"View Details"** from the dropdown
3. Details section expands below the script entry

#### Editing Script Configuration

To modify script parameters after adding but before deploying:

{% hint style="info" %}
You can only edit scripts with "New" status. Once deployed, script parameters cannot be changed through the Toolkit interface.
{% endhint %}

1. Locate the script with **"New"** status
2. Click the **three-dot menu (⋮)**
3. Select **"View Details"** to expand
4. Click **"Edit Function App Details"** button
5. Modify the configuration parameters:
   * Update resource group name
   * Change passwords
   * Adjust other parameters
6. Save changes
7. Script remains in "New" status ready for deployment with updated parameters

**Limitations:**

* Cannot edit scripts that have been deployed
* Cannot change script type (dedicated ↔ shared)
* Some auto-generated parameters cannot be edited

#### Redeploying Scripts

If you need to redeploy an environment:

{% hint style="warning" %}
Redeployment is not currently supported through the Toolkit interface. Attempting to redeploy will likely cause issues.
{% endhint %}

**Do NOT:**

* Deploy the same script twice
* Try to "refresh" an environment by redeploying

**If you need to rebuild an environment:**

1. Delete the existing environment (see next section)
2. Create and deploy a new script
3. Reconfigure all settings

**Alternative approaches:**

* For configuration changes: Update settings directly in the environment
* For infrastructure changes: Modify resources in Azure Portal
* For major changes: Contact support for guidance

#### Deleting Deployment Scripts

The delete function permanently removes both the script entry from the Toolkit AND the actual Azure resources created by that deployment.

**⚠️ CRITICAL DELETE WARNING**

**When you delete a deployment script:**

* All Azure resources in the resource group are **permanently deleted**
* All databases are **permanently deleted**
* All data is **permanently lost**
* There is **no undo** or recovery option
* Nothing backs up your environment before deletion
* This action **cannot be reversed**

**You will lose:**

* Virtual machines and all installed software
* SQL databases and all data
* Storage accounts and all files/media
* Network configuration
* All platform settings and configurations
* All deployed projects and their data

**Only delete a script when:**

* Testing/learning and want to clean up resources
* Environment is no longer needed
* You have backed up any important data elsewhere
* You understand data will be permanently lost

**Never delete a script for:**

* Production environments (unless permanently retiring)
* Environments with live user data
* Active QA environments in use by your team
* Environments you might need in the future

**How to Delete a Script**

1. Navigate to **Infrastructure > \[Environment] > Infrastructure Scripts**
2. Locate the script you want to delete
3. Click the **three-dot menu (⋮)** next to the script name
4. Select **"Delete"** from the dropdown menu
5.  A warning dialog appears:

    ```
    Warning: This will delete the deployment script and all 
    associated Azure resources. This action cannot be undone.

    Continue with deletion?
    ```
6. If you're absolutely certain, confirm deletion
7. The deletion process begins:
   * Runs in the background
   * Status may show briefly as "Deleting"
   * Takes several minutes to complete
8. When deletion completes:
   * Script removed from the Toolkit list
   * Resource group and all contents deleted from Azure

**Verify Deletion**

After deletion completes, verify in Azure Portal:

1. Navigate to **Resource Groups**
2. The deleted resource group should no longer appear
3. If it still exists, check Azure's "Deleted" items or Activity Log

**Known Issues and Limitations**

**Status Display:**

* Deletion progress may not display clearly
* Script may disappear from list before Azure deletion completes
* Check Azure Portal to confirm resources are actually deleted

**Partial Deletions:**

* If deletion fails partway through, some resources may remain
* You may need to manually delete remaining resources in Azure Portal
* Look for orphaned resources in Azure to avoid ongoing costs

**Stuck Deletions:**

* If delete runs indefinitely (>15 minutes), check Azure Portal
* Some resources have dependencies that must delete in order
* Resources with locks cannot be deleted automatically
* Soft-deleted resources (SQL, Key Vault) may require additional steps

**Planned Enhancement**

Future releases will expand the delete warning to display exactly which Azure resources will be deleted before confirming, providing better visibility into what will be removed.

**Future Changes to Delete Functionality**

The behavior of the delete function will change in future releases:

**For environment scripts (QA, Production):**

* Delete functionality may be disabled completely
* Or restricted to require administrator approval
* Or replaced with "disable" that shuts down without deleting

**For custom scripts (future feature):**

* Delete functionality will remain available
* Allows users to remove their own Azure resources
* Provides flexibility for custom resource management

**Rationale:** Accidentally deleting an entire environment (especially Production) is catastrophic. Future versions will make this harder to do unintentionally while still allowing removal of test/temporary resources.

### Environment Management

The Infrastructure Management section includes environment availability controls that determine whether environments appear in deployment screens throughout the Toolkit.

#### Understanding Enable/Disable

Each environment has an enable/disable setting:

* **Development Environment**: Always enabled (cannot be disabled)
* **QA Environment**: Can be enabled or disabled
* **Production Environment**: Can be enabled or disabled

**What enabling/disabling controls:**

* Visibility in deployment dropdown menus
* Availability when deploying projects
* Appearance in environment-related screens

**What enabling/disabling does NOT control (currently):**

* Does not start or stop Azure resources
* Does not affect infrastructure costs
* Does not back up or restore data
* Does not modify anything in Azure

#### Current Behavior (v25.3)

When you enable or disable an environment and save changes:

**Enabling an environment:**

* Updates the environment record in the Toolkit database
* Makes the environment available in deployment screens
* Allows users to select this environment when deploying projects
* Environment appears in all relevant dropdowns

**Disabling an environment:**

* Updates the environment record in the Toolkit database
* Hides the environment from deployment screens
* When users try to deploy and environment is disabled, they see a message that the environment is not active
* Projects cannot be deployed to the disabled environment

**What does NOT happen:**

* Azure infrastructure remains running (VM, databases, etc.)
* All resources continue to consume Azure credits
* No backup or shutdown occurs
* No data is moved or protected

{% hint style="info" %}
Currently, enable/disable only controls Toolkit visibility. It does not affect actual infrastructure. This is a limitation of the v25.3 implementation.
{% endhint %}

#### Intended Future Behaviour

The enable/disable functionality is designed for future capabilities:

**When you disable an environment (future):**

* System should shut down the environment:
  * Stop the VM (deallocate to stop charges)
  * Back up databases to blob storage
  * Save configuration state
  * Reduce infrastructure costs to minimum (storage only)
* Environment data is preserved but infrastructure is offline
* Significant cost savings for unused environments

**When you enable an environment (future):**

* System should restore the environment:
  * Start the VM
  * Restore databases from backup
  * Restore configuration state
  * Bring environment back online
* Environment returns to operational state
* Incurs full infrastructure costs again

**Use cases this will enable:**

* Turn off QA environment on weekends/holidays to save costs
* Temporarily disable Production during maintenance windows
* Reduce spending on temporarily unused environments
* Quick environment recovery when needed again

{% hint style="info" %}
**Status:** This functionality is not yet implemented. The infrastructure exists in the interface but the automation does not. This is on the development roadmap for future releases.
{% endhint %}

#### Accessing Environment Settings

To manage environment enable/disable settings:

1. Navigate to **Infrastructure** from the main menu
2. Click on **Azure Infrastructure**
   * This is different from "Infrastructure Scripts"
   * Look for environment management section
3. The environment management interface displays:
   * Development Environment: Enabled (checkbox disabled/grayed out)
   * QA Environment: Enabled/Disabled checkbox (can toggle)
   * Production Environment: Enabled/Disabled checkbox (can toggle)

#### Modifying Environment Status

To enable or disable an environment:

1. Navigate to **Infrastructure > Azure Infrastructure**
2. Locate the environment you want to modify:
   * QA Environment
   * Production Environment
   * (Cannot modify Development)
3. **To Enable:**
   * Check the "Enabled" checkbox (or toggle switch to ON)
4. **To Disable:**
   * Uncheck the "Enabled" checkbox (or toggle switch to OFF)
5. Click **"Save Changes"** button at the bottom
6. The environment availability updates immediately:
   * Changes take effect immediately throughout the Toolkit
   * Deployment dropdowns update
   * Users see changes on next screen refresh

#### Practical Use Cases (Current Functionality)

Given the current limitations, here's when to use enable/disable:

**Disable an environment when:**

* Environment deployment failed and you're not using it yet
* You want to prevent team members from deploying to it temporarily
* Environment is misconfigured and you're fixing issues
* You want to hide it while you're still setting it up

**Enable an environment when:**

* Deployment is complete and environment is ready for use
* Configuration is finished and tested
* You want team members to be able to deploy projects
* Environment is fully operational

**Don't use disable for:**

* Saving costs (doesn't stop Azure resources currently)
* "Shutting down" the environment (doesn't affect infrastructure)
* Backing up data (doesn't trigger any backup)

#### Workaround for Stopping Environment (Current Version)

If you need to actually stop a QA environment to save costs:

**Manual Method:**

1. In Azure Portal, navigate to your QA resource group
2. **Stop the VM:**
   * Find the Virtual Machine resource
   * Click "Stop" (not "Shutdown")
   * Choose "Stop (Deallocated)" to avoid compute charges
   * VM state changes to "Stopped (deallocated)"
3. **Databases continue running** (can't easily stop Azure SQL)
4. **When you need the environment again:**
   * Start the VM in Azure Portal
   * Wait for VM to boot (2-5 minutes)
   * Services should automatically start

**Cost Savings:**

* Stopped (deallocated) VM: No compute charges
* SQL Databases: Still incur charges (can't stop them easily)
* Storage: Still incurs minimal charges
* Network: Minimal ongoing charges

**Typical savings:** 40-60% of environment cost by stopping VM

#### Best Practices for Environment Management

1. **Always Enable After Successful Deployment:**
   * Don't forget this step - new environments are disabled by default
   * Team members can't use environment until enabled
2. **Disable During Extended Maintenance:**
   * If you need to do major configuration work
   * Prevents others from deploying during your changes
   * Communicate with team about downtime
3. **Don't Rely on Disable for Security:**
   * Disabled environments are still accessible via IP address
   * Disabling only hides from Toolkit deployment screens
   * Use proper security measures (passwords, network rules)
4. **Document Environment Status:**
   * Keep team informed about environment availability
   * Note in documentation when environment is disabled and why
   * Set expectations about when it will be re-enabled
5. **Plan for Future Functionality:**
   * Understand that future versions will actually shut down infrastructure
   * Design processes with that future capability in mind
   * Be ready to leverage cost savings when feature is available

### Troubleshooting

This section covers common issues encountered when deploying and managing infrastructure, along with their solutions.

#### Deployment Issues

**Deployment Status Stuck at "Busy"**

**Symptom:** Script shows "Busy" status for over 90 minutes with no progress.

**Possible Causes:**

* Azure deployment failed but didn't report back to Toolkit
* Network connectivity issues between Toolkit and Azure
* Azure quota limits reached
* Platform installation failed during Custom Script Extension phase

**Resolution Steps:**

1. **Check Azure Portal deployment status:**
   * Navigate to Resource Groups > Your QA resource group
   * Click "Deployments" in left sidebar
   * Look for your deployment (usually has timestamp in name)
   * Check if it's still running, succeeded, or failed
2. **If deployment succeeded in Azure but Toolkit shows "Busy":**
   * This is a known issue where status doesn't update
   * Manually verify all resources were created
   * Check if VM is running
   * Check platform installation logs (see below)
   * Consider the deployment successful if resources exist
3. **If deployment is still running in Azure after 90 minutes:**
   * Check which resource is being created
   * Custom Script Extension is the longest phase (30-45 minutes)
   * If stuck on specific resource, may need to cancel and retry
4. **If deployment failed in Azure:**
   * Click on failed deployment to see error details
   * Common errors:
     * **Quota Exceeded**: Request quota increase in Azure Portal
     * **VM Size Unavailable**: Choose different region or VM size
     * **Network Conflicts**: Resource naming conflict, choose different names
     * **Authorization Failed**: Check permissions on subscription
5. **Check Platform Installation:**
   * RDP to the VM (get IP from Azure Portal)
   * Navigate to `C:\temp\setup\`
   * Check if `setup.log` exists and is being updated
   * Look for errors in the log file
   * Installation attempts up to 3 retries (`setup_1.log`, `setup_2.log`)

**Deployment Shows "Deployed" But Resources Missing**

**Symptom:** Toolkit shows "Deployed" status but some or all Azure resources are missing.

**Known Issue:** Deployment can report success even when platform installation fails. This is a current limitation being addressed.

**Resolution Steps:**

1. **Check Azure Portal:**
   * Navigate to your resource group
   * Count the resources - should have 8-12 items depending on configuration
   * Compare to expected resources list (see "What Gets Created" section)
2. **If infrastructure resources exist but platform not accessible:**
   * Platform installation likely failed
   * RDP to the VM
   * Check `C:\temp\setup\setup.log`
   * Look for error messages in the log
3. **Common platform installation failures:**
   * Download of installation packages failed (network issue)
   * Required software installation failed (Windows feature issues)
   * Database creation failed (App Registration not configured)
   * Services failed to start (configuration errors)
4. **If significant resources are missing:**
   * ARM template deployment partially failed
   * Check Azure deployment logs for specific resource failures
   * May need to delete resource group and retry deployment
5. **Contact Support:**
   * Provide screenshots of error messages
   * Provide `setup.log` file from VM (if accessible)
   * Provide Azure deployment logs
   * Note the exact point where deployment failed

**Deployment Fails Immediately**

**Symptom:** Status changes to "Failed" within minutes of starting deployment.

**Possible Causes:**

* Invalid parameters provided
* Naming conflicts with existing resources
* Insufficient permissions
* Azure service outage

**Resolution Steps:**

1. **Check error message in Toolkit** (if displayed)
2. **Check Azure Portal deployment logs:**
   * Navigate to Resource Groups > Click your resource group name
   * If resource group wasn't created, check subscription-level deployments
   * Look for failed deployment with red X
   * Click deployment to see detailed error
3.  **Common errors and fixes:**

    **"Resource name already exists":**

    * Another resource group with that name exists
    * Choose a different resource group name
    * Or delete the existing resource group first

    **"Quota exceeded":**

    * You've hit Azure subscription limits for VMs, cores, or SQL databases
    * Request quota increase in Azure Portal
    * Or choose smaller VM size if available

    **"Location not available":**

    * Chosen Azure region doesn't support the VM size
    * Try different region (ideally same as Dev environment)
    * Or choose different VM size

    **"Authorization failed":**

    * Your account lacks permissions to create resources
    * Contact Azure subscription administrator
    * Ensure you have Contributor role on subscription or resource group
4. **Fix the issue and retry:**
   * Delete the failed script from Toolkit
   * Add script again with corrected parameters
   * Deploy again

**Cannot Access Environment After Deployment**

**Symptom:** Deployment succeeded but cannot access environment via browser at IP address.

**Possible Causes:**

* VM is not running
* Network Security Group (NSG) blocking traffic
* IIS not started
* Platform installation incomplete

**Resolution Steps:**

1. **Verify VM is running:**
   * Azure Portal > Resource Groups > Your resource group
   * Find Virtual Machine resource
   * Status should show "Running"
   * If "Stopped", click "Start"
2. **Verify Public IP assigned:**
   * Find "Public IP address" resource
   * Click on it
   * Verify IP address is assigned (not blank)
   * Copy the IP address
3. **Check in browser:**
   * Open browser to `http://[IP-ADDRESS]`
   * Don't use HTTPS yet (no certificate installed)
   * Don't add any path - just the IP
4. **If connection times out:**
   * Check NSG rules:
     * Find "Network Security Group" resource
     * Click "Inbound security rules"
     * Verify rule allowing HTTP (port 80) from your IP
     * If missing, add inbound rule for port 80
5. **If connection refused:**
   * RDP to the VM
   * Check if IIS is running:
     * Open IIS Manager
     * Verify websites are started
     * Check if ports are listening: `netstat -ano | findstr :80`
6. **If shows IIS default page instead of Toolkit:**
   * Platform installation didn't complete
   * Check `C:\temp\setup\setup.log` for errors
   * Services may need to be started manually

#### Project Build/Deploy Issues

**Cannot Build Projects in New Environment**

**Symptom:** After deploying QA environment, attempting to build a project fails with database creation error.

**Cause:** App Registration not configured properly.

**Error messages you might see:**

* "Failed to create database"
* "Authorization failed"
* "Cannot connect to SQL Server"
* "Deployment Agent error"

**Resolution:**

1. **Verify App Registration exists:**
   * Azure Portal > Azure Active Directory
   * App registrations > Find your app registration
   * Note the Application (client) ID
2. **Verify Client Secret created:**
   * Click on your App Registration
   * Certificates & secrets
   * Verify a client secret exists and is not expired
   * If expired or missing, create new secret
   * **Copy the secret value immediately** (only shown once)
3. **Configure in Deployment Agent:**
   * Login to QA environment (via IP address)
   * Navigate to Platform Settings > Deployment Agent
   * Enter Azure Client ID
   * Enter Azure Client Secret
   * Save changes
4. **Verify App Registration permissions:**
   * App Registration should have appropriate Azure permissions
   * Typically needs Contributor role on subscription or resource group
   * Contact support for exact permissions required
5. **Test with simple project:**
   * Try building a basic test project
   * Monitor build logs for specific errors
   * If still fails, check Deployment Agent logs

**Projects Deploy But Don't Work**

**Symptom:** Project builds and deploys successfully but application doesn't function correctly in QA.

**Possible Causes:**

* Missing configuration
* Database connection issues
* Services not running
* Network/firewall blocking internal communication

**Resolution:**

1. **Check project deployment logs** in Toolkit
2. **Verify databases created:**
   * Azure Portal > SQL Server > Databases
   * Confirm project databases exist
   * Check if any errors in database creation
3. **Check IIS websites:**
   * RDP to VM
   * Open IIS Manager
   * Verify project websites exist and are started
   * Check application pool status
4. **Check application logs:**
   * Navigate to project log location on VM
   * Look for application errors
   * Check for missing configuration or connection errors
5. **Verify configuration:**
   * Check project-specific configuration
   * Verify connection strings
   * Confirm all required settings copied from Dev

#### Environment Management Issues

**Environment Doesn't Appear in Deployment Dropdown**

**Symptom:** QA environment deployed successfully but doesn't appear when trying to deploy projects.

**Cause:** Environment not enabled in Infrastructure > Azure Infrastructure settings.

**Resolution:**

1. Navigate to **Infrastructure > Azure Infrastructure**
2. Find QA Environment row
3. Check the "Enabled" checkbox
4. Click "Save Changes"
5. Refresh your browser
6. QA should now appear in deployment dropdowns

**Can't Remote Desktop to VM**

**Symptom:** Cannot connect to VM via Remote Desktop.

**Possible Causes:**

* VM not running
* NSG blocking RDP port
* Wrong credentials
* Public IP not assigned

**Resolution:**

1. **Verify VM is running** in Azure Portal
2. **Check NSG rules:**
   * Find Network Security Group
   * Inbound security rules
   * Verify rule allowing RDP (port 3389) from your IP
   * Add rule if missing
3. **Verify credentials:**
   * Use VM Admin username and password from deployment
   * Format: just username, not domain\username
   * Try resetting password in Azure Portal if forgotten
4. **Verify Public IP:**
   * Find Public IP address resource
   * Confirm IP is assigned
   * Try connecting to that specific IP
5. **Check local firewall:**
   * Ensure your local firewall allows outbound RDP
   * Try from different network if corporate firewall blocking

#### Deletion Issues

**Script Delete Runs Indefinitely**

**Symptom:** Clicked delete but script doesn't disappear and Azure resources still exist after 15+ minutes.

**Possible Causes:**

* Resource locks preventing deletion
* Resources with dependencies (must delete in order)
* Soft-deleted resources requiring additional steps
* Azure API issues

**Resolution:**

1. **Check Azure Portal:**
   * Navigate to resource group
   * See if resources are actually being deleted
   * Look for deletion in progress
2. **Check for resource locks:**
   * Resource group > Locks
   * If locks exist, delete them first
   * Then retry deletion
3. **Manual deletion:**
   * If automatic deletion stalls, delete manually:
   * Azure Portal > Resource group
   * Click "Delete resource group"
   * Type resource group name to confirm
   * This forces deletion of all contents
4. **Check for soft-deleted resources:**
   * Some resources (SQL, Key Vault) soft-delete
   * May need to purge from soft-delete state
   * Azure Portal > Resource type > Deleted items
   * Permanently delete from there

**Partial Deletion**

**Symptom:** Some resources deleted but others remain, script removed from Toolkit.

**Cause:** Deletion failed partway through, leaving orphaned resources.

**Resolution:**

1. **Find remaining resources:**
   * Azure Portal > Resource Groups
   * Check if resource group still exists
   * Note which resources remain
2. **Delete remaining resources manually:**
   * Delete each resource individually
   * Or delete entire resource group if present
3. **Check for hidden costs:**
   * Orphaned resources still incur Azure charges
   * Ensure nothing remains that shouldn't
4. **Prevent in future:**
   * Always verify deletion completes
   * Check Azure Portal after deletion
   * Clean up manually if automatic deletion fails

#### Performance Issues

**Environment Runs Slowly**

**Symptom:** QA environment responds slowly, applications lag, deployments take excessive time.

**Possible Causes:**

* Undersized VM
* SQL Server resource contention (if using shared)
* Network latency
* Too many concurrent users

**Resolution:**

1. **Check VM size:**
   * Azure Portal > VM > Size
   * May need to scale up to larger VM
   * Stop VM, resize, restart
2. **Check SQL Server performance:**
   * If using shared SQL, check if Dev environment also slow
   * May indicate SQL Server overwhelmed
   * Consider scaling up SQL tier
   * Or switch to dedicated SQL Server
3. **Check Azure region:**
   * Ensure region is geographically close to users
   * High latency if region far from user location
4. **Monitor resource utilization:**
   * Azure Portal > VM > Metrics
   * Check CPU, memory, disk, network usage
   * Scale up if consistently high

#### Getting Help

If you can't resolve an issue using this troubleshooting guide:

**Contact ComUnity Support:**

Provide the following information:

1. **Description of the issue:**
   * What you were trying to do
   * What happened vs. what you expected
   * When the issue started
2. **Environment details:**
   * Environment name (Dev/QA/Prod)
   * Azure subscription ID
   * Resource group name
   * Toolkit version
3. **Screenshots:**
   * Error messages in Toolkit
   * Azure Portal deployment logs
   * Any relevant screens showing the issue
4. **Log files (if accessible):**
   * `C:\temp\setup\setup.log` from VM
   * Azure deployment logs (export from Portal)
   * Application logs if project-related
5. **Steps to reproduce:**
   * What steps lead to the issue
   * Can you reproduce it consistently?

**Support Channels:**

* Support portal: \[URL to be provided]
* Email: \[Email to be provided]
* Phone: \[Phone to be provided]

**For urgent Production issues:**

* Mark as "High Priority" or "Production Down"
* Include impact statement (number of users affected, business impact)

### Best Practices

Follow these recommendations for successful infrastructure management:

#### Planning and Architecture

1. **Start with Shared SQL for QA:**
   * Test the deployment workflow with lower-cost option
   * Evaluate performance before committing to dedicated for Production
   * Understand the process before making expensive infrastructure decisions
2. **Use Dedicated SQL for Production:**
   * Don't compromise on Production environment isolation
   * Better performance predictability for customer-facing applications
   * Easier troubleshooting and scaling
3. **Test Before Deploying to Production:**
   * Deploy to QA first
   * Verify entire deployment process works correctly
   * Identify and fix issues before creating Production
   * Practice post-deployment configuration steps
4. **Plan for Multiple Environments:**
   * Development (auto-created)
   * QA (deploy first)
   * Staging (optional, consider for complex projects)
   * Production (deploy last, after testing workflow)

#### Deployment Process

1. **Document Your Decisions:**
   * Record why you chose shared vs. dedicated SQL
   * Note all custom parameters used
   * Keep passwords in secure password manager
   * Document any non-standard configuration
2. **Use Descriptive Naming:**
   * Resource groups: `projectname-qa`, `projectname-prod`
   * Clear naming helps identify resources in Azure
   * Easier to manage costs and permissions
3. **Monitor Deployment Progress:**
   * Don't just start deployment and walk away
   * Check Azure Portal periodically
   * Catch errors early if deployment fails
   * Especially important for first deployment
4. **Verify Immediately After Deployment:**
   * Don't wait days to check if deployment succeeded
   * Run through verification checklist promptly
   * Easier to troubleshoot fresh deployments
   * Resources are still in failed state if issues exist

#### Post-Deployment Configuration

1. **Complete All Setup Steps:**
   * Don't skip post-deployment configuration
   * App Registration is critical - configure immediately
   * Change default passwords on first login
   * Complete all checklist items before considering deployment done
2. **Test Incrementally:**
   * After enabling environment, test basic access
   * Deploy simple test project before real projects
   * Verify each capability before relying on it
   * Catch configuration issues early
3. **Secure Production Environments:**
   * Change all default credentials immediately
   * Configure custom domain and SSL certificate
   * Set up appropriate firewall rules
   * Implement backup policies
   * Document security measures

#### Operational Management

1. **Enable Environments Only When Ready:**
   * Don't enable until post-deployment setup is complete
   * Prevents users from deploying to misconfigured environment
   * Communicate with team when enabling
2. **Document Environment Status:**
   * Maintain documentation about environment readiness
   * Note configuration details for each environment
   * Keep team informed of environment availability
   * Record any ongoing issues or limitations
3. **Regular Verification:**
   * Periodically verify environments are functioning correctly
   * Check that backups are running (Production)
   * Monitor Azure costs for unexpected spikes
   * Verify SSL certificates haven't expired
4. **Cost Management:**
   * Monitor Azure costs for each environment
   * Stop/deallocate VMs when not needed (currently manual)
   * Consider environment shutdown during non-business hours
   * Scale down resources that are over-provisioned

#### Troubleshooting and Support

1. **Check Toolkit First, Then Azure:**
   * Status in Toolkit may lag behind actual Azure status
   * Always verify in Azure Portal if Toolkit status unclear
   * Azure Portal is the source of truth for infrastructure
2. **Keep Logs:**
   * Download setup.log after deployments
   * Save deployment logs from Azure Portal
   * Helpful for troubleshooting later issues
   * Required when contacting support
3. **Know When to Contact Support:**
   * Don't spend hours troubleshooting complex issues
   * Contact support if stuck for more than 30 minutes
   * Support has access to internal tools and knowledge
   * Especially important for Production issues
4. **Provide Good Information:**
   * Clear description of issue
   * Steps to reproduce
   * What you've already tried
   * Screenshots and log files
   * Better information = faster resolution

#### Avoiding Common Mistakes

❌ **Don't:**

* Deploy full environment scripts to existing environments
* Delete Production environments without backups
* Skip App Registration configuration
* Leave default passwords in Production
* Deploy directly to Production without testing in QA first
* Ignore deployment errors - investigate immediately
* Assume deployment succeeded without verifying

✅ **Do:**

* Test with BLOB Storage script first to learn workflow
* Complete all post-deployment setup before using environment
* Verify every deployment in Azure Portal
* Keep passwords secure and change defaults
* Follow proper Dev → QA → Production promotion process
* Monitor costs and optimize resource usage
* Maintain good documentation of your infrastructure

#### Long-term Maintenance

1. **Plan for Growth:**
   * Monitor resource usage over time
   * Scale up before hitting limits, not after
   * Anticipate increased costs as usage grows
   * Review architecture periodically
2. **Stay Updated:**
   * Follow Toolkit release notes
   * Understand upcoming changes to infrastructure features
   * Plan for migration to new interfaces when released
   * Leverage new features as they become available
3. **Document Everything:**
   * Architecture decisions and rationale
   * Configuration details for each environment
   * Credentials and access information (securely)
   * Troubleshooting history and resolutions
   * Changes made over time
4. **Regular Reviews:**
   * Quarterly review of environment performance
   * Annual review of architecture decisions
   * Evaluate if shared SQL still appropriate
   * Consider consolidation or separation of environments

### Related Documentation

For complete understanding of the Toolkit ecosystem, refer to these related guides:

#### Core Infrastructure Documentation

* **\[Azure Marketplace Purchase Guide]** - How to purchase and initially deploy the Toolkit from Azure Marketplace (in development)
* **\[Initial Setup Checklist]** - Post-marketplace deployment steps before using Infrastructure Management (in development)
* **\[App Registration Setup Guide]** - Detailed steps for creating and configuring Azure App Registration with correct permissions (in development)

#### Configuration Guides

* **\[Observability Configuration]** - Setting up monitoring and observability URLs for platform components (in development)
* **\[Domain Name & SSL Certificate Setup]** - Configuring custom domains and HTTPS for Production environments (in development)
* **\[SQL Server Architecture Guide]** - Deep dive into shared vs. dedicated SQL Server decision-making (in development)

#### Operational Guides

* **\[Environment Planning Guide]** - Strategic guidance on environment design and management (in development)
* **\[Azure Resource Management]** - Understanding and managing Azure resources created by the Toolkit (in development)
* **\[Backup and Disaster Recovery]** - Implementing backup policies and recovery procedures (in development)

#### Feature-Specific Documentation

* **\[Reports Configuration]** - Setting up PowerBI reports to monitor your environments
  * Includes connecting PowerBI to MS SQL databases
  * Environment-specific report configuration
  * Creating custom dashboards
* **\[Communications Configuration]** - Managing communication providers across environments
* **\[Observability Features]** - Using Client Analytics, Metrics, and Traces to monitor application performance

#### Support Resources

* **\[Troubleshooting Compendium]** - Comprehensive guide to common issues and solutions (in development)
* **\[Support Engagement Guide]** - When and how to contact ComUnity support (in development)
* **\[Best Practices Library]** - Detailed operational best practices for Toolkit management (in development)

#### External Documentation

* [**Official Azure Documentation**](https://docs.microsoft.com/azure) - Microsoft's comprehensive Azure resource documentation
* [**Azure Pricing Calculator**](https://azure.microsoft.com/pricing/calculator) - Estimate costs for your infrastructure
* [**Azure Architecture Center**](https://docs.microsoft.com/azure/architecture) - Best practices for Azure deployments

#### Feedback and Updates

As the Toolkit evolves, documentation will be updated to reflect new features and improvements:

* Infrastructure Management interface will change significantly in future releases
* Enable/disable functionality will be enhanced to actually manage environment state
* Custom scripts capability will be added
* Additional pre-configured scripts will become available

**Stay informed:**

* Check Toolkit release notes for new features
* Review updated documentation with each release
* Provide feedback on documentation gaps or unclear areas

**Documentation feedback:**

* Report errors or outdated information to \[documentation team]
* Suggest additional topics that would be helpful
* Share your experience to improve guides for others

### Appendix: Quick Reference

#### Common Tasks Quick Guide

| Task                            | Navigation Path                                                       | Key Action                                  |
| ------------------------------- | --------------------------------------------------------------------- | ------------------------------------------- |
| **View infrastructure scripts** | Infrastructure > \[Environment] > Infrastructure Scripts              | View available scripts and status           |
| **Deploy QA environment**       | Infrastructure > QA > Infrastructure Scripts > Add Script > Deploy    | 45-60 minute process                        |
| **Enable environment**          | Infrastructure > Azure Infrastructure > Toggle Enable > Save          | Makes environment available for deployments |
| **Check deployment status**     | Infrastructure > \[Environment] > Infrastructure Scripts              | View status column                          |
| **Delete environment**          | Infrastructure > \[Environment] > Infrastructure Scripts > ⋮ > Delete | ⚠️ Permanent deletion                       |
| **Configure App Registration**  | Platform Settings > Deployment Agent                                  | Enter Client ID and Secret                  |
| **Access new environment**      | Browser to http://\[Public-IP]                                        | Get IP from Azure Portal                    |

#### Deployment Checklist

Before deploying QA or Production:

```
[ ] Development environment operational
[ ] App Registration created and configured
[ ] Decided: Shared or Dedicated SQL Server
[ ] Resource group name chosen
[ ] VM and SQL passwords prepared (stored securely)
[ ] Tested workflow with BLOB Storage script
[ ] Verified permissions and Azure access
[ ] Time allocated (45-60 minutes for deployment + 30 minutes for configuration)
```

After deployment completes:

```
[ ] Status shows "Deployed" in Toolkit
[ ] All resources visible in Azure Portal
[ ] VM is running
[ ] Can access environment via IP address
[ ] Logged in with default credentials
[ ] Changed default password
[ ] Enabled environment in Azure Infrastructure
[ ] Configured App Registration in Deployment Agent
[ ] Deployed test project successfully
[ ] Verified project works in new environment
```

#### Status Values Reference

| Status       | Meaning                           | What to Do                                      |
| ------------ | --------------------------------- | ----------------------------------------------- |
| **New**      | Script added but not deployed     | Click Deploy when ready                         |
| **Busy**     | Deployment in progress            | Wait 45-60 minutes, monitor in Azure Portal     |
| **Deployed** | Deployment completed successfully | Verify resources, configure, enable environment |
| **Success**  | Alternative success indicator     | Same as Deployed                                |
| **Failed**   | Deployment failed                 | Check Azure logs, troubleshoot, retry           |

#### Azure Resources Reference

Resources created by full environment deployment:

| Resource Type          | Dedicated SQL | Shared SQL | Purpose                         |
| ---------------------- | ------------- | ---------- | ------------------------------- |
| Resource Group         | 1             | 1          | Container for all resources     |
| Virtual Machine        | 1             | 1          | Hosts platform components       |
| SQL Server             | 1             | 0          | Database server (or uses Dev's) |
| SQL Databases          | Multiple      | Multiple   | Platform and project databases  |
| Storage Account        | 1             | 1          | File and media storage          |
| Virtual Network        | 1             | 1          | Network infrastructure          |
| Network Security Group | 1             | 1          | Firewall rules                  |
| Network Interface      | 1             | 1          | VM network connection           |
| Public IP Address      | 1             | 1          | External access endpoint        |
| Managed Disk           | 1             | 1          | VM OS storage                   |
| Application Insights   | 1             | 1          | Monitoring (if configured)      |

#### Estimated Timeline Reference

| Activity                          | Duration      | Notes                                    |
| --------------------------------- | ------------- | ---------------------------------------- |
| **BLOB Storage deployment**       | 5-10 minutes  | Good for testing workflow                |
| **Full environment deployment**   | 45-60 minutes | ARM template + platform installation     |
| **Post-deployment configuration** | 30-60 minutes | App Registration, settings, verification |
| **First project deployment**      | 10-20 minutes | After environment ready                  |
| **Environment deletion**          | 5-15 minutes  | Permanent removal of all resources       |
| **VM start/stop**                 | 2-5 minutes   | Manual operation in Azure Portal         |

#### Default Credentials Reference

**New Environment Access:**

* URL: `http://[Public-IP-Address]`
* Username: `admin@comunityplatform.com`
* Password: `admin`

**⚠️ Change immediately after first login!**
