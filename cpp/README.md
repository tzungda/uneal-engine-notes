# set ini into
GConfig->SetString(TEXT("CategoryName"), TEXT("ItemName"), *ItemValue, IniFilePath );

# update to the ini file
GConfig->Flush( false, ShotInfoFile);

# normalize the ini file path
FConfigCacheIni::NormalizeConfigIniPath( FString::Printf(TEXT("%s%s/%s.ini"), *FPaths::GeneratedConfigDir(), ANSI_TO_TCHAR(FPlatformProperties::PlatformName()), TEXT("FileName")) );