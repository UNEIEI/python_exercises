from flask import Flask
from werkzeug.routing import Baseconverter
from flask.ext.script import Manager

#flask动态路由只提供了 int, float, path 三种转换器
#如果要在flask程序的动态路由中使用regex转换器
class RegexConverter(Baseconverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex=items[0]
        
app = Flask(__name__)
#添加RegexConverter. dict[new_key]=new_value
app.url_map.converters['regex'] = RegexConverter

manager = Manager(app) 

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#定义模版过滤器，转义模版中的markdown
@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)  #在模版中使用：{{ txt|md }}
    
#使用regex动态路由示例
@app.route('/user/<regex("[a-z]{3}"):username>') 
def user(username):
    return 'Hello %s' % username      

#更新代码时，实时刷新呈现运行效果    
@manager.command  #增加命令行指令 dev
def dev():        #运行命令：python flask_test.py dev
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')     #实时监测当前文件夹下所有文件，也可指定某个文件，如'static/*.*'
    live_server.serve(open_url=True)
    
if __name__ = '__main__':
    manager.run()  #启动服务器：python flask_test.py runserver