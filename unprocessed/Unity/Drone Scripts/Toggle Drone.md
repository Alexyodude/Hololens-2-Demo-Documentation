### Summary

- **Drone Management**: The class allows for activating and deactivating drones, which follow the user within certain conditions.
- **Explosion Handling**: It includes functionality to handle drone destruction, complete with an explosion effect.
- **Dynamic Interaction**: The drones dynamically adjust their positions relative to the user during gameplay.

## `ToggleDrone` Class Explanation

### Namespaces

```C#
using System;
using System.Collections.Generic;
using UnityEngine;
```

- **`using System;`**: Provides basic data types and functionalities.
- **`using System.Collections.Generic;`**: Provides access to generic collections like `List`.
- **`using UnityEngine;`**: Provides access to Unity-specific classes and methods.

### Class Definition

```C#
public class ToggleDrone : MonoBehaviour
```

- **`public`**: Makes the class accessible from other scripts and visible in Unity's Inspector.
- **`class ToggleDrone`**: Defines a class named `ToggleDrone`.
- **`: MonoBehaviour`**: Inherits from `MonoBehaviour`, allowing the script to be attached to Unity GameObjects and access Unity lifecycle methods like `Start` and `Update`.
### Variables

- **`public GameObject explosion;`**: Reference to the explosion prefab that will be instantiated when a drone is destroyed.
- **`public GameObject DronePrefab;`**: Reference to the drone prefab that will be instantiated in the scene.
- **`public GameObject user;`**: Reference to the user (likely the player or a central object) that the drones will follow.
- **`private List<GameObject> Drones = new List<GameObject>();`**: A list to keep track of the instantiated drone GameObjects.
- **`public int numDrone = 10;`**: Number of drones to spawn when drones are activated.
- **`Boolean isDrone = false;`**: A flag to determine whether drones are currently active or not.

### `Update` Method

```C#
private void Update()
{
    if (isDrone)
    foreach (GameObject drone in Drones)
    {
        if (drone != null)
        {
            if (Vector3.Distance(drone.transform.position, user.transform.position) > 4 || drone.transform.position.y < -0.2)
            {
                drone.transform.position = Vector3.MoveTowards(drone.transform.position, user.transform.position, 0.1f);
            }
        }
    }
}

```
- **Purpose**: Continuously checks the state of drones and updates their positions to move them towards the user.
- **Drone Movement**:
    - The drones move towards the user's position if they are too far (more than 4 units away) or if they are below a certain Y-axis threshold (`y < -0.2`).
    - The drones move with a speed of `0.1f` units per frame.
- **`isDrone`**: Only checks and moves drones if `isDrone` is `true`.

### `OnDrone` Method

```C#
public void OffDrone()
{
    foreach (GameObject drone in Drones)
    { 
        Destroy(drone); 
    }
    Drones.Clear();
    isDrone = false;
}
```

- **Purpose**: Deactivates all active drones and clears the `Drones` list.
- **Drone Removal**:
    - Iterates through the `Drones` list, destroying each drone GameObject.
    - Clears the `Drones` list to remove all references to the destroyed drones.
- **`isDrone`**: Sets the flag to `false` to indicate that drones are no longer active.

### `droneDestroy` Method

```C#
public void droneDestroy(GameObject drone)
{
    Destroy(Instantiate(explosion, drone.transform.position, Quaternion.identity), 2f);
    drone.transform.position = user.transform.position + user.transform.forward * 0.5f;
}
```

- **Purpose**: Handles the destruction of a specific drone, including triggering an explosion effect.
- **Explosion Effect**:
    - Instantiates an explosion prefab at the drone's position.
    - The explosion is automatically destroyed after 2 seconds to clean up the scene.
- **Drone Position Reset**:
    - After triggering the explosion, the drone's position is reset to a point slightly in front of the user (`0.5f` units in the direction the user is facing).