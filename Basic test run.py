from ursina import *

app = Ursina()

# Create a 3D cube as the target object (player or character)
player = Entity(model='cube', color=color.orange)

# Set the initial camera position for a top-down perspective
camera.position = (0, 30, -30)  # Set the initial camera position
camera.rotation = (45, 0, 0)   # Set the initial camera rotation (no rotation on z-axis)

# Set the camera to orthographic mode
# camera.orthographic = True

# Set the initial orthographic camera size and minimum/maximum FOV values
initial_fov = 20
min_fov = 10
max_fov = 50
camera.fov = initial_fov

# Create the ground plane with a larger texture scale
ground = Entity(model='plane', scale=(10, 1, 10), color=color.green, texture='white_cube', texture_scale=(10, 10))

# Variable to control the camera panning speed
panning_speed = 30  # Adjust this value for the desired panning speed
rotation_speed = 30 # Adjust this value for the desired rotation speed

# Camera offset to follow the player
camera_offset_pos = (0, 30, -30)
camera_offset_rot = (45, 0, 0)


# Enable or disable camera following
follow_player = True
player_moving = False

def update():
    global initial_fov, follow_player, player_moving

    # Check if the player is moving
    if held_keys['a'] or held_keys['d'] or held_keys['w'] or held_keys['s']:
        player_moving = True
    else:
        player_moving = False

    # Basic player movement (you can replace this with your game logic)
    if held_keys['a']: player.x -= 1 * time.dt
    if held_keys['d']: player.x += 1 * time.dt
    if held_keys['w']: player.z += 1 * time.dt
    if held_keys['s']: player.z -= 1 * time.dt

    # Check if the right mouse button is held down for manual panning
    if held_keys['right mouse']:
        # Disable camera following during manual panning
        follow_player = False
        camera.x += mouse.velocity.x * panning_speed
        camera.y += mouse.velocity.y * panning_speed
    else:
        # Enable camera following when the right mouse button is released
        follow_player = player_moving


    # Rotate the camera based on cursor movement when Shift+left click is pressed
    if held_keys['left mouse']:
        follow_player = False
        camera.rotation_y += mouse.velocity.x * rotation_speed
        camera.rotation_x -= mouse.velocity.y * rotation_speed  # Invert rotation direction for vertical movement
    else:
        # Enable camera following when the right mouse button is released
        follow_player = player_moving

    # Update the camera's position to follow the player if enabled
    if follow_player:
        camera.position = camera_offset_pos

        camera.rotation = camera_offset_rot        

def input(key):
    global follow_player

    # Control the camera FOV using the "scroll up" and "scroll down" keys
    if key == 'scroll up':
        camera.fov -= 5
    if key == 'scroll down':
        camera.fov += 5

    # Clamp FOV to the specified range
    camera.fov = clamp(camera.fov, min_fov, max_fov)

    if key == 'e':
        #reset camera
        camera.position = (0, 30, -30)  # Set the initial camera position
        camera.rotation = (45, 0, 0)   # Set the initial camera rotation (no rotation on z-axis)

app.run()


