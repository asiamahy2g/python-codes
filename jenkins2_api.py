                       
import jenkins
import csv
def list_jobs(jenkins_url,jenkins_user,jenkins_password):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password= jenkins_password)
    jobs=server.get_jobs()
    list_of_jobs=[]
    for i in jobs:
        list_of_jobs.append([i['name'],i['url'],i.get('color')])
    return list_of_jobs

#list_jobs('54.172.51.138:8080','devops','devops')


def jenkins_csv_file(my_list):
    with open ("jenkins_inventory.csv", 'w', newline='') as j:
        pen = csv.writer(j)
        header=['JOBS_NAME', 'JOB_URL', 'JOB_LAST_BUILD_STATUS']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)
    j.close
jenkins_csv_file(list_jobs('http://35.175.140.55:8080','devmanny','devops'))

"""def startjobs():
    pass"""