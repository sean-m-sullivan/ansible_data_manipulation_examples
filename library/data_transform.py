#!/usr/bin/python

# Copyright: (c) 2023, Sean Sullivan <ssulliva@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule
from ansible.errors import AnsibleError

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}
DOCUMENTATION = '''
---
module: data_transform
author: "Sean Sullivan (ssulliva@redhat.com)"
short_description: transform data in module
description:
    - transform data in module.
options:
    data_in:
      description:
        - Data to parse
      required: True
      type: dict
'''


EXAMPLES = '''
- name: Gather project dir
  data_transform:
    data_in: "{{ data }}"
'''

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        data_in=dict(type="list", elements='dict', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # Gather inputs
    data_in = module.params['data_in']

    # normailze and dict the site survey
    output_dict = {}
    for item in data_in:
        #normalized_site_dict = site['dc_name']
        if item['dc_name'] != "NONE":
            site_dict[site['dc_name'].strip().replace(" ", "").lower()] = site['dc_site_id']
    result['site_dict'] = site_dict
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
