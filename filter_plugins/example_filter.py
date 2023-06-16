#!/usr/bin/python

DOCUMENTATION = """
name: example_filter
author: "Sean Sullivan (@sean-m-sullivan)"
short_description: Return data on workflows from the workflow API
description:
    - This plugin sorts through workflows and workflow nodes to return information on what is present.

"""

EXAMPLES = r"""
- name: Transform Data
    ansible.builtin.set_fact:
    data_out: "{{ workflow_job_templates | example_filter }}"

## Output
# TASK [Show output] ***********************************************************************************************
# ok: [localhost] => {
#     "data_out": {
#         "approval_nodes": [
#             "Approval to Continue"
#         ],
#         "inventory_sources": [
#             "RHVM-01",
#             "RHVM-01"
#         ],
#         "job_templates": [
#             "workflow_test_template",
#             "workflow_test_template",
#             "Demo Job Template",
#             "Demo Job Template",
#             "workflow_test_template"
#         ],
#         "workflows": [
#             "Complicated workflow schema",
#             "Simple workflow schema"
#         ]
#     }
# }
"""

from ansible.errors import AnsibleFilterError


class FilterModule(object):
    def filters(self):
        return {"example_filter": self.workflow_manip}

    def workflow_manip(self, data_in: dict):
        workflow_data = {}

        workflow_data["workflows"] = []
        workflow_data["job_templates"] = []
        workflow_data["inventory_sources"] = []
        workflow_data["approval_nodes"] = []
        for workflow in data_in:
            workflow_data["workflows"].append(workflow["name"])
            for node in workflow["related"]["workflow_nodes"]:
                if node["unified_job_template"]["type"] == "inventory_source":
                    workflow_data["inventory_sources"].append(
                        node["unified_job_template"]["name"]
                    )
                elif node["unified_job_template"]["type"] == "job_template":
                    workflow_data["job_templates"].append(
                        node["unified_job_template"]["name"]
                    )
                elif node["unified_job_template"]["type"] == "workflow_approval":
                    workflow_data["approval_nodes"].append(
                        node["unified_job_template"]["name"]
                    )
                else:
                    raise AnsibleFilterError(
                        "Failed to find valid node: {0}".format(workflow)
                    )
        return workflow_data
