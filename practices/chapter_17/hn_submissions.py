import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()[:10]
submission_dicts = []
print('IDs are:', submission_ids)
count = 1
for submission_id in submission_ids:
    # 对于每篇文章执行API调用
    url = 'https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json'
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    if submission_r.status_code == 200:
        print('successful! num'+str(count))
        count += 1

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, comment_dicts = [], []
for submission_dict in submission_dicts:
    # print('\nSubmission Title:', submission_dict['title'])
    # print("Discussion link:", submission_dict['link'])
    # print("Comments:", submission_dict['comments'])
    titles.append(submission_dict['title'])
    comment_dict = {
        'value': submission_dict['comments'],
        'xlink': submission_dict['link'],
    }

    comment_dicts.append(comment_dict)

my_style = LS('#336633', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart_cmt = pygal.Bar(my_config, style=my_style)
chart_cmt.x_labels = titles
chart_cmt.add('cmts', comment_dicts)
chart_cmt.render_to_file('hn_submission_visual.svg')


