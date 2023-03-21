import boto3
import sys
from functions import *

resources = []

portfolio_tag = [
    {
        'Key' : 'Portfolio',
        'Value' : 'Managed Services'
    }
]

portfolio_tag_dictionary = [
    {
        'Portfolio' : 'Managed Services',
    }
]

# def get_tags_ec2():
#     client = boto3.client('ec2')
#     response = client.describe_tags()

#     for i in response["Tags"]:
#         resource = {}
#         resource["ResourceType"] = i["ResourceType"]
#         resource["ResourceId"] = i["ResourceId"]
#         resources.append(resource)

#     seen = set()
#     new_l = []

#     for d in resources:
#         t = tuple(d.items())
#         if t not in seen:
#             seen.add(t)
#             new_l.append(d)

#     for i in new_l:
#         print(i)


def create_tags(resource_ids, tags):
    client = boto3.client('ec2')

    response = client.create_tags(    
        Resources=resource_ids,
        Tags=tags
        )
    print(resource_ids)


def create_tags_elb(resource_arns, tags):
    client = boto3.client('elbv2')
    for i in resource_arns:
        elb_arn = []
        elb_arn.append(i)
        response = client.add_tags(ResourceArns=elb_arn,Tags=tags)
    print(resource_arns)


def create_tags_rds(resource_arns, tags):
    client = boto3.client('rds')
    for i in resource_arns:
        print(i)
        response = client.add_tags_to_resource(ResourceName=i,Tags=tags)
    print(resource_arns)

def create_tags_redshift(resource_arns, tags):
    client = boto3.client('redshift')
    for i in resource_arns:
        response = client.create_tags(ResourceName=i,Tags=tags)
    print(resource_arns)

def create_tags_lambda(resource_arns, tags):
    client = boto3.client('lambda')
    for i in resource_arns:
        response = client.tag_resource(Resource=i,Tags=tags[0])
    print(resource_arns)

def create_tags_cw_loggroup(resource_arns, tags):
    client = boto3.client('logs')
    for i in resource_arns:
        response = client.tag_log_group(logGroupName=i,tags=tags[0])
    print(resource_arns)

# def create_tags_dynamodb(resource_arns, tags):
#     client = boto3.client('logs')
#     for i in resource_arns:
#         response = client.tag_log_group(logGroupName=i,tags=tags[0])
#     print(resource_arns)




resource_type = sys.argv[1]




if resource_type == 'instance':
    list_of_resources = list_ec2()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'ami':
    list_of_resources = list_ami()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'volumes':
    list_of_resources = list_volume()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'snap':
    list_of_resources = list_snap()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'eip':
    list_of_resources = list_eip()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'sg':
    list_of_resources = list_sg()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'kp':
    list_of_resources = list_keypair()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'eni':
    list_of_resources = list_eni()
    if list_of_resources != []:
        create_tags(list_of_resources,tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'lb':
    list_of_resources = list_lb()
    if list_of_resources != []:
        create_tags_elb(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'tg':
    list_of_resources = list_tg()
    if list_of_resources != []:
        create_tags_elb(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'rds':
    list_of_resources = list_rds()
    if list_of_resources != []:
        create_tags_rds(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'rdssnap':
    list_of_resources = list_rds_snapshots()
    if list_of_resources != []:
        create_tags_rds(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'redshift':
    list_of_resources = list_redshift()
    print(list_of_resources)
    if list_of_resources != []:
        create_tags_redshift(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'vpc':
    list_of_resources = list_vpc()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'subnet':
    list_of_resources = list_subnet()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'rt':
    list_of_resources = list_routetable()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'igw':
    list_of_resources = list_igw()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'vpce':
    list_of_resources = list_vpcendpoint()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'natgw':
    list_of_resources = list_natgw()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'vpngw':
    list_of_resources = list_vpngw()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'vpcpeering':
    list_of_resources = list_vpcpeer()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'tgw':
    list_of_resources = list_transitgw()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")

elif resource_type == 'tgwatt':
    list_of_resources = list_transitgw_att()
    if list_of_resources != []:
        create_tags(list_of_resources, tags=portfolio_tag)
    else:
        print("No Resources")







elif resource_type == 'lambda':
    list_of_resources = list_lambda()
    if list_of_resources != []:
        create_tags_lambda(list_of_resources, tags=portfolio_tag_dictionary)
    else:
        print("No Resources")

elif resource_type == 'logs':
    list_of_resources = list_cwloggroups()
    if list_of_resources != []:
        create_tags_cw_loggroup(list_of_resources, tags=portfolio_tag_dictionary)
    else:
        print("No Resources")

elif resource_type == 'dynamodb':
    list_of_resources = list_dynamodb()
    print(list_of_resources)
    # if list_of_resources != []:
    #     create_tags_cw_loggroup(list_of_resources, tags=portfolio_tag_dictionary)
    # else:
    #     print("No Resources")