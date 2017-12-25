#!env python
"""
the demo APIs to show how to use Comprehend service to detect the entities
"""
import boto3
import time

client = boto3.client('comprehend', region_name="us-east-1")

def start_topics_detection_job_doc_per_line():
    """
    use the sample doc per file to generate the topic detection job.
    s3://rafacomprehend/ONE_DOC_PER_LINE/ is already world wild readable
    but you may need to set up correct IAM role and output S3 location
    :return: None
    """
    response = client.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': 's3://rafacomprehend/ONE_DOC_PER_LINE/Sample.txt',
            'InputFormat': 'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 's3://rafacomprehend/topicmodelingoutput'
        },
        DataAccessRoleArn='arn:aws:iam::620428855768:role/comprehend-s3-topic-modeling',
        JobName='Sample_ONE_DOC_PER_LINE_'+str(int(time.time())),
        NumberOfTopics=30
    )
    print response


def start_topics_detection_job_doc_per_file():
    """
    use the sample doc per file to generate the topic detection job.
    s3://rafacomprehend/ONE_DOC_PER_FILE/ is already world wild readable
    but you may need to set up correct IAM role and output S3 location
    :return: None
    """
    response = client.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': 's3://rafacomprehend/ONE_DOC_PER_FILE/',
            'InputFormat': 'ONE_DOC_PER_FILE'
        },
        OutputDataConfig={
            'S3Uri': 's3://rafacomprehend/topicmodelingoutput'
        },
        DataAccessRoleArn='arn:aws:iam::620428855768:role/comprehend-s3-topic-modeling',
        JobName='Sample_ONE_DOC_PER_FILE_'+str(int(time.time())),
        NumberOfTopics=30
    )
    print response

def list_topics_detection_job_by_name(topicname):
    """
    the function print out the jobs which match the prefix of the topicname
    :param topicname: it could be exact name or prefix
    :return: None but the function will print the output
    """
    jobs = client.list_topics_detection_jobs(
        Filter={
            'JobName': topicname
        }
    )['TopicsDetectionJobPropertiesList']
    for job in jobs:
        format_print_jobs(job)

def list_topics_detection_job_by_status(status):
    """
    the function print out the jobs which match status
    :param status: it could be exact in 'SUBMITTED | IN_PROGRESS | COMPLETED | FAILED'
    :return: None but the function will print the output
    """
    if status not in ['SUBMITTED', 'IN_PROGRESS', 'COMPLETED', 'FAILED']:
        print "status must be 'SUBMITTED | IN_PROGRESS | COMPLETED | FAILED'"
        return

    jobs = client.list_topics_detection_jobs(
        Filter={
            'JobStatus': status
        }
    )['TopicsDetectionJobPropertiesList']
    for job in jobs:
        format_print_jobs(job)

def describe_topic_by_id(jobid):
    """
    use describe_topics_detection_job to get the job details
    :param jobid: the exact job id
    :return: None but will print the job details
    """
    job = client.describe_topics_detection_job(
        JobId=jobid
    )['TopicsDetectionJobProperties']
    format_print_jobs(job)


def format_print_jobs(job):
    """
    a help function to print the job in format
    :param job: the job dictionary
    :return: None but will print the output
    """
    print "\nJobName: " + job['JobName']
    for k,v in job.iteritems():
        if k <> 'JobName':
            print "\t" + str(k) + ": " + str(v)


def convert_topic_file():
    """
    AWS provides a sample topic modeling file in s3://public-sample-us-east-1/Sample.txt
    Once you download it and Store it in ./topic/Sample.txt, you can ran the ad-hoc script to generate text file for each line
    :param None:
    :return: process, None to return
    """
    index = 0
    with open("./topic/Sample.txt") as sample:
        for line in sample:
            targetfile = open("./topic/Sample-" + str(index) + ".txt", "w")
            targetfile.write(line)
            targetfile.flush()
            targetfile.close()
            index += 1


if __name__ == "__main__":
    # start_topics_detection_job_doc_per_line()
    # start_topics_detection_job_doc_per_file()
    # list_topics_detection_job_by_status('FAILED')
    # list_topics_detection_job_by_name('Sample_ONE_DOC_PER_FILE_')
    # describe_topic_by_id('34570bdca0bb93b2b0a8d2597f4aeba3')
    pass

