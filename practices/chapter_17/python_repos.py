import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code:', r.status_code)

# 将API响应储存到一个变量中
response_dict = r.json()

# 处理响应结果
# print(response_dict.keys())
# print(response_dict['incomplete_results'])
print('Total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict.keys()))
# for key in sorted(repo_dict.keys()):
#     print(key)

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
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
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos1.svg')






