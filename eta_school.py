import datetime
import googlemaps

def get_commute_duration():
    
    home_address = "home_address"
    work_address = "work_address"
    
    google_maps_api_key = "API Key"
    gmaps = googlemaps.Client(key=google_maps_api_key)
    
    directions = gmaps.directions(home_address, work_address)
    first_leg = gmaps.directions[0]['legs'][0]
    duration = first_leg['duration']['text']
    return duration

def send_text_message(message):
    account_sid = "twilio_sid"
    auth_token = "twilio_token"
    from_phone_number = "from_phone_number"
    to_phone_number = "to_phone_number"
    
    client = Client(account_sid, auth_token)
    
    client.message.create(
        body=body,
        from_=from_phone_number,
        to = to_phone_number
    )
    print("Text mesaage sent!")
    
def main():
    duration = get_commute_duration()
    
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')
    
    message = (
    f"Good Morning!\n\n"
    f"Estimated commute time from home to work at 9 am: {duration}.\n\n"
    f"Leave now for work at 9am to arrive at approximately {arrival_time}.\n"
    )
    
    send_text_message(message)