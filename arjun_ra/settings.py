#!/usr/bin/env python
# Copyright(c) 2017, Ciena, Corp. All rights reserved.

import os

DEFAULT_CONFIG_DIRPATH = os.path.join(os.path.dirname(__file__), 'config/dev')
DEFAULT_PORT = 8080

RA_NAME = 'arjun_ra'

BPPROV_MODEL_DIRPATH = os.path.join(os.path.dirname(__file__), 'model')

RESOURCES_DIR = os.path.join(BPPROV_MODEL_DIRPATH, 'resources')
RP_CONFIG = os.path.join(RESOURCES_DIR, 'rp_config.yaml')

DOMAIN_MANAGER_RP = True

# TYPE_GROUP is the general type of resource supported by the RA
TYPE_GROUP = 'Demo'

# RESOURCE_TYPES lists the specific types of resources supported by the RA
RESOURCE_TYPES = ['Demo-A']

VENDOR = 'Ciena'

AUTHOR = 'Ciena Engineer'

STATIC_PATHS = {
    '/images/': os.path.join(os.path.dirname(__file__), 'model/graphics/images'),
}

ENDPOINTS = ['cli', 'snmp']
