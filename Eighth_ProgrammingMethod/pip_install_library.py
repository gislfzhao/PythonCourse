# -*- coding: utf-8 -*-
import os
libs = {"numpy", "wheel", "jieba", "requests",
        "pyinstaller", "pygame"}
for lib in libs:
    try:
        # os.chdir(r"C:\Users\GISzhao\Desktop\PythonCourse")
        # print(os.getcwd())
        # os.system('cd')
        os.system(r"C:\Users\GISzhao\Desktop\PythonCourse\venv\Scripts\python.exe -m pip install " + lib)
        # if os.path.exists('dist'):
        #     print("Exists dist")
        print("Successful Install.")
    except BaseException as e:
        print("Failed", e.args)
