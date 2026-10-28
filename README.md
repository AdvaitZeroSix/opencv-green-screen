# OpenCV Green Screen

A real-time green screen (chroma key) effect in Python. Any green area in your webcam feed is replaced with a background image of your choice.

## How it works

1. Grab one frame and resize `background.jpeg` to match it.
2. For every frame, convert it to HSV colour space and mask the pixels in a green range (hue 25 to 95).
3. Clean the mask with a morphological open and dilate to remove speckle.
4. Keep the camera pixels where the mask is empty, take the background where it is set, and add the two together.

It uses plain colour masking, so it needs no GPU and no trained model. It is a small demo: the green range is fixed in `main.py`, so you may need to adjust it for your lighting.

## Requirements

- Python 3.8 or newer
- A webcam
- A green cloth or green wall behind you

## Run it

```bash
pip install -r requirements.txt
python main.py
```

Press `q` to quit.

## Use your own background

Replace `background.jpeg` with any JPG or JPEG image of your own, keeping the same file name, and run it again. No code changes are needed.
