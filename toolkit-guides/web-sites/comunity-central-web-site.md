# ComUnity Central Web Site

Community Central is a specialised website project type within the ComUnity Developer Toolkit, designed to act as the central portal for a solution. Unlike regular static web sites, this option generates a React-based app with project scaffolding and local development capabilities.

{% hint style="warning" %}
> Only one Community Central site can exist per project. If you need more than one, use the regular Web site feature instead.
{% endhint %}

## Key Features

* React app generator: When a Community Central website is created, a full React project is generated in the background. This includes installing dependencies and building the app using the toolkit’s internal CI process.
* Editable via Toolkit: Files and folders are visible and editable from the Toolkit UI, with additional controls coming soon (e.g., set default document).
* Download project: Once the build completes, a “Download Project” button becomes available, allowing you to customise the Community Central app outside the Toolkit.
* Accessible via a URL: Like regular websites, the app is accessible through a /sw/ static web handler.

## Creating a Community Central Web site

To create a ComUnity Central Website follow these steps,

1. Open your project in the Toolkit and navigate to the Web sites section.
2. At the top-section of the UI you will see a tile labelled ComUnity Central web site. If you don’t already have a Community Central Website you will be presented with an option to Add ComUnity Central. Otherwise, you will be shown with options to Open or  Edit the web site.
3. Click Add ComUnity Central to begin the setup process.
4. The website will be created. This may take some time as a React project is generated and built in the background.
5. Once complete, the ComUnity Central tile will update  providing you with options to click Open web site to preview the site in a new tab, or else click Edit to view and manage the project files.

## Managing Your ComUnity Central Website

Once your Community Central Website has been created, you can manage its content and customise the boilerplate directly within the Toolkit.

### Edit or Upload Files

Click Edit on the Community Central tile to open the file manager.

From here, you can:

* View the Site URL – Use the external link icon to launch the site in a new tab.
* Add a folder – Create new directories to organise your content.
* Add a file – Upload individual static assets such as .js, .html, .css, or images.
* Upload archive – Import a .zip file containing a complete site structure.
* Download site archive – Export the current folder and file structure.
* Download project archive – Export the full React project scaffold for offline development and advanced customisation.

#### Common Files You’ll See

* index.html – The default entry point for your site (must be placed at the root).
* favicon.ico – Optional site icon.
* assets/ – A folder typically used to hold images, fonts, or other static resources.
* site\_created – An internal marker file used by the platform.

{% hint style="warning" %}
> If index.html is missing or not at the root level, your site may not load correctly.
{% endhint %}



