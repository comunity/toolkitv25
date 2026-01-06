# Tags

The Tags feature in the ComUnity Developer Toolkit provides a powerful organisational system for categorising and managing Azure resources within your platform. This system enables administrators to create custom classification schemes that align with their organisational needs, from cost allocation and environment tracking to ownership and infrastructure management.

Tags offer a flexible framework for organising resources through a three-tier structure: Categories contain Tags, which are assigned Values on individual resources. This hierarchical approach allows teams to establish governance standards while maintaining the flexibility to adapt to diverse operational requirements.

## Understanding the Tag Structure

The tagging system operates through three distinct levels, each serving a specific purpose in the organisational hierarchy.

**Tag Categories** serve as logical groupings that organise related tags together. For example, an Infrastructure category might contain tags related to technical operations, while a FinOps category groups tags used for financial tracking and cost allocation. Categories provide both organisational structure within the settings interface and role-based access control, ensuring users only see and work with tags relevant to their responsibilities.

**Tag Names** represent the actual classification dimensions you want to track. Common examples include environment, stack, project, owner, business-unit, and cost-centre. Each tag name can be marked as either Required or Optional, allowing administrators to enforce governance policies by ensuring critical tags are always assigned to resources.

**Tag Values** are the specific classifications applied to individual resources. For instance, an environment tag might have values like dev, test, or prod, while a stack tag could have values like observability, platform, or security. These values drive the dynamic grouping capabilities in the Infrastructure Catalogue.

<figure><img src="../../.gitbook/assets/image (516).png" alt=""><figcaption><p>Tag hierarchy showing Categories (Infrastructure, FinOps) containing Tag Names (environment, stack, owner) with Required/Optional indicators</p></figcaption></figure>

## Managing Tag Categories

Tag categories form the foundation of your tagging system, providing both organisational structure and security boundaries. This section covers how categories use role-based access control to ensure appropriate access, and guides you through creating categories and adding tags to them.

### Role-Based Access Control for Categories

Tag categories implement role-based access control to ensure users only interact with tags appropriate to their organisational responsibilities. When creating a category, administrators assign it to a specific role, which determines who can view and use the tags within that category.

**The available roles include:**

* **None** - Accessible to all users
* **Azure Developer** - Restricted to Azure Developer role
* **Developer** - Restricted to Developer role
* **Lead Developer** - Restricted to Lead Developer role
* **Operations** - Restricted to Operations role
* **Organisation administrator** - Restricted to Organisation administrator role
* **Viewer** - Restricted to Viewer role

Users assigned to a particular role can only see categories and their associated tags if the category has been configured for their role. This creates natural boundaries between different areas of responsibility within the organisation.

The Organisation administrator role typically has access to all categories regardless of their role assignment, enabling comprehensive oversight and management of the tagging system. The None option creates categories that are accessible to all users, useful for universal classification schemes that should be available organisation-wide.

### Create a Tag Category

**Prerequisites:**

* Organisation administrator access
* Access to Organisation Settings

**Steps:**

1. Navigate to **Organisation Settings** in the ComUnity Toolkit
2. Select **Tags** from the left navigation menu
3. Click **"Create a new category"** at the bottom of the categories list
4. In the "Create a new category" dialog:
   * Enter a **Category name** (e.g., "Infrastructure", "FinOps", "Security")
   * Select the appropriate **Role** from the dropdown to control who can access this category:
     * Choose **None** if all users should see this category
     * Choose a specific role (e.g., Developer, Operations) to restrict access
5. Click **Create**

**Result:** The new category appears in the categories list. You can now add tags to this category.

**Tips:**

* Use descriptive category names that clearly indicate their purpose
* Consider your organisation's role structure when assigning category access
* Finance-related tags should typically use specific roles to control access to cost data
* General operational tags can use "None" for broad accessibility

### Assign Tags to a Category

**Prerequisites:**

* A tag category must already exist
* Organisation administrator access

**Steps:**

1. Navigate to **Organisation Settings > Tags**
2. Locate the category you want to add tags to
3. Click **"View category"** or the dropdown arrow to expand the category
4. Click **"Add Tag name"** within the expanded category
5. In the "Create a new Tag" dialog:
   * Enter a **Tag name** (e.g., "environment", "stack", "owner")
   * (Optional) Enter a **Description** to provide context for users
   * Check the **Required** checkbox if this tag must be assigned to all resources
6. Click **Create**

**Result:** The tag appears in the category with an indicator showing whether it's Required or Optional. The tag is now available for users with appropriate role access to assign to resources.

**Tips:**

* Use lowercase, hyphenated names for consistency (e.g., "cost-centre", not "Cost Centre")
* Mark tags as Required only when enforcement is truly necessary
* The Description field helps users understand what values are appropriate

## Configuring Pre-defined Tag Values

Pre-defined options allow administrators to specify a set of standardised values for a tag. When users assign this tag to resources, they can select from these pre-defined values through a dropdown menu, ensuring consistency across the organisation and reducing data entry errors.

Pre-defined options are particularly useful for tags where you want to enforce a controlled vocabulary, such as environment names (dev, test, staging, prod), regions, or cost centres. Instead of allowing free-form text entry, users select from administrator-defined values.

**Prerequisites:**

* Organisation administrator access
* An existing tag (or you can add pre-defined options when creating a new tag)

### Assign Pre-defined Options to a Tag

**Steps:**

1. Navigate to **Organisation Settings > Tags**
2. Expand the category containing the tag you want to configure
3. Click on the tag name to open the **"Editing a tag"** dialog
4. Locate the **"Pre-defined options"** field below the Required checkbox
5. Enter a value in the Pre-defined options text field (e.g., "dev")
6. Click the **"Add"** button to add the value to the pre-defined list
7. Repeat steps 5-6 for each value you want to add (e.g., "prod", "qa", "staging")
8. Click **Save** to apply the changes

**Result:** The pre-defined values appear as removable tags below the input field (e.g., "dev ×", "prod ×", "qa ×"). When users assign this tag to resources, they will see these values in a dropdown menu for easy selection.

### Removing Pre-defined Options

To remove a pre-defined value from a tag:

1. Open the **"Editing a tag"** dialog for the tag
2. Locate the value you want to remove in the list of pre-defined options
3. Click the **×** (close) icon next to the value
4. Click **Save** to apply the changes

{% hint style="info" %}
Removing a pre-defined option does not affect resources that have already been assigned that value. Existing tag assignments remain intact. However, users will no longer be able to select the removed value when assigning tags to new resources.
{% endhint %}



### How Pre-defined Options Appear to Users

When a tag has pre-defined options configured, users assigning that tag to a resource will see a dropdown menu instead of a free-text input field. This provides several benefits:

* **Consistency:** All resources use the same standardised values
* **Speed:** Users can quickly select from available options without typing
* **Accuracy:** Eliminates typos and variations (e.g., "dev" vs "Dev" vs "development")
* **Discoverability:** Users can see all valid options at a glance

### Assign Tags to Resources

**Prerequisites:**

* Access to the **Infrastructure** > **Catalogue**
* Permission to view the tag category (based on your role)

**Steps:**

1. Navigate to **Infrastructure > Catalogue**
2. Locate the resource you want to tag in the resource list
3. Click **View properties** for that resource to view its current meta data information which may include preconfigured tags.
4.  Click the ellipsis button adjacent to **View Properties** and select the **Edit resources tag**:<br>

    <figure><img src="../../.gitbook/assets/image (520).png" alt=""><figcaption><p>Edit resource tags</p></figcaption></figure>
5.  A **Resource Properties** dialog will appear:<br>

    <figure><img src="../../.gitbook/assets/image (521).png" alt=""><figcaption><p>Resource Properties Dialog</p></figcaption></figure>
6. In the Resource Properties dialog:
   * Select a **Tag Category** from the dropdown (you'll only see categories assigned to your role)
   * Select a **Tag Name** from the dropdown (shows tags within the selected category)
   * The interface displays existing tag assignments and shows which tags need values
7. Enter a **Tag value** in the text field (e.g., "dev", "prod", "observability")
8. Click **Save**

**Result:** The tag is assigned to the resource and syncs to Azure. You can verify by expanding the resource details in the catalogue or checking the Azure Portal.

<figure><img src="../../.gitbook/assets/image (518).png" alt=""><figcaption><p>Resource Properties dialog showing Tag Category dropdown (Data selected), Tag Name field, and tag value input. Note the 'Project : No value assigned yet' indicator for required tags</p></figcaption></figure>

**Tips:**

* Use consistent tag values across resources (e.g., always "dev", not mixing "dev", "development", "Development")
* Required tags show a red indicator and "No value assigned yet" message
* You can assign multiple tags to a single resource by selecting different categories and tag names
* Previously assigned tags appear as removable badges (e.g., "environment : dev ⊗")

### How to Use Group By Tag

**Prerequisites:**

* At least one resource must have tag values assigned
* Access to the Infrastructure Catalogue

**Steps:**

1. Navigate to **Infrastructure > Catalogue**
2. Locate the **"Group By Tag"** dropdown above the resource table
3. Click the dropdown and select a tag name (e.g., "stack", "environment", "owner")
4. The resource list reorganizes into collapsible sections based on tag values

**Result:** Resources are grouped under section headers matching their tag values. You'll see:

* Gray section headers for each unique tag value (e.g., "observability", "platform")
* A yellow **"\~untagged\~"** section for resources without that tag assigned
* Resources nested under their respective tag value sections

<figure><img src="../../.gitbook/assets/image (519).png" alt=""><figcaption><p>Resources grouped by 'test-tag' showing three sections: 'group-A', 'group-B', and '~untagged~' (highlighted in yellow) for resources without the tag assigned</p></figcaption></figure>

**To change grouping:**

* Select a different tag from the "Group By Tag" dropdown
* The view updates immediately to show groupings for the new tag

**Tips:**

* Grouping by "environment" helps distinguish dev/test/prod resources
* Grouping by "stack" shows infrastructure organization
* The "\~untagged\~" section helps identify resources that need categorization
* Sections are collapsible - click to expand/collapse

### How to Filter Resources by Tags

**Prerequisites:**

* Resources must have tag values assigned
* Access to the Infrastructure Catalogue

**Steps:**

1. Navigate to **Infrastructure > Catalogue**
2. Locate the **"Tag"** filter dropdown in the toolbar (top of the page)
3. Click the **"Tag"** dropdown
4. Select a specific tag value to filter by (e.g., "dev", "observability")

**Result:** The resource list shows only resources with the selected tag value. Resources without that tag value are hidden from view.

**To clear the filter:**

* Select **"All Tags"** from the Tag dropdown
* The view returns to showing all resources

**Combining Filters and Grouping:**

* You can use the Tag filter and Group By Tag simultaneously
* Example: Filter by "environment:dev" then Group By "stack" to see how dev resources are organised by **stack**

### How to Verify Tags in Azure Portal

**Prerequisites:**

* Access to Azure Portal
* Tags assigned through ComUnity Toolkit

**Steps:**

1. Open the **Azure Portal** (portal.azure.com)
2. In the top search bar, type **"tags"** and press Enter
3. Select **"Tags"** from the search results
4. In the Azure Tags interface:
   * Search for a specific tag name (e.g., "environment")
   * Click on a tag value (e.g., "dev")
5. Azure displays all resources with that tag assignment

**Result:** You can verify that tags created in ComUnity Toolkit are properly synchronised to Azure and visible in Azure's native tag management interface.

**Tips:**

* Tags sync immediately when saved in ComUnity Toolkit
* Azure's tag interface shows the same tag names and values
* You can also view tags on individual resources in Azure Portal under the resource's "Tags" section

### Common Use Cases

Organisations implement tagging strategies for diverse operational needs, each taking advantage of the flexible three-tier structure and role-based access control to meet specific requirements.

#### Environment Management

**Scenario:** Distinguish resources across development, testing, and production environments

**Configuration:**

* Create a category: "Infrastructure" (Role: Developer or Operations)
* Add tag: "environment" (Required)
* Common values: "dev", "test", "staging", "prod"

**Benefits:**

* Prevents configuration errors by clearly identifying environment boundaries
* Enables environment-specific Azure policies and access controls
* Simplifies cleanup of development resources while protecting production
* Supports cost analysis by environment

#### Cost Allocation and Financial Management

**Scenario:** Track spending across business units, projects, and cost centres for chargeback reporting

**Configuration:**

* Create a category: "FinOps" (Role: Finance team role or Organisation administrator)
* Add tags:
  * "business-unit" (Required)
  * "cost-centre" (Required)
  * "project" (Optional)
* Common values: Specific to your organization (e.g., "sales", "engineering", "CC-12345", "Project-Phoenix")

**Benefits:**

* Generates accurate chargeback reports in Azure Cost Management
* Prevents unauthorised modifications to financial metadata through role restrictions
* Tracks budget consumption for specific initiatives
* Enables financial forecasting by business unit or project

#### Infrastructure Organisation

**Scenario:** Group related technical components and assign ownership

**Configuration:**

* Create a category: "Infrastructure" (Role: Operations)
* Add tags:
  * "stack" (Required)
  * "owner" (Required)
* Common values:
  * stack: "observability", "platform", "networking", "security"
  * owner: Team names or individual names

**Benefits:**

* Helps teams understand dependencies between resources
* Facilitates maintenance planning across related components
* Provides clear accountability and escalation paths
* Supports coordination during deployments

#### Compliance and Governance

**Scenario:** Enforce organisational standards and maintain audit trails

**Configuration:**

* Create a category: "Compliance" (Role: Organisation administrator or Security role)
* Add tags:
  * "data-classification" (Required)
  * "compliance-scope" (Required)
* Common values:
  * data-classification: "public", "internal", "confidential", "restricted"
  * compliance-scope: "GDPR", "HIPAA", "PCI-DSS", "None"

**Benefits:**

* Ensures every resource includes metadata for audit trails
* Prevents accumulation of untagged resources through Required enforcement
* Maintains trustworthy classification through role-based access control
* Supports regulatory reporting and compliance audits

### Best Practices

**Establish Naming Conventions:**

* Use lowercase with hyphens for tag names (e.g., "cost-centre", not "Cost\_Centre")
* Keep tag values consistent (always "dev", never mixing "dev", "development", "Development")
* Document your tag schema and value options for your organisation

**Plan Your Category Structure:**

* Align categories with organisational responsibilities
* Use role-based access to create appropriate security boundaries
* Avoid creating too many categories - aim for 3-7 logical groupings

**Use Required Tags Strategically:**

* Mark only essential tags as Required to avoid creating unnecessary overhead
* Typical required tags: environment, owner, cost-centre
* Optional tags provide flexibility for additional context

**Leverage Grouping and Filtering:**

* Use Group By Tag to visualise resource organisation
* Regularly check the "**\~untagged\~**" section to maintain tagging compliance
* Combine filtering and grouping for powerful resource discovery

**Integrate with Azure Capabilities:**

* Use the same tags in Azure Policy for governance automation
* Leverage tags in Azure Cost Management for financial analysis
* Apply tags in Azure Backup policies and retention rules

**Maintain Tag Hygiene:**

* Periodically audit untagged resources
* Review and update tag values as organisational structure changes
* Remove obsolete tags and categories to keep the system manageable
