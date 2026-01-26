---
hidden: true
---

# Media Server Image Manipulation Tutorial  A Comprehensive Guide to Dynamic Image Processing

### 1. Introduction

The ComUnity Developer Toolkit's Media Server provides powerful image manipulation capabilities through URL-based modifiers derived from [Graphics Magick](http://www.graphicsmagick.org/). This allows you to dynamically transform images on-the-fly without storing multiple versions of the same image.

**Key benefits include:**

* Reduced storage requirements - store one image, generate multiple variations
* Automatic caching of transformed images for improved performance
* Browser-friendly delivery with partial GET requests for large files
* Device-adaptive content optimisation

### 2. Understanding URL Structure

All image manipulation requests follow a consistent URL pattern:

```
<<Base URL>>/u/<<args>>
```

#### 2.1 URL Components

| Argument | Type            | URL Pattern                                              |
| -------- | --------------- | -------------------------------------------------------- |
| **d**    | Direct          | `/u/d/<<SHA File Name>>`                                 |
| **f**    | Friendly        | `/u/f/<<Friendly File Name>>`                            |
| **icon** | Icon            | `/u/icon/<<RRGGBB>>/<<size>>/<<opacity>>/<<icon_image>>` |
| **g**    | Graphics Magick | `/u/g/<<SHA File Name>>/<<modifier>>`                    |

The **'g' (Graphics Magick)** argument is where all image manipulation happens. You append modifiers to transform images dynamically.

### 3. Image Modifier Reference

The following modifiers can be chained together in the URL to apply multiple transformations to an image. Each modifier follows the pattern:

```
/u/g/<<SHA_filename>>/$modifier1/$modifier2/$modifier3
```

#### 3.1 $autoOrient - Auto Orient

**Syntax:** `$autoOrient`

Automatically adjusts the orientation of an image based on its EXIF metadata. This is especially useful for photos taken with mobile devices or cameras that record orientation data.

**Use Case:** Mobile uploads, camera photos that appear rotated incorrectly.

**Example:**

```
/u/g/image.png/$autoOrient
```

#### 3.2 $blur - Gaussian Blur

**Syntax:** `$blur/<<radius>>/<<sigma>>`

Applies a Gaussian blur to reduce noise or soften details. The radius parameter specifies the blur kernel size, and sigma controls the standard deviation. Larger values create more blur.

**Parameters:**

* **radius** - Size of the blur kernel
* **sigma** - Standard deviation for smoother transitions

**Use Case:** Background blur effects, privacy masking, depth of field simulation.

**Example:**

```
/u/g/image.png/$blur/5/2
```

#### 3.3 $border - Add Border

**Syntax:** `$border/<<width>>/<<height>>/<<colour>>`

Adds a colored border around the image. The color can be specified using hexadecimal values (e.g., #FF0000), RGB values, or color names.

**Parameters:**

* **width** - Border width in pixels
* **height** - Border height in pixels
* **colour** - Border color (hex, RGB, or name)

**Example:**

```
/u/g/image.png/$border/5/5/FF0000
```

#### 3.4 $charcoal - Charcoal Effect

**Syntax:** `$charcoal/<<factor>>`

Applies a charcoal sketch effect by emphasizing edges and contours while reducing detail. Higher factor values produce more pronounced results.

**Use Case:** Artistic photo effects, sketch-style images.

**Example:**

```
/u/g/image.png/$charcoal/2
```

#### 3.5 $colorize - Color Tint

**Syntax:** `$colorize/<<red>>/<<green>>/<<blue>>`

Applies a color tint by blending the original colors with specified RGB values (0-255). Setting all values to 0 creates grayscale; setting all to 255 creates fully saturated tint.

**Use Case:** Sepia tones, color-themed branding, vintage effects.

**Example:**

```
/u/g/image.png/$colorize/100/50/0
```

#### 3.6 $contrast - Adjust Contrast

**Syntax:** `$contrast/<<+-multiplier>>`

Adjusts image contrast by multiplying pixel values. Values > 1 increase contrast, values between 0-1 decrease it. Negative values invert the image.

**Example:**

```
/u/g/image.png/$contrast/1.5
```

#### 3.7 $crop - Crop Image

**Syntax:** `$crop/<<x>>/<<y>>`

Crops the image to specified dimensions. X represents width, Y represents height in pixels.

**Use Case:** Thumbnail generation, removing unwanted image portions.

**Example:**

```
/u/g/image.png/$crop/300/200
```

#### 3.8 $drawText - Add Text Overlay

**Syntax:** `$drawText/<<x>>/<<y>>/<<text>>/<<colour>>/<<fontSize>>`

Adds text at specified coordinates with custom color and size.

**Parameters:**

* **x, y** - Top-left coordinates in pixels
* **text** - Text content
* **colour** - Text color
* **fontSize** - Text size in points

**Use Case:** Watermarks, titles, captions, labels.

**Example:**

```
/u/g/image.png/$drawText/20/50/Copyright/FFFFFF/24
```

#### 3.9 $enhance - Enhance Image

**Syntax:** `$enhance`

Applies automatic enhancement by adjusting brightness, contrast, and sharpness to improve overall clarity and detail.

**Example:**

```
/u/g/image.png/$enhance
```

#### 3.10 $equalize - Histogram Equalization

**Syntax:** `$equalize`

Applies histogram equalization to improve contrast by evenly distributing pixel values across the available range.

\{% hint style="warning" %\} **Warning:** May create exaggerated or unnatural appearance in some images. \{% endhint %\}

**Example:**

```
/u/g/image.png/$equalize
```

#### 3.11 $flatten - Flatten Layers

**Syntax:** `$flatten`

Merges all image layers into a single layer. This is a destructive operation.

**Use Case:** Combining multi-layer images, simplifying complex images.

**Example:**

```
/u/g/image.png/$flatten
```

#### 3.12 $flip - Flip Vertically

**Syntax:** `$flip`

Flips the image along the vertical axis (left to right), creating a mirror image.

**Example:**

```
/u/g/image.png/$flip
```

#### 3.13 $flop - Flip Horizontally

**Syntax:** `$flop`

Flips the image along the horizontal axis (top to bottom), creating an upside-down version.

**Example:**

```
/u/g/image.png/$flop
```

#### 3.14 $normalize - Normalize Contrast

**Syntax:** `$normalize`

Adjusts contrast and brightness so that the full range of pixel values is utilized. Darkest pixels become black, brightest become white.

**Use Case:** Poorly exposed photos, uneven lighting correction.

**Example:**

```
/u/g/image.png/$normalize
```

#### 3.15 $oil - Oil Painting Effect

**Syntax:** `$oil/<<radius>>`

Simulates an oil painting by applying brushstroke-like textures. Larger radius values create more pronounced effects.

**Example:**

```
/u/g/image.png/$oil/3
```

#### 3.16 $resize - Resize Image

**Syntax:** `$resize/<<width>>/<<height>>/<<options>>`

Resizes the image with various options for handling aspect ratio and dimensions.

**Options:**

* **m** - Maintain aspect ratio (width and height are minimum)
* **!** - Exact size (ignore aspect ratio)
* **p** - Size in percentage
* **a** - Maximum area in pixels
* **g** - Change dimensions only if exceeded
* **s** - Resize only if both dimensions are less

**Examples:**

```
/u/g/image.png/$resize/300/200/!  (exact size)
/u/g/image.png/$resize/50/50/p    (50% of original)
/u/g/image.png/$resize/800/600/m  (maintain aspect ratio)
```

#### 3.17 $rotate - Rotate Image

**Syntax:** `$rotate/<<colour>>/<<degrees>>`

Rotates the image by specified degrees with an optional background color for empty space.

\{% hint style="warning" %\} **Warning:** Large rotation angles may result in quality loss. \{% endhint %\}

**Example:**

```
/u/g/image.png/$rotate/FFFFFF/45
```

#### 3.18 $sepia - Sepia Tone

**Syntax:** `$sepia`

Applies a vintage sepia tone effect by reducing saturation and applying a brownish-yellow color cast.

**Example:**

```
/u/g/image.png/$sepia
```

#### 3.19 $thumb - Create Thumbnail

**Syntax:** `$thumb/<<size>>`

Creates a thumbnail with specified maximum size.

**Example:**

```
/u/g/image.png/$thumb/150
```

#### 3.20 $type - Change Image Type

**Syntax:** `$type/<<type>>`

Converts the image to a specified type.

**Available Types:**

* Bilevel
* Grayscale
* Palette
* PaletteMatte
* TrueColor
* TrueColorMatte
* ColorSeparation
* Optimize

**Example:**

```
/u/g/image.png/$type/Grayscale
```

### 4. Practical Examples

Here are real-world examples combining multiple modifiers:

#### 4.1 Profile Picture Processing

Auto-orient, resize to 200x200, and enhance:

```
/u/g/profile.jpg/$autoOrient/$resize/200/200/!/$enhance
```

#### 4.2 Product Image Optimization

Resize maintaining aspect ratio, add white border, and normalize:

```
/u/g/product.png/$resize/800/600/m/$border/10/10/FFFFFF/$normalize
```

#### 4.3 Vintage Photo Effect

Apply sepia tone and slight blur for aged look:

```
/u/g/photo.jpg/$sepia/$blur/1/0.5
```

#### 4.4 Artistic Rendering

Convert to charcoal sketch and adjust contrast:

```
/u/g/landscape.jpg/$charcoal/2/$contrast/1.3
```

#### 4.5 Watermarked Image

Resize and add text watermark:

```
/u/g/photo.jpg/$resize/1200/800/m/$drawText/20/760/Copyright2024/FFFFFF/24
```

### 5. Best Practices

#### 5.1 Performance Optimisation

* **Leverage caching:** The Media Server automatically caches transformed images, reducing CPU usage on subsequent requests
* **Chain modifiers efficiently:** Combine multiple operations in a single request rather than making sequential requests
* **Use appropriate sizes:** Don't request unnecessarily large images; resize to the actual display size

#### 5.2 Image Quality

* **Start with high-quality sources:** Upload high-resolution original images for best transformation results
* **Test modifier combinations:** Some modifiers work better together than others; experiment to find optimal results
* **Use autoOrient first:** Always apply `$autoOrient` before other transformations for mobile uploads

#### 5.3 Security Considerations

* **Public vs Managed Server:** The default Media Server allows anonymous read access. For sensitive content, use the managed server with permission-based and time-bound access
* **Validate inputs:** When constructing URLs programmatically, validate user inputs to prevent injection attacks
* **Use SHA naming:** The SHA-based file naming prevents duplication and maintains version integrity

#### 5.4 Common Pitfalls

* **Overusing blur:** Large blur values can make images unrecognizable; start with small values
* **Ignoring aspect ratio:** Using exact resize (!) can distort images; prefer maintaining aspect ratio
* **Excessive rotation:** Large rotation angles may cause quality degradation; use `$autoOrient` when possible
* **Modifier order:** Some operations should be performed in specific order (e.g., crop before resize for better quality)

### 6. Quick Reference Table

Common modifier combinations for frequent use cases:

| Use Case            | Modifier Combination                                    |
| ------------------- | ------------------------------------------------------- |
| Mobile Photo Upload | `$autoOrient/$resize/800/600/m`                         |
| Square Thumbnail    | `$thumb/150`                                            |
| Vintage Effect      | `$sepia/$blur/1/0.5`                                    |
| Product Image       | `$resize/1200/1200/m/$border/5/5/FFFFFF/$enhance`       |
| Sketch Art          | `$charcoal/2/$type/Grayscale`                           |
| High Contrast B\&W  | `$type/Grayscale/$contrast/1.5/$normalize`              |
| Watermarked Photo   | `$resize/1920/1080/m/$drawText/20/1040/©2024/FFFFFF/18` |

### 7. Conclusion

The Media Server's image manipulation capabilities provide a powerful and flexible solution for dynamic image processing. By chaining modifiers in the URL, you can transform images on-the-fly without the overhead of storing multiple versions.

**Key takeaways:**

* Use URL-based modifiers for dynamic transformations
* Leverage automatic caching for performance
* Chain modifiers for complex effects
* Consider security with managed vs public servers
* Start with high-quality source images

### Additional Resources

* [Graphics Magick Documentation](http://www.graphicsmagick.org/)

