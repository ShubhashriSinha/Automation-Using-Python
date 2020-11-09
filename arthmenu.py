import os
import boto3

import sys
import getpass

while True:

    print("""
    \n
    ...................................WELCOME TO MENU PROGRAM...................................
    \n
    ################## \t\t\t 1. Aws Menu 
    ################## \t\t\t 2. Hadoop Menu
    ################## \t\t\t 3. LVM Menu
    ################## \t\t\t 4. Web Server
    ################## \t\t\t 5. Yum Menu
    ################## \t\t\t 6. Docker
    ################## \t\t\t 7. Exit 
    \n
    """)

    option = input("\nEnter the Menu option : ")
    if '1' in option:
        while True:
            print("""
            \n
            ...................................WELCOME TO AWS MENU PROGRAM...................................
            \n
            ################## \t\t\t 1. Aws key pairs 
            ################## \t\t\t 2. Create ec2 instance
            ################## \t\t\t 3. Aws Security Groups 
            ################## \t\t\t 4. Action on ec2 Instance 
            ################## \t\t\t 5. Ebs volume 
            ################## \t\t\t 6. S3 bucket
            ################## \t\t\t 7. Go Back To Main Menu
            ################## \t\t\t 8. Exit 
            \n
            """)

            x = input("Enter your choice from the above list : ")
            print("\n")

            if '1' in x:
                print("\t\t\t\tYou entered in aws key pairs now select your option")
                print("\n")
                print("\t\t\t\t\t 1. Describe key pairs")
                print("\t\t\t\t\t 2. Create Key pairs")
                print("\t\t\t\t\t 3. Delete key pairs")
                print("\n")
                x1 = input("Enter the Key pairs option : ")

                if '1' in x1:
                    ec2 = boto3.client('ec2')
                    response = ec2.describe_key_pairs()
                    print(response)

                elif '2' in x1:
                    x2 = input("Enter your Key pair name : ")
                    ec2 = boto3.client('ec2')
                    response = ec2.create_key_pair(KeyName=x2)
                    print(response)

                elif '3' in x1:
                    ec2 = boto3.client('ec2')
                    response = ec2.delete_key_pair(KeyName=x2)
                    print(response)

                else :
                    print("Wrong Choice")

            elif '2' in x:
            
                a = input("Enter your Image Id : ")
                print("\n")
                b = int(input("Enter your Count : "))
                print("\n")
                c = input("Enter your Instance type : ")
                print("\n")
                d = input("Enter your Key name : ")
                print("\n")
                e = input("Enter your Subnet Id : ") 
                print("\n")  
                ec2 = boto3.resource('ec2')
                instance = ec2.create_instances(
                    ImageId = a ,
                    MinCount = b ,
                    MaxCount = b ,
                    InstanceType = c ,
                    KeyName = d ,
                    SubnetId =  e )
                print (instance[0].id)

            elif '3' in x:
            
                print("\t\t\t\t\t Aws Security Groups")
                print("\n")
                print("\t\t\t\t\t 1. Create Security Group")
                print("\t\t\t\t\t 2. Describe Security Groups")
                print("\t\t\t\t\t 3. Delete Security Group")
                print("\n")
                x1 = input("Enter the Aws Security Group option : ")

                if '2' in x1:
                    from botocore.exceptions import ClientError

                    ec2 = boto3.client('ec2')

                    try:
                        s = input("\nEnter security group Id : ")
                        response = ec2.describe_security_groups(GroupIds=[s])
                        print(response)
                    except ClientError as e:
                        print(e)

                elif '1' in x1:
                    from botocore.exceptions import ClientError

                    ec2 = boto3.client('ec2')

                    response = ec2.describe_vpcs()
                    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

                    try:
                        response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                                            Description='DESCRIPTION',
                                                            VpcId=vpc_id)
                        security_group_id = response['GroupId']
                        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

                        data = ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[
                                {'IpProtocol': 'tcp',
                                'FromPort': 80,
                                'ToPort': 80,
                                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                                {'IpProtocol': 'tcp',
                                'FromPort': 22,
                                'ToPort': 22,
                                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
                            ])
                        print('Ingress Successfully Set %s' % data)
                    except ClientError as e:
                        print(e)

                elif '3' in x1:
                    from botocore.exceptions import ClientError

                    # Create EC2 client
                    ec2 = boto3.client('ec2')

                # Delete security group
                    try:
                        s = input("\nEnter security group Id : ")
                        response = ec2.delete_security_group(GroupId = s)
                        print('Security Group Deleted')
                    except ClientError as e:
                        print(e)

                else:
                    print("Wrong Option Selected")

            elif '4' in x:
                print("""
                \t\t\t\t\t Action on ec2 Instances
                \n
                \t\t\t\t\t 1. Descibe Instance
                \t\t\t\t\t 2. Start and Stop Instance
                \t\t\t\t\t 3. Reboot Instance
                \t\t\t\t\t 4. terminate Instance
                \n
                """)
                x1 = input("Enter the Option for Action on ec2 Instances  : ")

                if '1' in x1:
                    ec2 = boto3.client('ec2')
                    response = ec2.describe_instances()
                    print(response)

                elif '2' in x1:

                
                    print("""
                    \n 1. start Instance
                    \n 2. stop Instance
                    """)
                    from pprint import pprint

                    a = input("\nEnter the option : ")
                    client = boto3.client('ec2')
                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:
                            print ("\n\t",inst_id['InstanceId'])

                    iid = input("\nEnter your instance id : ")

                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:

                            if '1' in a:
                                print("\nstarting your Instance...\n")
                                res = client.start_instances(InstanceIds=[iid])
                                print(res)
                                break
                            
                            elif '2' in a:
                                print("\nstoping your Instance...\n")
                                res = client.stop_instances(InstanceIds=[iid])
                                print(res)
                                break
                            
                elif '3' in x1:
                    print("\n\tYour Instances Ids are : \n")
                    from pprint import pprint
                    client = boto3.client('ec2')
                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:
                            print ("\n\t",inst_id['InstanceId'])

                    iid = input("\nEnter your instance id : ")


                    res = client.reboot_instances(InstanceIds=[iid])
                    print("\n",res)
                    print("\nYour Instance is getting Rebooted")

                elif '4' in x1:
                    print("\n\tYou have selected option for terminating your ec2 Instances \n")
                    print("\n\tYour Instances Ids are : \n")
                    from pprint import pprint
                    client = boto3.client('ec2')
                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:
                            print ("\n\t",inst_id['InstanceId'])

                    iid = input("\nEnter your instance id : ")

                    a = input("\nAre you sure you want to terminate yes/no : ")

                    if 'yes' in a:
                        st = client.stop_instances(InstanceIds=[iid])
                        te = client.terminate_instances(InstanceIds=[iid])
                        print("\n",st,"\n\n",te,"\n  ")
            elif '5' in x:
                print("\t\t\t\tAWS EBS volume")
                print("\n")
                print("\t\t\t\t\t 1. Create ebs volume")
                print("\t\t\t\t\t 2. Attach ebs volume")
                print("\t\t\t\t\t 3. Detach ebs volume")
                print("\t\t\t\t\t 4. Create Snapshot")
                print("\t\t\t\t\t 5. Delete ebs volume")
                print("\n")
                x1 = input("Enter the AWS EBS Volume option : ")

                if '1' in x1:
                    a = input("Enter the Availability Zone : ")
                    print("\n")
                    b = int(input("Enter the size : "))
                    print("\n")
                    c = input("Enter your volume type (ex: standard,io1,io2,gp2,sc1,st1) : ")
                    print("\n")
                    client = boto3.client('ec2') 
                    response = client.create_volume(
                        AvailabilityZone= a,
                        Size= b ,
                        VolumeType= c,
                    )
                    print(response)

                elif '2' in x1:
                    from pprint import pprint
                    client = boto3.client('ec2')
                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:
                            print ("\n\t",inst_id['InstanceId'])
                    b = input("\nEnter Instance Id : ")
                    print("\n")
                    for each_vol in client.describe_volumes()['Volumes']:
                        print ("\n\t",each_vol['VolumeId'])
                    c = input("\nEnter Volume Id : ")
                    print("\n")
                    response = client.attach_volume(
                        Device = '/dev/sdf',
                        InstanceId = b,
                        VolumeId= c,
                    )
                    print(response)

                elif '3' in x1:
                    from pprint import pprint
                    client = boto3.client('ec2')
                    for each_ins in client.describe_instances()['Reservations']:
                        for inst_id in each_ins['Instances']:
                            print ("\n\t",inst_id['InstanceId'])
                    b = input("\nEnter Instance Id : ")
                    print("\n")
                    for each_vol in client.describe_volumes()['Volumes']:
                        print ("\n\t",each_vol['VolumeId'])
                    c = input("\nEnter Volume Id : ")
                    print("\n")
                    response = client.detach_volume(
                        Device= '/dev/sdf' ,
                        Force=True,
                        InstanceId= b ,
                        VolumeId= c ,
                    )
                    print(response)

                elif '5' in x1:
                    from pprint import pprint
                    client = boto3.client('ec2')
                    print("\t Volume Ids")
                    for each_vol in client.describe_volumes()['Volumes']:
                        print ("\n\t",each_vol['VolumeId'])

                    c = input("\nEnter Volume Id : ")
                    print("\n")

                    response = client.delete_volume(
                        VolumeId = c,
                    )
                    print(response)

                elif '4' in x1:
                    from pprint import pprint
                    client = boto3.client('ec2')
                    print("\t Volume Ids")
                    for each_vol in client.describe_volumes()['Volumes']:
                        print ("\n\t",each_vol['VolumeId'])

                    c = input("\nEnter Volume Id : ")
                    print("\n")

                    b = input("you can add a description to your snapshot : ")
                    print("\n")

                    response = client.create_snapshot(
                        Description = b,
                        VolumeId = c,
                
                    )
                    print(response)

            elif '8' in x:
                exit()

            elif '7' in x:
                break

            elif '6' in x:
                print("\t\t\t\tS3 Bucket")
                print("\n")
                print("\t\t\t\t\t 1. Create S3 Bucket")
                print("\t\t\t\t\t 2. List Bucket ")
                print("\t\t\t\t\t 3. Upload File")
                print("\n")
                x1 = input("Enter the S3 bucket option : ")

                s3 = boto3.client('s3')

                if '1' in x1:
                    a = input("\t Enter your Bucket name : ")
                    print("\n")
                    b = s3.create_bucket(Bucket = a)
                    print(b,"\n\t\t","Your Bucket has been created..")

                elif '2' in x1:
                    response = s3.list_buckets()
                    buckets = [bucket['Name'] for bucket in response['Buckets']]
                    print("\n\tBucket List: %s" % buckets)

                elif '3' in x1:
                    response = s3.list_buckets()
                    buckets = [bucket['Name'] for bucket in response['Buckets']]
                    print("\n\tBucket List: %s" % buckets)
                    bucket_name = input("\nEnter your bucket name from above list : ")
                    print("\n\t\tnote : your file should be present in the same folder : ")
                    filename = input("\nEnter your file name : ")
                    bucket_name = 'my-bucket'
                    r = s3.upload_file(filename, bucket_name, filename)
                    print("\n",r)
                    print("\n\t\t your file has been uploaded sucessfully..  ")

        else:
            print("Wrong Choice ...")
    elif '7' in option:
        exit()

    elif '2' in option:
        os.system("tput setaf 3")
        print("\t\t\tWelcome to my hadoop menu :)")
        os.system("tput setaf 7")
        print("\t\t\t ----------------------")

        password=getpass.getpass("Enter the password : ")
        print(password)

        if password != "mymenu" :
            print("Incorrect Password")
            exit()	

        r = input("Where you want to run this menu? (local) : ")
        print(r)

        #while True :
        #	os.system("clear")	

        os.system("tput setaf 2")
        while True:
            print("""
            \n
            Press 1 : To install jdk and hadoop
            Press 2 : To setup namenode
            Press 3 : To setup datanode 
            Press 4 : To check report of datanodes
            Press 5 : To check list of contents on cluster
            Press 6 : To check active daemon (jps)
            Press 7 : To upload (put) a file on the cluster
            Press 8 : To upload a file of specific block size
            Press 9 : To see (cat) the file uploaded on cluster
            Press 10: To remove file from cluster
            Press 11: To get back to main menu
            Press 12: To exit
            """)
            os.system("tput setaf 6")
            ch=input("Enter your Choise : ")
            print(ch)
            os.system("tput setaf 7")

            if r == "local":
                
                if int(ch) == 3:
                    os.system("tput setaf 67")
                    print("""ENTER in next Config file : 
                    <property>
                    <name>dfs.data.dir</name>
                    <value>/dn1</value>
                    </property>
                    \n """)
                    os.system("tput setaf 7")

                    r = input("Press ENTER")
                    print(r)
                    
                    os.system("vim /etc/hadoop/hdfs-site.xml")

                    os.system("tput setaf 67")
                    print("""ENTER in next Config file : 
                    <property>
                    <name>fs.default.name</name>
                    <value>hdfs://(NameNode IP here):9001</value>
                    </property>
                    \n """)
                    os.system("tput setaf 7")

                    r = input("Press ENTER")
                    print(r)

                    os.system("vim /etc/hadoop/core-site.xml")
                    os.system("mkdir /dn1")
                    os.system("systemctl stop firewalld")
                    os.system("hadoop-daemon.sh start datanode")
                    os.system("jps")
                elif int(ch) == 1:
                    os.system("rpm -ivh /root/jdk-8u171-linux-x64.rpm")
                    os.system("rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")
                elif int(ch) == 2:
                    os.system("tput setaf 67")
                    print("""ENTER in next Config file : 
                    <property>
                    <name>dfs.name.dir</name>
                    <value>/nn</value>
                    </property>
                    \n """)
                    os.system("tput setaf 7")

                    r = input("Press ENTER")
                    print(r)
                    
                    os.system("vim /etc/hadoop/hdfs-site.xml")

                    os.system("tput setaf 67")
                    print("""ENTER in next Config file : 
                    <property>
                    <name>fs.default.name</name>
                    <value>hdfs://(your IP here):9001</value>
                    </property>
                    \n """)
                    os.system("tput setaf 7")

                    r = input("Press ENTER")
                    print(r)

                    os.system("vim /etc/hadoop/core-site.xml")
                    os.system("mkdir /nn")
                    os.system("hadoop namenode -format")
                    os.system("systemctl stop firewalld")
                    os.system("hadoop-daemon.sh start namenode")
                    os.system("jps")

                elif int(ch) == 4:
                    os.system("hadoop dfsadmin -report")
                elif int(ch) == 5:
                    os.system("hadoop fs -ls /")
                elif int(ch) == 6:
                    os.system("jps")
                elif int(ch) == 7:
                    os.system("tput setaf 67")
                    fname = input("Enter the file Name : ")
                    print(fname)
                    os.system("tput setaf 7")
                    os.system("hadoop fs -put {} /".format(fname))
                elif int(ch) == 8:
                    os.system("tput setaf 67")
                    fname=input("Enter the file name : ")
                    print(fname)
                    size=input("Enter the block size : ")
                    print(size)
                    os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(size,fname))
                    os.system("tput setaf 7")
                elif int(ch) == 9:
                    os.system("tput setaf 67")
                    fname=input("Enter the file name : ")
                    print(fname)
                    os.system("tput setaf 7")
                    os.system("hadoop fs -cat /{}".format(fname))
                elif int(ch) == 10:
                    os.system("tput setaf 67")
                    fname=input("Enter the file name : ")
                    print(fname)
                    os.system("tput setaf 7")
                    os.system("hadoop fs -rm /{}".format(fname))
                elif int(ch) == 12:
                    exit()
                elif int(ch) == 11:
                    break
                else:
                    print("Not Supported")


            
            else:
                os.system("tput setaf 1")
                print("WRONG INPUT")
                os.system("tput setaf 7")

            input("\nPress Enter to Continue..")

    if '3' in option:
        while True:
            os.system("tput setaf 3")
            print("\t\t\tWelcome to my LVM menu :)")
            os.system("tput setaf 7")
            print("\t\t\t ----------------------")


            os.system("tput setaf 2")
            print("""
            \n
            Press 1 : To create LVM partition in your system
            Press 2 : To provide elasticity to hadoop DataNode storage
            Press 3 : To extend the size of hadoop DataNode storage
            Press 4 : To get back to main menu
            Press 5 : To exit
            """)
            os.system("tput setaf 6")
            ch=input("Enter your Choise : ")
            print(ch)
            os.system("tput setaf 7")

                
            if int(ch) == 2:
                os.system("tput setaf 2")
                print("""
                Press 1 : To list the devices attached to this system
                Press 2 : to continue	
                """)
                
                os.system("tput setaf 6")
                ch1=input("Enter your choise : ")
                print(ch1)
                os.system("tput setaf 7")

                if int(ch1) == 1:
                    os.system("fdisk -l")
                    os.system("tput setaf 6")
                    d1=input("Enter 1st device : ")
                    print(d1)
                    d2=input("Enter 2nd device : ")
                    print(d2)
                    vg=input("Enter the vg name : ")
                    print(vg)
                    lv=input("Enter the name of partition(lv name) : ")
                    print(lv)
                    size=input("Enter the size of partition in GiB : ")
                    print(size)

                    os.system("tput setaf 7")
                    os.system("pvcreate {}".format(d1))
                    os.system("pvcreate {}".format(d2))
                    os.system("vgcreate {} {} {}".format(vg,d1,d2))
                    os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
                    os.system("tput setaf 6")
                    r=input("\n Press ENTER to check details of your partition")
                    print(r)
                    os.system("tput setaf 7")
                    os.system("lvdisplay {}/{}".format(vg,lv))
                    os.system("tput setaf 6")
                    path=input("Enter the LV Path : ")
                    print(path)
                    os.system("tput setaf 7")
                    os.system("mkfs.ext4 {}".format(path))
                    os.system("mkdir /l1")
                    os.system("mount {} /l1".format(path))
                    os.system("tput setaf 6")
                    print("\n Now enter the directory name as /l1 in next config file")
                    s=input("Press ENTER to continue")
                    print(s)		
                    os.system("tput setaf 7")
                    os.system("vim /etc/hadoop/hdfs-site.xml")
                    os.system("tput setaf 6")
                    print("DONE!!")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    Press 1 : To check details of physical volume (pv)
                    Press 2 : To check details of volume group (vg)
                    Press 3 : To check details of partition (lv)
                    Press 4 : To check details of all the partitions (lv)
                    Press 5 : To exit
                    Press 6 : To continue
                    """)
                    os.system("tput setaf 6")
                    chh=input("Enter your Choise : ")
                    print(chh)
                    os.system("tput setaf 7")
                    
                    if int(chh) == 1:
                        os.system("tput setaf 6")
                        c=input("Enter the name of pv : ")
                        print(c)
                        os.system("tput setaf 7")
                        os.system("pvdisplay {}".format(c))
                    elif int(chh) == 2:
                        os.system("vgdisplay {}".format(vg))
                    elif int(chh) == 3:
                        os.system("lvdisplay {}/{}".format(vg,lv))
                    elif int(chh) == 4:
                        os.system("lvdisplay")
                    elif int(chh) == 5:
                        exit()
                    #elif int(chh) == 6:
                        #(To continue)
                    else :
                        os.system("tput setaf 1")
                        print("WRONG INPUT")
                        os.system("tput setaf 7")

                elif int(ch1) == 2:
                    os.system("tput setaf 6")
                    d1=input("Enter 1st device : ")
                    print(d1)
                    d2=input("Enter 2nd device : ")
                    print(d2)
                    vg=input("Enter the vg name : ")
                    print(vg)
                    lv=input("Enter the name of partition(lv name) : ")
                    print(lv)
                    size=input("Enter the size of partition : ")
                    print(size)

                    os.system("tput setaf 7")
                    os.system("pvcreate {}".format(d1))
                    os.system("pvcreate {}".format(d2))
                    os.system("vgcreate {} {} {}".format(vg,d1,d2))
                    os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
                    os.system("tput setaf 6")
                    r=input("\n Press ENTER to check details of your partition")
                    print(r)
                    os.system("tput setaf 7")
                    os.system("lvdisplay {}/{}".format(vg,lv))
                    os.system("tput setaf 6")
                    path=input("Enter the LV Path : ")
                    print(path)
                    os.system("tput setaf 7")
                    os.system("mkfs.ext4 {}".format(path))
                    os.system("mkdir /l1")
                    os.system("mount {} /l1".format(path))
                    os.system("tput setaf 6")
                    print("\n Now enter the directory name as /l1 in next config file")
                    s=input("Press ENTER to continue")
                    print(s)		
                    os.system("tput setaf 7")
                    os.system("vim /etc/hadoop/hdfs-site.xml")
                    os.system("tput setaf 6")
                    print("DONE!!")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    Press 1 : To check details of physical volume (pv)
                    Press 2 : To check details of volume group (vg)
                    Press 3 : To check details of partition (lv)
                    Press 4 : To check details of all the partitions (lv)
                    Press 5 : To exit
                    Press 6 : To continue
                    """)
                    os.system("tput setaf 6")
                    chh=input("Enter your Choise : ")
                    print(chh)
                    os.system("tput setaf 7")
                    
                    if int(chh) == 1:
                        os.system("tput setaf 6")
                        c=input("Enter the name of pv : ")
                        print(c)
                        os.system("tput setaf 7")
                        os.system("pvdisplay {}".format(c))
                    elif int(chh) == 2:
                        os.system("vgdisplay {}".format(vg))
                    elif int(chh) == 3:
                        os.system("lvdisplay {}/{}".format(vg,lv))
                    elif int(chh) == 4:
                        os.system("lvdisplay")
                    elif int(chh) == 5:
                        exit()
                    #elif int(chh) == 6:
                        #(To continue)
                    else :
                        os.system("tput setaf 1")
                        print("WRONG INPUT")
                        os.system("tput setaf 7")

                else :
                    os.system("tput setaf 1")
                    print("WRONG INPUT")
                    os.system("tput setaf 7")
            elif int(ch) == 3:
                os.system("tput setaf 6")
                i=input("Press ENTER to check space left in your vg")
                print(i)
                vgg=input("Enter the vg name")
                print(vgg)
                os.system("tput setaf 7")
                os.system("vgdisplay {}".format(vgg))
                os.system("tput setaf 6")
                cont=input("Press ENTER to Continue")
                print(cont)
                size=input("Enter the size to extend")
                print(size)
                i1=input("Press ENTER to get details of lv in your system")
                print(i1)
                os.system("tput setaf 7")
                os.system("lvdisplay")
                os.system("tput setaf 6")
                i2=input("Press ENTER to continue")
                print(i2)
                i3=input("Enter the lv path")
                print(i3)
                os.system("tput setaf 7")
                os.system("lvextend --size +{}G {}".format(size,i3))
                os.system("resize2fs {}".format(i3))
                os.system("tput setaf 2")
                print("\nYour DataNode Storage has been successfully extended!!")
                os.system("tput setaf 7")

            elif int(ch) == 1:
                os.system("tput setaf 2")
                print("""
                Press 1 : To list the devices attached to this system
                Press 2 : to continue	
                """)
                
                os.system("tput setaf 6")
                ch1=input("Enter your choise : ")
                print(ch1)
                os.system("tput setaf 7")

                if int(ch1) == 1:
                    os.system("fdisk -l")
                    os.system("tput setaf 6")
                    d1=input("Enter 1st device : ")
                    print(d1)
                    d2=input("Enter 2nd device : ")
                    print(d2)
                    vg=input("Enter the vg name : ")
                    print(vg)
                    lv=input("Enter the name of partition(lv name) : ")
                    print(lv)
                    size=input("Enter the size of partition : ")
                    print(size)

                    os.system("tput setaf 7")
                    os.system("pvcreate {}".format(d1))
                    os.system("pvcreate {}".format(d2))
                    os.system("vgcreate {} {} {}".format(vg,d1,d2))
                    os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
                    os.system("tput setaf 6")
                    r=input("\n Press ENTER to check details of your partition")
                    print(r)
                    os.system("tput setaf 7")
                    os.system("lvdisplay {}/{}".format(vg,lv))
                    os.system("tput setaf 6")
                    path=input("Enter the LV Path : ")
                    print(path)
                    os.system("tput setaf 7")
                    os.system("mkfs.ext4 {}".format(path))
                    os.system("mkdir /l1")
                    os.system("mount {} /l1".format(path))
                    print("DONE!!")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    Press 1 : To check details of physical volume (pv)
                    Press 2 : To check details of volume group (vg)
                    Press 3 : To check details of partition (lv)
                    Press 4 : To check details of all the partitions (lv)
                    Press 5 : To exit
                    Press 6 : To continue
                    """)
                    os.system("tput setaf 6")
                    chh=input("Enter your Choise : ")
                    print(chh)
                    os.system("tput setaf 7")
                    
                    if int(chh) == 1:
                        os.system("tput setaf 6")
                        c=input("Enter the name of pv : ")
                        print(c)
                        os.system("pvdisplay {}".format(c))
                    elif int(chh) == 2:
                        os.system("vgdisplay {}".format(vg))
                    elif int(chh) == 3:
                        os.system("lvdisplay {}/{}".format(vg,lv))
                    elif int(chh) == 4:
                        os.system("lvdisplay")
                    elif int(chh) == 5:
                        exit()
                    #elif int(chh) == 6:
                        #(To continue)
                    else :
                        os.system("tput setaf 1")
                        print("WRONG INPUT")
                        os.system("tput setaf 7")
                elif int(ch1) == 2:
                    os.system("tput setaf 6")
                    d1=input("Enter 1st device : ")
                    print(d1)
                    d2=input("Enter 2nd device : ")
                    print(d2)
                    vg=input("Enter the vg name : ")
                    print(vg)
                    lv=input("Enter the name of partition(lv name) : ")
                    print(lv)
                    size=input("Enter the size of partition : ")
                    print(size)

                    os.system("tput setaf 7")
                    os.system("pvcreate {}".format(d1))
                    os.system("pvcreate {}".format(d2))
                    os.system("vgcreate {} {} {}".format(vg,d1,d2))
                    os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
                    os.system("tput setaf 6")
                    r=input("\n Press ENTER to check details of your partition")
                    print(r)
                    os.system("tput setaf 7")
                    os.system("lvdisplay {}/{}".format(vg,lv))
                    os.system("tput setaf 6")
                    path=input("Enter the LV Path : ")
                    print(path)
                    os.system("tput setaf 7")
                    os.system("mkfs.ext4 {}".format(path))
                    os.system("mkdir /l1")
                    os.system("mount {} /l1".format(path))
                    print("DONE!!")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    Press 1 : To check details of physical volume (pv)
                    Press 2 : To check details of volume group (vg)
                    Press 3 : To check details of partition (lv)
                    Press 4 : To check details of all the partitions (lv)
                    Press 5 : To exit
                    Press 6 : To continue
                    """)
                    os.system("tput setaf 6")
                    chh=input("Enter your Choise : ")
                    print(chh)
                    os.system("tput setaf 7")
                    
                    if int(chh) == 1:
                        os.system("tput setaf 6")
                        c=input("Enter the name of pv : ")
                        print(c)
                        os.system("tput setaf 7")
                        os.system("pvdisplay {}".format(c))
                    elif int(chh) == 2:
                        os.system("vgdisplay {}".format(vg))
                    elif int(chh) == 3:
                        os.system("lvdisplay {}/{}".format(vg,lv))
                    elif int(chh) == 4:
                        os.system("lvdisplay")
                    elif int(chh) == 5:
                        exit()
                    #elif int(chh) == 6:
                        #(To continue)
                    else :
                        os.system("tput setaf 1")
                        print("WRONG INPUT")
                        os.system("tput setaf 7")

                else :
                    os.system("tput setaf 1")
                    print("WRONG INPUT")
                    os.system("tput setaf 7")

            elif int(ch) == 5:
                exit()

            elif int(ch) == 4:
                break
                

            else :

                os.system("tput setaf 1")
                print("WRONG INPUT")
                os.system("tput setaf 7")
            
            input("\n\t\t\t\tPress enter to continue..")


    elif '4' in option:
        print("\n\t\tYou have entered Web Server option")
        print("\n\t\tNow webserver will be created in Aws")
        input("\npress enter to continue..")
        os.system("yum install httpd")
        print("\nApache web server has been installed")
        input("\npress enter to continue..")
        os.system("lsblk")
        print("\nListing Disk")
        input("\npress enter to continue..")
        os.system("mount /dev/xvdh /var/www/html")
        input("\Disk has been mounted on your web server")
        os.system("lsblk")
        input("\npress enter to continue..")
        a = input("\nenter your s3 bucket name : ")
        os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1".format(a))
        print("\ns3 bucket has been created..")
        print("\nNOw put your image file into linux root folder and rename it as test.jpg")
        input("\npress enter to continue..")
        os.system("aws s3 cp /root/test.jpg s3://{}/test.jpg".format(a))
        os.system("aws clountfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(a))
        print("\nNow enter your html data by pressing enter..")
        input("""if you don't know about html dont worry just copy it and paste in opening file and save it:
	    <h1>Welcome to webserver</h1>
	    <body bgcolor='aquablue' >
	    <p>Your webserver is configured! </p>

        if you copied then press any key:""")
        input("\npress enter to continue..")
        os.system("vim /var/www/html/web.html")
        input("\nyour web server has been created successfully  now search in brower by ip-adress/web.html")

    elif '5' in option:
        while True:
            os.system("tput setaf 3")
            print("\t\t\tWelcome to my menu :)")
            os.system("tput setaf 7")
            print("\t\t\t ---------------------")


            os.system("tput setaf 2")
            print("""
            \n
            Press 1 : To configure yum
            Press 2 : To check repolist (check if yum is configured or not)
            Press 3 : To check if software is present in yum or not
            Press 4 : To install any software
            Press 5 : To go to main menu
            Press 6 : To exit
            """)
            os.system("tput setaf 6")
            ch=input("Enter your Choise : ")
            print(ch)
            os.system("tput setaf 7")

                
            if int(ch) == 1:
                os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-	latest-8.noarch.rpm")
                os.system("dnf install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm")

            elif int(ch) == 2:
                os.system("yum repolist")

            elif int(ch) == 3:
                os.system("tput setaf 6")
                c=input("Enter the software name you want to check")
                print(c)
                os.system("tput setaf 7")
                os.system("dnf list {}".format(c))
            elif int(ch) == 4:
                os.system("tput setaf 6")
                c1=input("Enter the software name you want to install")
                print(c1)
                os.system("tput setaf 7")
                os.system("dnf install {}".format(c1))
            elif int(ch) == 5:
                break
            elif int(ch) == 6:
                exit()
            else :
                os.system("tput setaf 1")
                print("WRONG INPUT")
                os.system("tput setaf 7")
            
            input("\nPress enter to continue...")

    elif '6' in option:
        while True:
            print("""1.ConFigure Docker On  Your OS
            2.TO stop docker
            3.To start docker
            4.To launching Container
            5. To start and attach container (it is for already existed container)
            6. to stop container
            7. To check how many container is running
            8. To check how many container is present in your docker(either stopped or running)
            9. To Delete/ Remove the container 
            10. To go back to main menu
            11. exit	
                """)
            os.system("tput setaf 7")
            i_n = int(input("enter your choice:"))

            #os.system("gedit")
            if i_n == 1:
                os.system("tput setaf 2")
                print("""1.For ConFiguring  Docker On  Your OS.
                        there are some steps required to do
                        Step 1.Check for Docker repo if not there then add
                        step 2.Install docker 
                        step 3.Start docker service
                    
                    """)
                os.system("tput setaf 7")
                print("now 1st step started....")
                print("checking for docker repo...")
                os.system("yum repolist")
                check = input("see there is any repo of docker if yes then type y or Y and if no then type n or N")
                if check == "N" or check == "n" :
                    
                    a = input("""copy this and paste it when editor will open .
            [docker123]
            baseurl=http://download.docker.com/linux/centos/7/x86_64/stable/
            gpgcheck=0

            if copied then press any key:""")
                    os.system("cd //etc//yum.repos.d && gedit docker1.repo")
                print("step 1 completed!")
                print("moving to step 2nd ")
                print("step 2 started...")
                print("if there ask for y/n then press y")
                os.system("yum install docker-ce --nobest")
                print("2nd step completed")
                print("step 3 starting docker service")
                os.system("systemctl enable docker")
                print("step 3rd completed")
                print("your docker configured!")
            elif i_n == 2:
                os.system("systemctl stop docker")
            elif i_n == 3:
                os.system("systemctl start docker")
            elif i_n == 4:
                print("""for launching the container/Os:-
                        there are some step to follow 
                        1.download the container
                        2.Install and Run the container 
                        """)
                print("step1 begins....")
                os_name = input("which container/os do you want to download enter name:")
                p = "docker pull " +os_name
                os.system(p)
                print("step 1 completed")
                print("-----------------------------------------------------")
                print("step2 begins....")
                os_= input("which container/os do you want to launch enter name : version(e.g: centos:8,ubuntu 14.04):")
                os_name = input("Enter your Container name :")
                p = "docker run -it --name " +os_name+" "+os_
                os.system(p)
                print("step 2 completed")
                print("-----------------------------------------------------")
            elif i_n == 5:
                os_name = input("Enter your Container name :")
                p = "docker start " + os_name
                os.system(p)
                p = "docker attach " + os_name
                os.system(p)
            elif i_n == 6:
                os_name = input("Enter your Container name :")
                p = "docker stop " + os_name
                os.system(p)
            elif i_n == 7:
                os.system("docker ps")
            elif i_n == 8:
                os.system("docker ps -a")
            elif i_n == 9:
                ask = input("You have to know Container ID to remove It, Do you know Container ID(y/n): ")
                if ask == "y":
                    os_name = input("Enter your Container ID:")
                else:
                    os.system("docker ps -a")
                    pr=input("Which container do you want to remove and Copy the Id of container,If copied then press any key:")
                    os_name = input("Enter your Container ID:")
                    
                p = "docker rm " + os_name
                os.system(p)
            
            if i_n == 10:
                break

            if i_n == 11:
                exit()
            else:
                print("\nInvalid choice!")

            input("\nPress enter to continue..")

    else:
        print("\nwrong choice...")

    input("\n\t\t\t\tPress enter to continue..")




    
