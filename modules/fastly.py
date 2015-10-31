
#!/usr/bin/python

# 'fastly'.

DOCUMENTATION = '''
---
module: fastly
short_description: Run Ansible against fastly api
description:
- Run Ansible against fastly api
author: Justin Holmes
version_added: 2.0
'''
EXAMPLES = '''
# Create a topic
  - local_action:
      module: fastly
      key: "d3cafb4dde4dbeef"
      service: "SU1Z0isxPaozGVKXdv0eY"
      command: "purge_all"

'''
import fastly

def main:
    module = AnsibleModule(
        argument_spec=dict(
            key=dict(default='d3cafb4dde4dbeef', type='str', required=True),
            service=dict(default='SU1Z0isxPaozGVKXdv0eY', type='str', required=True)
            command=dict(default='purge_all', type='str', required=True)
        ),
        supports_check_mode=False,
    )

    key = module.params.get('key')
    service = module.params.get('service')
    command = module.params.get('command')

    api = fastly.API()
    api.authenticate_by_key(key)

    if command === 'purge_all':
        apicall = api.purge_service(service)
        module.exit_json(changed=apicall)
        sys.exit(0)


main()
