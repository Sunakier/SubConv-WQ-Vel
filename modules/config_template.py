template_default = {
    "HEAD": {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "external-controller": ":9090",

        "dns": {
            "enable": True,
            "listen": "0.0.0.0:1053",
            "default-nameserver": [
                "223.5.5.5",
                "8.8.8.8",
                "1.1.1.1"
            ],
            "nameserver-policy": {
                "geosite:gfw,geolocation-!cn": [
                    "https://1.1.1.1/dns-query",
                    "https://1.0.0.1/dns-query",
                    "https://8.8.8.8/dns-query"
                ]
            },
            "nameserver": [
                "https://223.5.5.5/dns-query",
                "https://1.12.12.12/dns-query",
                "https://8.8.8.8/dns-query"
            ],
            "fallback": [
                "https://1.1.1.1/dns-query",
                "https://1.0.0.1/dns-query",
                "https://8.8.8.8/dns-query"
            ],
            "fallback-filter": {
                "geoip": False,
                "geoip-code": "CN",
                "ipcidr": [
                    "240.0.0.0/4"
                ]
            },
            "fake-ip-filter": [
                "+.lan",
                "+.microsoft*.com",
                "localhost.ptlogin2.qq.com"
            ]
        }
    },

    # test_url = "https://www.apple.com/library/test/success.html"
    "TEST_URL": "https://www.gstatic.com/generate_204",

    "RULESET": [
        ["ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/OpenAi.list"],
        ["ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/ChatBot.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/LocalAreaNetwork.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/UnBan.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanAD.list"],
        ["应用净化", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanProgramAD.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyList.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyListChina.list"],
        ["隐私防护", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyPrivacy.list"],
        ["谷歌FCM", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/GoogleFCM.list"],
        ["谷歌服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Google.list"],
        # ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/GoogleCN.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Adobe.list"],
        ["微软Bing", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Bing.list"],
        ["微软云盘", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/OneDrive.list"],
        ["微软服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Microsoft.list"],
        ["苹果服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Apple.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Telegram.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Epic.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Origin.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Sony.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Steam.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Nintendo.list"],
        ["YouTube", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/YouTube.list"],
        ["国内媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaMedia.list"],
        ["国外媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ProxyMedia.list"],
        ["节点选择", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ProxyGFWlist.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaIp.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaDomain.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaCompanyIp.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Download.list"],
        ["全球直连", "[]GEOIP,CN"],
        ["漏网之鱼", "[]FINAL"]
    ],

    "CUSTOM_PROXY_GROUP": [
        {
            "name": "自动选择",
            "type": "url-test",
            "rule": False
        },
        {
            "name": "手动切换1",
            "type": "select",
            "manual": True,
            "rule": False
        },
        {
            "name": "手动切换2",
            "type": "select",
            "manual": True,
            "rule": False
        },
        {
            "name": "故障转移",
            "type": "fallback",
            "rule": False
        },
        {
            "name": "负载均衡",
            "type": "load-balance",
            "rule": False
        },
        {
            "name": "香港负载均衡",
            "type": "load-balance",
            "rule": False,
            "regex": r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        },

        # Rule groups
        {
            "name": "ChatBot",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "Telegram",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "YouTube",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "国外媒体",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "国内媒体",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "谷歌FCM",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "谷歌服务",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "微软Bing",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "微软云盘",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "微软服务",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "苹果服务",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "Telegram",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "全球直连",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "广告拦截",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "应用净化",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "隐私防护",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "漏网之鱼",
            "type": "select",
            "prior": "PROXY"
        },

        # Region groups
        {
            "name": "香港节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        },
        {
            "name": "台湾节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇹🇼|TW|Taiwan|新北|彰化|CHT|台|HINET"
        },
        {
            "name": "狮城节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇸🇬|SG|Singapore|狮城|^新[^节北]|[^刷更]新[^节北]"
        },
        {
            "name": "日本节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇯🇵|JP|Japan|Tokyo|Osaka|Saitama|东京|大阪|埼玉|日"
        },
        {
            "name": "韩国节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇰🇷|KO?R|Korea|首尔|韩|韓"
        },
        {
            "name": "美国节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇺🇸|US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥"
        }
    ]
}

template_zju = {
    "HEAD": {
        "mixed-port": 7890,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "external-controller": ":9090",

        "dns": {
            "enable": True,
            "listen": "0.0.0.0:1053",
            "default-nameserver": [
                "223.5.5.5",
                "8.8.8.8",
                "1.1.1.1"
            ],
            "nameserver-policy": {
                "geosite:gfw,geolocation-!cn": [
                    "https://1.1.1.1/dns-query",
                    "https://1.0.0.1/dns-query",
                    "https://8.8.8.8/dns-query"
                ],
                "+.zju.edu.cn": [
                    "10.10.0.21",
                    "https://1.1.1.1/dns-query",
                    "https://1.0.0.1/dns-query",
                    "https://8.8.8.8/dns-query"
                ]
            },
            "nameserver": [
                "https://223.5.5.5/dns-query",
                "https://1.12.12.12/dns-query",
                "https://8.8.8.8/dns-query"
            ],
            "fallback": [
                "https://1.1.1.1/dns-query",
                "https://1.0.0.1/dns-query",
                "https://8.8.8.8/dns-query"
            ],
            "fallback-filter": {
                "geoip": False,
                "geoip-code": "CN",
                "ipcidr": [
                    "240.0.0.0/4"
                ]
            },
            "fake-ip-filter": [
                "+.lan",
                "+.microsoft*.com",
                "localhost.ptlogin2.qq.com"
            ]
        }
    },

    # test_url = "https://www.apple.com/library/test/success.html"
    "TEST_URL": "https://www.gstatic.com/generate_204",

    "RULESET": [
        ["PT站", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/PrivateTracker.list"],
        ["ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/OpenAi.list"],
        ["ChatBot", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/ChatBot.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/LocalAreaNetwork.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/UnBan.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanAD.list"],
        ["应用净化", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanProgramAD.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyList.list"],
        ["广告拦截", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyListChina.list"],
        ["隐私防护", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/BanEasyPrivacy.list"],
        ["谷歌FCM", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/GoogleFCM.list"],
        ["谷歌服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Google.list"],
        # ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/GoogleCN.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Adobe.list"],
        ["微软Bing", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Bing.list"],
        ["微软云盘", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/OneDrive.list"],
        ["微软服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Microsoft.list"],
        ["苹果服务", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Apple.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Telegram.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Epic.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Origin.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Sony.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Steam.list"],
        ["Telegram", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/Nintendo.list"],
        ["YouTube", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Ruleset/YouTube.list"],
        ["国内媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaMedia.list"],
        ["国外媒体", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ProxyMedia.list"],
        ["节点选择", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ProxyGFWlist.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaIp.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaDomain.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/ChinaCompanyIp.list"],
        ["全球直连", "https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/Download.list"],
        ["全球直连", "[]GEOIP,CN"],
        ["漏网之鱼", "[]FINAL"]
    ],

    "CUSTOM_PROXY_GROUP": [
        {
            "name": "自动选择",
            "type": "url-test",
            "regex": "^(?!.*(ZJU|浙大|内网|✉️)).*",
            "rule": False
        },
        {
            "name": "手动切换1",
            "type": "select",
            "manual": True,
            "rule": False
        },
        {
            "name": "手动切换2",
            "type": "select",
            "manual": True,
            "rule": False
        },
        {
            "name": "故障转移",
            "type": "fallback",
            "regex": "^(?!.*(ZJU|浙大|内网|✉️)).*",
            "rule": False
        },
        {
            "name": "负载均衡",
            "type": "load-balance",
            "regex": "^(?!.*(ZJU|浙大|内网|✉️)).*",
            "rule": False
        },
        {
            "name": "香港负载均衡",
            "type": "load-balance",
            "rule": False,
            "regex": r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        },

        # Rule groups
        {
            "name": "✔ ZJU-INTL",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "✔ ZJU",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "ChatBot",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "Telegram",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "YouTube",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "国外媒体",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "国内媒体",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "谷歌FCM",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "谷歌服务",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "微软Bing",
            "type": "select",
            "prior": "PROXY"
        },
        {
            "name": "微软云盘",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "微软服务",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "苹果服务",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "Telegram",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "PT站",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "全球直连",
            "type": "select",
            "prior": "DIRECT"
        },
        {
            "name": "广告拦截",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "应用净化",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "隐私防护",
            "type": "select",
            "prior": "REJECT"
        },
        {
            "name": "漏网之鱼",
            "type": "select",
            "prior": "PROXY"
        },

        # Region groups
        {
            "name": "香港节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇭🇰|HK|Hong|Kong|HGC|WTT|CMI|港"
        },
        {
            "name": "台湾节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇹🇼|TW|Taiwan|新北|彰化|CHT|台|HINET"
        },
        {
            "name": "狮城节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇸🇬|SG|Singapore|狮城|^新[^节北]|[^刷更]新[^节北]"
        },
        {
            "name": "日本节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇯🇵|JP|Japan|Tokyo|Osaka|Saitama|东京|大阪|埼玉|日"
        },
        {
            "name": "韩国节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇰🇷|KO?R|Korea|首尔|韩|韓"
        },
        {
            "name": "美国节点",
            "type": "url-test",
            "rule": False,
            "regex": r"🇺🇸|US|America|United.*?States|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥"
        }
    ]
}
