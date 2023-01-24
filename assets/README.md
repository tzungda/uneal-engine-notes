### Get all assets in, eg. path = /Game/MyFolder
assets = unreal.AssetRegistryHelpers.get_asset_registry().get_assets_by_path( path, recursive = True )

### Asset type
asset.get_class().get_name() #.eg 'Sequencer', 'World'

### Get asset path
asset_path = assets[i].package_name

### Load level
unreal.EditorLoadingAndSavingUtils.load_map( asset_path )

### Save level
unreal.EditorAssetLibrary.save_asset( asset_path, only_if_is_dirty=True )

### Get asset name
assets[i].asset_name 
