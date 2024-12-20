# Customize here
$token = ""

# Host vars
$ErrorActionPreference = 'SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls" # Helps avoid issues with TLS on some servers
$global:ipAddr = ""
$global:macAddr = ""
$networkAdapters = Get-NetAdapter -Physical | Where-Object { $_.Status -eq 'Up' }
$networkAdapters | ForEach-Object {
    $adapterInfo = $_
    $ipAddresses = (Get-NetIPAddress -InterfaceIndex $adapterInfo.IfIndex -AddressFamily IPv4 | Where-Object { $_.IPAddress -ne '0.0.0.0' }).IPAddress
    $macAddress = $adapterInfo.MacAddress

    $global:ipAddr += ($ipAddresses -join ", ") + " "
    $global:macAddr += $macAddress + " "
}

# Funcs
$fullOutput = ""
function appendOutput {
    param (
        [string]$command
    )

    $output = Invoke-Expression $command | Out-String

    $global:fullOutput += $output + "`n"
}
# appendOutput -command "get-service sense"

$uri = "https://api.riposte.cc/riposte/" + $token
$headers = @{
    "accept" = "application/json"
    "Content-Type" = "application/json"
}
$body = @{
    "token" = $token
    "hostname" = $env:computername
    "ip" = $ipAddr
    "mac" = $macAddr
    "output" = $fullOutput
} | ConvertTo-Json

Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body
