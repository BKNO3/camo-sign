Camo sign
#########

.. image:: https://travis-ci.org/BKNO3/camo-sign.svg?branch=master
    :target: https://travis-ci.org/BKNO3/camo-sign


Create signed URLs for use with camo_.

.. _camo: https://github.com/atmos/camo


Installation
============

::

    pip install camo-sign


Example usage
=============

.. code-block:: pycon

    >>> from camo_sign import create_signed_url

    >>> base_url = 'https://camo.example.com/'
    >>> secret_key = b'OMGWTFBBQ'
    >>> image_url = 'http://example.com/img.jpg'

    >>> create_signed_url(base_url, secret_key, image_url)
    https://camo.example.com/22fd0910eeefa6db9d4b105aa92c56d09bccf05f/687474703a2f2f6578616d706c652e636f6d2f696d672e6a7067'


Recipe: replace links in HTML
=============================

This can be easily done using eg. ``lxml``:

.. code-block:: python

    def replace_image_links(html, camo_url, camo_key):
        document = lxml.html.fromstring(html)
        for elem in document.xpath('//img'):
            old_src = elem.attrib['src']
            if old_src.startswith(('http://', 'https://')):
                new_src = create_signed_url(camo_url, camo_key, old_src)
                elem.attrib['src'] = new_src
        output = lxml.html.tostring(document).decode()
        return output


Links
=====

- `PYPI page <https://pypi.python.org/pypi/camo-sign>`_
- `GitHub repository <https://github.com/BKNO3/camo-sign/>`_
- `Travis CI builds <https://travis-ci.org/BKNO3/camo-sign>`_
