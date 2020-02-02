# Multiple Choice for Anki
#
# Copyright (C) 2018-2020  zjosua <https://github.com/zjosua>
#
# This file is based on __init__.py from Glutanimate's
# Cloze Overlapper Add-on for Anki
#
# Copyright (C)  2016-2019 Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from aqt import gui_hooks, mw

from .main import *
from .sc_template import initializeSCModels
from .mc_template import initializeMCModels
from .kprim_template import initializeKprimModels

def delayedInit():
    initializeSCModels()
    initializeMCModels()
    initializeKprimModels()

gui_hooks.profile_did_open.append(delayedInit)
gui_hooks.webview_did_receive_js_message.append(on_js_message)
gui_hooks.card_will_show.append(prepare_answer)
mw._multiple_choice = MultipleChoice()