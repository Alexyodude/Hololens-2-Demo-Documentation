Download Unity and install the lts (latest) version of the game engine. make sure to select universal UWP(windows platform) and windows when downloading the version.

Follow the tutorial below:
[XR Step-by-Step 2023! Hololens 2: Setting up your Project in Unity 2022 + MRTK 2.8.3 + Visual Studio 2022 – Lance Larsen – Microsoft MVP – Hololens / VR / AR](http://www.lancelarsen.com/xr-step-by-step-2023-hololens-2-setting-up-your-project-in-unity-2022-mrtk-2-8-3-visual-studio-2022/)

- **(Unity Hub)** Click **Projects** -> click **New Project**

![[Pasted image 20240813092828.png]]

- **(Unity Hub)** Click **Editor Version** -> Click the newest **Unity** version

![[Pasted image 20240813092946.png]]

- (**Unity Hub)** Click **3D** template -> Set **Project Name** -> Choose **Location** -> Click **Create Project**

![[Pasted image 20240813093115.png]]

- **(Unity Hub)** Click on the new project!

![[Pasted image 20240813093133.png]]

- We need to change the project to build for a Hololens…
- **(Unity Toolbar) File** -> **Build Settings…**

![[Pasted image 20240813093557.png]]

1. Click **Add Open Scenes** (this adds our current Unity scene to the **Scenes in Build** and checks it)
2. Switch **Platform** to **Universal Windows Platform**
3. Switch **Architecture** -> **ARM 64-bit**
4. Switch **Minimum Platform Version** -> **10.0.18362.0** (or newer) — if you don’t see this version, then you need to update your **Windows SDK** see previous blog post
5. Check **Copy References** (when we open up Visual Studio, this makes intellisense, etc. work!)
6. Click **Switch Platform**

![[Pasted image 20240813093651.png]]

- Run **MixedRealityFeatureTool.exe**
    - Open the folder where you saved your **Mixed Reality Feature Tool** to find the exe

![[Pasted image 20240813093656.png]]Pick **Start**

![[Pasted image 20240813093713.png]]

1. Set the **Project Path** to your new **Unity** project
2. Click **Discover Features**

![[Pasted image 20240813093721.png]]

1. Expand **Platform Support**
2. Check **Mixed Reality OpenXR Plugin**
3. Click **Get Features**

![[Pasted image 20240813093925.png]]

- Click **Import**

![[Pasted image 20240813093932.png]]

- Click **Approve**
![[Pasted image 20240813093937.png]]

- Click **Exit**

![[Pasted image 20240813093943.png]]

- **(Unity)** Open your Unity project – you will see that it’s importing the **Mixed Reality OpenXR Plugin**
- Click **Yes** to use the new input system, and **Unity** will restart

![[Pasted image 20240813094000.png]]

- **(Unity Toolbar)** Note that we now have a new **Mixed Reality** menu!

![[Pasted image 20240813094007.png]]

- **(Unity Toolbar) Edit** -> **Project Settings**

![[Pasted image 20240813094016.png]]

We need to configure our **Universal Windows Platform XR Plug-in Management**

1. ****(Project Settings)**** Click **XR Plug-in Management**
2. Click **Universal Windows Platform settings** tab
3. Check **OpenXR**
4. Check **Microsoft HoloLens feature group**
5. Click the **Warning Icon**

![[Pasted image 20240813094023.png]]

- Click **Fix All**

![[Pasted image 20240813094030.png]]

- Give Unity a little bit to make all fixes, and you’ll likely be left with **“At least one interaction profile must be added…”** -> Click **Edit**

![[Pasted image 20240813094039.png]]

- (**Project Settings -> OpenXR)** Click the “+” under **Interaction Profiles**

![[Pasted image 20240813094047.png]]

- Add **Eye Gaze Interaction Profile**
- Add **Microsoft Hand Interaction Profile**

![[Pasted image 20240813094053.png]]

- Next to **Eye Gaze Interaction Profile**-> Click the **Warning Icon**

![[Pasted image 20240813094058.png]]

- Click **Fix All**

![[Pasted image 20240813094104.png]]

Now we need to do the same setup for the **Windows, Mac, Linux XR Plug-in Management**

1. **(Project Settings)** Click **XR Plug-in Management**
2. Click **Windows, Mac, Linux** **settings** tab
3. Check **OpenXR**
4. Check **Microsoft HoloLens feature group**
5. Click the **Warning Icon**

![[Pasted image 20240813094109.png]]

- Click **Edit**

![[Pasted image 20240813094114.png]]

- Add **Eye Gaze Interaction Profile**
- Add **Microsoft Hand Interaction Profile**

![](http://www.lancelarsen.com/wp-content/uploads/2023/03/image-52-1024x576.png)

![[Pasted image 20240813094133.png]]

- **(Unity Toolbar) Mixed Reality** -> **Project** -> **Apply recommended project settings for HoloLens 2**

![[Pasted image 20240813094142.png]]

- Click **Fix All**

![[Pasted image 20240813094149.png]]

- Click **Edit**

![[Pasted image 20240813094210.png]]

- Look for all issues to be marked as good!

![[Pasted image 20240813094218.png]]

Now we need to add the MRTK files into our project – note, you **-can-** add MRTK to your project via the **Mixed Reality Feature Tool** however I’ve found that this doesn’t always add everything, i.e. such as all the MRTK Examples code – but dragging them in is easy and has always worked for me!

1. **(Unity)** Click **Project** tab
2. Click **Assets** folder
3. Drag **Microsoft.MixedReality.Toolkit.Unity.Foundation.2.8.3.unitypackage** into the **Assets** section (as shown by arrow)

![[Pasted image 20240813094228.png]]

- **(Import Unity Package)** Click **Import**

![[Pasted image 20240813094235.png]]

- Back to **Unity**, the **MRTK Project Configurator** should appear
- **(MRTK Project Configurator)** Click **Apply Settings**

![[Pasted image 20240813094406.png]]

- **(Project Settings)** At this point everything -should- be good, but if anything needs to be fixed it will be highlighted

![[Pasted image 20240813094412.png]]

- **(MRTK Project Configurator)** Click **Apply**

![[Pasted image 20240813094427.png]]

- Click **Next**

![[Pasted image 20240813094433.png]]

- Click **Import TMP Essentials** (TextMesh Pro is needed by MRTK and is generally highly useful!)

![[Pasted image 20240813094444.png]]

- Click **Done**

![[Pasted image 20240813094451.png]]

- Now add the other **MRTK Unity Packages** (one at a time) into the **Assets** section
    - **[Recommended]** Microsoft.MixedReality.Toolkit.Unity.Tools.2.8.3.unitypackage
    - **[**Recommended**]** Microsoft.MixedReality.Toolkit.Unity.Examples.2.8.3.unitypackage
    - **[**Recommended**]** Microsoft.MixedReality.Toolkit.Unity.Extensions.2.8.3.unitypackage
    - **[Optional]** Microsoft.MixedReality.Toolkit.Unity.TestUtilities.2.8.3.unitypackage
- When you’re all done, you’ll see the following folders in your **Assets**!

![[Pasted image 20240813094459.png]]

Then connect to the Hololens 2 remotely by going in the unity project then Mixed Reality > Remoting > Holographic Remoting for Play Mode.

Inside the Hololens 2 open the App named "Holographic Remoting". Type the ip address seen inside the app into the settings inside "Holographic Remoting for Play Mode" in the unity project. Leave the port as is and make sure to press "enable holographic remoting for play mode". 

This should setup the Hololens 2 to be play tested. 

The current project features and improvements are described in [[Version]].  