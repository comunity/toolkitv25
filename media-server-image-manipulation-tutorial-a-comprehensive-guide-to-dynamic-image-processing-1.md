# Media Server Image Manipulation Tutorial  A Comprehensive Guide to Dynamic Image Processing

## Introduction

The ComUnity Platform Media Server provides robust capabilities for managing media assets including images, documents, and other file types. This tutorial will guide you through the process of uploading images to the Media Server and using them in your application screens.

**You will learn how to:**

* Upload images to the Media Server via the Toolkit UI
* Understand the SHA-based file naming convention
* Access uploaded files using File URL and SHA URL
* Add images to application screens using the Image control
* Apply image manipulation modifiers to transform images

### Uploading Images to the Media Server

The Media Server Upload interface provides a convenient, environment-specific upload utility for managing media assets. Each deployment environment (Development, QA, and Production) has its own dedicated Media Server, ensuring that media files can be tested independently without risk to live data.

#### Step 1: Navigate to Media Server Settings

1. Open your project in the ComUnity Developer Toolkit.
2. Click on the **Settings icon** (gear) next to your project name to open Project Settings.
3. Select your target environment tab (e.g., **Development environment**).
4. In the left sidebar, click on **Media Server**.

{% hint style="info" %}
Each deployment environment has its own Media Server. Files uploaded to the Development environment will not be available in QA or Production until uploaded separately to those environments.
{% endhint %}

#### Step 2: Understanding the Environment Tabs

At the top of the Project Settings dialog, you will see environment tabs:

| Environment                 | Purpose                          |
| --------------------------- | -------------------------------- |
| **Global**                  | For shared project-wide settings |
| **Development environment** | For testing during development   |
| **QA environment**          | For quality assurance testing    |
| **Production environment**  | For live deployment              |

Select the appropriate environment tab first, then click on **Media Server** in the sidebar to access that environment's media upload interface.

![Media Server Upload Interface](https://claude.ai/chat/Screenshot_2026-01-26_at_09_44_14.png) _Figure 1: Media Server Upload Interface showing the Development environment selected_

#### Step 3: Upload Your File

1. _(Optional)_ Enter an **Upload path** to specify a subdirectory under `/u/` for organizing your files.
2. Drag and drop your image file into the upload area, or click the **"Select a file"** button to browse.
3. Wait for the upload to complete. The file will appear in the **Uploaded Files** panel on the right.

> **Note:** Each file uploaded to the media server is stored using a SHA-based naming convention that prevents duplicate uploads and supports version integrity.

#### Step 4: Access Your Uploaded File URLs

Once uploaded, each media file provides two types of URLs:

| URL Type     | Description                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **File URL** | A permanent public URL using the friendly filename for direct access or embedding.                                                    |
| **SHA URL**  | A deterministic, hashed path derived from the file's contents and metadata. This prevents duplication and supports version integrity. |

![File URLs After Upload](https://claude.ai/chat/Screenshot_2026-01-26_at_09_44_42.png) _Figure 2: File URL and SHA URL displayed after successful upload_

Both URLs are displayed at the bottom of the upload panel. You can click on the file entry to copy either URL for use in your application.

{% hint style="info" %}
The SHA URL is particularly useful when you need to ensure that content hasn't changed, as any modification to the file would result in a different SHA hash.&#x20;
{% endhint %}

#### SHA File Naming Convention

All files uploaded to the media server follow a SHA-based file naming convention:

**For image file types:**

```
SHA_of_file.red.green.blue.alpha.width.height.file_extension
```

Example:

```
081b278349bb8499788bca8427f11063c73a666a66a8422840311e3397de5ad5.186.188.189.0.300.300.png
```

**For other file types:**

```
SHA_of_file.file_extension
```

Example:

```
0aa941b04274ae04dc5a9bd214f7d5214f36e6de.txt
```

{% hint style="warning" %}
The SHA File Naming convention prevents duplicate file uploads. However, note that uploading an existing file will overwrite it. Always verify you're not accidentally replacing important files.
{% endhint %}

## Adding Images to Application Screens

After uploading your images to the Media Server, you can use them in your application screens using the Image screen control. This section demonstrates how to add and configure an image on a screen.

#### Step 1: Navigate to the Screens Section

1. In the left sidebar of the Toolkit, click on **"Screens"**.
2. Select the screen where you want to add an image, or create a new screen.

#### Step 2: Add an Image Control

1. In the **Screen Controls** panel on the right, locate the **"Image"** control.
2. Drag the Image control and drop it onto your screen structure.
3. A placeholder image will appear in the screen preview.

![Screen View with Image Control](https://claude.ai/chat/Screenshot_2026-01-26_at_09_43_51.png) _Figure 3: Screen View showing Image control with Properties panel_

#### Step 3: Configure the Image Properties

When you select an Image control, the Properties panel displays the following options:

| Property          | Description                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| **Name**          | The system-generated name of the image control (e.g., NewsBanner2).                                     |
| **Image**         | The SHA URL or file path of the image. You can upload a new image or paste a URL from the Media Server. |
| **Image Preview** | Shows a preview of the selected image before saving.                                                    |

#### Step 4: Set the Image Source

You have two options to set the image:

**Option A: Upload directly**

* Click the **"Upload image"** button in the Properties panel.
* Select an image file from your computer.

**Option B: Use Media Server URL**

* Copy the SHA URL from your Media Server upload.
* Paste it into the **"Image"** field in the Properties panel.

#### Step 5: Save Your Changes

1. Verify the image appears correctly in the Image Preview.
2. Click the **"Save"** button at the bottom of the Properties panel.

### Part 3: Image Manipulation Using URL Modifiers

The ComUnity Media Server supports powerful image manipulation capabilities through URL modifiers. When fetching images, you can append optional arguments to transform them on-the-fly without modifying the original file.

#### Understanding URL Structure

The basic format for retrieving images with manipulation is:

```
<<Base URL>>/u/g/<<SHA File Name>>/<<modifier>>
```

**URL Arguments:**

| Argument | Type            | URL Format                                               |
| -------- | --------------- | -------------------------------------------------------- |
| `d`      | Direct          | `/u/d/<<SHA File Name>>`                                 |
| `f`      | Friendly        | `/u/f/<<Friendly File Name>>`                            |
| `g`      | Graphics Magick | `/u/g/<<SHA File Name>>/<<modifier>>`                    |
| `icon`   | Icon            | `/u/icon/<<RRGGBB>>/<<size>>/<<opacity>>/<<icon_image>>` |

#### Common Image Modifiers

Here are the most frequently used image manipulation modifiers:

| Modifier                            | Description                                                                                                                                                 |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$resize/width/height/options`      | Resize image to specified width and height. Options: `m` (maintain ratio), `!` (exact size), `p` (percentage), `g` (only if exceeds), `s` (only if smaller) |
| `$rotate/color/degrees`             | Rotate image by specified degrees. Background color fills empty space.                                                                                      |
| `$crop/x/y`                         | Crop image to specified width (x) and height (y) in pixels.                                                                                                 |
| `$thumb/size`                       | Create a thumbnail with specified maximum size.                                                                                                             |
| `$blur/radius/sigma`                | Apply Gaussian blur. Higher radius = more blur.                                                                                                             |
| `$sepia`                            | Apply sepia tone effect for a vintage look.                                                                                                                 |
| `$autoOrient`                       | Auto-rotate based on EXIF data. Useful for mobile uploads.                                                                                                  |
| `$flip`                             | Flip vertically (mirror along horizontal axis).                                                                                                             |
| `$flop`                             | Flip horizontally (mirror along vertical axis).                                                                                                             |
| `$charcoal/factor`                  | Apply charcoal sketch effect. Higher factor = more pronounced.                                                                                              |
| `$colorize/red/green/blue`          | Apply color tint (values 0-255).                                                                                                                            |
| `$contrast/multiplier`              | Adjust contrast. Values >1 increase, <1 decrease contrast.                                                                                                  |
| `$enhance`                          | Apply automatic image enhancement algorithm.                                                                                                                |
| `$equalize`                         | Apply histogram equalization for improved contrast.                                                                                                         |
| `$normalize`                        | Normalize brightness and contrast across full pixel range.                                                                                                  |
| `$oil/radius`                       | Apply oil painting effect. Larger radius = more pronounced.                                                                                                 |
| `$border/width/height/color`        | Add a border around the image.                                                                                                                              |
| `$drawText/x/y/text/color/fontSize` | Add text overlay at specified position.                                                                                                                     |

#### Example: Using Image Manipulation in a Screen

The screenshot below shows an image being used in a Content control with rotation applied:

![Image with Rotation Modifier](https://claude.ai/chat/Screenshot_2026-01-26_at_09_44_55.png) _Figure 4: Image with rotation modifier ($rotate/180) applied in Content control_

In this example, the Markdown field contains an image reference with a rotation modifier:

```markdown
![Alt text]
(/u/g/acece449d9339a6298c2fd5a26f9aa1ffbb0e885c7f1e
c421987a98c6fb43747.197.201.202.255.3024.1700.png/$rotate/180)
```

{% hint style="info" %}
The `$rotate/180` modifier at the end of the URL rotates the image 180 degrees. You can chain multiple modifiers by appending them with forward slashes.
{% endhint %}

#### Chaining Multiple Modifiers

You can apply multiple transformations by chaining modifiers:

```
/u/g/<<SHA File Name>>/$resize/300/200/$sepia/$blur/2/1
```

This example would:

1. Resize the image to 300x200 pixels
2. Apply sepia tone
3. Apply a slight blur

### Part 4: Best Practices and Tips

#### File Organisation

* Use descriptive filenames before uploading to make files easier to identify.
* Consider using the Upload path field to organize files into logical subdirectories.
* Keep track of your File URLs and SHA URLs for easy reference.

#### Performance Optimisation

* Use the `$thumb` modifier to create smaller versions for thumbnails and previews.
* Apply `$resize` to reduce bandwidth when full-resolution images aren't needed.
* The Media Server caches transformed images, so repeated requests are served quickly.

#### Mobile Considerations

* Always use `$autoOrient` for images that may be uploaded from mobile devices.
* This ensures images display correctly regardless of how the device was held when the photo was taken.

#### Environment Management

* Test uploads in Development environment before promoting to QA or Production.
* Remember that file deletions are permanent and scoped to the selected environment only.
* Each environment has its own Media Server, so you'll need to upload files to each environment where they're needed.
* Use the same filenames across environments for consistency in your application code.

{% hint style="warning" %}
Deletion is permanent and scoped to the selected environment only. Always double-check before deleting files, especially in Production.
{% endhint %}

### Summary

In this tutorial, you learned how to:

1. Navigate to Media Server settings via **Project Settings > \[Environment] > Media Server**
2. Upload images using drag-and-drop or file selection
3. Understand the difference between File URL and SHA URL
4. Add Image controls to screens and configure their properties
5. Apply image manipulation modifiers like resize, rotate, crop, and effects

For more detailed information about all available modifiers and advanced features, refer to the complete Media Server documentation in the ComUnity Platform documentation.

### Quick Reference Card

#### Navigation Path

```
Project Settings > Development/QA/Production environment > Media Server
```

#### URL Patterns

```
Direct access:     /u/d/<<SHA File Name>>
Friendly name:     /u/f/<<Friendly File Name>>  
With modifiers:    /u/g/<<SHA File Name>>/<<modifier>>
```

#### Most Used Modifiers

```
$resize/width/height/m    - Resize maintaining aspect ratio
$thumb/size               - Create thumbnail
$rotate/color/degrees     - Rotate image
$crop/width/height        - Crop to size
$autoOrient               - Fix mobile orientation
$sepia                    - Vintage effect
```
