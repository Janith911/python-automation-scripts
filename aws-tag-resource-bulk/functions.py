import boto3

resource_ids = []

def list_ec2():
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
        resource_ids.append(i['Instances'][0]['InstanceId'])
    return resource_ids

def list_ami():
    client = boto3.client('ec2')
    response = client.describe_images(Owners=['self'])
    for i in response['Images']:
        resource_ids.append(i['ImageId'])
    return resource_ids

def list_volume():
    client = boto3.client('ec2')
    response = client.describe_volumes()
    for i in response['Volumes']:
        resource_ids.append(i['VolumeId'])
    return resource_ids

def list_snap():
    client = boto3.client('ec2')
    response = client.describe_snapshots(OwnerIds=['self'])
    for i in response['Snapshots']:
        resource_ids.append(i['SnapshotId'])
    return resource_ids

def list_eip():
    client = boto3.client('ec2')
    response = client.describe_addresses()
    for i in response['Addresses']:
        resource_ids.append(i['AllocationId'])
    return resource_ids

def list_sg():
    client = boto3.client('ec2')
    response = client.describe_security_groups()
    for i in response['SecurityGroups']:
        resource_ids.append(i['GroupId'])
    return resource_ids

def list_keypair():
    client = boto3.client('ec2')
    response = client.describe_key_pairs()
    for i in response['KeyPairs']:
        resource_ids.append(i['KeyPairId'])
    return resource_ids

def list_eni():
    client = boto3.client('ec2')
    response = client.describe_network_interfaces()
    for i in response['NetworkInterfaces']:
        resource_ids.append(i['NetworkInterfaceId'])
    return resource_ids

def list_lb():
    client = boto3.client('elbv2')
    response = client.describe_load_balancers()
    for i in response['LoadBalancers']:
        resource_ids.append(i['LoadBalancerArn'])
    return resource_ids

def list_tg():
    client = boto3.client('elbv2')
    response = client.describe_target_groups()
    for i in response['TargetGroups']:
        resource_ids.append(i['TargetGroupArn'])
    return resource_ids

def list_redshift():
    client = boto3.client('redshift')
    response = client.describe_clusters()
    for i in response['Clusters']:
        arn = i['ClusterNamespaceArn']
        arn = arn.replace('namespace', 'cluster')
        arn_list = arn.split(':')
        arn_list[-1] = i['ClusterIdentifier']
        new_arn = ""
        for j in arn_list:
            new_arn = new_arn + ":" + j
        resource_ids.append(new_arn)

    return resource_ids

def list_rds():
    client = boto3.client('rds')
    response = client.describe_db_instances()
    for i in response['DBInstances']:
        resource_ids.append(i['DBInstanceArn'])
    return resource_ids

def list_rds_snapshots():
    client = boto3.client('rds')
    response = client.describe_db_snapshots()
    for i in response['DBSnapshots']:
        resource_ids.append(i['DBSnapshotArn'])
    return resource_ids



def list_vpc():
    client = boto3.client('ec2')
    response = client.describe_vpcs()
    for i in response['Vpcs']:
        resource_ids.append(i['VpcId'])
    return resource_ids

def list_subnet():
    client = boto3.client('ec2')
    response = client.describe_subnets()
    for i in response['Subnets']:
        resource_ids.append(i['SubnetId'])
    return resource_ids

def list_routetable():
    client = boto3.client('ec2')
    response = client.describe_route_tables()
    for i in response['RouteTables']:
        resource_ids.append(i['RouteTableId'])
    return resource_ids

def list_igw():
    client = boto3.client('ec2')
    response = client.describe_internet_gateways()
    for i in response['InternetGateways']:
        resource_ids.append(i['InternetGatewayId'])
    return resource_ids

def list_vpcendpoint():
    client = boto3.client('ec2')
    response = client.describe_vpc_endpoints()
    for i in response['VpcEndpoints']:
        resource_ids.append(i['VpcEndpointId'])
    return resource_ids

def list_natgw():
    client = boto3.client('ec2')
    response = client.describe_nat_gateways()
    for i in response['NatGateways']:
        resource_ids.append(i['NatGatewayId'])
    return resource_ids

def list_vpngw():
    client = boto3.client('ec2')
    response = client.describe_vpn_gateways()
    for i in response['VpnGateways']:
        resource_ids.append(i['VpnGatewayId'])
    return resource_ids

def list_vpcpeer():
    client = boto3.client('ec2')
    response = client.describe_vpc_peering_connections()
    for i in response['VpcPeeringConnections']:
        resource_ids.append(i['VpcPeeringConnectionId'])
    return resource_ids

def list_transitgw():
    client = boto3.client('ec2')
    response = client.describe_transit_gateways()
    for i in response['TransitGateways']:
        resource_ids.append(i['TransitGatewayId'])
    return resource_ids

def list_transitgw_att():
    client = boto3.client('ec2')
    response = client.describe_transit_gateway_attachments()
    for i in response['TransitGatewayAttachments']:
        resource_ids.append(i['TransitGatewayAttachmentId'])
    return resource_ids



###### LAMBDA FUNCTIONS ######
def list_lambda():
    client = boto3.client('lambda')
    response = client.list_functions()
    for i in response['Functions']:
        resource_ids.append(i['FunctionArn'])
    return resource_ids

###### CLOUDWATCH ######

def list_cwloggroups():
    client = boto3.client('logs')
    response = client.describe_log_groups()
    for i in response['logGroups']:
        resource_ids.append(i['logGroupName'])
    return resource_ids

###### DYNAMODB ######

def list_dynamodb():
    client = boto3.client('dynamodb')
    response = client.list_tables()
    for i in response['TableNames']:
        resource_ids.append(i)
    return resource_ids