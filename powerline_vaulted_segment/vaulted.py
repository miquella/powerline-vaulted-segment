from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.theme import requires_segment_info


@requires_segment_info
def vaulted(pl, segment_info, prefix=''):
    '''Return the current vaulted vault

    :param string prefix:
        The prefix to use in front of the vault name
    '''
    vault = segment_info['environ'].get('VAULTED_ENV', None)
    if vault:
        return '{0}{1}'.format(prefix, vault)
