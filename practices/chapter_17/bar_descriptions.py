import pygal
import requests
import json
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()

repo_dicts = response_dict['items']
# print(repo_dicts)
# print(repo_dicts[0]['description'])

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # 处理属性为空的情况
    if repo_dict['description'] == None:
        print(repo_dict['name'] + 'has nothing in description.')
        repo_dict['description'] = 'nothing to show'
    if repo_dict['html_url'] == None:
        print(repo_dict['name'] + 'has nothing in html_url.')
        repo_dict['html_url'] = 'https://www.baidu.com'
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# plot_dicts = [
#     {'value': 16101, 'label': 'Description of httpie.'},
#     {'value': 15028, 'label': 'Description of django.'},
#     {'value': 14798, 'label': 'Description of flask.'},
# ]
print(len(names), names)
print(len(plot_dicts), plot_dicts)
# with open('WTF.json', 'w') as f:
#     json.dump(plot_dicts, f)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects'
chart.x_labels = names
# chart.x_labels = ['haha', 'heihei', 'houhou']
chart.add('', plot_dicts)
chart.render_to_file('python_repos2.svg')
# 思考: 为什么这里不加这些个config就会报错,还他妈是解码错误.
