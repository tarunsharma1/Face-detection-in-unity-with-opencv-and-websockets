# Face-detection-in-unity-with-opencv-and-websockets
Face detection in unity using opencv and .net sockets to send frames. Also includes the python server file which is to be run.
Now since every frame is being streamed to opencv, alot can be done like face detection, face recognition, object recognition using machine learning etc.
All opencv code is present in the python server file itself.


1.you need opencv first...so google how to install...a blog that might be useful is 
http://www.daveperrett.com/articles/2010/12/14/face-detection-with-osx-and-python/

2.To the player object in unity, attach the script screencapture.cs

3.Keep the haar_frontalface_default.xml in the same location as python_tcp_server.py

4.run python_tcp_server.py

5.run unity

6. In unity create a 3D object example cube, drag a picture of the human into unity and then onto the cube object in the window. The face should appear on the cube.

7. When the cube (face) is visible, emit a sound or something..right now its Debug.Log("face");
