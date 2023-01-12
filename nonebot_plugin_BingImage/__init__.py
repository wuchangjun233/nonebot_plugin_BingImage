from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.ntchat import MessageSegment
from nonebot.adapters.ntchat import MessageEvent
from nonebot.log import logger


from .utils import *

Help_info = "Bing机器人帮助 \n🌈世界那么大，通过Bing到处看看~ \n🗺 /bing 获取今天的美图(图和故事) \n💻/bing电脑 获取今天的美图(单横板图片)\n📱/bing手机 获取今天的美图(单竖版图片)\n🔧更多功能开发中🔧 "

help_matcher = on_command("bing帮助", aliases={'Bing帮助', '必应帮助', },priority=21)
bing_matcher = on_command("bing", aliases={'必应', 'bing每日一图', 'bing美图', 'Bing', 'BING'},priority=22)

bing_desktop_matcher = on_command("bing电脑图片",
                                  aliases={'bing桌面端图片', '电脑图片', '桌面端图片', 'bing电脑', 'bing桌面图片',
                                           'bing横版'}, priority=23)
bing_mobile_matcher = on_command("bing手机图片",
                                 aliases={'bing移动端图片', '手机图片', '移动端图片', 'bing手机', 'bing竖版', },
                                 priority=24)


@help_matcher.handle()
async def help(bot: Bot, event: MessageEvent):
    await help_matcher.send(str(MessageSegment.text(Help_info)))


@bing_matcher.handle()
async def bing(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingImageURL())
    description = getBingDescription()
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    msg_title = str(description['title'])
    msg_headline = str("图片主题：" + description['headline'])
    msg_desc = str("图片故事：" + description['description'])
    msg_maintext = str("图片介绍：" + description['main_text'])
    msg = msg_title + ("\n") + ("\n") + msg_headline + ("\n") + (
        "\n") + msg_maintext + ("\n") + ("\n") + msg_desc
    await bing_matcher.send(MessageSegment.text(msg) + msg_img)
    logger.info("消息发送成功!")


@bing_desktop_matcher.handle()
async def bing_desktop(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingImageURL())
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    await bing_desktop_matcher.send(msg_img)
    logger.info("消息发送成功!")


@bing_mobile_matcher.handle()
async def bing_mobile(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingVerticalImageURL())
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    await bing_mobile_matcher.send(msg_img)
    logger.info("消息发送成功!")
