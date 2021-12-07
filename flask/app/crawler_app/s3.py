import boto3
from app.crawler_app import config, logger

s3_client = boto3.client('s3')

def upload_file(file,filename):
    try:
        path= config.user['job_id']+'_'+config.user['stage_id']+'/'
        s3_client.put_object(Body=file,Bucket=config.admin['bucket_name'],Key=path+filename)
        # logger.log_info_writer('uploaded file in '+path+filename)
    except Exception as e:
        pass
        # print(e)

def display_files_in_given_bucket(bucket_name):

    response = s3_client.list_objects(Bucket=bucket_name)
    for i in response['Contents']:
        print(i['Key'])


# uploading local file 
# s3_client.upload_file("0000.html",config.admin['bucket_name'],"fleet/0000.html")


# for deleting files
# delete_res = s3_client.delete_object(Bucket="wallytesting", Key="fleet/0000.html")

#to download file
# s3_client.download_file('wallytesting','3021_1/0001.html','samp.html')

# display_files_in_given_bucket("wallytesting")