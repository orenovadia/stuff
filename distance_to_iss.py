import requests


class GeoLocation(object):
    modulu = 360

    def __init__(self, longitude, latitude):
        super(GeoLocation, self).__init__()
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return 'Location< {} , {} >'.format(self.longitude, self.latitude)

    def __sub__(self, other):
        return GeoLocation((self.longitude - other.longitude),
                           (self.latitude - other.latitude))


def get_iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    position = response.json()['iss_position']
    return GeoLocation(float(position['longitude']),
                       float(position['latitude']))


def get_my_location():
    response = requests.get('http://ipinfo.io')
    long, lat = response.json()['loc'].split(',')
    return GeoLocation(float(long),
                       float(lat))


def main():
    iss_location = get_iss_location()
    my_location = get_my_location()
    print 'iss @ ', iss_location
    print 'me @ ', my_location
    print 'angular distance:', iss_location - my_location


if __name__ == '__main__':
    main()
