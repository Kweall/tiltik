import os
import unittest
from database import *

if flag:
    print("Базы данных нет")
else:
    print("База данных есть")

if len(os.listdir('runs/track/'+os.listdir('runs/track')[-1])) > 1:
    print('Видео есть')
else:
    print('Видео нет')