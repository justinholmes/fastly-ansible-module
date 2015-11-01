#!/usr/bin/env python
# (c) 2015, Justin Holmes <justin@nascency.co.uk>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DOCUMENTATION = '''
---
module: fastly
short_description: Run Ansible against fastly api
description:
- Run Ansible against fastly api
author: Justin Holmes
version_added: 1.6
'''
EXAMPLES = '''
# purge cdn for a service
  - local_action:
      module: fastly
      key: "d3cafb4dde4dbeef"
      service: "SU1Z0isxPaozGVKXdv0eY"
      command: "purge_all"

'''

import sys
import fastly

def main():
    argument_spec=dict(
        key=dict(type='str', required=True),
        service=dict(type='str', required=True),
        command=dict(type='str', required=True)
    )
    module = AnsibleModule(argument_spec, supports_check_mode=False)

    key = module.params.get('key')
    service = module.params.get('service')
    command = module.params.get('command')

    api = fastly.API()
    api.authenticate_by_key(key)

    if command == 'purge_all':
        apicall = api.purge_service(service)
        module.exit_json(changed=apicall)
        sys.exit(0)


# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
