#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_sample_module

short_description: This is my sample module

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Your Name (@yourhandle)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the sample module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.modCheckList import modCheckList
import json
#from . context import rolepath
import os,sys
#rolepath=os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
#facts.collect()
#rolepath=os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
# asdf


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=False),
        new=dict(type='bool', required=False, default=False),
        write_result=dict(type='bool', required=False, default=False),
        check_fact=dict(type='str', required=True),
        stig_id=dict(type='str', required=True),
        checklist_name=dict(type='str', required=True),
        output_path=dict(type='str', required=True),
        input_path=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        ##changed=True,
        changed=False,
        original_message='',
        message='SUCCESS!'
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
        #module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['stig_id']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['stig_id']:
        result['changed'] = False
        #results['changed'] = True

    def gen_checklist():
        ckl = modCheckList(
                f"{module.params['input_path']}/rhel7_05252019.ckl",
                f"{module.params['output_path']}/rhel7_05252019.ckl",
                module.params['stig_id'],
                module.params['check_fact'])
        ckl.mark_checklist()
        ckl.write_checklist()

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['write_result'] is True:
        if module.params['check_fact'] == "Open":
            gen_checklist()
            module.fail_json(msg='check_fact rule was "Open"', **result)
        if module.params['check_fact'] == "Not_A_Finding":
            gen_checklist()
            module.exit_json(msg='check_fact rule was "Not_A_Finding"')

        module.exit_json(msg=f"checklist_output: {module.params['output_path']}/rhel7_05252019.ckl",**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
