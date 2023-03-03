import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

# Prompt the user to enter an IP address
ip_address = input('Enter an IP address: ')

# Get information about the IP address using the ipinfo.io API
api_key = 'put yo ipinfo key here'
response = requests.get(f'https://ipinfo.io/{ip_address}?token={api_key}')
if response.status_code == 200:
    ip_data = response.json()
    print(ip_data)
else:
    print(f'Error getting IP information. Status code: {response.status_code}')
    print(response.text)
    exit()

# Read the Discord webhook URL from a file
with open('webhook_info.txt', 'r') as file:
    webhook_url = file.readline().strip()
    webhook_name = file.readline().strip()
    webhook_pfp = file.readline().strip()

# Create a Discord webhook
webhook = DiscordWebhook(url=webhook_url, username=webhook_name, avatar_url=webhook_pfp)

# Create a Discord embed with information about the IP address
embed = DiscordEmbed(title=f'IP information for {ip_address}', color='00ff00')
if 'ip' in ip_data:
    embed.add_embed_field(name='IP Address', value=ip_data['ip'])
if 'hostname' in ip_data:
    embed.add_embed_field(name='Hostname', value=ip_data['hostname'])
if 'city' in ip_data:
    embed.add_embed_field(name='City', value=ip_data['city'])
if 'region' in ip_data:
    embed.add_embed_field(name='Region', value=ip_data['region'])
if 'country' in ip_data:
    embed.add_embed_field(name='Country', value=ip_data['country'])
if 'postal' in ip_data:
    embed.add_embed_field(name='Postal Code', value=ip_data['postal'])
if 'loc' in ip_data:
    embed.add_embed_field(name='Latitude/Longitude', value=ip_data['loc'])
if 'timezone' in ip_data:
    embed.add_embed_field(name='Timezone', value=ip_data['timezone'])
if 'org' in ip_data:
    embed.add_embed_field(name='Organization', value=ip_data['org'])

webhook.add_embed(embed)

# Send the Discord webhook message
response = webhook.execute()
if response.status_code == 204:
    print('Webhook message sent successfully')
else:
    print(f'Error sending webhook message. Status code: {response.status_code}')
    print(response.text)
