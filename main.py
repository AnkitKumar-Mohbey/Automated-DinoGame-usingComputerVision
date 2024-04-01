import cv2
import cvzone
import numpy as np
import pyautogui
form cvzone.FPS import FPS
from mss import mss

def capture_screen_region_opencv(x, y, desired_width, desired_height):
  screenshot = pyautogui.screenshot(region=(x, y, desired_width, desired_height))
  screenshot = np.array(screenshot)
  screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
  return screenshot

