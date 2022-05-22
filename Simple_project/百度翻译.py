import json
import execjs
import requests


class baidufy:
    def __init__(self) -> None:
        self.url = 'https://fanyi.baidu.com/v2transapi'
        self.lan_url = "https://fanyi.baidu.com/langdetect"
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
            'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_d17dfba89ee05878101ef2baf40364861617960676487; MCITY=-%3A; BIDUPSID=8045A52CC1AFD5AD97737144A130A31C; PSTM=1609426674; BDUSS=dFYXZMfndlQW94fkUtQzdVTVJlcWw0ZE1MT3dsUGhhTVYtMkNkYWJuMXVTRkJpSVFBQUFBJCQAAAAAAAAAAAEAAADtofQJOTI4MTM1MDI3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG67KGJuuyhiVm; BDUSS_BFESS=dFYXZMfndlQW94fkUtQzdVTVJlcWw0ZE1MT3dsUGhhTVYtMkNkYWJuMXVTRkJpSVFBQUFBJCQAAAAAAAAAAAEAAADtofQJOTI4MTM1MDI3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG67KGJuuyhiVm; APPGUIDE_10_0_2=1; BAIDUID=C279AA27756CA244C284B7AD0D4DA28F:FG=1; BAIDU_WISE_UID=wapp_1647497129037_104; RT="z=1&dm=baidu.com&si=x08knciiif&ss=l0uwgyqk&sl=2&tt=31r&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3f2&ul=3zc&hd=40j"; BAIDUID_BFESS=6CDC0C2D4E2DBD60CD88A535713F6D6A:FG=1; H_PS_PSSID=35104_31254_35979_36087_34584_36142_36036_35994_35322_26350_36114_36100_36061; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1646894658,1647154786,1647515982,1647914774; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1647915093; ab_sr=1.0.1_NDZmOGJiYzQ2OGJkYTkzMjVhMzU3OTg5OTNjYjljODA1ZWUyNDVkZTM5Y2JjZmUwNDM1NzhjZWYyZGZjMTczNWQ2ZTU5YTlhZjk4NWY3ZjgyZTNmNzQ4MWUxNDgzMTAwYjdlMmNlMzQ5OTdmYzViNjZkOTNhMmIxZjg2Y2E0ZDY1MjZjNDYwYjYxMTA3ZTBhMDJhNmU3ZWZjY2VjNzkzYWY0MGEyMDU4YWRjZWU0Mjg3YTcyNzQ2ZGE0YzNiZGEx'

        }

    def get_sign(self, word):
        with open('baidufy.js', 'r') as f:
            js_test = f.read()
        sign = execjs.compile(js_test).call('e', word)
        return sign

    def set_data(self, word, sign):
        lan_data = {
            'query': word,
        }
        lan_rs = self.send_post(url=self.lan_url, data=lan_data)
        lan = json.loads(lan_rs)["lan"]
        
        
        
        
        data = {
            'from': lan,
            'to': "en" if lan=="zh" else "zh",
            'query': word,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': sign,
            'token': 'd7609730674760cf96025b9266f75572',
            'domain': 'common'
        }
        return data

    def send_post(self, url, data):
        response = requests.post(url, data=data, headers=self.header)
        return response.content.decode()

    def print_rs(self, rs):
        # 提取数据
        rs_dict = json.loads(rs)
        result = rs_dict['trans_result']['data'][0]['dst']
        return result

    def run(self):
        word = input('请输入你要翻译的内容：')
        sign = self.get_sign(word)
        data = self.set_data(word, sign)
        rs = self.send_post(self.url, data)
        result = self.print_rs(rs)
        print("翻译结果是：", result)


if __name__ == '__main__':
    baidufy = baidufy()
    baidufy.run()
