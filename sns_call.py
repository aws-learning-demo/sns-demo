# Create topic
import boto3
sns= boto3.client('sns',region_name="us-east-2")
topic_name= "demo-sns"
response = sns.create_topic(Name=topic_name)
topic_arn = response["TopicArn"]
print(topic_arn)

# List topics
response = sns.list_topics()
topics = response["Topics"]
print(topics)

'''
# Delete topics
sns.delete_topic(TopicArn=topic_arn)
# Create SMS subscription
response = sns.subscribe(TopicArn=topic_arn, Protocol="SMS", Endpoint="+48123456789")
subscription_arn = response["SubscriptionArn"]
'''
# Create email subscription
email="rakesh444saw@gmail.com"
response = sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
subscription_arn = response["SubscriptionArn"]
print(subscription_arn)

# List all subscriptions
response = sns.list_subscriptions()
subscriptions = response["Subscriptions"]

print(subscriptions)

# List subscriptions by topic
response = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
subscriptions = response["Subscriptions"]
print(subscriptions)

'''
# Delete subscription
sns.unsubscribe(SubscriptionArn=subscription_arn)

# Delete multiple subscriptions (here: all SMS ones)
for sub in subscriptions:
	if sub["Protocol"] == "sms":

		sns.unsubscribe(sub["SubscriptionArn"])
        
 '''       
       
