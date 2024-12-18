### Version 0.1

![[Pasted image 20240807150758.png]]  

 - UI with toggle and press buttons:
 
    - [[Create Box]]
    - [[Toggle Enemy]]
    - [[Toggle Drone]]
    - [[Toggle Pistol]]
    - [[Toggle Mesh]]

- Box creation and destruction based on set boundary
- Enemies and drones are set before as public variables so it is constant
- Enemies spawn randomly on meshes with a normal vector roughly pointing up
- Enemy prefab humanoid asset provide a human target
- Enemies move in straight lines unless it collides with a mesh ([[Random Movement]])

    - Colliding results in a random direction to be selected
    - Enemies respawn if they leave the set boundary
    - Custom tag "Enemy" selected to differentiate object when collision is detected with another object

- Drone prefab asset provides more intuitive response for the user
- Drones move towards the user's ray pointer

    - Separation between the drones are provided by [[Drone Boid]] script
    - Custom tag "Destroy" selected to differentiate object when collision is detected with another object
    
- Mesh visibility changes between visible and [[Occlusion]]
- The pistol's relative position and orientation is used to instantiate the bullet

    -  Bullet has custom tag "Destroy" selected for enemy and weapon collision logic

Ideas to improve are listed here, "[[Improvements]]".