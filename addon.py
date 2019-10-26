from xbmcswift2 import Plugin, xbmcgui
from resources.lib import freethoughtradio

plugin = Plugin()
URL = "https://ffrf.libsyn.com/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.libsyn.com%2Fp%2Fassets%2F6%2Fe%2F5%2F6%2F6e56d84bbcb7efba%2Fft-radio-blogs_1200x1200.jpg&f=1"},        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.libsyn.com%2Fp%2Fassets%2F6%2Fe%2F5%2F6%2F6e56d84bbcb7efba%2Fft-radio-blogs_1200x1200.jpg&f=1"},
    ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = freethoughtradio.get_soup(URL)
    playable_podcast = freethoughtradio.get_playable_podcast(soup)
    items = freethoughtradio.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = freethoughtradio.get_soup(URL)
    playable_podcast1 = freethoughtradio.get_playable_podcast1(soup)
    items = freethoughtradio.compile_playable_podcast1(playable_podcast1)
    return items
if __name__ == '__main__':
    plugin.run()
