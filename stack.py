import numpy as np
import matplotlib.pyplot as plt

stack = ['.Net',
 '.Net',
 '2FA',
 'AIX',
 'API Gateway',
 'API Gateway',
 'API Gateway',
 'API Gateway',
 'API Testing',
 'ASP.NET',
 'AV',
 'AWS',
 'AWS',
 'AWS',
 'AWS',
 'AWS',
 'AWS',
 'AWS',
 'AWS Serverless Services',
 'Active Directory',
 'Administration',
 'Agile',
 'Agile',
 'Agile',
 'Amazon AWS',
 'Amazon AWS',
 'Analityczne Myślenie',
 'Analityczne Myślenie',
 'Android',
 'Angielski',
 'Angular',
 'Angular',
 'Angular',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Ansible',
 'Apache',
 'Apache',
 'Apache',
 'Apache Kafka',
 'Apache Tomcat',
 'Atlassian',
 'Automation Tools',
 'Avamar',
 'Azure',
 'Azure',
 'Azure',
 'Azure',
 'Azure',
 'Azure',
 'Azure',
 'Azure',
 'Azure AD',
 'Azure DevOps',
 'Azure DevOps',
 'Azure DevOps',
 'Backend',
 'Bash',
 'Bash',
 'Bash',
 'Bash',
 'Bash',
 'Bash',
 'Bazy Danych',
 'Bazy Danych',
 'Bazy Danych',
 'Big Data',
 'Bitbucket',
 'Bitbucket',
 'Bluetooth Low Energy/BLE',
 'Brocade',
 'Burp Suite',
 'Business Intelligence',
 'C',
 'C',
 'C#',
 'C#',
 'C#',
 'C#',
 'C++',
 'C++',
 'C++',
 'C++',
 'C/C++',
 'CFT',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CI/CD',
 'CISSP',
 'CentOS',
 'CentOS',
 'Check Point Maestro',
 'Check Point VSX',
 'Children',
 'Cloud',
 'Cloud (preferably Azure)',
 'Cloud Computing',
 'Communication Skills',
 'Confluence',
 'Continuous Delivery',
 'Continuous Integration',
 'CyberArk',
 'Cypress',
 'Cypress',
 'DAM',
 'DB2',
 'Data Center',
 'Data Warehousing',
 'Data Warehousing',
 'Databases',
 'Databases',
 'Databases',
 'Databases',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps',
 'DevOps tools',
 'DevOps tools',
 'Django',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'Docker',
 'ETL tools',
 'ETL tools',
 'ETL tools',
 'ETL tools',
 'Elasticsearch',
 'Elasticsearch',
 'Elasticsearch',
 'Elasticsearch',
 'Elasticsearch',
 'Embedded',
 'Embedded C',
 'Embedded C',
 'Embedded Systems',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'English',
 'Ethernet',
 'Firewall',
 'Functional Testing',
 'GCP',
 'GCP',
 'GCP',
 'GUI Testing',
 'Gateway',
 'Gerrit',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'Git',
 'GitHub',
 'GitLab',
 'GitLab',
 'GitLab',
 'Gitlab/Github',
 'GlusterFS',
 'Golang',
 'Google Cloud',
 'Google Cloud Platform',
 'Google Cloud Platform',
 'Grafana',
 'Groovy',
 'Groovy',
 'HANA',
 'HTML',
 'HTTP',
 'HTTP protocol',
 'Hardware',
 'Helm',
 'Hibernate',
 'Hibernate',
 'Hibernate',
 'HikVision',
 'IAM/PAM',
 'IBM MQ',
 'IIS',
 'IPsec',
 'IPsec',
 'ISO',
 'IT Security',
 'IT Support',
 'IT Support',
 'IT Support',
 'ITIL',
 'ITIL',
 'ITIL',
 'Incident management',
 'JFrog Xray',
 'JIRA',
 'JIRA',
 'JIRA',
 'JIRA',
 'JIRA',
 'Jasper',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java',
 'Java 11',
 'Java/.NET',
 'JavaScript',
 'JavaScript',
 'JavaScript',
 'JavaScript',
 'JavaScript',
 'JavaScript',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Kali Linux',
 'Kanban',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux',
 'Linux (Debian)',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux / Unix',
 'Linux Kernel',
 'Linux Server',
 'Linux/Bash/AD/OAuth/Okta',
 'MITRE ATT&CK',
 'MS Power BI',
 'MS SQL',
 'MS SQL Server',
 'MS SQL Server',
 'MS-SQL-Server',
 'MVC',
 'Management',
 'Maven',
 'Maven',
 'MaxDB',
 'Metasploit',
 'Microservice Architecture',
 'Microservices',
 'Microservices',
 'Microsoft Office 365',
 'Microsoft SCCM',
 'Microsoft SQL',
 'Microsoft Server',
 'MongoDB',
 'Monitoring Tools',
 'Monitoring Tools',
 'Morpheus',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'MySQL',
 'NAS',
 'NAS',
 'NIST',
 'Networker',
 'Networking',
 'NoSQL',
 'Node.js',
 'Nomad',
 'OOP',
 'OSB / MQ',
 'OWASP',
 'Octopus',
 'OpenShift',
 'OpenShift',
 'OpenShift',
 'OpenShift',
 'OpenShift',
 'OpenShift',
 'OpenStack',
 'Oracle',
 'Oracle',
 'Oracle',
 'Oracle DB',
 'Oracle DB',
 'Oracle DB',
 'Oracle SQL',
 'Oracle SQL',
 'Oracle SQL',
 'PHP',
 'PHP',
 'PHP',
 'PHP',
 'PHP 7.x',
 'PHP Laravel',
 'PKI',
 'PKI',
 'PL/SQL',
 'PL/SQL',
 'PL/SQL',
 'Pentesting',
 'Pentesting',
 'Percona',
 'Perl',
 'PostgreSQL',
 'PostgreSQL',
 'PostgreSQL',
 'PostgreSQL',
 'PostgreSQL',
 'PostgreSQL',
 'Postman',
 'Postman',
 'Postman',
 'Powershell',
 'Project Management',
 'Project Management',
 'Prometheus',
 'Prometheus',
 'Prometheus',
 'Prometheus',
 'Puppet',
 'Puppet',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python scripting',
 'Python/Bash',
 'QA',
 'QML',
 'Qt',
 'RCA',
 'REST',
 'REST API',
 'REST API',
 'REST API',
 'REST API',
 'RESTful APIs',
 'RTOS',
 'RTOS',
 'RabbitMQ',
 'RabbitMQ',
 'RabbitMQ',
 'Rancher',
 'React',
 'React',
 'React Native',
 'ReactJS',
 'ReactJS',
 'Red Hat',
 'Red Hat',
 'RedHat Linux',
 'Redis',
 'Redis',
 'Redux',
 'Relacyjne Bazy Danych',
 'Relational Databases',
 'Relational Databases',
 'Roger',
 'Ruby',
 'Ruby on Rails',
 'SAN',
 'SAP',
 'SAP ABAP',
 'SAP Fiori',
 'SDLC',
 'SDN',
 'SIEM',
 'SIEM',
 'SOAP',
 'SOAR',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL Server',
 'SRE',
 'SSL',
 'SSL',
 'SUSE Manager',
 'SVN',
 'SaaS',
 'SaltStack',
 'Satel',
 'Scala',
 'Scala',
 'Scripting',
 'Scripting languages',
 'Scrum',
 'Scrum',
 'Scrum',
 'Scrum',
 'Scrum',
 'Security',
 'Shell',
 'Shell',
 'Shell',
 'Snowflake',
 'SoapUI',
 'Software Development',
 'Solid',
 'SonarQube',
 'Sonicwall',
 'Spring',
 'Spring',
 'Spring',
 'Spring',
 'Spring',
 'Spring',
 'Spring Boot',
 'Spring Boot',
 'Spring Boot',
 'Storage',
 'Symfony',
 'Symfony',
 'Synabase',
 'T-SQL',
 'TCP',
 'TCP/IP',
 'TCP/IP',
 'TCP/IP',
 'Tableau',
 'TeamCity',
 'TeamCity',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'Terraform',
 'TibcoEMS',
 'Tomcat',
 'Troubleshooting',
 'Troubleshooting',
 'Twig',
 'TypeScript',
 'TypeScript',
 'TypeScript',
 'TypeScript',
 'UML',
 'Ubiquiti',
 'Unix',
 'Unix',
 'VMware',
 'VMware',
 'VMware',
 'VPN',
 'Varnish',
 'Vue.js',
 'WMware',
 'Web Services',
 'Web Services',
 'WebLogic',
 'Windows',
 'Windows',
 'Windows',
 'Windows',
 'Windows',
 'Windows',
 'Windows Server',
 'Windows Server',
 'Windows Server',
 'Workstation',
 'Zabbix',
 'Zabbix',
 'aaa',
 'aaa',
 'analysis skills',
 'architektura systemów inf',
 'iOS',
 'pytest',
 'software testing',
 'sys. wysokiej dostępności']


uniq = np.unique(stack)

counted = []
for i in range(len(uniq)):
    # print(f'{uniq[i]} - {stack.count(uniq[i])}')
    counted.append(stack.count(uniq[i]))


stack_dict = {}
for i in range(len(uniq)):
    stack_dict[uniq[i]] = counted[i]

sorted = sorted(stack_dict.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted)

# print(converted_dict)
__import__('pprint').pprint(converted_dict, sort_dicts=False)

# for key in converted_dict:
#     print(key)
#
# for val in converted_dict.values():
#     print(val)



y_pos = np.arange(len(converted_dict))
# counted.sort()
tech = converted_dict.values()

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, tech, align='center')
ax.set_yticks(y_pos, labels=converted_dict)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_title('Tech Stack')

# Label with specially formatted floats
ax.bar_label(hbars)
# ax.set_xlim(right=max(counted)+max(counted)*0.1)  # adjust xlim to fit labels

plt.show()
