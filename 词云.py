from PIL import Image
import wordcloud
import jieba
f=open('文本.txt', 'r', encoding='utf-8')
text=f.read()
f.close()
lst=jieba.lcut(text)
m=' '.join(lst)
print('开始制作词云...')
s = {'的','并','和','是','或','人','它','也','对','像','等'}
mac = 'PingFang.ttc'
win = 'simhei.ttf'
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    font_path=win,
    stopwords=s,
    background_color='gold',
    colormap='rainbow',
)
w.generate(m)
w.to_file('词云.png')


print('词云图片已生成,开始展示图片')

p = Image.open('词云.png')
p.show()
print('图片展示完成')

