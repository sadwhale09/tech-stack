import numpy as np
import matplotlib.pyplot as plt

stack = ['API Gateway',
 'Administration',
 'Agile',
 'Airflow',
 'Ansible',
 'Ansible',
 'Ansible',
 'Apache Spark',
 'Autosar',
 'Azure',
 'Bash',
 'Bazy Danych',
 'C++',
 'CI/CD',
 'CI/CD',
 'Cloud Data Warehouses',
 'Confluence',
 'DBT',
 'Dagster',
 'Data',
 'Databricks',
 'DevOps',
 'Docker',
 'Docker',
 'English',
 'Gerrit',
 'Git',
 'Git',
 'GitHub',
 'GitHub',
 'Groovy',
 'JIRA',
 'JIRA',
 'JMS',
 'Java',
 'Java',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Jenkins',
 'Kafka',
 'Kubernetes',
 'Kubernetes',
 'Kubernetes',
 'Linux',
 'Linux / Unix',
 'Management',
 'OpenShift',
 'Palantir Foundry',
 'Perl',
 'Power BI',
 'Project Management',
 'Prometheus',
 'PySpark',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'Python',
 'QlikSense',
 'RPA',
 'Rancher',
 'Relational Databases',
 'SAP',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'SQL',
 'Scala',
 'Scrum',
 'Shell',
 'Snowflake',
 'Spring',
 'SysML',
 'Tableau',
 'TeamCity',
 'Terraform',
 'Tomcat',
 'TypeScript',
 'UML',
 'Unix',
 'WebLogic']



uniq = np.unique(stack)

counted = []
for i in range(len(uniq)):
    print(f'{uniq[i]} - {stack.count(uniq[i])}')
    counted.append(stack.count(uniq[i]))


'''
plt.style.use('_mpl-gallery')

# make data:
# x = 0.5 + np.arange(8)
limit = len(counted)
x = 0.1 + np.arange(limit)
y = counted

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, limit), xticks=np.arange(1, limit),
       ylim=(0, limit), yticks=np.arange(1, limit))

plt.show()
'''




y_pos = np.arange(len(uniq))
# counted.sort()
tech = counted

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, tech, align='center')
ax.set_yticks(y_pos, labels=uniq)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_title('Tech Stack')

# Label with specially formatted floats
ax.bar_label(hbars)
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
