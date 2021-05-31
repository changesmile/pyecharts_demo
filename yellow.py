import re
import time
import requests
import os


class GetYellow:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }

    def get_data(self, url):
        session = requests.session()
        data = session.get(url, headers=self.headers)
        # print(data.text)
        return data.content.decode('UTF-8')

    def pares_data(self, data):
        total_data = []
        iamge_list = re.findall(r'<img data-src="(.*?)" class="lazy"', data)  # 图片地址
        url_list = re.findall(r'<a href="(.*?)" class="box"', data)  # 详细的介绍界面的url
        designation_list = re.findall(r'<div class="uid">(.*?)</div>', data)  # 番号
        next_page_url = re.findall(r'<a rel="next" class="pagination-next" href="(.*?)">下一頁</a>', data)[0]  # 下一页url
        if len(next_page_url) > 0:
            next_page_url = 'https://javdb7.com' + next_page_url
        else:
            next_page_url = None
        for i, j, k in zip(iamge_list, url_list, designation_list):
            temp = {'image_url': i, 'detail_url': 'https://javdb7.com' + j, 'designation_list': k}
            total_data.append(temp)
        return total_data, next_page_url

    def save_file(self, total):
        for i in total:
            url = i['image_url']
            with open('./pic/' + i['designation_list'] + '.jpg', 'wb') as fd:
                fd.write(requests.get(url).content)
                # 将图片名命名为番号并保存
                # print(requests.get(url).content)
                time.sleep(0.2)

    def run(self):
        url = 'https://javdb7.com/'
        data = self.get_data(url)
        total_data, next_page_url = self.pares_data(data)
        self.save_file(total_data)

        for i in range(0, 5):  # 爬1到5页
            data = self.get_data(next_page_url)
            total_data, next_page_url = self.pares_data(data)
            self.save_file(total_data)
        # 这是循环到最后一页的
        # while True:
        #     if next_page_url == None:
        #         break
        #     else:
        #         data = self.get_data(next_page_url)
        #         total_data, next_page_url = self.pares_data(data)
        #         self.save_file(total_data)


if __name__ == '__main__':
    folder = os.path.exists('./pic')
    if not folder:
        os.makedirs('./pic')
    yellow = GetYellow()
    yellow.run()
