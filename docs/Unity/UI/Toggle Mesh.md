### Summary

- **Mesh Visibility Management**: The `ToggleMesh` class provides an interface for toggling the visibility of spatial meshes in a Mixed Reality environment.
- **Observer Utilization**: The class leverages the `IMixedRealitySpatialAwarenessMeshObserver` to control whether meshes are visible (`Visible`) or hidden but still interactive (`Occlusion`).
- **Integration with MRTK**: This class is integrated with the Mixed Reality Toolkit (MRTK), making it a useful component for applications that require dynamic control over spatial awareness features.

## `ToggleMesh` Class Explanation
### Namespaces

- **`using UnityEngine;`**: Provides access to Unity's core classes and functionalities.
- **`using Microsoft.MixedReality.Toolkit.SpatialAwareness;`**: Provides access to Mixed Reality Toolkit (MRTK) spatial awareness functionalities, specifically for handling spatial meshes.

### Class Definition

```C#
public class ToggleMesh : MonoBehaviour
```

- **`public class ToggleMesh`**: Defines a class named `ToggleMesh`.
- **`: MonoBehaviour`**: Inherits from `MonoBehaviour`, allowing this class to be attached to Unity GameObjects and to utilize Unity's lifecycle methods such as `Start` and `Update`.
### Variables

- **`private IMixedRealitySpatialAwarenessMeshObserver observer;`**: A private variable of type `IMixedRealitySpatialAwarenessMeshObserver` that will hold the reference to the mesh observer. This observer is responsible for managing spatial meshes in the Mixed Reality environment.

### `Start` Method

```C#
void Start()
{
    // Use CoreServices to quickly get access to the IMixedRealitySpatialAwarenessSystem
    var spatialAwarenessService = Microsoft.MixedReality.Toolkit.CoreServices.SpatialAwarenessSystem;

    // Cast to the IMixedRealityDataProviderAccess to get access to the data providers
    var dataProviderAccess = spatialAwarenessService as Microsoft.MixedReality.Toolkit.IMixedRealityDataProviderAccess;
    
    // Get the specific mesh observer by name
    observer = dataProviderAccess.GetDataProvider<IMixedRealitySpatialAwarenessMeshObserver>("OpenXR Spatial Mesh Observer");
}
```

- **Purpose**: The `Start` method is called when the script is first initialized. It sets up the reference to the spatial mesh observer so that the class can control the display of spatial meshes.
    
- **Accessing Spatial Awareness System**:
    
    - The `CoreServices.SpatialAwarenessSystem` is used to access the spatial awareness system provided by the MRTK.
    - This service is cast to `IMixedRealityDataProviderAccess` to gain access to various data providers, including mesh observers.
- **Retrieving the Mesh Observer**:
    
    - The script retrieves the specific mesh observer named "OpenXR Spatial Mesh Observer". This observer manages the spatial mesh data, including how and when the meshes are displayed.

### `MeshOn` Method

```C#
public void MeshOn()
{
    if (observer != null)
    {
        observer.DisplayOption = SpatialAwarenessMeshDisplayOptions.Visible;
        /* Debug.Log("Mesh display turned on.");
           Debug.Log(observer.DisplayOption);
           Debug.Log(observer.Name);*/
    }
}
```

- **Purpose**: This method turns on the visibility of the spatial meshes.
    
- **Visibility Control**:
    
    - Checks if the `observer` is not null (i.e., it has been successfully retrieved).
    - Sets the `DisplayOption` of the `observer` to `SpatialAwarenessMeshDisplayOptions.Visible`, making the spatial meshes visible in the Mixed Reality environment.
- **Optional Debugging**:
    
    - The commented-out `Debug.Log` statements can be used for debugging purposes to confirm that the mesh display has been turned on and to check the observer's current settings.

### `MeshOff` Method

```C#
public void MeshOff()
{
    if (observer != null)
    {
        observer.DisplayOption = SpatialAwarenessMeshDisplayOptions.Occlusion;
        /* Debug.Log("Mesh display turned off.");
           Debug.Log(observer.DisplayOption);
           Debug.Log(observer.Name);*/
    }
}
```

- **Purpose**: This method turns off the visibility of the spatial meshes by setting them to occlusion mode.
    
- **Occlusion Control**:
    
    - Similar to the `MeshOn` method, this checks if the `observer` is not null.
    - Sets the `DisplayOption` to `SpatialAwarenessMeshDisplayOptions.Occlusion`, which hides the spatial meshes from view but still allows them to interact with other objects (like occluding virtual objects).
- **Optional Debugging**:
    
    - The commented-out `Debug.Log` statements can be used to verify that the mesh display has been turned off and to check the observer's current settings.