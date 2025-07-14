# Extending Visual Studio Projects

## Overview

From version **25.2** onwards, the ComUnity Developer Toolkit supports full extension of the auto-generated Visual Studio project. Developers can now:

* Add custom files and folders
* Reference external **NuGet packages**
* Include additional **.NET Framework references**

These enhancements remove the previous limitation where customisation beyond basic code injection required direct server access. Projects downloaded from the Toolkit can now reflect a much broader range of development use cases.

### Accessing the Feature in the Toolkit

To access the Visual Studio Project customisation tools:

1. Navigate to your project from the main Projects view.
2. Click on the Project Settings panel.
3. In the left-hand menu, select Visual Studio project.
4. A tabbed interface will be presented:
   * Files: Upload templates, configuration files, or other resources.
   * NuGet packages: Add external packages for runtime and development needs.
   * Framework references: Enable additional .NET Framework libraries.

<figure><img src="../../.gitbook/assets/image (487).png" alt=""><figcaption></figcaption></figure>

#### Files Tab

* Project path: Specify the internal file path under the custom/ directory (e.g. templates/ReportTemplate.xlsx).
* File upload: Drag and drop a file, or click Select a file.
* Uploaded files will appear in the list and be included on the next project rebuild.



> Note: All uploaded files are stored under the custom/ directory. Files cannot be added to other areas of the solution structure.

## 1. Adding Custom Files and Directories

The Toolkit allows uploading arbitrary files that are automatically included in the custom directory of your Visual Studio project.

Example:

Upload an Excel file under custom/templates/ReportTemplate.xlsx and reference it in your service logic to generate a custom report.

## 2. Adding NuGet Packages

You can now include third-party libraries by specifying NuGet package dependencies through the Toolkit.

### How it works:

* Specify the **package name** and **version** in the Toolkit interface under the relevant entity or service configuration.
* Rebuild the project.
* The package is downloaded and added to the project during build.
* Code referencing the package can be written in the relevant custom service class.

**Example**:\
To read Excel files, add:

```
Package Name: ClosedXML  
Version: 0.97.0
```

You can then use `ClosedXML` to open and manipulate Excel spreadsheets programmatically.

## 3. Adding .NET Framework References

In addition to NuGet packages, you can now enable specific .NET Framework references that your custom code requires.

### How it works:

* Select the desired system libraries (e.g. `System.Xml.Linq`) from a list in the Toolkit.
* These are added as references in the `.csproj` file during build.
* They become available to all custom classes within the project.

**Example**:\
Enable `System.Xml.Linq` to use:

```csharp
using System.Xml.Linq;
```

for XML manipulation.

## Typical Workflow

1. **Write and test your code locally**\
   Develop in Visual Studio using the downloaded project. Use the `custom` folder for all your extensions.
2. **Mirror changes in the Toolkit**
   * Upload any files required (e.g. templates).
   * Define NuGet packages and/or framework references under the corresponding entity or service.
3. **Rebuild the project**\
   Rebuild via the Toolkit. All new references and resources will be included in the generated Visual Studio project.
4. **Download and build**\
   Open the new project in Visual Studio, restore packages if needed, and build successfully.

## Notes

* **Entity Framework**: The Toolkit uses the Code-First approach. Model files are regenerated during build and cannot be edited directly.
* **Persistent configuration**: Custom files, NuGet packages, and references are stored in the Toolkit’s configuration and persist across rebuilds.
* **No manual patching**: These enhancements eliminate the need to manually edit the project on the server or after download.

## Example Use Case

You need to generate a formatted Excel report for a data export feature:

1. Upload `ReportTemplate.xlsx` under `custom/templates/`.
2. Add the `ClosedXML` NuGet package via the Toolkit.
3. Add your report generation logic under `custom/MyEntity/MyEntityService.cs`.
4. Enable `System.IO` if required.
5. Rebuild and download the project.
6. Your code compiles successfully and can now generate Excel files using the uploaded template.

## Availability

This feature is available in Toolkit **v25.2** and above. Ensure your environment is up to date to access this functionality.
