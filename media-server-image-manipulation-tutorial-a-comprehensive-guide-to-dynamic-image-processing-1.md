# Media Server Image Manipulation Tutorial: A Comprehensive Guide to Dynamic Image Processing

In this tutorial, you'll upload an image to the ComUnity Platform Media Server, add it to an application screen, and then apply transformations to create different versions of the same image—all without editing the original file.

By the end, you'll have a working image displayed in your app with rotation applied, and you'll know how to resize, crop, and apply effects to any image using simple URL modifications.

### Before You Begin

Make sure you have:

* Access to the ComUnity Developer Toolkit
* An existing project open in the Toolkit
* An image file ready to upload (PNG or JPEG work best for image manipulation)

### Step 1: Open the Media Server

Let's start by navigating to where you'll upload your image.

1.  In your project, click the **Settings icon** (the gear) next to your project name. The Project Settings dialog opens.<br>

    <figure><img src=".gitbook/assets/image (538).png" alt=""><figcaption></figcaption></figure>
2. You'll see environment tabs at the top: **Global**, **Development environment**, **QA environment**, and **Production environment**. Click on **Development environment** since we're just testing for now.
3. In the left sidebar, click on **Media server**.

You should now see the Media Server upload interface with a drag-and-drop area and an "Uploaded Files" panel on the right.

<figure><img src=".gitbook/assets/image (537).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Each environment has its own separate Media Server. This means an image you upload to Development won't exist in QA or Production until you upload it there too. This keeps your testing isolated from your live application.
{% endhint %}

### Step 2: Upload Your Image

Now let's get your image into the Media Server.

1. Find your image file on your computer.
2. Drag it into the upload area, or click **"Select a file"** to browse.
3. Wait a moment while the file uploads. Once complete, your file appears in the **Uploaded Files** panel on the right with a green checkmark.
4. Click on your uploaded file in the list. At the bottom of the panel, you'll see two URLs appear:
   * **File URL** – Uses your original filename, like: `https://toolkitv3.comunity.me/u/f/my-photo.png`
   *   **SHA URL** – Uses a unique hash based on the file contents, like: `https://toolkitv3.comunity.me/u/d/77d55728427f43cce27624d37658dd11292f1f8c42d288af059b27297127e551.139.127.120.0.2048.1368.png`

       <figure><img src=".gitbook/assets/image (539).png" alt=""><figcaption></figcaption></figure>
5. Copy the **SHA URL** – you'll need this in the next step. The SHA URL is longer but it's what you'll use when you want to manipulate the image later.

{% hint style="info" %}
Notice the numbers in the SHA filename? For images, the Media Server embeds colour and dimension information right in the filename: `SHA.red.green.blue.alpha.width.height.extension`. This helps the server process your image efficiently.
{% endhint %}

### Step 3: Add the Image to a Screen

With your image uploaded, let's display it in your application.

1. Close the Project Settings dialog and click **Screens** in the left sidebar.
2. Select the screen where you want to add your image, or create a new screen.
3. In the **Screen Controls** panel on the right, find the **Image** control.
4. Drag the Image control onto your screen structure where you want the image to appear.
5. With the Image control selected, look at the **Properties** panel on the right. You'll see fields for **Name** and **Image**.
6.  In the **Image** field, paste just the SHA filename portion—you don't need the full URL. For example:

    ```
       b6f8a18cd693b3f4f0d1de0a58b53a8793ab53b569863ba5c86b1e6f9e39bda8.176.176.181.254.476.548.avif
    ```

    The Toolkit automatically resolves this to the correct Media Server URL.
7.  Once you've entered a valid image reference, an **Image Preview** appears below the field showing your image. This confirms the Toolkit found and loaded your image successfully. Click **Save** and **Launch** your project.<br>

    <figure><img src=".gitbook/assets/image (540).png" alt=""><figcaption></figcaption></figure>

Your image is now part of your screen. When users view this screen in your app, they'll see the image you uploaded.

### Step 4: Apply Image Manipulation Using a Content Control

Here's where the Media Server becomes powerful. Instead of opening an image editor to rotate your photo, you can apply transformations directly through the URL. To do this, you'll use a **Content control** with Markdown syntax rather than the Image control.

1. Go back to your screen in the **Screens** section.
2. From the **Screen Controls** panel, drag a **Paragraph** (Content) control onto your screen structure.
3. With the Content control selected, look at the **Properties** panel. You'll see a **Markdown** field.
4. Enter your image using Markdown image syntax, but this time construct the URL for graphics manipulation. Change `/u/d/` to `/u/g/` and add your modifier at the end:

```markdown
   ![Alt text](/u/g/acece449d9339a6298c2fd5a26f9aa1ffbb0e885c7f1ec421987a98c6fb43747.197.201.202.255.3024.1700.png/$rotate/180)
```

5. Click **Save**.&#x20;
6. **Launch** your project. Your image now displays rotated 180 degrees!

Let's break down what changed in the URL:

* `/u/g/` tells the Media Server you want to apply graphics manipulation (instead of `/u/d/` for direct access)
* `$rotate/180` at the end rotates the image 180 degrees

{% hint style="info" %}
The Content control with Markdown gives you full control over image URLs, making it perfect for applying transformations. The Image control is simpler but doesn't support URL modifiers.
{% endhint %}

### Step 5: Try More Transformations

Now that you understand how modifiers work, try these variations in your Content control's Markdown field:

**Create a thumbnail (150 pixels):**

```markdown
![Thumbnail](/u/g/YOUR_SHA_FILENAME/$thumb/150)
```

**Resize to exactly 300×200 pixels:**

```markdown
![Resized](/u/g/YOUR_SHA_FILENAME/$resize/300/200/!)
```

**Resize to fit within 400×300 while keeping proportions:**

```markdown
![Resized](/u/g/YOUR_SHA_FILENAME/$resize/400/300/m)
```

**Apply a vintage sepia effect:**

```markdown
![Sepia](/u/g/YOUR_SHA_FILENAME/$sepia)
```

**Add a soft blur:**

```markdown
![Blurred](/u/g/YOUR_SHA_FILENAME/$blur/3/2)
```

**Combine multiple effects** – just chain them together:

```markdown
![Combined](/u/g/YOUR_SHA_FILENAME/$resize/300/300/m/$sepia/$blur/2/1)
```

This creates a 300×300 thumbnail with sepia toning and a subtle blur, all from a single URL.

### Step 6: Fix Mobile Photo Orientation

If you're building an app where users upload photos from their phones, you'll encounter a common problem: photos appear rotated incorrectly. This happens because phones store rotation data separately from the image itself.

The fix is simple. Add `$autoOrient` to your image URL in the Markdown:

```markdown
![Photo](/u/g/YOUR_SHA_FILENAME/$autoOrient)
```

This reads the photo's orientation data and rotates it correctly. For any user-uploaded mobile photos, this modifier should be your default.

### Step 7: Upload to Other Environments

Your image works perfectly in Development. Now let's prepare it for QA testing.

1. Open **Project Settings** again.
2. This time, click the **QA environment** tab.
3. Click **Media server** in the sidebar.
4. Upload the same image file.

The image now exists in both Development and QA. When you're ready for production, repeat this process on the **Production environment** tab.

{% hint style="info" %}
Your image URLs will work the same way in each environment—only the base URL changes. The SHA filename stays identical because it's based on the file contents, not where you uploaded it.
{% endhint %}

### What You've Learned

You've completed a full workflow with the ComUnity Media Server:

1. You navigated to the Media Server through Project Settings, selecting your environment first.
2. You uploaded an image and discovered the two URL types—File URL for readable links and SHA URL for version integrity.
3. You added a simple image to a screen using the **Image control** with just the SHA filename.
4. You learned that the **Content control** with Markdown syntax lets you apply image manipulation by using `/u/g/` URLs with modifiers.
5. You applied transformations like rotation, resizing, and effects by adding modifiers to the URL.
6. You discovered `$autoOrient` for handling mobile uploads.
7. You understood that each environment has its own Media Server, keeping development isolated from production.

### Quick Reference

When you need to manipulate images, remember this pattern:

```
Change:  /u/d/filename  (direct access)
To:      /u/g/filename/$modifier  (graphics manipulation)
```

Common modifiers you'll use often:

* `$thumb/size` – Create a thumbnail
* `$resize/width/height/m` – Resize maintaining aspect ratio
* `$rotate/color/degrees` – Rotate the image
* `$crop/width/height` – Crop to size
* `$autoOrient` – Fix mobile photo orientation
* `$sepia` – Vintage effect
* `$blur/radius/sigma` – Soften the image

The server caches your transformed images, so the first request does the processing and subsequent requests are served instantly.

### Next Steps

Now that you're comfortable with the basics, try:

* Using the `$drawText` modifier to add watermarks to images
* Creating an icon set using the `/u/icon/` path with custom colours
* Setting up a content screen that displays user-uploaded photos with `$autoOrient` applied automatically
