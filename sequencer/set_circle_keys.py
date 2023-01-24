# For UE5.0.3

def get_selected_actor( ) -> None:
    """
    Get selected actors and return the first one. 
    The UE module probably will be replaced by another one in the future
    """
    selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()
    if selected_actors:
        return selected_actors[0]
    return None

def find_spawnable_by_actor_name( actor_name ) -> None:
    """
    Get the spawnable of the current level sequence for the given actor name(label)
    Repalce get_current_level_sequence with get_focused_level_sequence should be working as well
    """
    level_sequence = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()
    spawnables = level_sequence.get_spawnables()

    for spawnable in spawnables :
        if spawnable.get_display_name() == actor_name :
            return spawnable
    return None
    
def get_transform_track( spawnable ) -> None:
    """
    Get the transform track of the given spawnable
    """
    tracks = spawnable.get_tracks()
    for track in tracks:
        if track.get_display_name() == 'Transform':
            return track
    return None
        
def get_location_and_rotation_channels( track ) -> dict:
    """
    Get location and rotation channels
    """
    loc_rot_dict = {}
    sections = track.get_sections()
    for section in sections:
        for channel in section.get_all_channels():
            if channel.channel_name == 'Location.X':
                loc_rot_dict['Location.X'] = channel
            elif channel.channel_name == 'Location.Y':
                loc_rot_dict['Location.Y'] = channel
            elif channel.channel_name == 'Location.Z':
                loc_rot_dict['Location.Z'] = channel
            elif channel.channel_name == 'Rotation.X':
                loc_rot_dict['Rotation.X'] = channel
            elif channel.channel_name == 'Rotation.Y':
                loc_rot_dict['Rotation.Y'] = channel
            elif channel.channel_name == 'Rotation.Z':
                loc_rot_dict['Rotation.Z'] = channel
    return loc_rot_dict

def set_circle_keys( world_center, start_frame, end_frame, frame_stride ) -> None:
    """
    Set keys along the circle constructed with the given arguments
    """
    selected_actor = get_selected_actor()
    if not selected_actor:
        unreal.log_warning( 'No selected actor' )
        return None

    actor_label = selected_actor.get_actor_label()
    spawnable = find_spawnable_by_actor_name( actor_label )
    if not spawnable:
        unreal.log_warning( 'Cannot find spawnable' )
        return None

    track = get_transform_track( spawnable )
    if not spawnable:
        unreal.log_warning( 'Cannot get Transform track' )
        return None

    loc_rot_dict = get_location_and_rotation_channels( track )
    if len(loc_rot_dict) != 6:
        unreal.log_warning( 'Cannot get all location and rotation channels' )
        return None

    actor_location = selected_actor.get_actor_location()
    actor_rotation = selected_actor.get_actor_rotation()
    dir = actor_location - world_center
    radius = dir.length()

    frame = end_frame
    frame_range = end_frame - start_frame
    num_keys = frame_range/frame_stride
    degree_stride = 360 / num_keys
    degree = degree_stride
    rot_yaw = actor_rotation.yaw
    while frame >= start_frame: 
        new_loc = unreal.MathLibrary.rotate_angle_axis(dir, degree, unreal.Vector(0,0,1))
        new_loc = new_loc + world_center
        degree = degree + degree_stride

        frame_number = unreal.FrameNumber(frame)
        frame = frame - frame_stride
     
        new_loc_key_x = loc_rot_dict['Location.X'].add_key( frame_number, new_loc.x )
        new_loc_key_y = loc_rot_dict['Location.Y'].add_key( frame_number, new_loc.y )
        #
        rot_yaw = rot_yaw + degree_stride
        new_rot_key_yaw = loc_rot_dict['Rotation.Z'].add_key( frame_number, rot_yaw )

# Example: select a camera in the scene and run this:
#center = unreal.Vector() # world center 0 0 0
#set_circle_keys( center, 0, 600, 40 ) 