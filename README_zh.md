# C-CLAIM: 涓浗鍒戞硶鏉℃枃涓庡徃娉曡В閲婃槧灏勬暟鎹泦

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

[English Version / 鑻辨枃鐗圿(./README.md)

## 椤圭洰绠€浠?
鏈暟鎹泦閽堝涓崕浜烘皯鍏卞拰鍥藉垜娉曞強鍏跺徃娉曡В閲娿€佸徃娉曟枃浠讹紝绯荤粺鎬у湴鏋勫缓浜嗕粠娉曞緥鏉℃枃鍒版鐢憋紙缃悕锛夌殑鏄犲皠鍏崇郴銆傞€傜敤浜庢硶寰嬩俊鎭寲銆佹浠跺垎绫汇€佹櫤鑳藉徃娉曠瓑鐮旂┒鍜屽簲鐢ㄥ満鏅€?
## 鏁版嵁闆嗙粨鏋?
```text
C-CLAIM/
鈹溾攢鈹€ setup.py                 # 瀹夎鑴氭湰
鈹溾攢鈹€ MANIFEST.in              # 鎵撳寘娓呭崟
鈹溾攢鈹€ README.md                # 鑻辨枃鏂囨。
鈹溾攢鈹€ README_zh.md             # 涓枃鏂囨。
鈹斺攢鈹€ c_claim/
    鈹溾攢鈹€ data/
    鈹?  鈹溾攢鈹€ 鍒戞硶鏉℃枃.csv          # 鍒戞硶鏉℃枃鍘熸枃鍙婃鐢辨爣娉?    鈹?  鈹溾攢鈹€ 鍒戞硶鍙告硶瑙ｉ噴.csv       # 鏈€楂樹汉姘戞硶闄㈠徃娉曡В閲?    鈹?  鈹溾攢鈹€ 鍒戞硶鍙告硶鏂囦欢.csv       # 鍏朵粬閲嶈鍙告硶鏂囦欢
    鈹?  鈹溾攢鈹€ 绔犺妭妗堢敱琛?jsonl       # 鎸夌珷鑺傝仛鍚堢殑妗堢敱绱㈠紩
    鈹?  鈹斺攢鈹€ 鏍囧噯妗堢敱琛?txt         # 484椤规爣鍑嗘鐢辨竻鍗?    鈹斺攢鈹€ __init__.py              # Python Reader
```

## 鏁版嵁瀛楁璇存槑

### 鍒戞硶鏉℃枃

| 瀛楁 | 绫诲瀷 | 璇存槑 |
|------|------|------|
| chapter | string | 绔犺妭鍚嶇О |
| article_no | string | 鏉℃枃缂栧彿锛堝"绗竴鐧鹃浂浜屾潯"锛墊
| text | string | 鏉℃枃鍘熸枃 |
| category | string | 鏉℃枃绫诲埆锛堟湰浣?淇妗堢瓑锛墊
| case_types | string | 妗堢敱鍒楄〃锛圝SON鏁扮粍鏍煎紡锛墊

### 鍙告硶瑙ｉ噴/鍙告硶鏂囦欢

| 瀛楁 | 绫诲瀷 | 璇存槑 |
|------|------|------|
| title | string | 鏂囦欢鏍囬 |
| issue | string | 鍙戝竷鏈熷彿 |
| source_url | string | 鍘熸枃閾炬帴 |
| text | string | 瀹屾暣鏂囦欢鍐呭 |
| matched_chapters | string | 鍏宠仈绔犺妭 |
| matched_case_types | string | 鍏宠仈妗堢敱 |

## 鏁版嵁鏉ユ簮涓庢爣娉?
### 鍒戞硶鏉℃枃
**鏉ユ簮**: 涓崕浜烘皯鍏卞拰鍥藉垜娉曪紙鍚巻娆′慨姝ｆ鍙婇噸瑕佸崟琛屽垜娉?鍐冲畾锛?
**鏍囨敞鏂瑰紡**: 浜虹被涓撳楂樼簿搴︽爣娉?> 鐢辨硶寰嬩笓涓氫汉鍛橀€愭潯闃呰鏉℃枃锛屾槑纭瘡鏉″搴旂殑妗堢敱锛堢姜鍚嶏級锛岀‘淇濇爣娉ㄥ噯纭巼銆?> **鐗规畩鏀跺綍璇存槑**锛氫负淇濊瘉缃悕瑕嗙洊鐨勫畬鏁存€э紝褰撳墠鏁版嵁闆嗛櫎鍒戞硶鍏稿強淇妗堝锛岃繕棰濆鏀跺綍浜嗐€婂叏鍥戒汉澶у父濮斾細鍏充簬鎯╂不楠楄喘澶栨眹銆侀€冩眹鍜岄潪娉曚拱鍗栧姹囩姱缃殑鍐冲畾銆嬶紙缃簬鈥滅涓夌珷 鐮村潖绀句細涓讳箟甯傚満缁忔祹绉╁簭缃?绗洓鑺?鐮村潖閲戣瀺绠＄悊绉╁簭缃€濇潯鏂囨湯灏撅級锛屼互鏄犲皠鈥滈獥璐姹囩姜鈥濄€?
### 鍙告硶瑙ｉ噴涓庡徃娉曟枃浠?**鏉ユ簮**: [鏈€楂樹汉姘戞硶闄㈠叕鎶ョ綉绔橾(http://gongbao.court.gov.cn/)

**鏍囨敞鏂瑰紡**: 澶фā鍨嬫爲鐘跺垎绫?+ 浜虹被涓撳浜屾鏍搁獙
> 1. 浣跨敤澶ц瑷€妯″瀷杩涜鍒濇鐨勬爲鐘剁粨鏋勫垎绫伙紝寤虹珛妗堢敱灞傜骇鍏崇郴
> 2. 鐢辨硶寰嬩笓瀹惰繘琛屼簩娆℃牳楠岋紝纭繚鍒嗙被鍑嗙‘鎬?
## 瀹夎

浠庢簮鐮佸畨瑁?

```bash
git clone https://github.com/Shiori-pope/c-claim.git
cd C-CLAIM
pip install -e .
```

## 蹇€熷紑濮?
```python
from c_claim import (
    load_articles,
    load_chapters,
    load_interpretations,
    load_documents,
    find_chapters_by_case_type,
    get_case_types,
)

# 鍔犺浇鍏ㄩ儴鍒戞硶鏉℃枃
articles = load_articles()
print(f"鏉℃枃鎬绘暟: {len(articles)}")

# 鎸夌珷鑺傛煡璇?articles = load_articles(chapter="鍗卞鍥藉瀹夊叏缃?)

# 鍔犺浇绔犺妭妗堢敱琛紙宸茶仛鍚堬級
chapters = load_chapters()
for chapter in chapters[:5]:
    print(f"{chapter['chapter']}: {len(chapter['case_types'])} 涓鐢?)

# 鎸夋鐢卞弽鍚戞煡璇㈡墍灞炵珷鑺?chapters = find_chapters_by_case_type("寮哄ジ缃?)
# ['绗洓绔?渚电姱鍏皯浜鸿韩鏉冨埄銆佹皯涓绘潈鍒╃姜']

# 鑾峰彇鎵€鏈夋鐢辨竻鍗?case_types = get_case_types()
print(f"妗堢敱鎬绘暟: {len(case_types)}")  # 484

# 鍔犺浇鍙告硶瑙ｉ噴锛坱itle 涓烘ā绯婂尮閰嶅叧閿瘝锛?interpretations = load_interpretations(title="娲楅挶")
# 杩斿洖鎵€鏈夋爣棰樹腑鍖呭惈"娲楅挶"鐨勫徃娉曡В閲?```

## 鏁版嵁缁熻

| 鏁版嵁闆?| 鏁伴噺 |
|--------|------|
| 鍒戞硶鏉℃枃 | 402 鏉?|
| 绔犺妭鏁?| 25 涓?|
| 鏍囧噯妗堢敱 | 484 椤?|
| 鍙告硶瑙ｉ噴 | 178 鏉?|
| 鍙告硶鏂囦欢 | 164 鏉?|

## 浣滆€?
| 濮撳悕 | 璐＄尞 |
|------|------|
| **鍒樻櫤鏉?* <sup>*</sup> | 鏍稿績浠ｇ爜寮€鍙戙€佹暟鎹姄鍙栥€佸ぇ妯″瀷鎻愮ず璇嶅伐绋?|
| **鍐瓙钀?* <sup>*</sup> | 娉曞緥涓撳鏍搁獙銆佽鐩栫巼澶嶆牳銆佸紓甯告暟鎹汉宸ユ爣娉?|
| **閭辩劧** <sup>*</sup> | 娉曞緥涓撳鏍搁獙銆佷竴鑷存€ф楠屻€佹寔缁暟鎹竻娲楄緟鍔?|
| **钁涘槈鑽?* <sup>*</sup> | 娉曞緥涓撳鏍搁獙銆佽嚜鍔ㄥ寲鎶芥牱鏍″銆佸紓甯告暟鎹汉宸ユ爣娉?|

> <sup>*</sup> *涓婅堪浣滆€呭鏈」鐩础鐚潎绛夛紝鎺掑悕涓嶅垎鍏堝悗銆?

## 寮曠敤

```bibtex
@misc{c-claim,
  title = {C-CLAIM: Chinese Criminal Law Article and Interpretations Mapping Dataset},
  author = {Zhijie Liu and Zixuan Feng and Ran Qiu and Jiarong Ge},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Shiori-pope/c-claim}
}
```

## 璁稿彲璇?
鏈暟鎹泦閲囩敤 [鐭ヨ瘑鍏变韩缃插悕-鐩稿悓鏂瑰紡鍏变韩 4.0 鍥介檯璁稿彲鍗忚](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) 杩涜璁稿彲銆?
## 鍏嶈矗澹版槑

鏈暟鎹泦浠呬緵鐮旂┒鍜屾暀鑲茬洰鐨勪娇鐢ㄣ€傛暟鎹唴瀹规潵婧愪簬鍏紑鐨勬硶寰嬫硶瑙勬枃浠讹紝鎴戜滑灏藉姏纭繚鏁版嵁鐨勫噯纭€э紝浣嗕笉瀵规暟鎹腑鐨勪换浣曢敊璇垨閬楁紡鎵挎媴璐ｄ换銆傝鐢ㄦ埛鍦ㄤ娇鐢ㄥ墠鑷鏍稿疄鍏抽敭淇℃伅銆?
## 鑱旂郴鏂瑰紡

濡傛湁闂鎴栧缓璁紝璇?[鎻愪氦 GitHub Issue](https://github.com/Shiori-pope/c-claim/issues)銆