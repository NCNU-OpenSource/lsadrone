# 無人機肢體學：革命性的飛行教學
[TOC]

## 動機發想 (Concept Development)
現在教育部正在推動**新興科技創新教學**，鼓勵學生善用科技學習，但因為金費和操作難度問題，在無人機領域的教學資源偏少，因此我們想打破現狀，透過**人自身的肢體語言來操控無人機**，將**運動和科技**做結合，**降低操控無人機的難度**並**提升學習趣味**，使用者也可以依照自己課堂上的需求更改對應的圖片，來更貼合課堂所需。
## 硬體設備 (Implementation Resources)
* CoDroneEDU
* computer
* （鏡頭）
## 軟體架構 (Existing Library/Software)
* OpenCV
* codron
* python3

## 執行過程 (Implementation Process)
* **程式執行流程圖**

![Untitled](https://hackmd.io/_uploads/ryLof7QuT.jpg)
* **程式檔案描述**
  * ++pose.json++
  >   每張圖片人體的各個座標點
  * ++pose_codrone.py++
  >   流程： 要與圖片做出相同的動作，才會跳下一張圖，並輸出True 若在規定時間內做不出來，也會跳下一張圖，並輸出。
  `註：
  90行可以調整要與模仿的圖片的相關性(暫定0.1)   
129行可以調整想要使用的視訊鏡頭，0的話代表預設的鏡頭，例如筆電的自帶鏡頭(暫定0)   
137行可以調整多久會換下一張圖片(暫定20秒)`

* **硬體準備**
  * 安裝linux虛擬機
  * 插上usb連接無人機遙控器，配對無人機
  * 利用程式碼（肢體）取代遙控器操控無人機
* **場地布置**
  * 找一個相對空曠的地方
  * 站在離電腦大約？公尺的位置。
    `原因:確保整個人能完全出現在電腦畫面裡，如果太靠近會導致無法抓到身體或其餘超出鏡頭的點。`
  * 將無人機放在身後`記得留安全距離，不要被打到了！`

## 善用所學 (Knowledge from Lecture)
* linux系統基本指令

## 前置下載 (Installation)
> 以下的指令環境為linux系統
1. 安裝pip，Python的包管理工具
```bash=
sudo apt-get install pip
```
2. 安裝OpenCV Python庫，用於圖像處理。
```bash=
pip install opencv-python
```
3. 安裝Mediapipe庫，用於處理媒體數據。
```bash=
pip install mediapipe
```
4.  這個Python庫用於處理鍵盤事件和模擬鍵盤操作。 

    `我們設定按下a，就可以強制停止所有操作使無人機降落，因此需要此套件。`
```bash=
pip install keyboard
```


## 遊戲規則 (Game rule)

## 實作影片 (Usage)

<!-- How to use your project -->

## 工作分配（Job Assignment）

|     | 姓名   | 負責內容                                           |
| --- | ------ | -------------------------------------------------- |
|   組長  | 楊期閎 | OpenCV影像辨識、創意發想、資料整理                 |
|  組員   | 羅彥翔 | OpenCV影像辨識、主機-無人機串接、程式彙整          |
|   組員  | 侯楷言 | 無人機指令部署、無人機組裝維修、程式彙整、創意發想 |
|  組員   | 陳品蓉 | 撰寫Readme、影片剪輯、創意發想、資料整理           |
|   組員  | 顏力維 | 主機-無人機串接                                    |

## 參考資料（References）
* [教育部全球資訊網](https://www.edu.tw/News_Content.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F&s=5E3E55E67AD94DE3)
* [交通部民用航空局-遙控無人機管理資訊系統](https://drone.caa.gov.tw/)
* [【python】opencv 2小時初學者教學 ｜ 影像辨識 ｜ 影像處理 ｜ 人臉辨識 ｜ 電腦視覺](https://www.youtube.com/watch?v=xjrykYpaBBM&t=401s)
* [【python】OpenCV + MediaPipe 手部追蹤 ｜ MediaPipe 教學 ｜ 影像辨識 ｜ 電腦視覺 ｜ AI 人工智慧](https://www.youtube.com/watch?v=x4eeX7WJIuA&t=591s)

## thank you ‪ꔛ‬♡‪
柏瑋學長、郁庭學長 : 思考方向提供  
瑜楓學長 : 協助測試