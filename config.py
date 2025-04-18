# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	FALSE	1774617414	SID	g.a000twhbPhyf2nFBEJjrhZsrmKTckE7bLwTFbSBukHFUWBiuZDEANlHW2nFrPbk-2mtqBt-d3wACgYKAb0SARQSFQHGX2MisovKvTPzjDYJ0Xwze12l_xoVAUF8yKqlWBuX3-xgbdgkx1WDDNqx0076
.youtube.com	TRUE	/	TRUE	1771593414	__Secure-1PSIDTS	sidts-CjIBEJ3XV0iE8Jj7Vr-Vee325nUrFC62rEqAHPcr3O-qkwuqIR7Xc4_G4L_OKG3l_w4NsBAA
.youtube.com	TRUE	/	TRUE	1771593414	__Secure-3PSIDTS	sidts-CjIBEJ3XV0iE8Jj7Vr-Vee325nUrFC62rEqAHPcr3O-qkwuqIR7Xc4_G4L_OKG3l_w4NsBAA
.youtube.com	TRUE	/	TRUE	1774617414	__Secure-1PSID	g.a000twhbPhyf2nFBEJjrhZsrmKTckE7bLwTFbSBukHFUWBiuZDEAKXm0w7jfCTmCuNTdYxGF_QACgYKAT0SARQSFQHGX2MicMAaTpGO462Jp32pTV2Y2BoVAUF8yKqDRYUSz4kDTBxuxabX0vQy0076
.youtube.com	TRUE	/	TRUE	1774617414	__Secure-3PSID	g.a000twhbPhyf2nFBEJjrhZsrmKTckE7bLwTFbSBukHFUWBiuZDEAaJIt_rPwYuWx7L_pBvg9EQACgYKAdcSARQSFQHGX2MiUPmQXYsWqeGPEM6Qc5m7ehoVAUF8yKqMxBVhj83rcn9a-GefUWRH0076
.youtube.com	TRUE	/	FALSE	1774617414	HSID	AnSge7RMzY3sVT1iq
.youtube.com	TRUE	/	TRUE	1774617414	SSID	AbIIvQfcjNFQUUFIU
.youtube.com	TRUE	/	FALSE	1774617414	APISID	fJ-fKDh7dZsRBtJQ/AUxca7UUaSx7aPRTj
.youtube.com	TRUE	/	TRUE	1774617414	SAPISID	EOUYKa4zPNr0K9Dw/AEVRuBpKdzOrBobqd
.youtube.com	TRUE	/	TRUE	1774617414	__Secure-1PAPISID	EOUYKa4zPNr0K9Dw/AEVRuBpKdzOrBobqd
.youtube.com	TRUE	/	TRUE	1774617414	__Secure-3PAPISID	EOUYKa4zPNr0K9Dw/AEVRuBpKdzOrBobqd
.youtube.com	TRUE	/	FALSE	1772111087	SIDCC	AKEyXzXf5OmbH0cP4aFMZGupVrlXVCihmSv6lD038kwxakL7tMDHRP1rx5xPCUpzfoPrwvU-
.youtube.com	TRUE	/	TRUE	1772111087	__Secure-1PSIDCC	AKEyXzXChNra_IXuQJKaq20GKplogFwYTWpL6LdEo19sXc3sLR1u0w5hNtADG4JR-qYHcWNN
.youtube.com	TRUE	/	TRUE	1772111087	__Secure-3PSIDCC	AKEyXzXrYv0M1M62I_ztAf-x1Y-cUXtWETZLGst5O4CLWvrtcJpzOHb01AvmsGq9bGu8GEDxpw
.youtube.com	TRUE	/	TRUE	1774617835	LOGIN_INFO	AFmmF2swRQIgZ3gelzAYyDkFbnwB75GBC_KK3--cw3_tG3Yan3lyVtsCIQDUmFJg2lVRVGk2ZepuxJXlSLYD1b1DLk12PT8LuoOKXQ:QUQ3MjNmeVNXTmtNcjZodE1PcTFBMTUtV0N2TXJsVHpuRS02bkFMaklsdFlwaUJITENaQ1ZUNlUzdEdFRjlqQW10c0NUYXRxSW1OaFpsNXgtcV84NWRqR0MwUkFzcE9KcUtxYXZWNFhmMzJ6N0pBVWlPUXMyd3ctNTd6ZW1qZ1B6b1lIYVo2UXRfNm5PUFY3YTJyUE9QbTNCcEw4THI3clNn
.youtube.com	TRUE	/	TRUE	1756122389	__Secure-ROLLOUT_TOKEN	CL-gmfP10OPZigEQy6WcyazSiwMYr-be_qHhiwM%3D
.youtube.com	TRUE	/	TRUE	1756127082	VISITOR_INFO1_LIVE	sLtxd7RaOq4
.youtube.com	TRUE	/	TRUE	1756127082	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgJQ%3D%3D
.youtube.com	TRUE	/	TRUE	1775135082	PREF	f6=40000000&tz=Asia.Kolkata&f7=100
.youtube.com	TRUE	/	FALSE	1740121460	ST-10d87nd	csn=RWQXIQky0d9RTq8C&itct=CG0Q_FoiEwj-h5XHmdSLAxXXjWYCHfRUEBsyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	FALSE	1740145530	ST-x3zc7r	csn=VNEM7hwVfOiXXS9K&itct=CGoQ_FoiEwiM5s6c89SLAxV2tFYBHY28ErMyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	FALSE	1740398801	ST-h3az29	csn=1dm2HeRfs0reoVLa&itct=CG0Q_FoiEwjT8tfdotyLAxWit1YBHVL-NqIyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
.youtube.com	TRUE	/	TRUE	1740407913	CONSISTENCY	AKreu9tLY14tChaHrxa17p4wopqr1NoI4Y2fri3ctp5lE81gJzu2WCuO97-nthENFGTSIB0wSymMSCCYxtR3L-i7q-CX6Gfy4IW5wAqZQ891ym3cW3LcbPitDII
.youtube.com	TRUE	/	FALSE	1740407388	ST-1yod0rt	csn=xbaMD_ZSl3bDpf1D&itct=CBAQ1TYiEwixs5u8wtyLAxVchNgFHfWHEqs%3D
.youtube.com	TRUE	/	TRUE	0	YSC	dHbtgZbNhUI
.youtube.com	TRUE	/	FALSE	1740575089	ST-13avi31	csn=TMcaElOy7oFUEZ6t&itct=CG0Q_FoiEwjjpby6s-GLAxXozjQHHVTGMoYyCmctaGlnaC1yZWNaD0ZFd2hhdF90b193YXRjaJoBBhCOHhieAQ%3D%3D
"""

API_ID = os.getenv("API_ID", "21018643")
API_HASH = os.getenv("API_HASH", "f92d506e522055e5bc182420c19900ca")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "") # for session encryption
IV_KEY = os.getenv("IV_KEY", "") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
