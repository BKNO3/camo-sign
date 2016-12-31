from camo_sign import create_signed_url


def test_can_sign_simple_url():
    signed = create_signed_url(
        base_url='https://camo.example.com/',
        hmac_key=b'OMGWTFBBQ',
        url='http://example.com/img.jpg')
    assert signed == (
        'https://camo.example.com/'
        '22fd0910eeefa6db9d4b105aa92c56d09bccf05f/'
        '687474703a2f2f6578616d706c652e636f6d2f696d672e6a7067')
