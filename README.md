# 無人機肢體學：革命性的飛行教學


## 動機發想 (Concept Development)
現在教育部正在推動**新興科技創新教學**，鼓勵學生善用科技學習，但因為金費和操作難度問題，在無人機領域的教學資源偏少，因此我們想打破現狀，透過**人自身的肢體語言來操控無人機**，將**運動和科技**做結合，**降低操控無人機的難度**並**提升學習趣味**，使用者也可以依照自己課堂上的需求更改對應的圖片，來更貼合課堂所需。
## 硬體設備 (Implementation Resources)
* CoDroneEDU
* computer
## 軟體架構 (Existing Library/Software)
* OpenCV
* codrone_edu
* python3
* pycharm

## 執行過程 (Implementation Process)
* **程式執行流程圖**

![Untitled](https://hackmd.io/_uploads/ryLof7QuT.jpg)
* **程式檔案描述**
  * find_node.py
  >   找出圖片的每個節點，並印出來
  * pose.json
  >   每張圖片人體的各個座標點
  * pose_codrone.py
  >   流程： 要與圖片做出相同的動作，才會跳下一張圖，並輸出True 若在規定時間內做不出來，也會跳下一張圖，並輸出。
  `註：
  89行可以調整要與模仿的圖片的相關性(暫定0.1)   
128行可以調整想要使用的視訊鏡頭，0的話代表預設的鏡頭，例如筆電的自帶鏡頭(暫定0)   
136行可以調整多久會換下一張圖片(暫定20秒)`

* **硬體準備**
  * 安裝linux虛擬機
  * 插上usb連接無人機遙控器，配對無人機
  * 利用程式碼（肢體）取代遙控器操控無人機
* **場地布置**
  * 找一個相對空曠的地方
  * 站在離電腦大約2.5-3公尺的位置。
    `原因:確保整個人能完全出現在電腦畫面裡，如果太靠近會導致無法抓到身體或其餘超出鏡頭的點。`
  * 將無人機放在身後`記得留安全距離，不要被打到了！`
  * **務必注意無人機相關法規，以免觸法**`室內不受法規限制、室外可能會有風、氣流等影響，變數較高`
 * **無人機路徑**
   * 開始執行：起飛
   * 第一個動作:後滑 
   * 第二個動作:前滑
   * 第三個動作:右滾
   * 第四個動作:右轉
   * 第五個動作:降落
* **可能會遇到的問題**
   * 起飛時需要等待一下
   * 在無人機執行動作時，電腦畫面會卡頓
   * 偵測到動作時會有小停頓
   * 電力、風、距離會影響無人機飛行
   * 鏡像讀取影像

## 善用所學 (Knowledge from Lecture)
* Linux系統基本指令

## 前置下載 (Installation)
> 以下的指令環境為Linux系統  

**第一種方法**

* 安裝pip，Python的包管理工具
```bash=
sudo apt-get install pip
```
* 安裝OpenCV Python庫，用於圖像處理。
```bash=
pip install opencv-python
```
* 安裝Mediapipe庫，用於處理媒體數據。
```bash=
pip install mediapipe
```
* 這個Python庫用於處理鍵盤事件和模擬鍵盤操作。 

    `我們設定按下a，就可以強制停止所有操作使無人機降落，因此需要此套件。`
```bash=
pip install keyboard
```
*  下載codrone_edu
```bash=
pip install codrone_edu
```

**第二種方法**
> [安裝 PyCharm](https://www.jetbrains.com/pycharm/)  

![截圖 2024-01-04 下午12.23.26](https://hackmd.io/_uploads/HkhRM2Qu6.png)

`從這裡下載 libraries`

![截圖 2024-01-04 下午12.26.12](https://hackmd.io/_uploads/ryMNr2md6.png)


## 遊戲規則 (Game rule)
完成螢幕上的指定動作，操控無人機的路徑，成功完成5個動作即可讓無人機安全降落，使用秒數較少者獲勝。

## 實作影片 (Usage)
https://drive.google.com/drive/folders/1--zeWyft_DF7-vA84BsUNzzYGPm9RO9h

## 工作分配（Job Assignment）

|     | 姓名   | 負責內容                                           |
| --- | ------ | -------------------------------------------------- |
|   組長  | 楊期閎 | OpenCV影像辨識、創意發想、資料整理、報告                 |
|  組員   | 羅彥翔 | OpenCV影像辨識、主機-無人機串接、程式彙整          |
|   組員  | 侯楷言 | 無人機指令部署、無人機組裝維修、程式彙整、創意發想 |
|  組員   | 陳品蓉 | 撰寫Readme、影片剪輯、創意發想、資料整理           |
|   組員  | 顏力維 | 主機-無人機串接                                    |

## 參考資料（References）
* [教育部全球資訊網](https://www.edu.tw/News_Content.aspx?n=9E7AC85F1954DDA8&sms=169B8E91BB75571F&s=5E3E55E67AD94DE3)
* [交通部民用航空局-遙控無人機管理資訊系統](https://drone.caa.gov.tw/)
* [【python】opencv 2小時初學者教學 ｜ 影像辨識 ｜ 影像處理 ｜ 人臉辨識 ｜ 電腦視覺](https://www.youtube.com/watch?v=xjrykYpaBBM&t=401s)
* [【python】OpenCV + MediaPipe 手部追蹤 ｜ MediaPipe 教學 ｜ 影像辨識 ｜ 電腦視覺 ｜ AI 人工智慧](https://www.youtube.com/watch?v=x4eeX7WJIuA&t=591s)
* [PyCharm The Python IDE for Professional Developers](https://www.jetbrains.com/pycharm/)

## thank you ‪ꔛ‬♡‪
柏瑋學長、郁庭學長、梓睿學長 : 思考方向提供  
瑜楓學長 : 協助測試
