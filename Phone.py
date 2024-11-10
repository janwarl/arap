import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


class Phone:
    def __init__(self, e164):
        self.e164 = e164


    def get_information(self):
        phone_num_obj = phonenumbers.parse(self.e164)
        information_a = [phonenumbers.is_valid_number(phone_num_obj),
                phonenumbers.is_possible_number(phone_num_obj),
                phonenumbers.format_number(phone_num_obj, phonenumbers.PhoneNumberFormat.NATIONAL),
                phonenumbers.format_number(phone_num_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                phonenumbers.format_number(phone_num_obj, phonenumbers.PhoneNumberFormat.E164),
                geocoder.description_for_number(phone_num_obj, 'en'),
                carrier.name_for_number(phone_num_obj, 'en'),
                timezone.time_zones_for_number(phone_num_obj)]

        information_b = ['Valid Number',
                         'Possible Number',
                         'National Number',
                         'International Number',
                         'E.164',
                         'Location',
                         'Carrier',
                         'TimeZone(s)']

        for label, info in zip(information_b, information_a):
            print(f'{label}: {info}')