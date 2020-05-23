import os, base64
from flask import Flask, render_template, request, flash

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException
from msrest.authentication import CognitiveServicesCredentials

# Create a ComputerVisionClient instance for calling the Computer Vision API
vision_key = os.environ["VISION_KEY"]
vision_endpoint = os.environ["VISION_ENDPOINT"]
vision_credentials = CognitiveServicesCredentials(vision_key)
vision_client = ComputerVisionClient(vision_endpoint, vision_credentials)

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Display the image that was uploaded
        image = request.files["file"]
        uri = "data:image/jpg;base64," + base64.b64encode(image.read()).decode("utf-8")
        image.seek(0)

        # Use the Computer Vision API to extract text from the image
        lines = extract_text_from_image(image, vision_client)

        # Flash the extracted text
        for line in lines:
            flash(line)

    else:
        # Display a placeholder image
        uri = "/static/placeholder.png"

    return render_template("index.html", image_uri=uri)

# Function that extracts text from images
def extract_text_from_image(image, client):
    try:
        result = client.recognize_printed_text_in_stream(image=image)
        lines=[]

        if len(result.regions) == 0:
            lines.append("Photo contains no text to translate")

        else:
            for line in result.regions[0].lines:
                text = " ".join([word.text for word in line.words])
                lines.append(text)

        return lines

    except ComputerVisionErrorException as e:
        return ["Computer Vision API error: " + e.message]

    except:
        return ["Error calling the Computer Vision API"]

#Defining the about Page
@app.route("/about")
def about():
    flash("This is am error message")
    return render_template("about.html")
# returning the Contact us page
@app.route("/contact")
def contact():
     return render_template("templates/master.html", message="this is the contact")