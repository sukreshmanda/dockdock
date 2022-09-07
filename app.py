from subprocess import check_output
import codecs
import re


class Container:
    def __init__(self, container_id, image, command, created, status, ports, names):
        self.id = container_id
        self.image = image
        self.command = command
        self.created = created
        self.status = status
        self.ports = ports
        self.names = names

    def __str__(self):
        return f'{self.id} {self.image} {self.command} {self.created} {self.status} {self.ports} {self.names}\n'

    def __repr__(self):
        return f'{self.id} {self.image} {self.command} {self.created} {self.status} {self.ports} {self.names}\n'


def docker_ps(hyphen_a=None, filter_out=None, hyphen_n=None):
    if hyphen_a is True:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "ps", "-a"]))) if x != '']
    elif filter_out is not None:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "ps", "--filter", filter_out]))) if
               x != '']
    elif hyphen_n is not None:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "ps", "-n", str(hyphen_n)]))) if
               x != '']
    else:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "ps"]))) if x != '']

    for i in range(len(out)):
        temp = [x for x in re.split(r'   ', out[i]) if x != '']
        if len(temp) == 6:
            temp.insert(5, "")
        out[i] = Container(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6])
    return out


class Image:
    def __init__(self, repo, tag, image_id, created, size):
        self.repo = repo
        self.tag = tag
        self.image_id = image_id
        self.created = created
        self.size = size

    def __str__(self):
        return f'{self.repo} {self.tag} {self.image_id} {self.created} {self.size}\n'

    def __repr__(self):
        return f'{self.repo} {self.tag} {self.image_id} {self.created} {self.size}\n'


def docker_images(name=None, filter_out=None):
    if name is not None:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "images", name]))) if x != '']
    elif filter_out is not None:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "images", "--filter", filter_out]))) if x != '']
    else:
        out = [x for x in re.split(r'\n', codecs.decode(check_output(["docker", "images"]))) if x != '']
    for i in range(len(out)):
        temp = [x for x in re.split(r'   ', out[i]) if x != '']
        out[i] = Image(temp[0], temp[1], temp[2], temp[3], temp[4])
    return out


print(docker_images(filter_out="dangling=false"))
