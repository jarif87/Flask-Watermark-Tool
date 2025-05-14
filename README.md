# ImageWatermarker

A Flask-based web application to add watermarks to images. Users can upload an image and apply either a logo watermark (centered with red guiding lines) or a text watermark (bottom-right in red). This app is particularly useful for watermarking medical images, such as lung disease X-rays (e.g., `lung_scc`, `lung_n`, `lung_aca`), to ensure proper attribution or branding.

## Features
- Upload an image and apply a logo or text watermark.
- Logo watermark: Centered on the image with red lines indicating the placement.
- Text watermark: Positioned at the bottom-right corner in red.
- Modern UI with a gradient background, glassmorphism effects, and animations using Tailwind CSS.
- Preview section to display the watermarked image.
- Success/error messages for user feedback.

## Directory Structure
```
ImageWatermarker/
├── static/
│   ├── style.css        # Custom styles for the UI
│   └── uploads/        # Directory to store watermarked images
├── templates/
│   └── index.html      # HTML template for the web interface
└── app.py              # Flask application with watermarking logic
└── README.md           # Project documentation

```


## Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/<your-username>/ImageWatermarker.git
   cd ImageWatermarker

1. **Create a Virtual Environment (Optional but recommended)**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. **Install Dependencies** 

```
pip install flask pillow opencv-python numpy
```
3. **Run the Application**
```
python app.py
```

# Usage
* Upload an Image: Click "Browse" to upload an image (e.g., a lung X-ray).

## Choose Watermark Type:
- Logo Watermark: Select the "Logo Watermark" option and upload a logo image. The logo will be centered with red guiding lines.

- Text Watermark: Select the "Text Watermark" option, enter your text, and it will appear in red at the bottom-right.

- Apply Watermark: Click "Apply Watermark" to process the image.

- Preview: View the watermarked image in the preview section.

- Feedback: Success or error messages will appear as green/red alerts.

# Dependencies
- Flask: Web framework for the app.

- Pillow: Image processing for loading and saving images.

- OpenCV (opencv-python): Applying watermarks to images.

- NumPy: Array operations for image processing.


# Notes
- The app uses Tailwind CSS (via CDN) for styling, with additional custom styles in static/style.css.

- Watermarked images are saved in static/uploads/ with randomly generated filenames.

- There’s no default placeholder image; the preview section shows a message until an image is watermarked.




