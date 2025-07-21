# Web Site

The ComUnity Developer Toolkit allows you to host static front-end sites and dynamic web portals directly within your project. This feature is ideal for deploying lightweight user interfaces, custom administration tools, or rich, interactive user portals.

This guide covers two types of web hosting options:

* Web Sites: For hosting standard static sites (HTML, CSS, JavaScript).
* Community Central: A specialised option for creating a modern, React-based central portal for your solution.

## Standard Web Sites

The Web Sites feature allows you to deploy and manage static web content directly from your Toolkit project. It is the perfect choice for simple landing pages, documentation, or basic front-end interfaces that don't require a complex build process.

**Common Use Cases**

* Project Landing Page: A simple marketing or informational microsite to introduce your solution.
* API Documentation: Host static HTML documentation for your project's APIs.
* Simple Admin Tools: Create basic forms and dashboards for internal project administration.
* Terms of Service Pages: Host standalone legal documents like privacy policies or terms of use.
* "Lite" User Portals: A lightweight interface for users to view information without the complexity of a full application.

**Key Capabilities**

* Host Static Content: Deploy websites built with HTML, CSS, JavaScript, images, and fonts.
* Integrated URL Routing: Websites are served through the platform's built-in `/w/` URL handler for seamless access.
* Direct File Management: Upload and manage your site's files and folders directly within the Toolkit.

**Understanding the URL Structure**

Every website you create is assigned a unique URL based on the following pattern:

`https://<domain>/w/<project-name>/<url-suffix>`

| Component          | Description                                    | Example                         |
| ------------------ | ---------------------------------------------- | ------------------------------- |
| `https://<domain>` | The base domain of your Toolkit environment.   | `https://toolkitv3.comunity.me` |
| `/w/`              | The platform's internal Static Web Handler.    | `/w/`                           |
| `<project-name>`   | The unique identifier of your Toolkit project. | `pokemon`                       |
| `<url-suffix>`     | A custom path you define during creation.      | `games`                         |

Example URL: `https://toolkitv3.comunity.me/w/pokemon/games/index.html`

### **Creating a Web Site**

1. Open your project and navigate to the Web sites section.
2. Scroll past the "Community Central" tile to the Web sites area.
3. Click **+Add** web site to open the creation dialog.
4. In the dialog, enter a URL suffix (e.g., `my-app`, `tools`, `admin`).
5. Click Create. Your website is now ready for you to upload content.

### **Managing Your Web Site**

Once a website is created, you can click  **Edit** on its tile to access the file manager. From here you can:

* Add file: Upload individual files like `index.html`, stylesheets, or scripts.
* Add folder: Create new directories to organise your content.
* Upload archive: Import a `.zip` file containing your entire site structure. This is the most efficient way to deploy a complete site.
* Download site archive: Export the current site files as a `.zip` archive.

> Note: Default File Requirement
>
> The default entry point for any website must be an index.html file placed at the root level of your uploaded files. If this file is missing or in a sub-folder, the site will not load correctly.

## Community Central

Community Central is a specialised web site project type within the ComUnity Developer Toolkit, designed to act as the central portal for a solution. Unlike regular static web sites, this option generates a React-based app with project scaffolding and local development capabilities.

**Why Use Community Central?**

While standard web sites are excellent for simple content, modern user portals demand complex UIs and streamlined development workflows. Community Central was built to meet these needs by providing:

* **Accelerated Setup**: Get a complete, build-ready React application with a single click, saving you from complex manual configuration.
* A "Golden Path" for Development: Start with a project scaffold that follows industry best practices, ensuring a solid, maintainable foundation.
* Streamlined Workflow: Easily download the project to work in a rich IDE like VS Code, then deploy your production build back to the Toolkit with a simple archive upload.
* **Focus on Your Application, Not on Tooling:** Spend your time building features, not wrestling with configuration.

**Common Use Cases**

* Customer Self-Service Portal: A full-featured portal for users to log in, manage their accounts, and view data.
* Interactive Data Dashboard: A dynamic Single Page Application (SPA) that presents data from your project's APIs with interactive charts and tables.
* Partner or Vendor Platform: A central hub for third-party partners to onboard and interact with your solution.
* The Primary UI for Your Solution: Build the complete, primary user-facing application for your entire project.

&#x20;React-based app with project scaffolding and local development capabilities.

{% hint style="warning" %}
> You can only create one Community Central site per project. If your solution requires multiple web portals, use the standard Web Site feature for any additional sites.
{% endhint %}

**Key Features**

| Feature                    | Description                                                                     |
| -------------------------- | ------------------------------------------------------------------------------- |
| Powered by React           | Automatically generates a complete React project and handles the initial build. |
| Integrated File Management | View, edit, and organise project files directly from the Toolkit's UI.          |
| Full Source Code Access    | Download the entire React project to work in your preferred local environment.  |
| Instant Live Preview       | Instantly accessible via the platform's `/w/` URL handler.                      |

### **Creating Your Community Central Site**

1. From your project's dashboard, navigate to the Web sites section.
2. Locate the Community Central web site tile at the top.
3. Click **Add Community Central** to begin the setup process.
4. Please be patient. The Toolkit is now generating the React project and running the initial build. This may take a few moments.
5. Once complete, the tile will update. You can now:
   * Click Open web site to preview your new portal.
   * Click Edit to start managing your project files.

### **Managing Your  ComUnity Central Web Site**

You have two primary ways to manage and customise your ComUnity Central site: directly within the Toolkit for quick edits, or by downloading the project for advanced development.

#### **Quick Edits of the ComUnity Central Web Site in the Toolkit**

For simple changes, click Edit on the Community Central tile. From the file manager, you can perform basic operations like Add file, Add folder, Upload archive, and Download site archive.

#### **Advanced Customisation of the ComUnity Central Web Site (Local Development)**

For major changes, work with the project on your local machine:

1. In the file manager view, click Download project archive.
2. Unzip the file and open the project folder in your preferred code editor (e.g., VS Code).
3. Follow the instructions in the `README.md` file to install dependencies and run the local development server (e.g., `npm install`, then `npm run dev`).
4. Make your code changes and test them locally.
5. When ready, run the build command (e.g., `npm run build`) to generate a `build` or `dist` folder.
6. Return to the Toolkit's file manager and use Upload archive to upload a `.zip` of the contents of your build folder. This deploys your changes.

**Understanding the File Structure**

When you open the file manager, you will see the compiled output of the React application. The key files are:

* `index.html`: The main entry point for your application. This file must remain at the root level.
* `favicon.ico`: The site icon. You can replace this with your own.
* `static/`: A folder containing the compiled and minified JavaScript, CSS, and other assets.
* `site_created`: An internal marker file used by the Toolkit. You can safely ignore this file.
