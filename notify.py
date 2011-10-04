# XChat Twitter DM notify plugin
# Copyright (C) 2011 Marco Mornati <ilmorna@gmail.com>
#
#   This library is free software; you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by the
#   Free Software Foundation; either version 3 of the License, or (at your
#   option) any later version.
#
#   This library is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
#   for more details.
#
# This script will check any chat message to you in your xchat (in DirectMessage are or in main chat directed to you)
# and will send a direct message to the configured twitter account.
# To use it you need to create a new application in your twitter account to retrieve consumer_key, secrets and access information
# Your application should naturally has read and write access to your twitter account
#

__module_name__ = "twitternotify"
__module_version__ = "0.1"
__module_description__ = "Notify direct messages to twitter"

import os
import twitter
pid = os.getpid()

import xchat
xchat.prnt(__module_description__ + " loaded")


def send_dm_twitter(word):
    api = twitter.Api(consumer_key='yourkey', consumer_secret='yoursecret', access_token_key='acctoken', access_token_secret='accsecret')
    credentials = api.VerifyCredentials()
    if credentials:
        print "Logged as %s" % credentials.name

    status = api.PostDirectMessage('twitter_nick', '%s: %s' % (word[0], word[1]))
    print status.created_at


def focus_cb(word, word_eol, userdata):
    send_dm_twitter(word)
    return xchat.EAT_NONE

def highlight_cb(word, word_eol, userdata):
    send_dm_twitter(word) 
    return xchat.EAT_NONE

def private_cb(word, word_eol, userdata):
    send_dm_twitter(word)    
    return xchat.EAT_NONE

xchat.hook_print("Focus Tab", focus_cb)
xchat.hook_print("Channel Action Hilight", highlight_cb)
xchat.hook_print("Channel Msg Hilight", highlight_cb)
xchat.hook_print("Private Message", private_cb)
xchat.hook_print("Private Message to Dialog", private_cb)
