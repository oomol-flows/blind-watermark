# Blind Watermark

A powerful image watermarking solution that lets you secretly embed and extract text messages in images without visibly altering them.

## What is Blind Watermarking?

Blind watermarking is a technique that hides information inside images in a way that's completely invisible to the human eye. Unlike traditional watermarks that you can see, blind watermarks are embedded into the mathematical structure of the image itself. This makes them perfect for:

- **Copyright protection** - Prove ownership of your images
- **Content authentication** - Verify if an image has been tampered with
- **Secure messaging** - Hide messages in plain sight
- **Digital forensics** - Track image origins and modifications

## How It Works

This project uses advanced mathematical techniques (DWT-DCT-SVD) to embed text information into images. The watermark survives common image operations like:
- Compression (JPEG, PNG)
- Resizing and cropping
- Basic image editing
- Format conversion

## Available Blocks

### 🔹 Add Text Water Mark
**Purpose**: Embeds hidden text messages into your images

**What you need**:
- An image file (JPEG, PNG, etc.)
- The text message you want to hide
- Optional: Output folder for the watermarked image

**What you get**:
- A new image that looks identical to the original
- The image now contains your hidden message
- Technical parameters needed for extraction

**Use cases**:
- Add copyright information to your photos
- Embed contact details in portfolio images
- Hide secret messages in images
- Mark images for tracking purposes

### 🔍 Extract Text Water Mark
**Purpose**: Reveals hidden text messages from watermarked images

**What you need**:
- A watermarked image file
- Technical parameters from the watermarking process

**What you get**:
- The hidden text message that was embedded in the image

**Use cases**:
- Verify ownership of copyrighted images
- Retrieve hidden information from images
- Authenticate image sources
- Decode secret messages

## Complete Workflow Example

1. **Start with your original image** - Any photo or image you want to protect
2. **Add your watermark** - Use the "Add Text Water Mark" block to embed your message
3. **Share the watermarked image** - The image looks unchanged but contains your hidden information
4. **Extract when needed** - Use the "Extract Text Water Mark" block to reveal the hidden message

## Real-World Applications

### For Photographers
- Protect your work by embedding copyright notices
- Track unauthorized use of your images
- Prove ownership in legal disputes

### For Businesses
- Brand protection for product images
- Secure document authenticity
- Internal image tracking systems

### For Security Professionals
- Digital forensics and investigation
- Secure communication channels
- Evidence authentication

### For Content Creators
- Protect artwork and designs
- Track image distribution
- Maintain attribution chains

## Key Benefits

- **Invisible Protection** - Watermarks are completely invisible to viewers
- **Robust Technology** - Survives common image processing operations
- **Easy to Use** - Simple drag-and-drop interface in OOMOL
- **Versatile** - Works with various image formats
- **Secure** - Uses advanced cryptographic techniques

## Getting Started

1. Import this package into your OOMOL workspace
2. Create a new flow using the provided blocks
3. Upload your image and enter your watermark text
4. Run the workflow to create your protected image
5. Use the extraction block anytime to verify the watermark

No programming knowledge required - just drag, drop, and configure!

## Technical Foundation

Built on proven mathematical methods:
- **DWT (Discrete Wavelet Transform)** - Analyzes image frequencies
- **DCT (Discrete Cosine Transform)** - Processes image blocks
- **SVD (Singular Value Decomposition)** - Embeds data robustly

These techniques ensure your watermarks are both invisible and durable.