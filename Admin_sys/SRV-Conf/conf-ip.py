import json
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def load_json_data_from_file(file_path):
    checkpath = verify_path(file_path)
    if checkpath == False:
        print(f"File {file_path} not found ")
        return False
    else:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data

def conf_datajson():
    return load_json_data_from_file(file_path='data/static.json')

def render_config(template_name, data):
    template = env.get_template(template_name)
    return template.render(data)


def save_built_conf(file_name, data):
    with open(file_name, 'w') as config_file:
        config_file.write(data)
    return True


def verify_path(file_path):
    try:
        with open(file_path) as f:
            pass
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return False
    

def create_config():
    try:
        return render_config('netplan-conf.j2', conf_datajson())
    except Exception as e:
        print(f"Une erreur s'est produite lors de la mise en place de la configuration : {str(e)}")
        return None
    

if __name__=="__main__":

    conf = create_config()
    print(conf)
    save_built_conf('test.yaml', conf)