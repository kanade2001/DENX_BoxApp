#!usr/bin/python
# -*- coding: utf-8 -*-

import cgi # CGIモジュールのインポート
import cgitb


cgitb.enable() # デバッグに使うので、本番環境では記述しない

print("Content-Type: text/html; charset=shift_jis") # HTMLを記述するためのヘッダ
print()

form = cgi.FieldStorage()

print('<p>こんにちは！%sさん</p>' % (form['username'].value))

# username, showname, studentid, nfcidをmember.csvに登録