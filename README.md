# SpoilAlert

SpoilAlert is a project built upon Computer Vision and Data Engineering concepts.
The project uses GCP cloud stack for development.
For CV - YoLo v4 is the current version of the model architecture.

### Custom Dataset
ObjectClassification.ipynb - a colab notebook along with LabelImg was used to generate custom dataset

### Model Training
SpoilAlert.ipynb is a Colab notebook used to train the model and run inferences.
The train model will be exported with its weights , labels and config files to other edge devices or ML tools.

### blinkpy/
blinkpy was forked to create custom code to push videos from blink camera to GCP storage
blinkpy.py's download_videos and parse_ function was customized to accomodate push to the GCP.
