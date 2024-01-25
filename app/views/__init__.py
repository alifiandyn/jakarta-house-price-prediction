from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('app/views/'))

# navbar = [['Home','/'],['Dataset', '/dataset'],['Exploratory Data Analysis','/eda'],['About','/about'],['Profile','/profile']]
navbar = [['Home','/'],['Dataset', '/dataset'],['Exploratory Data Analysis','/eda'],['Profile','/profile']]

def home(title,cardData,jakartaGeoJson):
    data = {
        'title': title,
        'navbarData':navbar,
        'navPosition':'Home',
        'cardData': cardData,
        'jakartaGeoJson': jakartaGeoJson,
    }
    template = env.get_template('index.html')
    rendered_html = template.render(data)
    return rendered_html

def dataset(title,dataset):
    data = {
        'title': title,
        'navbarData':navbar,
        'navPosition':'Dataset',
        'dataset':dataset
    }
    template = env.get_template('dataset.html')
    rendered_html = template.render(data)
    return rendered_html

def eda(title, heatmap, heatmapByPrice):
    data = {
        'title': title,
        'navbarData':navbar,
        'navPosition':'Exploratory Data Analysis',
        'heatmap':heatmap,
        'heatmapByPrice':heatmapByPrice,
    }
    template = env.get_template('eda.html')
    rendered_html = template.render(data)
    return rendered_html

def about(title):
    data = {
        'title': title,
        'navbarData':navbar,
        'navPosition':'About'
    }
    template = env.get_template('about.html')
    rendered_html = template.render(data)
    return rendered_html

def profile(title):
    data = {
        'title': title,
        'navbarData':navbar,
        'navPosition':'Profile'
    }
    template = env.get_template('profile.html')
    rendered_html = template.render(data)
    return rendered_html