from venues.models import Venue
from django.contrib.gis.geos import Point


def insert_venues():
    venues = [
        {
            'name': 'The Temple Bar',
            'address': '47-48 Temple Bar, Dublin, Ireland',
            'description': 'Iconic pub in the heart of Dublin.',
            'location': Point(-6.265074, 53.345308),  # Longitude, Latitude
            'opening_hours': 'Mon-Sun: 11:00 AM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Brazen Head',
            'address': '20 Lower Bridge St, Usher\'s Quay, Dublin, Ireland',
            'description': 'Ireland\'s oldest pub, dating back to 1198.',
            'location': Point(-6.2776, 53.3474),
            'opening_hours': 'Mon-Sun: 10:30 AM - 11:30 PM',
            'venue_type': 'Bar',
        },
        {
            'name': 'Guinness Storehouse',
            'address': 'St James\'s Gate, Ushers, Dublin 8, Ireland',
            'description': 'Visitor center at the Guinness brewery.',
            'location': Point(-6.2864, 53.3419),
            'opening_hours': 'Mon-Sun: 9:30 AM - 7:00 PM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Porterhouse',
            'address': '16-18 Parliament St, Temple Bar, Dublin, Ireland',
            'description': 'Brewpub with a variety of craft beers.',
            'location': Point(-6.2669, 53.3457),
            'opening_hours': 'Mon-Sun: 12:00 PM - 12:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Horseshoe Bar',
            'address': 'Shelbourne Rd, Ballsbridge, Dublin, Ireland',
            'description': 'Classic bar at The Shelbourne Hotel.',
            'location': Point(-6.2389, 53.3366),
            'opening_hours': 'Mon-Sun: 12:00 PM - 12:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'Dublin Castle',
            'address': 'Dame St, Dublin, Ireland',
            'description': 'Historic castle in the heart of Dublin.',
            'location': Point(-6.2676, 53.3439),
            'opening_hours': 'Mon-Sun: 9:45 AM - 5:45 PM',
            'venue_type': 'Restaurant',
        },
        {
            'name': 'The Sugar Club',
            'address': '8 Lower Leeson St, Saint Kevin\'s, Dublin, Ireland',
            'description': 'Popular nightclub with live music events.',
            'location': Point(-6.2560, 53.3341),
            'opening_hours': 'Thu-Sat: 11:00 PM - 3:00 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'The Harbour Bar',
            'address': '1-4 Dock Terrace, Bray, Co. Wicklow, Ireland',
            'description': 'Traditional Irish bar with live music.',
            'location': Point(-6.1072, 53.2025),
            'opening_hours': 'Mon-Sun: 12:00 PM - 11:30 PM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Stag\'s Head',
            'address': '1 Dame Ct, Dublin, Ireland',
            'description': 'Traditional Irish pub with Victorian interior.',
            'location': Point(-6.2656, 53.3445),
            'opening_hours': 'Mon-Sun: 11:00 AM - 11:30 PM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Woollen Mills',
            'address': '42 Ormond Quay Lower, North City, Dublin, Ireland',
            'description': 'Historic building housing a restaurant and bar.',
            'location': Point(-6.2645, 53.3460),
            'opening_hours': 'Mon-Sun: 8:00 AM - 11:30 PM',
            'venue_type': 'Restaurant',
        },
        {
            'name': 'The Grand Social',
            'address': '35 Liffey St Lower, North City, Dublin, Ireland',
            'description': 'Music venue and bar with a rooftop terrace.',
            'location': Point(-6.2698, 53.3474),
            'opening_hours': 'Mon-Sun: 12:00 PM - 3:00 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Workman\'s Club',
            'address': '10 Wellington Quay, Temple Bar, Dublin, Ireland',
            'description': 'Live music venue and club.',
            'location': Point(-6.2673, 53.3458),
            'opening_hours': 'Mon-Sun: 12:00 PM - 2:30 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'The Bernard Shaw',
            'address': '11-12 Richmond St S, Saint Kevin\'s, Dublin, Ireland',
            'description': 'Hipster hangout with a beer garden.',
            'location': Point(-6.2673, 53.3331),
            'opening_hours': 'Mon-Sun: 12:00 PM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Liquor Rooms',
            'address': '6-8 Wellington Quay, Temple Bar, Dublin, Ireland',
            'description': 'Stylish cocktail bar with a retro vibe.',
            'location': Point(-6.2674, 53.3457),
            'opening_hours': 'Mon-Sun: 5:00 PM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Dice Bar',
            'address': '79 Queen St, Smithfield, Dublin, Ireland',
            'description': 'Trendy spot with craft beers and live music.',
            'location': Point(-6.2793, 53.3473),
            'opening_hours': 'Mon-Sun: 5:00 PM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The George',
            'address': '89 South Great George\'s St, Dublin, Ireland',
            'description': 'Iconic LGBTQ+ nightclub.',
            'location': Point(-6.2679, 53.3437),
            'opening_hours': 'Mon-Sun: 2:00 PM - 3:00 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'The Twisted Pepper',
            'address': '54 Middle Abbey St, North City, Dublin, Ireland',
            'description': 'Multi-level nightclub and live music venue.',
            'location': Point(-6.2631, 53.3480),
            'opening_hours': 'Fri-Sat: 11:00 PM - 3:00 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'The Mercantile',
            'address': '28 Dame St, Dublin, Ireland',
            'description': 'Pub and live music venue in a historic building.',
            'location': Point(-6.2667, 53.3447),
            'opening_hours': 'Mon-Sun: 11:00 AM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Button Factory',
            'address': 'Curved St, Temple Bar, Dublin, Ireland',
            'description': 'Live music venue in a former factory.',
            'location': Point(-6.2668, 53.3452),
            'opening_hours': 'Mon-Sun: 11:00 AM - 2:30 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'Opium',
            'address': '26 Wexford St, Dublin, Ireland',
            'description': 'Asian-themed nightclub and cocktail bar.',
            'location': Point(-6.2632, 53.3344),
            'opening_hours': 'Thu-Sat: 5:00 PM - 2:30 AM',
            'venue_type': 'Nightclub',
        },
        {
            'name': 'The Vat House',
            'address': 'Temple Bar, Dublin, Ireland',
            'description': 'Traditional Irish pub in Temple Bar.',
            'location': Point(-6.2674, 53.3458),
            'opening_hours': 'Mon-Sun: 11:00 AM - 2:30 AM',
            'venue_type': 'Bar',
        },
        {
            'name': 'The Liquor Rooms',
            'address': '6-8 Wellington Quay, Temple Bar, Dublin, Ireland',
            'description': 'Stylish cocktail bar with a retro vibe.',
            'location': Point(-6.2674, 53.3457),
            'opening_hours': 'Mon-Sun: 5:00 PM - 2:30 AM',
            'venue_type': 'Bar',
        }
    ]
    for venue_info in venues:
        Venue.objects.create(**venue_info)


if __name__ == "__main__":
    insert_venues()
