import connexion
import six

from swagger_server import util

shoes = ['GUCCHIO', 'NIKE', "ADDIDIAS"]


def shoes_get():  # noqa: E501
    """shoes_get

    Getting all shoes # noqa: E501


    :rtype: None
    """
    shoe_str = ', '.join(shoes)
    return shoe_str, 200


def shoes_id_delete(id):  # noqa: E501
    """shoes_id_delete

    Delete shoe # noqa: E501

    :param id: Delete existing shoe
    :type id: int

    :rtype: None
    """
    try:
        shoes.pop(id)
    except IndexError:
        return 'Invalid id', 405
    except:
        return 'Server error', 500
    return 'Successfully delete', 200


def shoes_id_put(id, name):  # noqa: E501
    """shoes_id_put

    Change name of shoe # noqa: E501

    :param id: Change name of shoe by id
    :type id: int
    :param name: Add
    :type name: str

    :rtype: None
    """
    try:
        shoes[id] = name.decode('utf-8')
    except IndexError:
        return 'Invalid id', 405
    except:
        return 'Server error', 500
    return 'Successfully change name of shoe'


def shoes_post(name):  # noqa: E501
    """shoes_post

    Something # noqa: E501

    :param name: Add
    :type name: str

    :rtype: None
    """
    shoes.append(name.decode('utf-8'))
    return 'Success', 200
