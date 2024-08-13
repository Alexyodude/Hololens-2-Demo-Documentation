### Summary

- **Complex Behaviour**: The `DroneBoid` class integrates complex behaviours like separation, cohesion, alignment, and following user inputs, demonstrating an advanced use of Unity's physics and Mixed Reality Toolkit's input system.
- **Performance Considerations**: The script uses potentially expensive operations such as searching for objects by tag and frequent vector calculations, which might impact performance in a large-scale application.

## `DroneBoid` Class Explanation

### Namespaces

- **`using UnityEngine;`**: Provides access to Unity's core classes and functionalities.
- **`using Microsoft.MixedReality.Toolkit.Input;`**: Provides access to Mixed Reality Toolkit's input functionalities, used to track user interactions through various pointers.

### Class Definition

```C#
public class DroneBoid : MonoBehaviour
```

- **`public class DroneBoid`**: Defines a class named `DroneBoid`.
- **`: MonoBehaviour`**: Inherits from `MonoBehaviour`, allowing this class to be attached to Unity GameObjects and utilize Unity's lifecycle methods like `Start` and `Update`.

### Variables

- **Public floats (`maxSpeed`, `maxForce`, etc.)**: Define the behaviour limits and radii for boid operations, such as speed, force, and distances for neighbour interactions.
- **Private `Vector3` variables (`velocity`, `acceleration`)**: Used to calculate and apply movement physics.
- **Private `Rigidbody` (`rb`)**: The physics component used to apply forces for movement.

### `Start` Method

```C#
void Start()
{
    velocity = Random.insideUnitSphere * maxSpeed;
    rb = GetComponent<Rigidbody>();

    if (rb == null)
    {
        Debug.LogError("Rigidbody component not found on this GameObject");
    }
}
```

- **Initialization**:
    
    - **`velocity`**: Initializes with a random direction and magnitude limited by `maxSpeed`.
    - **`rb`**: Attempts to retrieve the `Rigidbody` component attached to the same GameObject.
- **Error Handling**:
    
    - Checks if `rb` is not null to ensure the script will function properly, logging an error if the component is missing.

### `Update` Method

```C#
void Update()
{
    List<GameObject> drones = new List<GameObject>(GameObject.FindGameObjectsWithTag("Destroy"));

    Vector3 separation = Separate(drones);
    Vector3 cohesion = Cohere(drones);
    Vector3 alignment = Align(drones);
    Vector3 userFollow = FollowUser();

    separation *= 2.0f;
    cohesion *= 1.0f;
    alignment *= 1.0f;
    userFollow *= 1.5f;

    acceleration = separation + cohesion + alignment + userFollow;
    velocity += acceleration * Time.deltaTime;
    velocity = Vector3.ClampMagnitude(velocity, maxSpeed);

    ApplyForce(velocity);

    if (velocity.sqrMagnitude > 0.01f)
    {
        transform.rotation = Quaternion.LookRotation(velocity);
    }
}
```

- **Dynamic Behavior**:
    - **Boid Functions**: Calculates forces from separate, cohesion, alignment, and user follow behaviors.
    - **Force Application**: Accumulates forces into `acceleration`, modifies `velocity`, and applies it via `ApplyForce`.

### Boid Behaviors (Methods like `Separate`, `Cohere`, `Align`, `Seek`)

- **Purpose**: Each function implements part of the boid flocking algorithm:
    - **`Separate`**: Avoids crowding by maintaining a minimum distance between each drone.
    - **`Cohere`**: Moves towards the average position of nearby drones to stay together.
    - **`Align`**: Aligns velocity with nearby drones to match their speed and direction.
    - **`Seek`**: Steers towards a target position.
- **Implementation**:
    - Each function calculates a steering force based on the boids' current positions and velocities, and these forces are combined to determine the drone's movement each frame.

### `FollowUser` Method

```C#
Vector3 FollowUser()
{
    var pointers = PointerUtils.GetPointers<IMixedRealityPointer>();
    foreach (var pointer in pointers)
    {
        if (pointer.Controller != null && pointer.IsInteractionEnabled)
        {
            Vector3 seekForce = Seek(pointer.Result.Details.Point);

            if (IsNaN(seekForce)) seekForce = Vector3.zero;

            return seekForce;
        }
    }
    return Vector3.zero;
}
```

- **User Interaction**:
    - Tracks user input through Mixed Reality Toolkit's pointers and guides the drone towards the pointed location.

### Utility Functions (`ApplyForce`, `IsNaN`)

- **`ApplyForce`**: Applies a force to the drone's `Rigidbody`, considering physics.
- **`IsNaN`**: Checks if a vector contains invalid (NaN) values to prevent errors in physics calculations.