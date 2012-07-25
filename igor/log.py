# -*- coding: utf-8 -*-
#
# Copyright (C) 2012  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Fabian Deutsch <fabiand@fedoraproject.org>
#

import logging
import logging.config
import tempfile

cache_fileobj = tempfile.NamedTemporaryFile()

log_config = {
    "version": 1,

    "formatters": {
        "default": {
            "format": '%(levelname)-8s - %(asctime)s - ' + \
                      '%(name)-15s - %(message)s'
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "cache": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": cache_fileobj
        }
    },

    "loggers": {
        "": {
            "handlers": ["console", "cache"],
            "level": "DEBUG",
            "propagate": True
        }
    }
}

logging.config.dictConfig(log_config)


def backlog():
    r = None
    cache_fileobj.flush()
    with open(cache_fileobj.name, "r") as f:
        r = f.read()
    return r
