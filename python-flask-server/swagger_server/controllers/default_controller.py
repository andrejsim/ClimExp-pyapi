import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def correlatefield_get(netcdf_source1=None, netcdf_source2=None, frequency=None, average=None, var=None, netcdf_target=None):
    """
    correlatefield_get
    
    :param netcdf_source1: field1 netcdf file used as source
    :type netcdf_source1: str
    :param netcdf_source2: field2 netcdf file used as source
    :type netcdf_source2: str
    :param frequency: freq?
    :type frequency: str
    :param average: avg?
    :type average: str
    :param var: var?
    :type var: str
    :param netcdf_target: netcdf file used as output
    :type netcdf_target: str

    :rtype: None
    """
    return 'do some magic!'
