# -*- coding: utf-8 -*-
#
# django-zodb - using Django and ZODB together
#
# Copyright (c) 2009, Triveos Tecnologia Ltda.
# See COPYING for license
#


from relstorage.storage import RelStorage

from django_zodb.storage import StorageFactory
from django_zodb.config import parse_bool, parse_tuple

class RelStorageFactory(StorageFactory):
    _storage = RelStorage
    _storage_args = (
        ('name', str, 'name'),
        ('create', parse_bool, 'create'),
        ('read_only', parse_bool, 'read_only'),
        ('blobstorage_dir', str, 'blob_dir'),
        ('poll_interval', int, 'poll_interval'),
        ('keep_history', parse_bool, 'keep_history'),
        ('replica_conf', str, 'replica_conf'),
        ('replica_timeout', float, 'replica_timeout'),
        ('pack_gc', parse_bool, 'pack_gc'),
        ('pack_dry_run', parse_bool, 'pack_dry_run'),
        ('pack_batch_timeout', float, 'pack_batch_timeout'),
        ('pack_duty_cycle', float, 'pack_duty_cycle'),
        ('pack_max_delay', float, 'pack_max_delay'),
        ('cache_servers', parse_tuple, 'cache_servers'),
        ('cache_module_name', str, 'cache_module_name'),
        ('cache_prefix', str, 'cache_prefix'),
        ('cache_local_mb', int, 'cache_local_mb'),
        ('cache_delta_size_limit', int, 'cache_delta_size_limit'),
    )

    def get_base_storage(self, **options):
        create = options.pop("create", True) # HACK: missing in relstorage.options.Options(?)
        adapter = self.get_adapter(options)
        return self._storage(adapter, create=create, **options)