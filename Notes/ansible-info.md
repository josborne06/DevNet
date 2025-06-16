# 🛠️ Ansible Cheat Sheet for Network Engineers

_A quick-reference guide for automating Cisco networks using Ansible. Tailored for Catalyst Center, NetBox, Cisco IOS XE devices, and includes security best practices._

---

## 📦 Ansible Basics

```bash
ansible --version                  # Show version
ansible-inventory --list          # Show parsed inventory
ansible-playbook pb.yml           # Run a playbook
ansible-vault encrypt vars.yml    # Encrypt secrets
```

**Structure**
```
inventory/
├── hosts.yml
group_vars/
  └── all.yml
playbooks/
  └── site.yml
roles/
  └── ios_config/
```

---

## 🔐 Security & Ansible Vault

### What Vault Is
Ansible Vault uses AES-256 encryption to protect sensitive data like passwords, tokens, and keys—keeping them safe in version control.

### Common Vault Commands
```bash
ansible-vault create secrets.yml
ansible-vault encrypt secrets.yml
ansible-vault decrypt secrets.yml
ansible-vault edit secrets.yml
ansible-vault view secrets.yml
ansible-vault rekey secrets.yml
```

### Encrypt a Single Variable
```bash
ansible-vault encrypt_string 'Cisco123!' --name 'ansible_password'
```

### Using Vault in Playbooks

**Encrypted `vault.yml`**
```yaml
ansible_user: admin
ansible_password: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  ... encrypted content ...
```

**Playbook with Vault**
```yaml
- name: Secure Cisco Config Backup
  hosts: core_switches
  gather_facts: no
  vars_files:
    - group_vars/all/vault.yml
  tasks:
    - name: Backup running-config
      cisco.ios.ios_config:
        backup: yes
```

**Run with Vault Password**
```bash
ansible-playbook playbook.yml --vault-password-file ~/.vault_pass
```

### Vault Tips
- Use `--ask-vault-pass` or `--vault-password-file` for secure automation
- Set `no_log: true` to prevent secrets from being printed
- Use multiple vault IDs for different environments:
  ```bash
  --vault-id dev@prompt --vault-id prod@prompt
  ```

### Learn More
- [Official Ansible Vault Docs](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [DigitalOcean: Ansible Vault Guide](https://www.digitalocean.com/community/tutorials/how-to-use-ansible-vault-to-secure-secrets)
- [CloudMyLab: Secure Ansible Credentials](https://www.cloudmylab.com/ansible-vault/)
- [Spacelift Vault Best Practices](https://spacelift.io/blog/ansible-vault)

---

## 🧠 Inventory Example (YAML)

```yaml
all:
  children:
    cisco_ios:
      hosts:
        rtr1:
          ansible_host: 192.168.1.1
          ansible_user: admin
          ansible_password: "{{ vault_pass }}"
          ansible_network_os: ios
```

---

## 📘 Common Modules

| Module              | Purpose                          |
|---------------------|----------------------------------|
| `ios_config`        | Push configs to IOS devices      |
| `ios_command`       | Run show commands                |
| `ios_facts`         | Gather facts                     |
| `netbox_device`     | Manage NetBox inventory          |
| `dnac_device_info`  | Query Catalyst Center info       |
| `uri`               | REST API for anything            |

---

## 📚 Example Tasks

**Push Configs**
```yaml
- name: Set hostname
  cisco.ios.ios_config:
    lines:
      - hostname {{ inventory_hostname }}
```

**Gather Facts**
```yaml
- name: Gather facts
  cisco.ios.ios_facts:
```

**DNAC Device Info**
```yaml
- name: Get DNAC device info
  cisco.dnac.device_info:
    dnac_host: "{{ dnac_host }}"
    dnac_username: "{{ dnac_user }}"
    dnac_password: "{{ dnac_pass }}"
    validate_certs: no
```

---

## 🧠 NetBox + Ansible

**Install Collection**
```bash
ansible-galaxy collection install netbox.netbox
```

**Example: Create Device**
```yaml
- name: Add device
  netbox.netbox.netbox_device:
    netbox_url: http://netbox.local
    netbox_token: "{{ netbox_token }}"
    data:
      name: "rtr1"
      device_type: "Cisco IOS-XE"
      device_role: "Core"
      site: "HQ"
    state: present
```

---

## 🪄 Templates (Jinja2)

**Template Example**
```jinja
interface {{ intf }}
 description Connected to {{ neighbor }}
 ip address {{ ip }} {{ mask }}
```

**Use in Task**
```yaml
- name: Configure interface from template
  cisco.ios.ios_config:
    src: intf_template.j2
```

---

## 🧪 Testing Tips

- Use `--check` and `--diff` for dry runs
- Lint playbooks with `ansible-lint`
- Test in EVE-NG, CML, or virtual labs

---

## 💡 Recommended Collections

```bash
ansible-galaxy collection install cisco.ios
ansible-galaxy collection install cisco.dnac
ansible-galaxy collection install netbox.netbox
```

---

## 🧵 Example Full Playbook

```yaml
- name: Backup Cisco Configs
  hosts: cisco_ios
  gather_facts: no
  tasks:
    - name: Show running config
      cisco.ios.ios_command:
        commands: show running-config
      register: output

    - name: Save to file
      copy:
        content: "{{ output.stdout[0] }}"
        dest: "backups/{{ inventory_hostname }}.txt"
```

---

## 📚 More Resources

- [Cisco Ansible Guide](https://developer.cisco.com/docs/ansible/)
- [NetBox Ansible Modules](https://github.com/netbox-community/ansible_modules)
- [Catalyst Center DevNet](https://developer.cisco.com/docs/dnac/)
- [Ansible Network Docs](https://docs.ansible.com/ansible/latest/network/index.html)

---

🧠 _Automate smart. Stay consistent. Version everything._