import yaml
def utils_cart_quantities(file):
    with open(file,'r',encoding="utf-8") as f:
        return yaml.safe_load(f)