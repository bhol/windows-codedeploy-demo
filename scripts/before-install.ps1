$ErrorActionPreference = 'Stop'

echo "Currently executing custom powershell script for BeforeInstall hook"

# Install IIS
Import-Module ServerManager; 
Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName 'IIS-WebServerRole', 'IIS-WebServer', 'IIS-ManagementConsole';
