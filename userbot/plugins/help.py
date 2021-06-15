# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import redis
import sys
import platform
import asyncio
from asyncio import create_subprocess_exec as asyncrunapp
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.events import register
from sys import version_info
from telethon import version
from platform import uname
from userbot import events

modules = CMD_HELP

# Ported by KENZO (Lynx-Userbot)
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Plugin tidak ditemukan.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("⚡")
        await asyncio.sleep(3)
        await event.edit("**Exvop UserBot**\n\n"
                         f"*Bot Dari {DEFAULTUSER}**\n**Modul: {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"                                                                                                                                                                                                                                                                                       
                         f"╰►| {string} ◄─\n\n")
        await event.reply(f"\n__Contoh__ : Ketik » `.help afk` Untuk Informasi Pengunaan Plugin afk.\nAtau Bisa Juga Dengan Cara, Ketik `.helpme` Untuk Menggunakan Inline Bot Dari @BotFather.\n Jika Tidak Tahu Caranya, Silahkan Bertanya ke » [sini](t.me/badboyanim « Terimakasih 🙏")
        await asyncio.sleep(1000)
        await event.delete()
