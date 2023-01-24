### Get selected actors
selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

### Repalce get_current_level_sequence with get_focused_level_sequence should be working as well
level_sequence = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()
spawnables = level_sequence.get_spawnables()

### Get Tracks
tracks = spawnable[i].get_tracks()

### Get Sections
sections = tracks[i].get_sections()

### Get Channels
channels = section[i].get_all_channels()
channels[i].channel_name #eg. 'Location.X', 'Rotation.Y'...etc

### Add Keys
frame_number = unreal.FrameNumber(frame)
new_key = channels[i].add_key( frame_number, key_value )

### Get Key Type
new_key.get_class().get_name() #eg. 'MovieSceneScriptingActualFloatKey' 

### Set Key Tangent
new_key.set_tangent_mode( key.get_tangent_mode() )
new_key.set_leave_tangent( key.get_leave_tangent() )
new_key.set_arrive_tangent( key.get_arrive_tangent() )
new_key.set_arrive_tangent_weight( key.get_arrive_tangent_weight() )
new_key.set_interpolation_mode( key.get_interpolation_mode() )
new_key.set_tangent_weight_mode( key.get_tangent_weight_mode() )
new_key.set_leave_tangent_weight( key.get_leave_tangent_weight() )



