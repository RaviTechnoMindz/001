class script(object):
    START_TXT = """š·š“š»š»š¾ š {},
š¼š š½š°š¼š“ šøš <a href=https://t.me/{}>{}</a>, šø š²š°š½ šæšš¾ššøš³š“ š¼š¾ššøš“š š, š¹ššš š°š³š³ š¼š“ šš¾ šš¾šš š¶šš¾ššæ š°š½š³ š¼š°šŗš“ š¼š“ š°š³š¼šøš½.. šš·š“š½ šš“š“ š¼š šæš¾šš“šš š¦¾\n\nšš ššššššš ššš\n<a href=https://t.me/Technomindzyt><b>ą¼ā¬š”šš„šššššššā¬ą¼</b></a>"""
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš š¼š š·š“š»šæ š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """<b>ā® š¼š š½š°š¼š“: šššššš ššššš</b>
<b>ā® š²šš“š°šš¾š: <a href=https://t.me/Technomindzyt><b>ź§ą¼ā¬š”šš„šššššššā¬ą¼ź§</b></a>
<b>ā® š»šøš±šš°šš: šæššš¾š¶šš°š¼</b>
<b>ā® š»š°š½š¶šš°š¶š“: šæššš·š¾š½ š¹</b>
<b>ā® š³š°šš° š±š°šš“: š¼š¾š½š¶š¾-š³š±</b>
<b>ā® š±š¾š šš“ššš“š: š·š“šš¾šŗš</b>
<b>ā® š±ššøš»š³ ššš°ššš: š1.0.43</b>
<b>ā® ššæš³š°šš“š: <a href=https://t.me/tmmainchannel>šššššš ššššš</a></b>
<b>ā® šš¾šššš±š“ š²š·š°š½š½š“š»: <a href=https://www.youtube.com/c/TechnoMindz>šššššš ššššš</a></b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban_user  - <code>to ban a user.</code>
ā¢ /unban_user  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>
<b>DEVS:</b>
- <a href=https://t.me/tmmainchannel><b>šššššš ššššš</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particular keyword and šššššš ššššš  will respond whenever a keyword is found the message
<b>NOTE:</b>
1. šššššš ššššš should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-šššššš ššššš  Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. šššššš ššššš supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/tmmainchannel)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>š°ššš¾ šµšøš»šš“š š¾š½/š¾šµšµ š¼š¾š³šš»š“..</b>
<b>š°ššš¾ šµšøš»šš“š šøš šš·š“ šµš“š°šššš“ šš¾ šµšøš»šš“š š°š½š³ šš°šš“  šš·š“ šµšøš»š“š š°ššš¾š¼š°ššøš²š°š»š»š šµšš¾š¼ š²š·š°š½š½š“š» šš¾ š¶šš¾ššæ. šš¾š š²š°š½ ššš“ šš·š“ šµš¾š»š»š¾ššøš½š¶ š²š¾š¼š¼š°š½š³š šš¾ š¾š½ š°š½š³ š¾šµšµ šš·š“ š°ššš¾šµšøš»šš“š šøš½ šš¾šš š¶šš¾ššæ.../</b>
<b>š²š¾š¼š¼š°š½š³š :-
<b>āŗāŗ /autofilter on - š“š½š°š±š»š“ š°ššš¾ šµšøš»šš“š šøš½ šš·š“ š¶šš¾ššæš.</b>
<b>āŗāŗ /autofilter off - š³šøšš°š±š»š“š³ š°ššš¾ šµšøš»šš“š šøš½ šš·š“ š¶šš¾ššæš.</b>
<b>āŗāŗ /set_template - šš“š š²šššš¾š¼ šøš¼š³š± šš“š¼šæš»š°šš“ šµš¾š š°ššš¾ šµšøš»šš“š.</b>
<b>āŗāŗ /get_template - š¶š“š š²šššš“š½š šøš¼š³š± šš“š¼šæš»š°šš“ š¾šµ š°ššš¾ šµšøš»šš“š.</b>
<b>š²šš“š³šøšš :- <a href=https://t.me/tmmainchannel>šššššš ššššš</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Techno Mindz
<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specifed user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code>
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š²š·š°šš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā Made By @TmMainChannel"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewBotUser
ID - <code>{}</code>
Name - {}
@TmMainChannel
"""
