import yaml

with open("data.yaml" , 'r') as f:
    data = yaml.full_load((f))

data['names'] = ['box' , 'pallet']
data['nc'] = 2

with open("data.yaml" , 'w') as f:
    yaml.dump(data , f)

