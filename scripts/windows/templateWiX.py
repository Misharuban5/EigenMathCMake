'''
Note the GUID's must be set in dictionary before using template.
'''
TEMPLATE_MAP = { \
'appName'  : 'math',
'companyName' : 'math.test',
'guidPrefix' : '12345678-1234-1234-1234',

'upgradeGUID' : 'None',   # ids product (constant over upgrades)
'appExecutableGUID' : 'None',
'appStartMenuItemGUID' : 'None',

'version' : '0.0.1',
'mimetypeExtension' : 'pnl'
 }

'''
Not used:
'productGUID' : '12345678-1234-1234-1234-000000000000',
'''


SOURCE_FILENAME_TEMPLATE = r'''${appName}.wxs'''
INTERMEDIATE_FILENAME_TEMPLATE = r'''${appName}.wixobj'''
OUT_FILENAME_TEMPLATE = r'''${appName}_$version.msi'''


WIX_TEMPLATE = r'''<?xml version="1.0"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
    <Product Id="*" 
        UpgradeCode="$upgradeGUID" 
        Version="$version" 
        Language="1033" 
        Name="$appName" 
        Manufacturer="$companyName">
        
        <Package InstallerVersion="300" 
          Compressed="yes"/>
        <Media Id="1" 
          Cabinet="$appName.cab" 
          EmbedCab="yes" />
          
        <!-- app icon 
        I'm not sure whether the Id MUST be so: could it be 'ProductIcon' or 'ProductIcon.ico' ?
        Is there an icon bundled in the .exe (that the app displays on its title bar)?
        Distinct from this icon that the desktop uses to represent app and mimetype.
        -->
        <Icon Id="$appName.ico" SourceFile="$appName.ico"/>
        <Property Id="ARPPRODUCTICON" Value="$appName.ico"/>
        

        <!-- Step 1: Define the directory structure -->
        <Directory Id="TARGETDIR" Name="SourceDir">
          
          <Directory Id="ProgramFilesFolder">
            <!-- a folder under "c:/Program Files/".  Will Windows allow without a subfolder? -->
            <Directory Id="AppRootDir" Name="$appName"/>
          </Directory>
          
          <Directory Id="ProgramMenuFolder">
            <Directory Id="ProgramMenuSubfolder" Name="$appName"/>
          </Directory>
          
        </Directory>


        <!-- Step 2: Add files to your installer package
        Here, source for WiX is working directory at WiX time (where WiX invoked, where .wxs is located.)
        -->
        <DirectoryRef Id="AppRootDir">
            <Component Id="AppBinaries" Guid="$appExecutableGUID">
                <File Id="AppExecutable" 
                  Source="../../out/build/x64-Debug/$appName.exe" 
                  KeyPath="yes" Checksum="yes"/>
                  
                <!-- register mimetype.  
                Probably not safe from conflict with existing mimetypes.
                Note this provides default icon comprising app icon on a floppy disk/document background.
                More specific icon requires changes to registry.
                Or ProgId.Icon attribute, advertised?
                FUTURE this whole section pretemplated into the template, if app does not have a mimetype.
                -->
                <ProgId Id="$appName.$mimetypeExtension" Description="$appName file type">
                  <Extension Id="$mimetypeExtension" ContentType="application/$mimetypeExtension">
                     <Verb Id="open" Command="open" TargetFile="AppExecutable" Argument='"%1"'/>
                  </Extension>
                </ProgId>
                
            </Component>
            
            <!-- FUTURE documents
            <Component Id="documentation.html" Guid="PUT-GUID-HERE">
                <File Id="documentation.html" Source="MySourceFiles\documentation.html" KeyPath="yes"/>
            </Component>
            -->
            
        </DirectoryRef>
        
        <DirectoryRef Id="ProgramMenuSubfolder">
          <Component Id="AppStartMenuItem" Guid="$appStartMenuItemGUID">
             <Shortcut Id="AppMenuShortcut" 
                   Name="$appName" 
                   Description="Start $appName" 
                   Target="[AppRootDir]$appName.exe" 
                   WorkingDirectory="AppRootDir"
                   Icon='$appName.ico' />
             <RegistryValue Root="HKCU" Key="Software\$companyName\$appName" 
                       Name="installed" Type="integer" Value="1" KeyPath="yes"/>
             <RemoveFolder Id="ProgramMenuSubfolder" On="uninstall"/>
           </Component>
        </DirectoryRef>
        
        <!-- FUTURE DesktopShortcut -->

        <!-- Step 3: Tell WiX what components a featureSet comprises -->
        <Feature Id="AppAndShortcuts" Title="App and shortcuts" Level="1">
            <ComponentRef Id="AppBinaries" />
            <ComponentRef Id="AppStartMenuItem"/>
            <!-- FUTURE Documents -->
            <!-- FUTURE DesktopShortcut -->
        </Feature>
    </Product>
</Wix>
'''
