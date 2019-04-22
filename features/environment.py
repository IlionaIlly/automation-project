
def before_all(context):
    userdata = context.config.userdata

    if "browser" in userdata:
        context.browser = userdata['browser']

    if "url" in userdata:
        context.url = userdata['url']
