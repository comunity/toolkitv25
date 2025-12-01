---
hidden: true
---

# Azure Marketplace Self-Service Deployment Guide

The ComUnity Developer Toolkit is available as a marketplace offer on Azure Marketplace. This guide walks through the deployment process from marketplace purchase to accessing your deployed toolkit.

#### What This Guide Covers

This guide walks you through deploying the Community Developer Toolkit from Azure Marketplace to a fully functional instance you can access and use.

**Deployment Method:** Azure Marketplace managed application\
**Target Users:** Azure administrators, technical users with Azure experience\
**Estimated Time:** 60-90 minutes (45-60 minutes automated deployment + setup time)

#### What Gets Deployed

Your deployment will create a complete Community Platform Toolkit environment including:

| Resource Type              | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| Virtual Machine            | Hosts the toolkit application                |
| SQL Database Server        | Database engine                              |
| SQL Databases              | Platform data storage                        |
| Container Apps Environment | Container orchestration                      |
| Application Insights       | Monitoring and diagnostics                   |
| Storage Accounts           | File and data storage                        |
| Networking Components      | Virtual network, public IP, network security |

**\[DRAFT: Complete resource list with specific SKUs pending]**

#### Deployment Timeline

Based on observed deployments:

* **Infrastructure provisioning:** 10-15 minutes
* **Toolkit installation scripts:** 30-45 minutes
* **Total deployment time:** 45-60 minutes

**Note:** Times may vary based on Azure region and current load.

#### Important Considerations

* &#x20;**Costs:** Azure resources incur charges. Review pricing before deployment.
* **Permissions:** You need Contributor or Owner role on the subscription.
* **Cool-off Period:** Available for test deployments - delete within specified period to avoid charges.
* **Preview Status:** This offering is currently in preview. Some features are being refined.

<mark style="color:red;">\[DRAFT: Exact cool-off period duration needs confirmation]</mark>

### Prerequisites

#### Required Access & Permissions

Before starting, ensure you have:

✅ **Azure Subscription**

* Active Azure subscription
* Contributor or Owner role on the subscription
* **\[DRAFT: Specific role requirements need verification]**

✅ **Access Credentials**

* Azure Portal access
* Logged in with the correct account
* Access to the subscription where you'll deploy

✅ **Planning Information**

* Chosen Azure region for deployment
* Resource group naming convention decided
* Password management solution ready (you'll create passwords during setup)

#### Technical Requirements

✅ **Network Access**

* Ability to access Azure Portal (https://portal.azure.com)
* Browser: Modern browser (Chrome, Edge, Firefox, Safari)
* No VPN restrictions blocking Azure resources

✅ **Time Allocation**

* 90 minutes for deployment and initial setup
* Availability to monitor deployment process

#### Optional But Recommended

* Azure CLI or PowerShell knowledge (for troubleshooting)
* SQL Server management experience (for database administration)
* Remote Desktop Protocol (RDP) client (for VM access if needed)

### Deployment Process

#### Step 1: Access the Azure Marketplace Offer

<mark style="color:red;">\[DRAFT: This section needs screenshots and exact URL]</mark>

**Option A: Direct Marketplace Link**

<mark style="color:red;">\[DRAFT: Exact marketplace URL pending]</mark>

1. Navigate to the Community Platform marketplace offer
2. You will see the offer page with plan options

**Option B: Via Azure Portal**

1. Log into Azure Portal: https://portal.azure.com
2. Click on "Create a resource" or navigate to Marketplace
3. Search for "Community Platform" or "City as a Platform"
4. Select the Community Platform offer from results

<mark style="color:red;">\[DRAFT: Need screenshots of marketplace search and offer listing]</mark>

#### Step 2: Review Offer Details

Before deployment, review:

* **Offer Description:** Overview of what gets deployed
* **Available Plans:** Different tiers (e.g., Innovator Plan)
* **Pricing Information:** Estimated costs
* **Support Options:** Available support channels

<mark style="color:red;">\[DRAFT: Plan comparison details pending]</mark>

#### Step 3: Select Your Plan

1. Review available plans (e.g., "Innovator Plan")
2. Select the plan that matches your needs
3. Click "Get it now" or "Create"

You will be redirected to the Azure Portal configuration page.

<mark style="color:red;">\[DRAFT: Need screenshots of plan selection]</mark>

#### Step 4: Configure Deployment Settings

You will be presented with a configuration form. Complete all required fields:

<mark style="color:red;">\[DRAFT: Current form is being updated. Screenshots show preliminary version]</mark>

**Subscription & Resource Group**

**Subscription:**

* Select the Azure subscription for this deployment
* Ensure you have appropriate permissions

**Resource Group:**

* **Create new** (recommended): Enter a unique name
  * Example: `communityplatform-prod-rg`
  * Use clear naming for easy identification
* **Use existing:** Select from dropdown (ensure it's empty or appropriate)

**Region/Location:**

* Select the Azure region for deployment
* Example: "South Africa North", "East US", "West Europe"
* Choose a region close to your users for best performance
* <mark style="color:red;">\[DRAFT: Region availability and restrictions need confirmation]</mark>

**Application Configuration**

**Application Name:**

* Enter a unique name for your deployment
* This may be used in resource naming
* **\[DRAFT: Naming constraints and usage need clarification]**

**Virtual Machine Password:**

* Create a strong password for VM administrator access
* **Required Format:**
  * Minimum 12 characters
  * Must include uppercase letters
  * Must include lowercase letters
  * Must include numbers
  * Must include special characters

⚠️ **IMPORTANT:**

* Save this password securely (password manager recommended)
* You'll need it for VM remote access
* Cannot be retrieved after deployment
* <mark style="color:red;">\[DRAFT: Password reset procedure needs documentation]</mark>

**Virtual Machine Username:**

* Default: `azureuser`
* <mark style="color:red;">\[DRAFT: Currently fixed - customisation pending investigation]</mark>
* This username has necessary permissions for deployment scripts

**Database Configuration**

<mark style="color:red;">\[DRAFT: SQL Server settings are currently auto-generated]</mark>

Currently, the following are automatically generated:

* SQL Server administrator username
* SQL Server administrator password

⚠️ **Known Limitation:** Auto-generated SQL credentials are not currently displayed to users after deployment. This is being addressed.

<mark style="color:red;">\[DRAFT: Future versions will allow custom SQL credentials]</mark>

**Toolkit Administrator Account**

**\[DRAFT: Currently using default credentials]**

Default toolkit login credentials:

* **Username:** admin@communityplatform.com
* **Password:** admin

⚠️ **Security Note:** Change these credentials immediately after first login.

<mark style="color:red;">\[DRAFT: Future versions will allow custom toolkit admin credentials during deployment]</mark>

#### Step 5: Review Configuration

<mark style="color:red;">\[DRAFT: Need screenshot of review page]</mark>

1. Review all settings you've entered
2. Verify subscription and region are correct
3. Confirm resource group name
4. Double-check password complexity

#### Step 6: Accept Terms & Create

1. Read and accept the Terms and Conditions
2. Review pricing information
3. Click **Create** to begin deployment

**What happens next:**

* Azure validates your configuration
* ARM template deployment begins
* You'll be redirected to deployment status page

<mark style="color:red;">\[DRAFT: Need screenshot of terms acceptance and create button]</mark>

### Monitoring Deployment

#### Understanding Resource Organisation

The deployment creates a specific structure:

```
 Marketplace Offering Resource Group (You created this)
  └──  Managed Application
      └──  Managed Resource Group (Auto-created)
          └──  Virtual Machine
          └──  SQL Server & Databases
          └──  Container Apps Environment
          └──  Application Insights
          └──  Networking Components
          └──  Storage Accounts
```

**Why this structure?**

* The marketplace creates a "managed application" wrapper
* Actual resources live in a separate "managed resource group"
* This allows for better resource lifecycle management

#### Accessing Deployment Status

**Initial Deployment Screen**

After clicking Create, you'll see:

<mark style="color:red;">\[DRAFT: Need screenshot of initial deployment screen]</mark>

* Deployment name
* Resource group
* Status: "Deployment in progress" or similar
* Estimated completion time (if shown)

**Detailed Progress View**

To see detailed deployment progress:

1. **Navigate to Resource Groups:**
   * In Azure Portal, click "Resource groups" in left menu
   * Or search for "Resource groups" in top search bar
2. **Locate Your Marketplace Resource Group:**
   * Find the resource group you created (e.g., `communityplatform-prod-rg`)
   * Click on the resource group name

<mark style="color:red;">\[DRAFT: Need screenshot of resource group list]</mark>

3. **Access the Managed Application:**
   * Inside your resource group, you'll see a "Managed Application"
   * Name: Usually matches your application name (e.g., "test-marketplace-offering")
   * Type: "Microsoft.Solutions/applications"
   * Click on this managed application

**\[DRAFT: Need screenshot showing managed application in resource group]**

4. **View Managed Resource Group:**
   * In the managed application Overview page
   * Look for "Managed resource group" field
   * Click the link to the managed resource group

**\[DRAFT: Need screenshot of managed application overview highlighting managed resource group link]**

5. **Check Deployment Details:**
   * In the managed resource group, look in the left sidebar
   * Under **Settings** section
   * Click **Deployments**

<mark style="color:red;">\[DRAFT: Need screenshot of Settings → Deployments navigation]</mark>

#### Interpreting Deployment Status

In the Deployments view, you'll see:

<mark style="color:red;">\[DRAFT: Need screenshot of deployment progress]</mark>

**Phase 1: Infrastructure Resources**

Green checkmarks (✅) indicate completed resources:

* Storage accounts
* Virtual network
* Network security groups
* Public IP address
* Virtual machine (created, but not configured yet)
* SQL Server
* SQL Databases
* Container apps environment
* Application Insights

**Typical duration:** 10-15 minutes

**Phase 2: Custom Script Extension (Toolkit Installation)**

The final and longest step:

* **Resource:** Custom Script Extension
* **Status during execution:** "Created" or "Running"
* **Status when complete:** "Succeeded" with green checkmark ✅

**What's happening:**

* VM is running installation scripts
* Toolkit software is being installed
* Configurations are being applied
* Services are being started

**Typical duration:** 30-45 minutes

<mark style="color:red;">\[DRAFT: Need screenshot of custom script extension in progress and completed]</mark>

#### Monitoring Tips

✅ **You can safely close the browser** - Deployment continues in background\
✅ **Refresh the page** - Click refresh to update status\
✅ **Check timestamps** - Each operation shows start time\
✅ **Review operation details** - Click on any operation for more info

**\[DRAFT: Screenshots of operation details needed]**

#### What to Do While Waiting

During the 45-60 minute deployment:

* ✅ Prepare your password management documentation
* ✅ Review toolkit documentation
* ✅ Plan your initial toolkit configuration
* ✅ Notify team members about upcoming access
* ❌ Don't close Azure Portal session entirely (keep tab open)
* ❌ Don't attempt to modify resources during deployment

### Accessing Your Toolkit

#### Step 1: Confirm Deployment Success

Before attempting access:

1. Navigate to the **Managed Resource Group → Settings → Deployments**
2. Verify the main deployment shows **"Succeeded"** with green checkmark
3. Specifically check that **Custom Script Extension** shows **"Succeeded"**

<mark style="color:red;">\[DRAFT: Need screenshot of completed deployment with all green checkmarks]</mark>

#### Step 2: Locate Your VM Public IP Address

**Method A: Via Virtual Machine Resource**

1. In the Managed Resource Group, click **Overview**
2. You'll see a list of all created resources
3. Click on **Type** column header to sort resources by type
4. Locate the **Virtual Machine** resource
5. Click on the Virtual Machine name

**\[DRAFT: Need screenshot of resource list with VM highlighted]**

6. In the VM Overview page, find **"Public IP address"**
7. The IP address will be displayed (e.g., `42.212.32.44`)

**\[DRAFT: Need screenshot of VM overview highlighting public IP address]**

**Method B: Via Public IP Resource**

1. In the Managed Resource Group resource list
2. Find resource of type **"Public IP address"**
3. Click on the public IP resource
4. The IP address is shown in the overview

**Copy this IP address** - You'll need it to access the toolkit.

#### Step 3: Access Toolkit Login Page

1. Open a new browser tab
2. Paste the public IP address in the address bar
3. Press Enter

**Expected Result:** The Community Platform Toolkit login page loads

**\[DRAFT: Need screenshot of toolkit login page]**

⚠️ **If the page doesn't load:**

* Verify deployment is completely finished (all resources show "Succeeded")
* Wait 2-3 minutes for services to fully start
* Check your network allows access to the IP address

#### Step 4: Log Into the Toolkit

Use the default credentials:

**Username:** `admin@communityplatform.com`\
**Password:** `admin` (lowercase)

**\[DRAFT: Screenshot of successful login and dashboard needed]**

#### Step 5: Change Default Password

🔒 **CRITICAL SECURITY STEP:**

Immediately after first login:

1. Navigate to user settings or admin panel
2. Change the default password
3. Update the admin email address if desired

<mark style="color:red;">\[DRAFT: Exact steps for changing password need documentation]</mark>

### Post-Deployment Setup

#### Credential Reference

After deployment, you have multiple sets of credentials:

| System                    | Username                    | Password                    | Purpose                             |
| ------------------------- | --------------------------- | --------------------------- | ----------------------------------- |
| **Virtual Machine (RDP)** | azureuser                   | \[You created during setup] | Remote access to VM for maintenance |
| **Toolkit Web Interface** | admin@communityplatform.com | admin (change immediately!) | Toolkit administration              |
| **SQL Server**            | \[Auto-generated]           | \[Auto-generated]           | Database administration             |

⚠️ **SQL Credential Gap:**

* SQL credentials are currently auto-generated during deployment
* **\[DRAFT: Method to retrieve SQL credentials pending - being implemented]**
* **Workaround:** Contact support if you need SQL access before this is resolved

#### Viewing Deployment Parameters

Some deployment information can be viewed:

1. Navigate to your **Marketplace Offering Resource Group**
2. Click on the **Managed Application**
3. In left sidebar under **Settings**, click **"Parameters and outputs"**

This shows some configuration values used during deployment.

**\[DRAFT: Screenshot of parameters and outputs page needed]**

**Limitations:**

* Passwords are not displayed (security measure)
* <mark style="color:red;">\[DRAFT: Output section to be enhanced with additional useful information]</mark>

#### When You Need VM Access

VM credentials are needed for:

**Administrative Tasks:**

* Installing additional software on the VM
* Reviewing VM-level logs
* Troubleshooting deployment issues
* Configuring Windows settings
* Advanced maintenance

**How to Access VM:**

1. Use Remote Desktop Protocol (RDP)
2. Connect to the public IP address
3. Username: `azureuser`
4. Password: \[The password you created during setup]

⚠️ **Normal Operations:** Most toolkit users never need VM access. This is for administrators only.

#### When You Need SQL Server Access

SQL Server credentials are needed for:

**Database Management:**

* Direct database queries
* Creating additional databases
* Backup and restore operations
* Performance tuning
* Connecting external tools (SQL Server Management Studio, Azure Data Studio)

**\[DRAFT: SQL credential retrieval process needs documentation]**

#### Initial Toolkit Configuration

After logging in, recommended first steps:

<mark style="color:red;">\[DRAFT: This section needs expansion with specific toolkit setup steps]</mark>

1. ✅ Change default admin password
2. ✅ Update admin email address
3. ✅ Review and configure toolkit settings
4. ✅ Create additional user accounts
5. ✅ Configure your first project

<mark style="color:red;">\[DRAFT: Links to toolkit user guide needed]</mark>

### Resource Management

#### Monitoring Your Resources

**In Azure Portal**

View your deployed resources:

1. Navigate to the **Managed Resource Group**
2. Click **Overview**
3. Review all resources and their status

**Health Indicators:**

* All resources should show as "Running" or active
* No error states visible
* VM should be "Running"

**\[DRAFT: Screenshot of healthy resource group needed]**

**Cost Monitoring**

Track your Azure costs:

1. In Azure Portal, navigate to **Cost Management + Billing**
2. View costs by resource group
3. Set up cost alerts (recommended)

**\[DRAFT: Typical monthly cost estimates needed]**

#### Scaling Resources

**\[DRAFT: Scaling procedures need documentation]**

Common scaling scenarios:

* Increasing VM size for better performance
* Scaling SQL Database tier
* Adjusting storage capacity

#### Backup and Disaster Recovery

**\[DRAFT: Backup strategy needs documentation]**

Recommended practices:

* Enable Azure Backup for VM
* Configure SQL Database automated backups
* Document recovery procedures

#### Deleting Your Deployment

⚠️ **WARNING:** This permanently deletes all data and cannot be undone.

**When to Delete**

* Completing a test deployment
* Decommissioning the platform
* Moving to a different deployment

**How to Delete**

**Method 1: Delete Marketplace Resource Group (Recommended)**

1. Navigate to **Resource Groups**
2. Find your marketplace offering resource group
3. Click **Delete resource group**
4. Type the resource group name to confirm
5. Click **Delete**

**\[DRAFT: Need screenshot of deletion confirmation dialog]**

**Expected Behaviour:**

* Deletes the marketplace offering resource group
* **\[DRAFT: NEEDS VERIFICATION]** Should automatically delete:
  * The managed application
  * The managed resource group
  * All platform resources within

<mark style="color:red;">\[DRAFT: Deletion cascade behaviour needs confirmation - does it delete managed resource group automatically or must it be deleted separately?]</mark>

**Verifying Complete Deletion**

After deletion:

1. Check that marketplace offering resource group is gone
2. Verify managed resource group is also deleted
3. **\[DRAFT: Expected deletion time needs documentation]**
4. Review Cost Management to confirm no ongoing charges

<mark style="color:red;">\[DRAFT: Detailed verification steps needed]</mark>

**If Resources Remain**

<mark style="color:red;">\[DRAFT: Cleanup procedures if automatic deletion fails]</mark>

If the managed resource group is not automatically deleted:

1. Manually navigate to the managed resource group
2. Delete it separately
3. Verify all resources are removed

### Troubleshooting

<mark style="color:red;">\[DRAFT: This entire section needs expansion with real examples from testing]</mark>

#### Deployment Issues

**Deployment Fails with Password Error**

**Symptoms:**

* Deployment fails during validation
* Error message about password requirements

**Solution:**

1. Ensure password meets all requirements:
   * Minimum 12 characters
   * Uppercase letters
   * Lowercase letters
   * Numbers
   * Special characters
2. Delete the failed deployment
3. Start a new deployment with compliant password

<mark style="color:red;">\[DRAFT: Screenshot of password validation error needed]</mark>

**Custom Script Extension Fails**

**Symptoms:**

* Infrastructure deploys successfully
* Custom script extension shows error or never completes

**\[DRAFT: Common causes and solutions need documentation]**

**Diagnostic Steps:**

1. Check deployment logs in Azure Portal
2. **\[DRAFT: How to access VM logs for script errors]**
3. Contact support with deployment ID

**Deployment Takes Longer Than Expected**

**What's Normal:**

* 45-60 minutes total deployment time
* Custom script extension: 30-45 minutes
* Some variance based on Azure region

**When to Worry:**

* Deployment exceeds 90 minutes
* No status updates for 30+ minutes
* Error messages appear

**\[DRAFT: How to check if deployment is stuck vs. just slow]**
