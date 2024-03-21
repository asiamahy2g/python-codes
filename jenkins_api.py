import jenkins
import os

server = jenkins.Jenkins('http://35.175.140.55:8080', username='devmanny', password='devops')
user = server.get_whoami()
version = server.get_version()
job_number=server.jobs_count()
nodes= server.get_nodes()
jobs= server.get_all_jobs()
os.system('clear')
#print(user['id'], version)

#print(job_number,nodes,jobs)

for job in jobs:
        print(f"job name is {job['name']}, job url is {job['url']}")