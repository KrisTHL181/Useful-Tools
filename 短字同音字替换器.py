import pypinyin,Pinyin2Hanzi,re
def convert(wait_replace):
    converted,s,ct,all_,values,f,dagparams="",[],[],[],[],[],Pinyin2Hanzi.DefaultDagParams()
    for fenci in wait_replace:
        if re.search("[^\u4e00-\u9fa5]",fenci) != None:
            continue
        for plus in pypinyin.lazy_pinyin(fenci,style=pypinyin.Style.TONE3,strict=False):
            all_.append(Pinyin2Hanzi.simplify_pinyin(pypinyin.contrib.tone_convert.to_normal(plus)))
    result = Pinyin2Hanzi.dag(dagparams, tuple(all_),path_num=20, log=True)
    for item in result: f.append([item.score,item.path])
    for data in f: values.append(data[0])
    return str().join(f[values.index(min(values))][1])

if __name__ == "__main__":
    while True:
        print(convert(input("待替换(将删除非中文字符):")))
