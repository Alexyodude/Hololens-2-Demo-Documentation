### Summary

- **Instantiation and Removal**: Handles spawning and removing enemy GameObjects based on various conditions.
- **Spatial Awareness**: Uses MRTK’s spatial awareness to place enemies on mesh surfaces.
- **Enemy Management**: Manages the lifecycle of enemies, including spawning, tracking, and removal.

## `ToggleEnemy` Class Explanation

### Namespaces

```C#
using Microsoft.MixedReality.Toolkit.SpatialAwareness;
using Microsoft.MixedReality.Toolkit;
using UnityEngine;
using System.Linq;
using System.Collections.Generic;
using System;
```

- **`using Microsoft.MixedReality.Toolkit.SpatialAwareness;`**: Provides access to spatial awareness features in the Microsoft Mixed Reality Toolkit (MRTK).
- **`using Microsoft.MixedReality.Toolkit;`**: Includes core functionalities of MRTK.
- **`using UnityEngine;`**: Provides access to Unity-specific classes and methods.
- **`using System.Linq;`**: Provides LINQ query capabilities for data manipulation.
- **`using System.Collections.Generic;`**: Provides access to generic collections such as `List`.
- **`using System;`**: Provides basic data types and functions.

### Class Definition

```C#
public class ToggleEnemy : MonoBehaviour
```
- **`public`**: Allows the class to be accessible from other scripts and Unity's Inspector.
- **`class ToggleEnemy`**: Defines the class named `ToggleEnemy`.
- **`: MonoBehaviour`**: Inherits from `MonoBehaviour`, allowing the script to be attached to Unity GameObjects and access Unity lifecycle methods.

### Variables

- **`public GameObject EnemyPrefab;`**: Prefab for the enemy model that will be instantiated in the scene.
- **`public Transform Player;`**: Reference to the player GameObject for orientation and position-related calculations.
- **`public GameObject NormalIndicator;`**: Prefab for a normal indicator (not used in the provided code).
- **`public Transform Parent;`**: Transform to act as the parent for instantiated enemies.
- **`public int enemyTotal = 10;`**: Total number of enemies to spawn.
- **`private IMixedRealitySpatialAwarenessMeshObserver observer;`**: Interface for accessing spatial awareness mesh data.
- **`private int count = 0;`**: Counter used to control the spawning frequency of enemies.
- **`private int killCount = 0;`**: Keeps track of the number of enemies killed.
- **`public float killYBoundary = -10f;`**: Y-axis boundary below which enemies are considered "fallen" and should be removed.
- **`private List<GameObject> numberEnemies = new List<GameObject>();`**: List to keep track of active enemy GameObjects.
- **`public Boolean enemySpawn = true;`**: Boolean flag to control whether enemies should be spawned.
### `Start` Method

```C#
void Start()
{
    var spatialAwarenessService = CoreServices.SpatialAwarenessSystem;
    var dataProviderAccess = spatialAwarenessService as      IMixedRealityDataProviderAccess;
    observer = dataProviderAccess.GetDataProvider<IMixedRealitySpatialAwarenessMeshObserver>("OpenXR Spatial Mesh Observer");
    if (observer == null)
    {
        Debug.LogError("Failed to get the spatial awareness mesh observer!");
        return;
    }
}
```
- **Purpose**: Initializes the spatial awareness mesh observer.
- **Spatial Awareness Service**: Retrieves the spatial awareness system and accesses the mesh observer.
- **Error Handling**: Logs an error if the mesh observer cannot be obtained.
### `Update` Method

```C#
void Update()
{
    if (enemySpawn)
    {
        if (numberEnemies.Count < enemyTotal && count == 400)
        {
            RandomMeshNormalCheck();
        }
        if (count < 400)
        {
            count++;
        }
        CheckFallenEnemies();
    }
    else
    {
        foreach (GameObject enemy in numberEnemies)
        {
            RemoveEnemy(enemy);
        }
    }
}

```

- **Purpose**: Manages enemy spawning and checks for fallen enemies.
- **Enemy Spawning**: Spawns enemies when the count is 400 and fewer enemies than `enemyTotal` exist.
- **Enemy Removal**: Removes all enemies if `enemySpawn` is `false`.

### `EnemySpawnOn` Method

```C#
public void EnemySpawnOn()
{
    enemySpawn = true;
}
```

- **Purpose**: Enables enemy spawning by setting `enemySpawn` to `true`.

### `EnemySpawnOff` Method

```C#
public void EnemySpawnOn()
{
    enemySpawn = true;
}
```

- **Purpose**: Disables enemy spawning by setting `enemySpawn` to `false`.

### `RandomMeshNormalCheck` Method

```C#
public void RandomMeshNormalCheck()
{
    var meshes = observer.Meshes.Values;
    if (!meshes.Any())
    {
        Debug.LogWarning("No meshes available from the observer.");
        return;
    }

    int randomMeshIndex = UnityEngine.Random.Range(0, meshes.Count());
    var randomMeshObject = meshes.ElementAt(randomMeshIndex);

    if (randomMeshObject.Filter == null)
    {
        Debug.LogWarning("Mesh filter is null for the selected mesh object.");
        return;
    }

    Mesh mesh = randomMeshObject.Filter.sharedMesh;
    if (mesh == null)
    {
        Debug.LogWarning("Mesh is null for the selected mesh object.");
        return;
    }

    Vector3[] vertices = mesh.vertices;
    Vector3[] normals = mesh.normals;

    if (vertices.Length == 0 || normals.Length == 0)
    {
        Debug.LogWarning($"No vertices ({vertices.Length}) or normals ({normals.Length}) available in the selected mesh.");
        return;
    }

    List<int> floor = new List<int>();
    for (int i = 0; i < normals.Length; i++)
    {
        if (normals[i].y > 0.9 && vertices[i].y < Player.transform.position.y + 0.2)
        {
            floor.Add(i);
        }
    }
    if (floor.Count == 0)
    {
        Debug.LogWarning("No floor normals found in the selected mesh.");
        return;
    }

    int randomIndex = floor[UnityEngine.Random.Range(0, floor.Count)];
    Vector3 randomPosition = vertices[randomIndex];

    Vector3 worldPosition = randomMeshObject.Filter.transform.TransformPoint(randomPosition);
    Vector3 offSetWorldPosition = new Vector3(worldPosition.x, worldPosition.y + 0.5f, worldPosition.z);
    GameObject enemyInstance = Instantiate(EnemyPrefab, offSetWorldPosition, transform.rotation, Parent);
    numberEnemies.Add(enemyInstance);
}
```

- **Purpose**: Spawns enemies at random positions on the floor of randomly selected meshes.
- **Mesh Selection**: Chooses a random mesh from available meshes.
- **Position Calculation**: Finds valid floor positions based on mesh normals and vertices.
- **Instantiation**: Creates and positions the enemy GameObject in the scene.

### `RemoveEnemy` Method

```C#
public void RemoveEnemy(GameObject enemy)
{
    numberEnemies.Remove(enemy);
    Destroy(enemy);
}
```

- **Purpose**: Removes an enemy from the list and destroys the GameObject.

### `EnterRagdollState` Method

```C#
public void EnterRagdollState(GameObject enemy)
{
    Animator animator = enemy.GetComponent<Animator>();
    StarterAssets.RandomMovement randomMovement = enemy.GetComponent<StarterAssets.RandomMovement>();

    animator.enabled = false;
    randomMovement.enabled = false;
    StartCoroutine(DestroyAfterDelay(enemy, 5f));
}
```

- **Purpose**: Switches an enemy to a ragdoll state by disabling its `Animator` and movement scripts, then schedules destruction.
- **Ragdoll Effect**: Disables components to simulate ragdoll physics.
- **Destruction**: Calls `DestroyAfterDelay` coroutine to remove the enemy after a delay.

### `DestroyAfterDelay` Method

```C#
private System.Collections.IEnumerator DestroyAfterDelay(GameObject enemy, float delay)
{
    yield return new WaitForSeconds(delay);
    RemoveEnemy(enemy);
}
```

- **Purpose**: Coroutine to wait for a specified delay before removing the enemy from the scene.

### `EnemyKilled` Method

```C#
public void EnemyKilled()
{
    killCount++;
}
```

- **Purpose**: Increments the kill count when an enemy is killed.

### `getKillCount` Property

```C#
public int getKillCount
{
    get { return killCount; }
}
```

- **Purpose**: Provides read-only access to the current kill count.

### `CheckFallenEnemies` Method

```C#
private void CheckFallenEnemies()
{
    for (int i = numberEnemies.Count - 1; i >= 0; i--)
    {
        if (numberEnemies[i].transform.position.y < killYBoundary)
        {
            RemoveEnemy(numberEnemies[i]);
        }
    }
}
```

- **Purpose**: Checks if any enemies have fallen below a certain Y-axis boundary and removes them if necessary.