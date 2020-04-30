#! /usr/bin/python3.6

env = input("Enter environment(PRD/MGT/CMH etc): ")
file = input("Enter the prefix file name: ")
# opening the file
f = open(file,'r')
a = []
for x in f:
    # Stripping new line
    prefix = x.rstrip()

    # splitting IP & mask and removing new line
    name = "NET-{}-{}-{}".format(env,x.split('/')[0].rstrip(),x.split('/')[1].rstrip())
    
    print("set address {} ip-netmask {}".format(name,prefix))
    a.append(name)

b = ' '.join(a)
print("set address-group NET-{}-SUBNETS static [ {} ]".format(env,b))
f.close()
