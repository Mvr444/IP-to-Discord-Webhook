# IP-to-Discord-Webhook


This Python script retrieves information about an IP address using the ipinfo.io API and sends it to a Discord webhook. The user is prompted to enter an IP address, and the script makes a GET request to the API to obtain information about that IP address. If the request is successful, the script creates a Discord embed containing details such as the IP address, hostname, city, region, country, and organization. The embed is then sent to the specified Discord webhook using the DiscordWebhook library. The name of the script and the webhook URL, username, and avatar are specified in a separate file for easy configuration. 
