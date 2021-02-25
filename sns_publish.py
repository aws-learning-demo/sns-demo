import boto3
sns= boto3.client('sns',region_name="us-east-2")
# Publish to topic
topic_arn="arn:aws:sns:us-east-2:849900374188:demo-sns"
sns.publish(TopicArn=topic_arn, 
            Message="hello from demo-sns ", 
            Subject="subject used in emails only")
            
'''
# Send a single SMS (no topic, no subscription neeed)
sns.publish(PhoneNumber="+48123456789", 
            Message="message text")
'''