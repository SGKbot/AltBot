#!/usr/bin/python


from ansible.module_utils.basic import *
import docker
try:
    import docker
    from docker import Client
except ImportError:
    from docker import APIClient as Client


if __name__ == '__main__':
    module = AnsibleModule(
        argument_spec = dict(
            id = dict(required=True),
            type = dict(default='container',
                        choises=['container', 'image'])
        ),
        supports_check_mode = True
    )

    id = module.params['id']
    type = module.params['type']

    client = Client()

    try:
        if type == 'image':
            attrs = client.inspect_image(id)
        elif type == 'container':
            attrs = client.inspect_container(id)
    except docker.errors.APIError as e:
        module.fail_json(attrs={}, msg=str(e))
    else:
        module.exit_json(failed=False, changed=False, attrs=attrs)
