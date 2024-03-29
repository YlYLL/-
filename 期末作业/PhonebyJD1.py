import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
 
from lxml import etree
import pymysql
 
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
 
wait = WebDriverWait(browser,50)
def search():
	browser.get('https://www.jd.com/')
	try:
		input = wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#key"))
		)#llist
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button"))
		)
		#input = browser.find_element_by_id('key')
		input[0].send_keys('phone')
		submit.click()
 
		total = wait.until(
			EC.presence_of_all_elements_located(
				(By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b')
			)
		)
		html = browser.page_source
		prase_html(html)
		return total[0].text
	except TimeoutError:
		search()
 
def next_page(page_number):
	try:
		#滑动到底部，加载出后三十个货物信息
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(10)
        #翻页动作
		button = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.pn-next > em'))
		)
		button.click()
		wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#J_goodsList > ul > li:nth-child(20)"))
		)
	#判断翻页成功
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a.curr"),str(page_number))
		)
		html = browser.page_source
		prase_html(html)
	except TimeoutError:
		return next_page(page_number)
 
def prase_html(html):
	conn=pymysql.connect(host='localhost',user='root',password='wangjiayue',db='mypachou',charset="utf8")
	cur=conn.cursor()
	html = etree.HTML(html)
	items = html.xpath('//li[@class="gl-item"]')
	for i in range(len(items)):
		if html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img') != "done":
			img=html.xpath('//div[@class="p-img"]//img')[i].get('data-lazy-img')
			print("img:", img)
		else :
			img=html.xpath('//div[@class="p-img"]//img')[i].get('src')
			print("img:",img)
		name=html.xpath('//div[@class="p-name p-name-type-2"]//em')[i].xpath('string(.)')
		print("title:", name)
		price=html.xpath('//div[@class="p-price"]//i')[i].text
		print("price:",price)
		commit=html.xpath('//div[@class="p-commit"]//a')[i].text
		print("commit", commit)
		cur.execute("INSERT INTO testmodel_test (name,price,img,commit) VALUES('%s','%s','%s','%s')"%(name,price,img,commit))
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	cur.close()
	conn.commit()
	conn.close()

def main():
    print("第",1,"页：")
    total=int(search())
    for i in range(2,total+1):
        time.sleep(3)
        print("第",i,"页：")
        next_page(i)


if __name__=="__main__":
    main()