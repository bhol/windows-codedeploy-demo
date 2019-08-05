$ErrorActionPreference = 'Stop'

echo "Currently executing custom powershell script for BeforeInstall hook"
Import-Module -Name ServerManager
Install-WindowsFeature Web-Server