---
hidden: true
---

# Infrastructure Management

The Infrastructure Management feature allows administrators to deploy and manage Azure environments for their Toolkit projects through pre-configured deployment scripts. This integration automates infrastructure provisioning, eliminating the need for manual Azure resource management.

{% hint style="info" %}
Current documentation is based on current implementation as of v25.3. Interface and functionality subject to change in future releases.
{% endhint %}

### Key Features

* **Automated Deployment Scripts**: Deploy Azure environments through pre-configured scripts that handle resource provisioning automatically. The Toolkit manages the deployment process in the background, allowing you to continue working on other tasks whilst infrastructure is being created.
* **Environment-Specific Management**: Manage separate Development, QA, and Production environments. QA and Production environments can be enabled or disabled to control their availability within the Toolkit.
* **Deployment Monitoring**: Track deployment progress through status indicators that update as infrastructure scripts execute. The system displays the current status of each deployment, such as "Busy" during execution and "Deployed" upon completion.
* **Role-Based Access Control**: Access to infrastructure management features is controlled through role-based access (RBA). Only users with the required permissions can create, manage, or deploy infrastructure scripts.

> **Note**: Infrastructure scripts require activation in each environment to match the specific deployment contexts of your project, similar to other primary features in the Toolkit.

### Accessing Infrastructure Management

Infrastructure management features are available to users with appropriate administrator permissions.

1. **Log In**: Access the Toolkit by entering your credentials.
2. **Open Your Project**: Locate and select your project within the Toolkit.
3. **Navigate to Infrastructure**: From the main menu, find and click on "Infrastructure". You will be presented with the infrastructure management interface.

> **Important Design Note**: The current infrastructure management interface will change in future releases. The screens are not according to the final design specifications, as these designs became available after the development cycle had begun. The layout will be significantly different, but the core functionality for managing infrastructure scripts will remain similar.

### Understanding Infrastructure Scripts

Infrastructure scripts are available within the Infrastructure section when you access a specific environment.

#### Available Script Types

When you navigate to Infrastructure and select an environment (such as QA), you will see infrastructure scripts. Three types of scripts are currently available:

1. **Environment with Dedicated SQL Server**: Creates a complete Azure environment with dedicated SQL Server resources. This script provisions a full environment and should not be run in existing QA or Production environments.
2. **Environment with Shared SQL Server**: Creates a complete Azure environment configured with shared SQL Server resources. Like the dedicated option, this script is for new environment provisioning only.
3. **QA Environment BLOB Storage Container**: Creates a resource group with a storage account. This is a simpler script suitable for testing the infrastructure deployment workflow.

> **Critical Warning**: The dedicated and shared SQL Server scripts spin up and take down complete environments. These scripts must not be run in the current Toolkit Next or Production environments, as those environments are already in place and must not be removed.

#### Script Execution Time

The BLOB Storage Container script completes relatively quickly. The full environment scripts (with SQL Server) take approximately 45 minutes to complete. During execution, these scripts create multiple items in Azure within the resource group and install platform components.

#### Future Script Categories

Future development will introduce custom scripts functionality, allowing users to define their own scripts to spin up Azure resources. The interface will categorise scripts differently:

* **Environment Scripts**: System-provided scripts for QA and Production environments (like the current scripts)
* **Custom Scripts**: User-defined scripts for spinning up custom Azure resources

The categorisation and layout of these screens will change with future releases.

### Viewing Infrastructure Scripts

To view available infrastructure scripts:

1. Navigate to **Infrastructure** from the main menu.
2. Select the environment you want to view (such as QA Environment).
3. Click on the infrastructure scripts section. You will see instructions for setting up and managing infrastructure scripts in your project environment.
4. If any infrastructure scripts already exist in the environment, you will see them listed on this screen. For each script, the display shows the script's name, its URL, and its current status.

Each listed script displays essential details including name, associated URL, and current status (such as "Active").

### Testing Infrastructure Deployment

The QA Environment BLOB Storage Container script provides a way to test the infrastructure deployment workflow without affecting existing environments.

#### Deploying the Test Script

1. Navigate to **Infrastructure** > **QA Environment** > **Infrastructure Scripts**.
2. Click **"Create a function app"** (or similar button to add a script).
3. In the configuration interface, provide the required parameters:
   * **Resource Group Name**: Enter a name for the resource group
4. Click the button to add the script.
5. The script appears in the infrastructure scripts list.
6. Click **Deploy** next to your newly added script.
7. The deployment begins and runs in the background. The status shows as "Busy" whilst the script executes.

#### Monitoring Progress

Once deployment begins:

* The status indicator updates automatically as the deployment progresses
* You can navigate away from the screen and work on other items in the Toolkit
* Return to the infrastructure scripts screen to check progress
* When deployment completes, the status updates to show "Deployed" or indicates success

> **Known Issue**: There is currently an alignment issue with the status display that will be addressed. The functionality works correctly, but the visual alignment of status information needs adjustment.

#### Verifying in Azure

When the script completes, it creates a resource group in Azure with the name you specified. The resource group contains a storage account. You can verify these resources exist by checking your Azure subscription.

### Deploying Full Environment Scripts

Full environment scripts create complete Azure infrastructure including multiple resources and platform installation.

> **Critical Warning**: Do not run the full environment scripts (Environment with Dedicated SQL Server or Environment with Shared SQL Server) in existing QA or Production environments. These scripts will attempt to create new environments and should only be used when provisioning fresh infrastructure.

#### When to Deploy Full Environments

Full environment scripts are intended for:

* Creating new environments in fresh Azure subscriptions
* Setting up isolated testing environments
* Initial environment provisioning under administrator guidance

#### Deployment Process

The deployment process follows the same steps as the BLOB Storage test:

1. Navigate to the appropriate environment
2. Select the infrastructure script
3. Add the script with required parameters
4. Review the configuration
5. Deploy the script
6. Monitor status through the interface

Full environment deployments take approximately 45 minutes to complete and create multiple items in the Azure resource group, including platform installation.

### Managing Deployment Scripts

After adding a script to your environment, management options are available through the interface.

#### Viewing Script Details

To view details about a deployed script:

1. Navigate to the infrastructure scripts list in your chosen environment
2. Click **View Details** to expand information about the selected script

The expanded view displays additional information about the script.

#### Editing Script Details

To modify a script:

1. Locate the script in the infrastructure scripts list
2. Click the **three-dot button (⋮)** next to the script
3. Select **View Details** from the dropdown menu to expand the script details
4. Choose **Edit Function App Details** to modify the script configuration

#### Deleting Deployment Scripts

The delete function removes a deployment script from the Toolkit.

> **Critical Warning**: When you delete a script, it deletes the actual Azure resources that were created by that deployment. This deletion is permanent and cannot be undone. At present, nothing backs up your environment before deletion, so everything is lost.

To delete a deployment script:

1. Click the **three-dot button (⋮)** next to the script name
2. Select **Delete** from the menu
3. The system displays a warning about deleting the resources
4. If you choose to continue with the deletion, the process begins

The deletion runs in the background. Once complete, the script is removed from the list, and the Azure resources (including the resource group) are deleted.

> **Planned Enhancement**: The delete warning will be expanded to display everything in Azure that will be deleted as part of the deletion process.

> **Future Changes**: The delete function behaviour will change in future releases. For environment scripts, delete functionality may be disabled or restricted. Custom scripts will retain the delete capability, allowing users to remove their own Azure resources.

### Environment Management

The Infrastructure Management section includes environment availability controls.

#### Accessing Environment Settings

Navigate to **Infrastructure** > **Azure Infrastructure** to access environment management.

The environment management interface displays:

* **Development Environment**: Cannot be disabled
* **QA Environment**: Can be enabled or disabled
* **Production Environment**: Can be enabled or disabled

#### Current Enable/Disable Behaviour

When you enable or disable an environment and save the changes:

* The change updates the environment record in the Toolkit
* **Disabling an environment**: Makes the environment not available in the deployment screens. When users attempt to deploy and the environment is deactivated, the system informs them that the environment is not active.
* **Current Limitation**: The enable/disable function only updates the record. It does not currently delete or modify anything in Azure. The Azure infrastructure remains unchanged.

#### Intended Future Behaviour

The enable/disable buttons are designed for future functionality:

* **When you disable an environment**: The system should shut down and back up the environment
* **When you enable an environment**: The system should restore the environment

This functionality is not yet implemented. Currently, the buttons only control whether the environment appears as available within the Toolkit.

#### Modifying Environment Status

To enable or disable an environment:

1. Navigate to **Infrastructure** > **Azure Infrastructure**
2. Locate the environment you want to modify (QA or Production)
3. Change the enable/disable setting
4. Save the changes

The environment availability updates within the Toolkit immediately.

### Additional Context

#### Automated Testing Environment

An automated testing environment is available for testing infrastructure deployment scripts. This environment is not always available—it is only accessible during specific testing periods. If you need to test full environment deployment scripts (rather than the BLOB Storage test script), arrangements can be made to use this automated environment during testing windows.

#### Screen Workflow Consistency

The BLOB Storage Container deployment demonstrates the exact workflow used for all infrastructure scripts. The screens and process flow are identical for full environment deployments; the only differences are:

* Deployment time (45 minutes vs. shorter time for BLOB Storage)
* Number of Azure resources created
* Platform installation with full environment scripts

Testing with the BLOB Storage script provides complete understanding of how the full deployment process works.

### Related Documentation

* For additional information on working with the Toolkit, refer to other relevant documentation sections.
* For Azure-specific resource management and best practices, refer to the official Azure documentation.

