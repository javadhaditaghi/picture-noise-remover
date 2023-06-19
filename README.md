# Picture Noise Remover

Picture Noise Remover is a web application built with Flask that allows users to remove noise from their pictures. It provides a simple and effective solution to enhance the visual quality of photos by reducing graininess and unwanted artifacts.

## Features

- Upload multiple pictures at once.
- Remove noise from the uploaded pictures.
- Display the resulting image after noise removal.
- Automatically remove the uploaded pictures after the result page is closed.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python (version 3.6 or later)
- OpenCV (cv2) library
- Flask library
- Numpy

## Installation

1. Clone the repository to your local machine.

2. Navigate to the project directory:

3. Install the required Python packages using pip:



## Usage

1. Start the Flask server:

2. Open your web browser and visit `http://localhost:5000` to access the application.

3. Select the pictures you want to remove noise from by clicking the "Select Pictures" button and choosing the desired files.

4. Click the "Submit" button to process the pictures and remove noise.

5. The resulting image will be displayed on the result page.

6. Close the result page, and the uploaded pictures will be automatically removed from the `static` folder.

## Customization

- You can customize the appearance of the web application by modifying the HTML templates (`index.html` and `result.html`) and the CSS styles (`style.css`).





