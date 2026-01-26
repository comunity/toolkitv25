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

1. In your project, click the **Settings icon** (the gear) next to your project name. The Project Settings dialog opens.
2. You'll see environment tabs at the top: **Global**, **Development environment**, **QA environment**, and **Production environment**. Click on **Development environment** since we're just testing for now.
3. In the left sidebar, click on **Media server**.

You should now see the Media Server upload interface with a drag-and-drop area and an "Uploaded Files" panel on the right.

> Each environment has its own separate Media Server. This means an image you upload to Development won't exist in QA or Production until you upload it there too. This keeps your testing isolated from your live application.

### Step 2: Upload Your Image

Now let's get your image into the Media Server.

1. Find your image file on your computer.
2. Drag it into the upload area, or click **"Select a file"** to browse.
3. Wait a moment while the file uploads. Once complete, your file appears in the **Uploaded Files** panel on the right with a green checkmark.
4. Click on your uploaded file in the list. At the bottom of the panel, you'll see two URLs appear:
   * **File URL** – Uses your original filename, like: `https://toolkitv3.comunity.me/u/f/my-photo.png`
   * **SHA URL** – Uses a unique hash based on the file contents, like: `https://toolkitv3.comunity.me/u/d/77d55728427f43cce27624d37658dd11292f1f8c42d288af059b27297127e551.139.127.120.0.2048.1368.png`
5. Copy the **SHA URL** – you'll need this in the next step. The SHA URL is longer but it's what you'll use when you want to manipulate the image later.

> Notice the numbers in the SHA filename? For images, the Media Server embeds colour and dimension information right in the filename: `SHA.red.green.blue.alpha.width.height.extension`. This helps the server process your image efficiently.

### Step 3: Add the Image to a Screen

With your image uploaded, let's display it in your application.

1. Close the Project Settings dialog and click **Screens** in the left sidebar.
2. Select the screen where you want to add your image, or create a new screen.
3. In the **Screen Controls** panel on the right, find the **Image** control.
4. Drag the Image control onto your screen structure where you want the image to appear.
5. With the Image control selected, look at the **Properties** panel. You'll see an **Image** field.
6. Paste the SHA URL you copied earlier into this field.
7. The **Image Preview** below should now show your image. If it looks correct, click **Save**.

Your image is now part of your screen. When users view this screen in your app, they'll see the image you uploaded.

### Step 4: Rotate the Image Using URL Modifiers

Here's where the Media Server becomes powerful. Instead of opening an image editor to rotate your photo, you can simply modify the URL.

Let's rotate your image 180 degrees:

1.  Take your SHA URL. It currently looks something like:

    ```
    https://toolkitv3.comunity.me/u/d/77d55728427f43cce...png
    ```
2.  Change `/u/d/` to `/u/g/` – this tells the Media Server you want to apply graphics manipulation:

    ```
    https://toolkitv3.comunity.me/u/g/77d55728427f43cce...png
    ```
3.  Add the rotation modifier at the end:

    ```
    https://toolkitv3.comunity.me/u/g/77d55728427f43cce...png/$rotate/white/180
    ```
4. Go back to your Image control's Properties and replace the URL with this new one.
5. Check the Image Preview – your image should now be upside down!

The `$rotate/white/180` part tells the server to rotate 180 degrees and fill any empty space with white. You can use any colour name or hex code, and any degree value.

### Step 5: Try More Transformations

Now that you understand how modifiers work, try these on your image:

**Create a thumbnail (150 pixels):**

```
/u/g/YOUR_SHA_FILENAME/$thumb/150
```

**Resize to exactly 300×200 pixels:**

```
/u/g/YOUR_SHA_FILENAME/$resize/300/200/!
```

**Resize to fit within 400×300 while keeping proportions:**

```
/u/g/YOUR_SHA_FILENAME/$resize/400/300/m
```

**Apply a vintage sepia effect:**

```
/u/g/YOUR_SHA_FILENAME/$sepia
```

**Add a soft blur:**

```
/u/g/YOUR_SHA_FILENAME/$blur/3/2
```

**Combine multiple effects** – just chain them together:

```
/u/g/YOUR_SHA_FILENAME/$resize/300/300/m/$sepia/$blur/2/1
```

This creates a 300×300 thumbnail with sepia toning and a subtle blur, all from a single URL.

***

### Step 6: Fix Mobile Photo Orientation

If you're building an app where users upload photos from their phones, you'll encounter a common problem: photos appear rotated incorrectly. This happens because phones store rotation data separately from the image itself.

The fix is simple. Add `$autoOrient` to your image URL:

```
/u/g/YOUR_SHA_FILENAME/$autoOrient
```

This reads the photo's orientation data and rotates it correctly. For any user-uploaded mobile photos, this modifier should be your default.

### Step 7: Upload to Other Environments

Your image works perfectly in Development. Now let's prepare it for QA testing.

1. Open **Project Settings** again.
2. This time, click the **QA environment** tab.
3. Click **Media server** in the sidebar.
4. Upload the same image file.

The image now exists in both Development and QA. When you're ready for production, repeat this process on the **Production environment** tab.

> Your image URLs will work the same way in each environment—only the base URL changes. The SHA filename stays identical because it's based on the file contents, not where you uploaded it.

### What You've Learned

You've completed a full workflow with the ComUnity Media Server:

1. You navigated to the Media Server through Project Settings, selecting your environment first.
2. You uploaded an image and discovered the two URL types—File URL for readable links and SHA URL for version integrity.
3. You added the image to a screen using the Image control.
4. You learned that changing `/u/d/` to `/u/g/` enables image manipulation.
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
