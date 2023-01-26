# create a new usd stage actor
actor_location = unreal.Vector( 0.0, 0.0, 0.0 )
actor_rotation = unreal.Rotator( 0.0, 0.0, 0.0 )
new_usd_stage_actor = unreal.EditorLevelLibrary.spawn_actor_from_class( unreal.UsdStageActor, actor_location, actor_rotation )