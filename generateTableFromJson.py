#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from io import StringIO


# In[2]:


# !pip install openpyxl


# In[3]:

#set the json file required for the output
path_file_json = "json/aws_test_infra.json"

data = pd.read_json(f"{path_file_json}")
a = data.accounts[0]


# In[4]:


output = pd.json_normalize(a["resources"]['cloudFront']['distributions'])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/cloudFront_distributions.xlsx") 


# In[5]:


output = pd.json_normalize(a["resources"]['route53']['hostedZones'])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/hostedZones_route53.xlsx") 


# In[6]:


output = pd.json_normalize(a["regions"][0]['resources']['alb']['loadBalancersV2'])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/loadBalancersV2.xlsx")


# In[7]:


output = pd.json_normalize(a["regions"][0]['resources']['alb']['targetGroups'])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/targetGroups.xlsx")


# In[8]:


output = pd.json_normalize(a["regions"][0]['resources']['apigateway']["restApis"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/restApis_apigateway.xlsx")


# In[9]:


output = pd.json_normalize(a["regions"][0]['resources']['apigatewayv2']["apis"])

if not output.empty:
    s = pd.Series([x+1 for x in range(len(output))])
    output.set_index([s],inplace=True)
    output.to_excel("output_excel/apis.xlsx")


# In[11]:


data = pd.json_normalize(a["regions"][0]['resources']['apigatewayv2']["apis"])

if not data.empty:
    frames = []
    
    for item in data["Routes"]:
        out = pd.json_normalize(item)
        frames.append(out)
    output = pd.concat(frames)
    if not output.empty:
        s = pd.Series([x+1 for x in range(len(output))])
        output.set_index([s],inplace=True)
        output.to_excel("output_excel/routes_apis.xlsx")


# In[16]:


data = pd.json_normalize(a["regions"][0]['resources']['apigatewayv2']["apis"])

if not data.empty:
    frames = []
    for item in data["Integrations"]:
        out = pd.json_normalize(item)
        frames.append(out)
    output = pd.concat(frames)
    if not output.empty:
        s = pd.Series([x+1 for x in range(len(output))])
        output.set_index([s],inplace=True)
        output.to_excel("output_excel/integrations_apis.xlsx")


# In[17]:


output = pd.json_normalize(a["regions"][0]['resources']['cloudtrail']["trails"])

if not output.empty:
    s = pd.Series([x+1 for x in range(len(output))])
    output.set_index([s],inplace=True)
    output.to_excel("output_excel/trails_cloudtrail.xlsx")


# In[18]:


output = pd.json_normalize(a["regions"][0]['resources']['dynamoDB']["tables"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/tables_dynamoDB.xlsx")


# In[19]:


data = pd.json_normalize(a["regions"][0]['resources']['ec2']["instances"])
frames = []

for item in data["Instances"]:
    out = pd.json_normalize(item)
    frames.append(out)
        
output = pd.concat(frames)
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/instances.xlsx")


# In[20]:


data = pd.json_normalize(a["regions"][0]['resources']['ec2']["networkAcls"])
frames = []

for item in data["Associations"]:
    out = pd.json_normalize(item)
    frames.append(out)
        
output = pd.concat(frames)

s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/Associations_networkAcls.xlsx")


# In[21]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["securityGroups"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/securityGroups_ec2.xlsx")


# In[22]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["subnets"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/subnets_ec2.xlsx")


# In[23]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["volumes"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/volumes_ec2.xlsx")


# In[24]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["vpcs"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/vpcs.xlsx")


# In[25]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["internetGateways"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/internetGateways_ec2.xlsx")


# In[26]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["natGateways"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/natGateways_ec2.xlsx")


# In[27]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["routeTables"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/routeTables_ec2.xlsx")


# In[28]:


data = pd.json_normalize(a["regions"][0]['resources']['ec2']["routeTables"])
frames = []
for item in data["Associations"]:
    out = pd.json_normalize(item)
    frames.append(out)
output = pd.concat(frames)
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
output.to_excel("output_excel/routeTablesAssociations_ec2.xlsx")


# In[29]:


data = pd.json_normalize(a["regions"][0]['resources']['ec2']["routeTables"])
frames = []
for item in data["Routes"]:
    out = pd.json_normalize(item)
    frames.append(out)
output = pd.concat(frames)
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
output.to_excel("output_excel/routes_ec2.xlsx")


# In[30]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["vpcEndpoints"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/vpcEndpoints_ec2.xlsx")


# In[31]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["vpcPeeringConnections"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/vpcPeeringConnections_ec2.xlsx")


# In[32]:


output = pd.json_normalize(a["regions"][0]['resources']['ec2']["elasticNetworkInterfaces"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/elasticNetworkInterfaces_ec2.xlsx")


# In[33]:


output = pd.json_normalize(a["regions"][0]['resources']["elasticache"]["clusters"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/clusters_elasticache.xlsx")


# In[ ]:





# In[34]:


output = pd.json_normalize(a["regions"][0]['resources']["elasticache"]["subnetGroups"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/subnetgroups_elasticache.xlsx")


# In[35]:


output = pd.json_normalize(a["regions"][0]['resources']['eventbridge']["rules"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/rules_eventbridge.xlsx")


# In[36]:


output = pd.json_normalize(a["regions"][0]['resources']['kinesis']["deliveryStreams"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/deliveryStreams_kinesis.xlsx")


# In[37]:


output = pd.json_normalize(a["regions"][0]['resources']['lambda']["functions"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/lambda_functions.xlsx")


# In[38]:


output = pd.json_normalize(a["regions"][0]['resources']['lambda']["eventSourceMappings"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/eventSourceMappings_lambda.xlsx")


# In[39]:


output = pd.json_normalize(a["regions"][0]['resources']['rds']["dbInstances"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/dbInstances_rds.xlsx")


# In[40]:


output = pd.json_normalize(a["regions"][0]['resources']['s3']["buckets"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/buckets_s3.xlsx")


# In[41]:


output = pd.json_normalize(a["regions"][0]['resources']['sns']["topics"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/topics_sns.xlsx")


# In[42]:


output = pd.json_normalize(a["regions"][0]['resources']['sns']["subscriptions"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/subscriptions_sns.xlsx")


# In[43]:


output = pd.json_normalize(a["regions"][0]['resources']['sqs']["queues"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/queues_sqs.xlsx")


# In[44]:


output = pd.json_normalize(a["regions"][0]['resources']['ecs']["clusters"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/clusters_ecs.xlsx")


# In[45]:


output = pd.json_normalize(a["regions"][0]['resources']['ecs']["services"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/services_ecs.xlsx")


# In[46]:


output = pd.json_normalize(a["regions"][0]['resources']['ecs']["tasks"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/tasks_ecs.xlsx")


# In[47]:


output = pd.json_normalize(a["regions"][0]['resources']['efs']["fileSystems"])
s = pd.Series([x+1 for x in range(len(output))])
output.set_index([s],inplace=True)
if not output.empty:
    output.to_excel("output_excel/fileSystems_efs.xlsx")


# In[48]:


output = pd.json_normalize(a["regions"][0]['resources']['cognito']["userPools"])

if not output.empty:
    s = pd.Series([x+1 for x in range(len(output))])
    output.set_index([s],inplace=True)
    output.to_excel("output_excel/userPools_cognito.xlsx")


# In[49]:


data = pd.json_normalize(a["regions"][0]['resources']['cognito']["userPools"])

if not data.empty: 
    frames = []
  
    for i in range(len(data)):
        
        for item in data.iloc[i]["UserPool.SchemaAttributes"]:
            
            item["UserPoolId"] = data.iloc[i]["UserPool.Id"]
            out = pd.json_normalize(item)
            frames.append(out)
            
        output = pd.concat(frames)
    
    if not output.empty:
        
        output.set_index('UserPoolId',inplace=True)

        output.to_excel("output_excel/SchemaAttributes_userPools.xlsx")



# In[50]:


#####################################################


# In[51]:


# item = "routeTables"
# data = pd.read_json(f"{item}.json")
# output = pd.json_normalize(data.routeTables)
# output.to_excel(f"{item}.xlsx")  

